def sort():
    nums = [6, 4, 3, 7, 5, 1, 2]

    print(f'nums: {nums}')
    # print(f'test: {merge([2], [])}')
    sorted = merge_sort(nums)
    print(f'sorted: {sorted}')

# データ列を分割する(通常、二等分する)
# 分割された各データ列で、含まれるデータが1個ならそれを返し、2個以上ならステップ1から3を再帰的に適用してマージソートする
# 二つのソートされたデータ列(1個であればそれ自身)をマージする

def merge_sort(nums):
    return split(nums)

def split(nums):
    if len(nums) == 1:
        return nums

    i_mid = len(nums) // 2
    left = nums[:i_mid]
    right = nums[i_mid:]

    return merge(split(left), split(right))

def merge(left , right):
    print(f'left: {left}, right: {right}')

    merged = []

    while len(left) > 0 & len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged = merged + left + right

    return merged


if __name__ == '__main__':
    sort()
