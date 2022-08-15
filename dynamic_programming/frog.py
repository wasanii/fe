"""Frog問題
n個の足場があり、それぞれの高さはheight[i](i=0, 1, ..., n-1)です。
カエルが足場0からn-1まで、足場1つか2つずつ跳ぶことができます。
このとき、足場の高低差がカエルにとってのコストになります。
足場n-1に到着したとき、コストの最小値はいくらになるでしょうか。"""


def main():
    n = 7
    height = [2, 9, 4, 5, 1, 6, 10]
    result = frog(n, height)
    print(f'result: {result}')


def frog(n, height):
    """動的計画法で解く。部分問題の結果を記録しながら解いていく。"""
    dp = [0] + [65535] * (n - 1)

    def solve(i):
        print(f'i: {i}, dp[{i}]: {dp[i]}')

        if i == 0:  # ベースケース
            return 0
        else:
            # i-1番目から飛んできた場合。i-1番目のコスト+i番目まで跳ぶコスト。
            dp[i] = min(dp[i], solve(i - 1) + abs(height[i] - height[i - 1]))

            # i-2番目から跳んでくる場合。i=1の場合を除く。
            if i > 1:
                dp[i] = min(dp[i], solve(i - 2) + abs(height[i] - height[i - 2]))

            return dp[i]

    return solve(n - 1)


if __name__ == '__main__':
    main()
