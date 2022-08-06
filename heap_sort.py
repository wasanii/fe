def execute():
    nums = [5, 2, 7, 3, 6, 1, 4]
    print(f'nums: {nums}')
    result = heap_sort(nums)
    print(f'result: {result}')


def build_heap(nums):
    # 降順ヒープをつくる

    # nord = [n for n in nums]
    # parent = [0 for n in range(len(nums))]
    # left = [n for n in parent]
    # right = [n for n in parent]

    # ヒープを初期化
    nord = []   # 値が入る
    parent = []  # parent[i], left[i], right[i] には、nord[i]からつながるノードの添字が入る
    left = []
    right = []

    for n in nums:
        i = nums.index(n)
        nord.append(n)
        left.append(0)
        right.append(0)

        if len(nord) == 1:  # 新規に根に追加
            parent.append(0)

        # 子を追加していく
        for j in range(i):  # 0番目から順に調べる
            if right[j] == 0:  # rightを持たない最初のノードが親に決定
                parent.append(j)
                if left[j] == 0:  # 親にleftがなければ子は親のleftになり、
                    left[j] = i
                else:  # leftがあれば、子は親のrightになる
                    right[j] = i
                break

        # 親>子ならを親子を入れ替える
        while nord[parent[i]] > nord[i]:
            nord[parent[i]], nord[i] = nord[i], nord[parent[i]]
            parent[parent[i]], parent[i] = parent[i], parent[parent[i]]
            left[parent[i]], left[i] = left[i], left[parent[i]]
            right[parent[i]], left[i] = left[i], left[parent[i]]
            i = parent[i]

    print(f'\nnord: {nord}')
    print(f'parent: {parent}')
    print(f'left: {left}')
    print(f'right: {right}')

    return nord, parent, left, right


def sort(heap):
    result = 0
    return result


def heap_sort(nums):

    heap = build_heap(nums)
    result = sort(heap)

    return result


if __name__ == '__main__':
    execute()