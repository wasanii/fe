def main():
    nums = [5, 2, 7, 3, 6, 1, 4]
    print(f'nums: {nums}\n')
    result = heap_sort(nums)
    print(f'\nresult: {result}')


def left_child(i_parent):
    return i_parent * 2 + 1


def right_child(i_parent):
    return i_parent * 2 + 2


def parent(i_child):
    return (i_child - 1) // 2


def heap_sort(nums):
    # 降順ヒープをつくる
    heap = build_heap(nums)

    # 降順ヒープの根から値を1つずつ選び出し、末尾の値と交換していく
    for last in range(len(nums) - 1, 0, -1):    # last: ヒープの後ろへ回すときの、宛先要素番号 ※停止の0 last > 0の意味
        heap[0], heap[last] = heap[last], heap[0]
        heap = rebuild_heap(heap, last - 1)
        print(f'heap(再構築後): {heap}')
    return heap


def build_heap(nums):
    heap = []

    for i in range(len(nums)):
        heap.append(nums[i])

        k = i  # 処理する要素番号。親子の入れ替え後に親へと伝播していくので変わりうる

        while k > 0:
            if heap[parent(k)] < heap[k]:  # ヒープの値が親<子なら、親と子の値を入れ替える
                heap[parent(k)], heap[k] = heap[k], heap[parent(k)]
                k = parent(k)  # 親がまだ上に行けるかどうか調べる。根まで行ったらk=0なので動きは止まる
            else:
                break

        print(f'heap: {heap}')

    return heap


def rebuild_heap(heap, heap_last):  # 根から要素番号heap_lastまで、heapを再構築する
    n = 0

    while left_child(n) <= heap_last:  # 子がなくなるまで続ける

        temp = left_child(n)  # とりあえず、親子の入れ替え候補を左の子にしておく
        if right_child(n) <= heap_last:  # 右の子があるならば…
            if heap[temp] <= heap[right_child(n)]:  # 左右の子の値を比べて…
                temp = right_child(n)  # 右が左以上ならば、入れ替えの対象は右になる

        if heap[n] < heap[temp]:  # 子が親よりも大きければ
            heap[n], heap[temp] = heap[temp], heap[n]  # 子と親を入れ替える
        else:
            return heap
        n = temp  # 親子の入れ替えがあったなら、入れ替えた子のほうが次回の親になる

    return heap


if __name__ == '__main__':
    main()
