# 候補をキューに詰めていき、先入れ先出しで探索する
# 木構造をどう表現しよう。
# vertex[0] = (2, 3, 4)  と、頂点を主体にするとわかりやすいけど、辺がいくつあるかが違ってくる。、
# edge[0] = (0, 1)と、辺を主体にすると、まとまりはいいけど、ある点からどこに伸びてるのかを探すのが手間？
# はたまた vertex[0, 1] = 1とか行列形式に？ これはメモリを頂点の個数**2で食うからだめかな

# 候補を出して、辿ったりするのはたぶんできる
# パスをどう作る

# 既に行った頂点も候補に入ってしまっている。
# これを華麗に取り除きたい

def main():
    # edge = [
    #     (0, 1),
    #     (0, 2),
    #     (0, 3),
    #     (1, 4),
    #     (1, 5),
    #     (2, 7),
    #     (3, 8),
    #     (3, 9),
    #     (4, 10),
    #     (6, 7),
    #     (9, 11)
    # ]
    vertex = [[1, 2, 3],
              [0, 4, 5],
              [0, 7],
              [0, 8, 9],
              [1, 10],
              [1],
              [7],
              [2, 6],
              [3],
              [3, 11],
              [4],
              [9]]
    start = 0
    finish = 6
    queue = []
    path = []

    print(f'vertex: {vertex}')
    path = breadth_search(vertex, start, finish, queue, path)
    print(f'path: {path}')


def breadth_search(vertex, start, finish, queue, path):

    # 軌跡を記録する
    path.append(start)

    # ゴールだったら終了
    if start == finish:
        return path

    # 頂点から行ける候補をキューに入れる

    queue.extend(vertex[start])

    # キューから一つ取り出し、その頂点にいく
    breadth_search(vertex, queue.pop(0), finish, queue, path)


if __name__ == '__main__':
    main()
