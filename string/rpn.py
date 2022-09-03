def reverse_poland_notation(expression: str) -> (str, float):
    """普通の記法を逆ポーランド記法に変換・計算する"""
    return rpn, result


if __name__ == '__main__':
    expression_ = ['4 6 2 + * 3 1 - 5 * -', '4 5 8 * + 9 3 / -']
    for exp_ in expression_:
        print(f"{exp_} -> {reverse_poland_notation(exp_)}")
