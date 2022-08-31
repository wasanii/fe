def compute(expression: str) -> int:
    """整数式を受け取って、その値を返す。商は整数になる。

    Args:
        expression(str): 整数と+-*/()でできた式
    Returns:
        (int)

    >>> compute('2*(34-(5+67)/8)')
    50
    >>> compute('2*(-1)')
    -2
    """

    # 解析処理
    opcnt: int = 0
    operator: list[str] = [' '] * 100
    priority: list[int] = [0] * 100
    value: list[int] = [0] * 100
    # value[0] = 0

    pri_low: int = 1    # + - の優先順位
    pri_high: int = 2   # * / の優先順位
    pri_nest: int = pri_high - pri_low + 1  # () の優先順位

    nest: int = 0

    for char in expression:
        if char.isdecimal():    # 数字0～9か?
            value[opcnt] = 10 * value[opcnt] + int(char)
        elif char == '+' or char == '-' or char == '*' or char == '/':
            operator[opcnt] = char
            if char == '+' or char == '-':
                priority[opcnt] = nest + pri_low
            else:
                priority[opcnt] = nest + pri_high
            opcnt += 1
            value[opcnt] = 0
        elif char == '(':
            nest += pri_nest
        elif char == ')':
            nest -= pri_nest

    # 計算処理
    while opcnt > 0:
        ip: int = 0
        for i in range(1, opcnt):   # 優先度が最大の演算子がどこにあるか調べる
            if priority[ip] < priority[i]:
                ip = i
        char: str = operator[ip]
        if char == '+':
            value[ip] = value[ip] + value[ip + 1]
        elif char == '-':
            value[ip] = value[ip] - value[ip + 1]
        elif char == '*':
            value[ip] = value[ip] * value[ip + 1]
        elif char == '/':
            value[ip] = value[ip] // value[ip + 1]
        for i in range(ip + 1, opcnt):
            value[i] = value[i + 1]
            operator[i - 1] = operator[i]
            priority[i - 1] = priority[i]
        opcnt -= 1

    return value[0]


if __name__ == '__main__':
    expr: str = '2*(34-(5+67)/8)'
    print(f"compute({expr}): {compute(expr)}")
    expr = '2*(-1)'  # valueの空欄は0で埋めてあるので、2*(0-1)と解釈されて正しく動作する
    print(f"compute({expr}): {compute(expr)}")
