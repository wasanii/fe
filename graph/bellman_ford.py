def bellman_ford() -> list[int]:

    # start = 0
    # finish = 6

    n_vertex = 7
    # n_edge = 12

    # 無向グラフ。負のコストや閉路はない
    edges = [
        [0, 1, 9],  # (頂点u, 頂点v, コスト)  0 <-> 1 のコストは9
        [0, 2, 2],
        [1, 2, 6],
        [1, 3, 3],
        [1, 4, 1],
        [2, 3, 2],
        [2, 5, 9],
        [3, 4, 5],
        [3, 5, 6],
        [4, 5, 3],
        [4, 6, 7],
        [5, 6, 4]
    ]
    print(f'edges: {edges}\n')
    inf = 1 << 24  # 16777216
    vertexes = [0] + [inf] * (n_vertex - 1)   # 始点のコストは0, 他は∞にセットする

    return solve(vertexes, edges)


def solve(vertexes, edges) -> list:

    path = []   # 始点から各頂点への最短路。行き止まりもあるので、後で探索してスタート→ゴールを探す

    is_updated = True

    while is_updated:
        # u -> v, v -> u で、コストを更新できないか調べる
        is_updated = False
        for from_, to, cost in edges:
            if vertexes[to] > vertexes[from_] + cost:    # u -> vの最小コストが更新されたら
                vertexes[to] = vertexes[from_] + cost      # 最小値を更新
                path.append([from_, to])   # 経路を記録
                print(f'updated: {path}')
                print(f'vertexes: {vertexes}\n')
                is_updated = True
            elif vertexes[from_] > vertexes[to] + cost:    # 逆方向でも同様にチェック
                vertexes[from_] = vertexes[to] + cost
                path.append([to, from_])
                print(f'updated: {path}')
                print(f'vertexes: {vertexes}\n')
                is_updated = True

    return vertexes


if __name__ == '__main__':
    minimum_cost = bellman_ford()
    print(f'minimum_cost: {minimum_cost}')
