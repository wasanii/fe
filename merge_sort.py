import math


def sort():
    nums = [6, 4, 3, 7, 5, 1, 2]

    print(f'nums: {nums}')
    result = merge_sort(nums)
    print(f'\nsorted: {result}')


def merge_sort(nums):
    length = len(nums)
    result = nums

    for level in range(math.ceil(math.log2(length))):   # O(n*log2(n))とよくわかる
        size = 2 ** level  # その段で比較するleft, rightの要素数  ※ ^ 記号はXORなので、2 ^ levelだと2 XOR 0で2になる！
        print(f'\nlevel: {level}')
        print(f'size: {size}')
        merged = []
        for i in range(0, length, size * 2):    # 下から1段ずつ処理する
            left_s = i          # 左右の組を作ってmergeする
            left_e = i + size
            right_e = min(left_e + size, length)
            merged = merged + merge(result[left_s: left_e], result[left_e: right_e])

        result = merged
        print(f'result: {result}')
    return result


def merge(left, right):
    print(f'left: {left}, right: {right}')
    if len(right) == 0:  # right == [] とはできなかったと思う
        print(f'merged: {left}')
        return left

    merged = []

    # left_i = 0
    # right_i = 0
    # for i in range(len(left) + len(right)):
    #     if left[left_i] < right[right_i]:
    #         merged.append(left[left_i])
    #         left_i += 1
    #     else:
    #         merged.append(right[right_i])
    #         right_i += 1
    #     if (left_i == len(left)) or (right_i == len(right)):
    #         break

    while (len(left) > 0) and (len(right) > 0):
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged = merged + left + right

    print(f'merged: {merged}')
    return merged


if __name__ == '__main__':
    sort()
