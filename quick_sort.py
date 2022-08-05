def sort():
    nums = [3, 5, 8, 1, 2, 9, 4, 7, 6]

    print(f'nums: {nums}')
    print(f'sorted: {quick_sort(nums)}')


def quick_sort(nums):
    # print(f'argument: {nums}')

    if len(nums) <= 1:  # 1つか[]なら分割統治終了
        return nums

    left = []
    right = []
    pivot = nums[len(nums) // 2]

    for n in nums:
        if n < pivot:
            left.append(n)
        elif pivot < n:
            right.append(n)
        else:   # n = Pivot
            pass

    print(f'left: {left}, pivot: {pivot}, right: {right}')

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    sort()
