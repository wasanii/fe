def a_star():
    """ A* アルゴリズムで最短経路を求める """
    # 各点とゴールとのヒューリスティックコストにはマンハッタン距離を使う
    # d12 = |x1 - x2| + | y1 - y2 |
    # nodes = [各点からゴールまでのマンハッタン距離]
    # edges = [ [[終点, 距離], [終点, 距離]],  # 辺1
    #           [[], [], ...],  # 辺2
    #           ...]

    # アプリでの解法
    # 迷路は各点の間のコストが1のグラフと解釈できる
    # 現地点からゴールへのコストの推定値も加味して探索する
    # この推定値(ヒューリスティックコスト)が、実際の最短経路より小さければ正解が得られる
    # 高い地点から低い地点へ行くイメージ。高い方にはわざわざ行かない
    #
    # 1. スタート地点を探索済にする
    # 2. スタートからたどれる点のコストをそれぞれ計算する
    # 3. コスト = そこにたどり着くまでののコスト + ゴールまでの推定コスト
    # 4. コストが最も低い点を1つ選ぶ
    # 1. (2回め)選んだ点を探索済にする