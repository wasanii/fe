from fixedqueue import FixedQueue


def main():
    # edge = [
    #     (0, 1),
    #     (0, 2),
    #     (0, 3),
    #     (1, 4),
    #     (1, 5),
    #     (2, 6),
    #     (3, 7),
    #     (3, 8),
    #     (4, 9),
    #     (6, 10),
    #     (8, 11)
    # ]
    vertex = [[1, 2, 3],
              [0, 4, 5],
              [0, 6],
              [0, 7, 8],
              [1, 9],
              [1],
              [2, 10],
              [3],
              [3, 11],
              [4],
              [6],
              [8]]
    start = 0
    finish = 10

    print(f'vertex: {vertex}')
    print(f'start: {start}, finish: {finish}')
    print()
    history = breadth_search(vertex, start, finish)
    print(f'history: {history}')


def breadth_search(vertex, start, finish) -> list[int] or int:
    history = []
    queue = FixedQueue(len(vertex))

    # 再帰は使わずに表現
    while len(history) < len(vertex):

        # 軌跡を記録する
        history.append(start)
        print(f'start: {start}')
        print(f'history: {history}')

        # ゴールだったら終了
        if start == finish:
            return history

        else:
            # 頂点から行ける候補をキューに入れる
            # 既に行ったところは通らない
            for v in vertex[start][::-1]:   # 番号の若い方から探索してほしいので逆順にする。.reversed()は破壊的で避ける
                if v in history:
                    continue
                else:
                    queue.enque(v)
            print('stack:', end='')
            queue.dump()
            print()

            # キューから一つ取り出し、その頂点にいく
            start = queue.pop()
    return -1


if __name__ == '__main__':
    main()
