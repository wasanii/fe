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
        self.front = 0                  # 先頭要素のカーソル [None, 5, 11, 8, None, ..., None ]なら、frontは1
        self.rear = 0                   # 末尾要素のカーソル 上記の例ならrearは4。次に要素を入れたいところがrear
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

    def enque(self, x: Any) -> None:
        """データをエンキュー"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x     # データをエンキューしたら、rearとnoを一つ増やす
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:      # rearがキューの容量capacityと同じになったら、rearを配列の添字0に戻す
            self.rear = 0

    def deque(self) -> Any:
        """データをデキュー"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]     # データをデキューしたら、frontは一つ進め、noは一つ減らす
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:      # frontがキューのcapacityと同じになったら、frontを添字0に戻す
            self.front = 0                   # 配列の末尾がキューの先頭だったら、次は配列の0番がキューの先頭になるわけ
        return x

    def pop(self) -> Any:
        """データをポップ"""
        if self.is_empty():
            raise FixedQueue.Empty
        self.rear -= 1          # rearをデクリメント。ここが今末尾データがある添字
        if self.rear == -1:     # 先頭から一周したら末尾から出てくる
            self.rear += self.capacity
        x = self.que[self.rear]     # rearの一つ前のデータを返す。rearが0のときはlen(que)-1にする
        self.no -= 1
        # if self.rear == self.capacity:      # rearがキューのcapacityと同じになったら、frontを添字0に戻す
        #     self.rear = 0                   # 配列の末尾がキューの先頭だったら、次は配列の0番がキューの先頭になるわけ
        return x

    def peek(self) -> Any:
        """データをピーク(先頭データを覗く)"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """キューからvalueを探して添字(見つからなければ-1)を返す"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity  # 添字が配列をひとまわりした場合を考えて、capacityとの剰余を使う
            if self.que[idx] == value:
                return idx  # 探索成功
        return -1   # 探索失敗

    def count(self, value: Any) -> Any:
        """キューに含まれるvalueの個数を返す"""
        c = 0
        for i in range(self.no):    # 底側(先に詰めたほう)から線形探索
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 探索成功
                c += 1                  # 入っている
        return c

    def __contains__(self, value: Any) -> bool:
        """キューにvalueは含まれているか"""
        return self.count(value)

    def clear(self) -> None:
        """キューを空にする"""
        self.no = self.front = self.rear = 0    # 値は消さなくてOK

    def dump(self) -> None:
        """全データを先頭→末尾の順に表示"""
        if self.is_empty():     # キューは空
            print('キューは空です。')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
