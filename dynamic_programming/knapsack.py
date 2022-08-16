"""ナップサック問題
"""


def main():
    n = 6
    max_weight = 6
    weight = [2, 1, 3, 2, 1, 5]
    value = [3, 2, 6, 1, 3, 85]
    print(f'(weight, value) = ', end='')
    for i in range(n):
        print(f'({weight[i]}, {value[i]})', end='')
    print()

    # dpテーブルを定義
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # dpループ
    for i in range(n):
        for w in range(max_weight + 1):

            # i番目の品物を選ぶ場合
            if w - weight[i] >= 0:
                dp[i + 1][w] = max(dp[i][w], dp[i][w-weight[i]] + value[i])

            # 選ばない場合
            else:
                dp[i + 1][w] = dp[i][w]

        print(f'dp[{i}] = {dp[i]}')

    print(f'dp[{n}] = {dp[n]}')

    print(f'value = {dp[n][max_weight]}')


if __name__ == '__main__':
    main()
