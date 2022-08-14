def bellman_ford() -> list[int]:

    vertex = [
        [1, 2],     # A は B, C につながっている
        [0, 2, 3, 4],
        [0, 3, 5],
        [1, 2, 4, 5],
        [1, 3, 5, 6],
        [2, 3, 4, 6],
        [4, 5]
    ]

    n = len(vertex)

    edge = [
        [None, 9, 2, None, None, None, None],   # e12 = 9 B→Cのコストが9
        [9, None, 6, 3, 1, None, None, None],
        [2, 6, None, 2, None, 9, None],
        [None, 3, 2, None, 5, 6, None],
        [None, 1, None, 5, None, 3, 7],
        [None, None, 9, 6, 3, None, 4],
        [None, None, None, None, 7, 4, None]
    ]

    start = 0
    finish = 6

    cost = [16777215] * n      # すべての頂点のコストを∞にセットする
    cost[start] = 0                   # 始点のコストは0

    return solve(vertex, cost, edge, start, finish)


def solve(vertex, cost, edge, start, finish) -> list:

    path = [None] * len(vertex)  # 頂点のコストが更新された際、どこから来たのかを記録する
    path[0] = start
    route = []

    before = 1073741824
    after = sum(cost)

    print(f'path: {path}')
    while after < before:
        before = after
        # v(i) -> v(j) で、コストを更新できないか調べる
        for i, v in enumerate(vertex):
            for j in v:
                if cost[j] > (cost[i] + edge[i][j]):    # v -> wの最小コストが更新された
                    cost[j] = cost[i] + edge[i][j]      # 最小値を更新
                    path[j] = i                         # 経路を記録
                    print(f'path: {path}')
                if cost[i] > (cost[j] + edge[j][i]):    # v -> wの最小コストが更新された
                    cost[i] = cost[j] + edge[j][i]      # 最小値を更新
                    path[i] = j                         # 経路を記録
                    print(f'path: {path}')
        after = sum(cost)

    # 頂点を逆にたどり、最短経路とする
    v = finish
    while v != start:
        print(f'v: {v}')
        route.append(v)
        v = path[v]
    route.append(start)

    return route[::-1]


if __name__ == '__main__':
    optimal_path = bellman_ford()
    print(f'route: {optimal_path}')
