# 近づける値
goal = 10000000

# 各都道府県の人口
pref = [
    5381733, 1308265, 1279594, 2333899, 1023119, 1123891, 1914039,
    2916976, 1974255, 1973115, 7266534, 6222666, 13515271, 9126214,
    2304264, 1066328, 1154008, 786740, 834930, 2098804, 2031903,
    3700305, 7483128, 1815865, 1412916, 2610353, 8839469, 5534800,
    1364316, 963579, 573441, 694352, 1921525, 2843990, 1404729,
    755733, 976263, 1385262, 728276, 5101556, 832832, 1377187,
    1786170, 1166338, 1104069, 1648177, 1433566
]

# 2021年のデータ。こっちでも1000万ちょうどになるみたい
# pref = [5224614, 1237984, 1210534, 2301996, 959502,
#         1068027, 1833152, 2867009, 1933146, 1939110,
#         7344765, 6284480, 14047594, 9237337, 2201272,
#         1034814, 1132526, 766863, 809974, 2048011,
#         1978742, 3633202, 7542415, 1770254, 1413610,
#         2578087, 8837685, 5465002, 1324473, 922584,
#         553407, 671126, 1888432, 2799702, 1342059,
#         719559, 950244, 1334841, 691527, 5135214,
#         811442, 1312317, 1738301, 1123852, 1069576,
#         1588256, 1467480]

min_total = 0
i = 0

def search(total, pos):
    global min_total, i
    i += 1
    if i % 1000000 == 0:
        print(i, min_total)
    # print(pos, min_total)
    if pos >= len(pref) or min_total == goal:
        return
    if total < goal:
        if abs(goal - (total + pref[pos])) < abs(goal - min_total):
            min_total = total + pref[pos]
        search(total + pref[pos], pos + 1)
        search(total, pos + 1)


search(0, 0)
print(min_total)
