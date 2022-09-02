def a_star(maze: list[str], start: (int, int), finish: (int, int)):
    """ A* アルゴリズムで最短経路を求める """
    # 各点とゴールとのヒューリスティックコストにはマンハッタン距離を使う
    # d12 = |x1 - x2| + | y1 - y2 |

    # アプリでの解法
    # 迷路は各点の間のコストが1のグラフと解釈できる
    # 現地点からゴールへのコストの推定値も加味して探索する
    # この推定値(ヒューリスティックコスト)が、実際の最短経路より小さければ正解が得られる
    # 高い地点から低い地点へ行くイメージ。高い方にはわざわざ行かない

    # 1. スタート地点を探索済にする
    # 2. スタートからたどれる点のコストをそれぞれ計算する
    # 3. コスト = そこにたどり着くまでののコスト + ゴールまでの推定コスト
    # 4. コストが最も低い点を1つ選ぶ
    # 1. (2回め)選んだ点を探索済にする

    # 各点からゴールまでの推定距離と初期コストを辞書として格納する
    est_cost: dict = dict()
    act_cost: dict = dict()
    for y, row in enumerate(maze):  # 外側のループで迷路を行ごとに分ける
        for x, cell in enumerate(row):  # 内側のループで行を文字に分ける
            if cell in (' ', 'S', 'G'):
                # est_cost.update({(x, y): manhattan_distance((x, y), finish)})     # 予想コスト
                est_cost[(x, y)] = manhattan_distance((x, y), finish)     # 予想コスト
                act_cost[(x, y)] = float('inf')     # 初期コスト
    act_cost[(start[0], start[1])] = 0     # スタート地点のコストは0

    dept = start
    # searched: set = set()
    searched: list = []
    dx_dy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # ←, →, ↑, ↓

    while dept != finish:
        print(f'dept: {dept}')
        # スタート地点を探索済にする
        # searched.add(dept)
        searched.append(dept)

        # スタートからたどれる点のコストをそれぞれ計算する
        for dx, dy in dx_dy:
            nxt = (dept[0] + dx, dept[1] + dy)
            if (nxt in act_cost) and (nxt not in searched):  # たどることができて、未探索の点
                # コスト = そこにたどり着くまでののコスト + ゴールまでの推定コスト
                new_cost = act_cost[dept] + est_cost[nxt]
                act_cost[nxt] = new_cost

        # コストが最も低い点を1つ選ぶ
        min_cost = float('inf')
        for key, value in act_cost.items():
            if value < min_cost:
                dept = key

    # searched.add(finish)
    searched.append(finish)

    # # コストの最も小さい地点を、スタートからたどる
    # shortest = []
    # dept = start
    # while dept != finish:
    #     shortest.append(dept)
    #     cost = float('inf')
    #     for dx, dy in dx_dy:
    #         nxt = (dept[0] + dx, dept[1] + dy)
    #         if (nxt in searched) and (nxt not in shortest) and (act_cost[nxt] < cost):
    #             cost = act_cost[nxt]
    #             dept = nxt
    # shortest.append(finish)

    return searched  # shortest


def manhattan_distance(start: (int, int), finish: (int, int)) -> int:
    """点どうしのマンハッタン距離を返す
        d12 = |x1 - x2| + | y1 - y2 |

    >>> manhattan_distance((3, 3), (7, 7))
    8
    """
    return abs(start[0] - finish[0]) + abs(start[1] - finish[1])


def update_maze(maze: list[str], shortest: list[(int, int)]) -> list[str]:
    """迷路に最短路を * で描いて返す"""
    result = maze.copy()

    for x, y in shortest[1: -1]:
        result[y] = result[y][0: x] + '*' + result[y][x + 1:]

    return result


def show_maze(maze: list[str]) -> None:
    for row in maze:
        print(row, end='\n')
    pass


def main():
    maze_str: str = '''
---------
|   |---|
| - ----|
| |S    |
| | --- |
| | |   |
| - - --|
|      G|
---------
'''
    maze = maze_str.strip().split('\n')     # 改行で区切って1行ごとに配列に格納
    start: (int, int) = (3, 3)
    finish: (int, int) = (7, 7)

    show_maze(maze)
    shortest = a_star(maze, start, finish)
    print(f'shortest: {shortest}')

    opt_maze = update_maze(maze, shortest)
    show_maze(opt_maze)


if __name__ == '__main__':
    main()
