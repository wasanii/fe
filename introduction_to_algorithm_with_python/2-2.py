def era_name(year: int) -> str:
    """西暦を元号を含む文字列に変換する"""
    era = [(2019, '令和'), (1989, '平成'), (1926, '昭和'), (1912, '大正'), (1868, '明治')]

    for first_year, name in era:
        if year >= first_year:
            return f'{name}{year - first_year + 1}年'
    return None


def answer(year: int) -> str:
    pass

if __name__ == '__main__':
    s = 1869
    e = 2020
    for i in range(s, e + 1):
        print(era_name(i))
