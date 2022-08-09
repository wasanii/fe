def directed_edge():
    start = [0, 1, 2, 3, 4, 2, 5, 4, 6]  # 辺 m の始点の番号
    end = [0, 2, 3, 4, 1, 5, 4, 6, 2]  # 辺 m の終点の番号
    edge_first = [0, 1, 2, 3, 4, 6, 8]  # 点 n の最初の接続辺の番号
    edge_next = [0, 0, 5, 0, 7, 0, 0, 0, 0]  # 辺 m の次の接続辺の番号。なければ0
    searched = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 一筆書きの経路を構成する探索済の辺の番号を順番に格納する(探索済の経路)
    path = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 一筆書きの経路を構成する確定済の辺の番号を順番に格納する(確定済の経路)
    current = [x for x in edge_first]  # 点 n を始点とする未探索の辺の中で最小の番号を格納する
    # 点 n を始点とする未探索の辺がない場合は0を格納する

    # vertex_number = 6  # グラフの点の個数
    edge_number = 8  # グラフの辺の個数

    # for i in range(vertex_number + 1):  # 各点での未探索の辺の番号を初期化
    #     current.append(edge_first[i])

    top = 1  # 探索済の経路の辺の格納位置を初期化
    last = edge_number  # 確定済の経路の辺の格納位置を初期化
    x = 1  # 出発点は点1

    while last >= 1:
        if current[x] != 0:     # 点xで未探索の辺があるなら (current[x]に0でない辺の番号が格納されているなら)
            temp = current[x]   # 点xからたどる接続辺はtemp
            searched[top] = temp    # 接続辺tempを探索済の経路に登録
            current[x] = edge_next[temp]     # 点xから次にたどる未探索の辺を格納
            x = end[temp]   # 接続辺tempの終点を点xにする
            top += 1
        else:
            top -= 1    # 探索済の辺を遡る
            temp = searched[top]    # 遡った辺はtemp
            path[last] = temp   # 辺tempを確定済にする
            x = start[temp]
            last -= 1

    # for i in range(1, edge_number + 1):
    #     print(path[i], end=' ')

    print(f'path = {path[1:]}')


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    directed_edge()

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
