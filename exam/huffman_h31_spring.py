def huffman(size: int, parent: list[int], left: list[int], right: list[int], freq: list[int])\
        -> (int, list[int], list[int], list[int], list[int]):
    """ハフマン木を表現する配列を生成する"""

    nsize: int = 0
    node: list[int] = []
    nsize, node = sort_node(size, parent, freq, nsize, node)

    while nsize >= 2:
        i: int = node[0]    # 最も小さい値を持つ要素組の要素番号
        j: int = node[1]    # 2番めに小さい値をもつ要素組の要素番号
        left[size] = i
        right[size] = j
        freq[size] = freq[i] + freq[j]  # 子の値の合計
        parent[i], parent[j] = size    # 子に親の値の要素番号を格納
        size += 1
        nsize, node = sort_node(size, parent, freq, nsize, node)

    return size, parent, left, right, freq


def sort_node(size: int, parent: list[int], freq: list[int], nsize: int, node: list[int]) -> (int, list[int]):
    """親が作成されていない節を抽出し、節の値の昇順に整列する。
    節を表す要素番号を順に配列 node に格納し、その個数を変数 nsize に格納する"""

    for i in range(size):
        if parent[i] < 0:
            node[nsize] = i
            nsize += 1
    node = sort(freq, nsize, node)
    return nsize, node


def sort(freq: list[int], nsize: int, node: list[int]) -> list[int]:
    """節を表す要素組の要素番号の配列 node を受け取り、
    要素番号に対応する要素組が表す節の値が昇順となるように整列する

    >>> sort([10, 2, 4, 3], 4, [0, 1, 2, 3])
    [1, 3, 2, 0]
    """
    freq_sorted = [x for x in freq]   # freq.sort()が破壊的なのでコピーを作る
    freq_sorted.sort()

    result = []
    for i in range(nsize):
        idx = freq.index(freq_sorted[i])
        result.append(node[idx])
        # noinspection PyTypeChecker
        freq[idx] = None    # 出現回数のリストに重複があった場合、同じ要素に2回ヒットしないよう値を消す

    return result


def encode(k: int, parent: list[int], left: list[int]) -> None:
    """ハフマン木から文字のビット表現を作成して表示する

    Args:
        k(int): 節を表す要素組の要素番号
        parent(list[int]): 節の親を表す要素組の要素番号を格納した配列
        left(list[int]): 節の左側の子を表す要素組の要素番号を格納した配列
    Returns:
          (None)

    >>> encode(1, [6, 4, 5, 4, 5, 6, -1], [-1, -1, -1, -1, 1, 2, 3])
    110
    """
    if parent[k] >= 0:    # 親が存在するなら、親をたどる
        encode(parent[k], parent, left)
        if k == left[parent[k]]:
            print('0', end='')  # 親の左なら 0 を表示する
        else:
            print('1', end='')
    pass


if __name__ == '__main__':
    # print(sort([10, 2, 4, 3], 4, [0, 1, 2, 3]))
    # encode(1, [6, 4, 5, 4, 5, 6, -1], [-1, -1, -1, -1, 1, 2, 3])
    # print()
    import doctest
    doctest.testmod(verbose=True)
