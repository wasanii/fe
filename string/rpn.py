def reverse_poland_notation(expression: str) -> str:
    """逆ポーランド記法の式を計算する"""
    stack = []
    
    for exp in expression.split():
        print(f'stack: {stack}')
        if exp.isdigit():   # 数字はスタックに詰める
            stack.append(exp)
        else:   # 演算子が出てきたら計算する
            right = stack.pop()
            left = stack.pop()
            stack.append(str(eval(left + exp + right)))

    return stack[0]


if __name__ == '__main__':
    expression_ = ['4 6 2 + * 3 1 - 5 * -', '4 5 8 * + 9 3 / -']
    for exp_ in expression_:
        print(f"{exp_} -> {reverse_poland_notation(exp_)}", end='\n\n')
