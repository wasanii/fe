import math
import matplotlib.pyplot as plt


def parse(s: str):
    return [(x[0], int(x[1:])) for x in s.split(';')]


class Marker:
    def __init__(self):
        self.x, self.y, self.angle = 0, 0, 0
        plt.xlim(-320, 320)  # x 軸の表示範囲を設定
        plt.ylim(-240, 240)  # y 軸の表示範囲を設定

    def forward(self, val):
        # 度数法で表した角度を、ラジアンで表した角度に変換
        rad = math.radians(self.angle)
        dx = val * math.cos(rad)
        dy = val * math.sin(rad)
        x1, y1, x2, y2 = self.x, self.y, self.x + dx, self.y + dy
        # (x1, y1) と (x2, y2) を結ぶ線分を描画
        plt.plot([x1, x2], [y1, y2], color='black', linewidth=2)
        self.x, self.y = x2, y2

    def turn(self, val):
        self.angle = (self.angle + val) % 360

    @staticmethod
    def show():
        plt.show()  # 描画結果を表示


def draw(s: str):
    instruments = parse(s)
    marker = Marker()
    stack = []
    operation_no = 0
    while operation_no < len(instruments):
        print(stack)
        code, val = instruments[operation_no]
        if code == 'F':
            marker.forward(val)
        elif code == 'T':
            marker.turn(val)
        elif code == 'R':
            stack.append({'operation_no': operation_no, 'rest': val})
        elif code == 'E':
            if stack[-1]['rest'] > 1:
                operation_no = stack[-1]['operation_no']
                stack[-1]['rest'] -= 1
            else:
                stack.pop()  # stackの末尾の要素を削除
        operation_no += 1
    marker.show()


if __name__ == '__main__':
    parse('R4;F100;T90;E0')
    draw('R2;R3;E0;E0')
    draw('R3;R4;F100;T90;E0;F100;E0')
    draw('R5;F100;T72;E0')
