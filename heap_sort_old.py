def main():
    nums = [5, 2, 7, 3, 6, 1, 4]
    print(f'nums: {nums}\n')
    result = heap_sort(nums)
    print(f'\nresult: {result}')


def heap_sort(nums):
    # 降順ヒープをつくる
    heap = build_heap(nums)

    # 降順ヒープの根から値を1つずつ取り出し、結果の配列に右から詰めていく
    result = sort(heap)
    return result


def build_heap(nums):
    heap = []

    for i in range(len(nums)):
        heap.append(nums[i])
        i_parent = (i - 1) // 2  # 親の添字がkなら、子の添字は2i+1, 2i+2。子の添字から親の添字を逆算する
        if i_parent >= 0:
            rebuild_heap(heap, i_parent)  # 降順になるよう再構築する
        print(f'heap: {heap}')

    return heap


def rebuild_heap(heap, i_parent):  # 添字kを根として、heapを再構築する
    if i_parent < 0:  # k < 0になるのは、新規にヒープに数字を追加したときだけ。ならそのまま帰す
        return heap
    length = len(heap)
    i_left = min(length - 1, i_parent * 2 + 1)
    i_right = min(length - 1, i_left + 1)

    if heap[i_left] < heap[i_right]:  # 大きい方だけ親と比較する
        if heap[i_parent] < heap[i_right]:  # 子が親より大きければ交換する
            heap[i_parent], heap[i_right] = heap[i_right], heap[i_parent]
            rebuild_heap(heap, (i_parent - 1) // 2)  # 親の親へ伝播させる
    else:
        if heap[i_parent] < heap[i_left]:  # 子が親より大きければ交換する
            heap[i_parent], heap[i_left] = heap[i_left], heap[i_parent]
            rebuild_heap(heap, (i_parent - 1) // 2)

    return heap


def sort(heap):
    result = []

    while len(heap) > 1:
        result.insert(0, heap[0])  # ヒープの先頭を取り出して、結果の配列に右から詰めていく
        heap[0] = heap.pop()  # ヒープの末尾から根に数を持ってくる
        rebuild_heap(heap, 0)  # 新たな根のからヒープを再構築する
        print(f'heap: {heap}')

    return heap + result


if __name__ == '__main__':
    main()
