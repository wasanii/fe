""" 固定長キュークラス
    リングバッファを用いるので、先頭・末尾の追加や削除がO(1)で行える
    普通に配列で先頭を抜いて後ろを詰めると、その都度O(n)になってしまう
"""

from typing import Any


class FixedQueue:

    class Empty(Exception):
        """空のFixedQueueに対してdequeあるいはpeakがよびだされたときに送出する例外"""
        pass

    class Full(Exception):
        """満杯のFixedQueueに対してenqueがよびだされたときに送出する例外"""
        pass

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.no = 0                     # 現在のデータ数。front == rearのときに、空か満杯かわからなくなるので必要
        self.front = 0                  # 先頭要素のカーソル
        self.rear = 0                   # 末尾要素のカーソル
        self.capacity = capacity        # キューの容量
        self.que = [None] * capacity    # キューの本体

    def __len__(self) -> int:
        """キューに押し込まれているデータ数を返す"""
        return self.no

    def is_empty(self) -> bool:
        """キューは空であるか"""
        return self.no <= 0     # ==にしないところが堅牢性を増すためのプロの技。ブラックボックステストでやるもんね

    def is_full(self) -> bool:
        """キューは満杯か"""
        return self.no >= self.capacity     # これも堅牢性。まねをしよう。
