def boyer_moore(target: str, sub: str) -> int:
    """Boyer-Moore法で文字列検索を行う

    Args:
        target(str): 検索される文字列
        sub(str): 検索する文字列

    Returns
        (int): 一致する場合は0始まりの先頭位置, 一致しない場合は-1を返す

    >>> boyer_moore('SHOEISHA SESHOP', 'SHA')
    5
    >>> boyer_moore('HAAA', 'AAA')
    1
    >>> boyer_moore('HAAA', 'CAA')
    -1
        """

    # subの後ろから比較する。一致しない場合、まとめて後ろにずらす。
    # sub='ABC' の場合、ずらす文字数は{'s': 2, 'u': 1} デフォルト値は3になる。
    dic_offset = dict()
    len_sub = len(sub)
    for i, s in enumerate(sub):
        dic_offset[s] = len_sub - i - 1

    # 比較
    len_target = len(target)
    i = 0
    while i < len_target - len_sub + 1:
        for j in range(len_sub - 1, -1, -1):
            if target[i + j] == sub[j]:  # 合っていた場合
                if j == 0:
                    return i    # 最後の1文字まで合っていたら、位置を返して終了
                else:
                    continue    # まだ終わっていないなら、探索続行
            else:  # 違っていた場合
                offset = dic_offset.get(target[i + j], len_sub)
                if j < len_sub - 1:  # 一番右よりも左側で違っていたら(一番右の1文字目で違っていたら、offset通りにずらす)
                    if offset < len_sub:  # ターゲットが辞書にある文字だった場合
                        offset = len_sub    # subの文字数分ずらす
                    else:   # 辞書にない文字で違っていた場合
                        offset = j + 1  # 違っていた文字の次から、次回の比較を始める

                i += offset
                break  # 違っていた場合は、j のループを抜けて移動

    return -1   # 最後までヒットがなかったら-1を返す


if __name__ == '__main__':
    print(f"'SHOEISHA SESHOP', 'SHA', {boyer_moore('SHOEISHA SESHOP', 'SHA')}")
    print(f"'HAAA', 'AAA', {boyer_moore('HAAA', 'AAA')}")
    print(f"'HAAA', 'CAA', {boyer_moore('HAAA', 'CAA')}")
