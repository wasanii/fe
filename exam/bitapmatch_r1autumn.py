def generate_bitmask(pat: str) -> (list[int], int):
    """
    Args:
        pat (str): 検索文字列

    Returns:
        (list[int], int): 文字'A'～'Z'に対応するビットマスクが格納される1次元配列, 検索文字列の文字数
         """

    pat_len: int = len(pat)

    mask: list[int] = [0b0 for _ in range(1, pat_len + 1)]  # mask[1]からmask[26]までを0b0で初期化

    for i in range(pat_len):
        mask[index(pat[i])] = 0b1 << i | mask[index(pat[i])]    # 下位から数えてi番目のビットの値を1にする

    print(f'mask={[bin(x) for x in mask]}, pat_len={pat_len}')
    return mask, pat_len


def generate_bitmask_regex(pat: str) -> (list[int], int):
    """
    []の正規表現に対応したマスクを作る。
    A[XY]Bなら、AXB, AYBを表現する。

    Args:
        pat (str): 検索文字列

    Returns:
        (list[int], int): 文字'A'～'Z'、正規表現[]に対応するビットマスクが格納される1次元配列, 検索文字列の文字数
         """

    original_pat_len: int = len(pat)
    pat_len = 0
    mode = 0    # []の中にいれば1、通常は0

    mask: list[int] = [0b0 for _ in range(1, pat_len + 1)]  # mask[1]からmask[26]までを0b0で初期化

    for i in range(original_pat_len):
        if pat[i] == '[':
            mode = 1
            pat_len += 1
        else:
            if pat[i] == ']':
                mode = 0
            else:
                if mode == 0:
                    pat_len += 1

            mask[index(pat[i])] = 0b1 << pat_len - 1 | mask[index(pat[i])]    # 下位から数えてi番目のビットの値を1にする

    print(f'mask={[bin(x) for x in mask]}, pat_len={pat_len}')
    return mask, pat_len


def index(s: str) -> int:
    """アルファベット順でn番目の英大文字を設定すると整数n(1<=n<=26)を返す"""

    return ord(s) - 64  # 'A'のUnicodeコードポイントは65


def bitap_match(text: str, pat: str) -> int:
    """textの文字番号の小さい方からpatと一致する文字列を検索し、
    見つかった場合は、一致した文字列の先頭に対応するtextの文字番号を返す。
    見つからなかった場合は、-1を返す。

    Args:
        text(str): 対象文字列
        pat(str): 検索文字列

    Returns:
        int: 見つかった場合は、textのうち一致した先頭の文字番号を返す。
            見つからなかった場合は、-1を返す。
        """

    print(f'text="{text}"')
    print(f'pattern="{pat}"')

    text_len: int = len(text)    # textの文字数
    # mask, pat_len = generate_bitmask(pat)
    mask, pat_len = generate_bitmask_regex(pat)
    status = 0b0
    goal = 1 << pat_len - 1

    for i in range(text_len):
        status = status << 1 | 0b1
        status = status & mask[index(text[i])]
        if status & goal != 0b0:
            return i - pat_len + 1

    return -1




if __name__ == '__main__':
    print(f'{bitap_match("AACBBAACABABAB", "ACABAB")}')
    print(f'{bitap_match("AACBBAACABABAB", "AC[BA]A[ABC]A")}')
