import math


def main():
    nums = [6, 4, 3, 7, 5, 1, 2]

    print(f'nums: {nums}\n')
    result = merge_sort(nums)
    print(f'\nsorted: {result}')


def merge_sort(nums):  # 併合フェーズ
    print(f'nums: {nums}')

    length = len(nums)

    if length == 1:  # 1コだけなら終了
        return nums

    mid = length // 2  # 半分に分ける
    left = merge_sort(nums[:mid])  # 左半分をマージソート
    right = merge_sort(nums[mid:])  # 右半分をマージソート

    result = merge(left, right)  # マージソートしたものを併合する

    return result


def merge(left, right):  # 分割統治フェーズ
    print(f'left: {left}, right: {right}')

    right.reverse()  # [5, 6], [2, 7] → [5, 6, 7, 2] にすると
    work = left + right  # 比較対象が先頭と末尾になるので比較しやすい
    result = []

    while len(work) > 0:
        if work[0] < work[-1]:  # 左端 < 右端 なら 左端を結果の配列に詰めていく
            result.append(work.pop(0))
        else:
            result.append(work.pop())

    print(f'merged: {result}')
    return result


if __name__ == '__main__':
    main()
