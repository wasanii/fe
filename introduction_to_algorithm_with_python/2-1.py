def leap_year(start: int, end: int) -> list[int]:
    """startからendの年までのうるう年を求める"""
    return [y for y in range(start, end + 1) if (y % 400 == 0) or (y % 4 == 0 and not y % 100 == 0)]


def answer(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    s = 1950
    e = 2050
    print(leap_year(s, e))
    for i in range(s, e + 1):
        print(f'{i} {answer(i)}')
