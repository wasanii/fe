def main() -> (list[int], list[int]):

    distance: list[[int]] = [
        [0, 2,  8,  4, -1, -1, -1],    # 点0 に隣接するのは点1, 点2, 点3で、そのコストはそれぞれ2, 8, 4
        [2, 0, -1, -1, 3, -1, -1],
        [8, -1, 0, -1, 2, 3, -1],
        [4, -1, -1, 0, -1, 8, -1],
        [-1, 3, 2, -1, 0, -1, 9],
        [-1, -1, 3, 9, -1, 0, 3],
        [-1, -1, -1, -1, 9, 3, 0],
    ]

    n_point: int = 7    # 地点数
    sp: int = 0         # 出発地の地点番号
    dp: int = 6         # 目的地の地点番号

    return shortest_path(distance, n_point, sp, dp)


def shortest_path(distance: list[list[int]], n_point: int, sp: int, dp: int) -> (list[int], int):
    """N個(N>1)の地点と、地点間を直接結ぶ経路および距離が与えられたとき、
    出発地から目的地に至る最短経路とその距離を求めるプログラム
    Args:
        distance (list[list[int]]): 地点間の距離が格納されている2次元配列
        n_point (int): 地点数
        sp (int): 出発地の地点番号
        dp (int): 目的地の地点番号

    Returns:
        (list[int], int): 出発地から目的地までの最短経路上の地点番号を目的地から出発地までの順に設定する1次元配列,
        出発地から目的地までの最短距離
         """

    # s_dist: int = 1 << 64   # 出発地から目的地までの最短距離に初期値を格納する

    s_route: list[int] = [-1 for _ in range(n_point)]   # 最短経路上の地点の地点番号に初期値を格納する
    p_dist: list[int] = [1 << 64 for _ in range(n_point)]   # 出発地から各地点までの最短距離に初期値を格納する
    p_fixed: list[bool] = [False for _ in range(n_point)]   # 各地点の最短距離の確定状態に初期値を格納する
    p_route: list[int] = [-1 for _ in range(n_point)]   # 仮の最短経路上の地点の地点番号に初期値を格納する

    p_dist[sp] = 0  # 出発地から出発地自体への最短距離に0を設定する

    while True:  # 最短経路探索処理
        i: int = 0
        while i < n_point:  # 未確定の地点を一つ探す
            if not p_fixed[i]:
                break   # 最内側の繰り返しから抜ける
            i += 1
        if i == n_point:    # 出発地から全ての地点までの最短距離が確定していれば
            break           # 最短経路探索処理から抜ける
        for j in range(i + 1, n_point):  # 最短距離がより短い地点を探す
            if not p_fixed[j] and p_dist[j] < p_dist[i]:
                i = j
        s_point: int = i  # 出発地からの最短距離が未確定の地点の中で、出発地からの距離が最も短い地点
        p_fixed[i] = True   # 出発地からの最短距離を確定する
        for j in range(n_point):
            if distance[s_point][j] > 0 and not p_fixed[j]:     # 地点jが地点s_pointに隣接して、かつ、出発地からの最短距離が未確定か？
                new_dist: int = p_dist[s_point] + distance[s_point][j]  # 出発地からs_pointを経由して地点jに到達する経路の距離を求める
                if new_dist < p_dist[j]:    # 既に算出してある最短経路p_dist[j]よりも短ければ
                    p_dist[j] = new_dist    # p_dist[j]とp_route[j]を更新する
                    p_route[j] = s_point
                    # このときp_dist[j]は、出発地から地点jまでの仮の最短距離となる
                    # p_route[j]には、そのときの地点jの直前の経由地の地点番号s_pointを設定する
    s_dist: int = p_dist[dp]     # 出発地から目的地までの最短距離をs_distに設定する
    j = 0
    i = dp
    while i != sp:  # 最短経路上の地点の地点番号を**目的地から出発地までの順に**配列s_routeに設定する
        s_route[j] = i
        i = p_route[i]
        j += 1
    s_route[j] = sp

    return s_route, s_dist


if __name__ == '__main__':
    shortest_route, shortest_dist = main()
    print(f'shortest_route(from destination to start): {shortest_route}')
    print(f'shortest_dist: {shortest_dist}')
