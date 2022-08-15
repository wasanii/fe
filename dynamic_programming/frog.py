"""Frog問題
n個の足場があり、それぞれの高さはheight[i](i=0, 1, ..., n-1)です。
カエルが足場0からn-1まで、足場1つか2つずつ跳ぶことができます。
このとき、足場の高低差がカエルにとってのコストになります。
足場n-1に到着したとき、コストの最小値はいくらになるでしょうか。"""

INF = 65535


def main():
    n = 7
    height = [2, 9, 4, 5, 1, 6, 10]
    result = frog(n, height)
    print(f'result: {result}')


def frog(n, height):
    """動的計画法で解く。部分問題の結果を記録しながら解いていく。"""

    def solve(i):
        print(f'i: {i}, dp[{i}]: {dp[i]}')

        # dpが更新されていたら即リターン。dpは1回しか更新されない
        if dp[i] < INF:
            return dp[i]

        # ベースケース 足場0のコストは0
        if i == 0:
            return 0

        # 答えをINFで初期化
        result = INF

        # 緩和処理
        # 足場 i - 1 から跳んできた場合。i-1番目のコスト+i番目まで跳ぶコスト。
        result = min(result, solve(i - 1) + abs(height[i] - height[i - 1]))

        # i - 2 から跳んできた場合。i = 1の場合を除く。
        if i > 1:
            result = min(result, solve(i - 2) + abs(height[i] - height[i - 2]))

        # 結果をメモ化して返す
        dp[i] = result
        return dp[i]

    dp = [INF] * n
    return solve(n - 1)


if __name__ == '__main__':
    main()
