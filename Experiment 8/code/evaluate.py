import re
import copy

position_value = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                  [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
                  [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
                  [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def lianwu(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'%d{5}' % current
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def huosi(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'0%d{4}0' % current
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def chongsi(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'0%d{4}%d|%d%d{4}0|%d0%d{3}|%d{3}0%d|%d{2}0%d{2}' % \
              (current, opponent, opponent, current, current, current, current, current, current, current)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def huosan(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'0%d{3}0|%d0%d{2}|%d{2}0%d' % (current, current, current, current, current)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def miansan(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'00%d{3}%d|%d%d{3}00|0%d0%d{2}%d|%d%d{2}0%d0|0%d{2}0%d%d|%d%d0%d{2}0|%d00%d{2}|%d{2}00%d|%d0%d0%d|' \
              r'%d0%d{3}0%d' % \
              (current, opponent, opponent, current, current, current, opponent, opponent, current, current, current,
               current, opponent, opponent, current, current, current, current, current, current, current, current,
               current, opponent, current, opponent)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def huoer(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'00%d{2}00|0%d0%d0|%d00%d' % (current, current, current, current, current)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def mianer(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'000%d{2}%d|%d%d{2}000|00%d0%d%d|%d%d0%d00|0%d00%d%d|%d%d00%d0|%d000%d|%d0%d0%d0%d|%d0%d{2}00%d|' \
              r'%d00%d{2}0%d' % \
              (current, opponent, opponent, current, current, current, opponent, opponent, current, current, current,
               current, opponent, opponent, current, current, current, current, opponent, current, current, opponent,
               opponent, current, opponent, opponent, current, opponent)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def sisi(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'%d%d{4}%d' % (opponent, current, opponent)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def sisan(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'%d%d{3}%d' % (opponent, current, opponent)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def sier(composition, pos_x, pos_y, current):
    if current == 1:
        opponent = 2
    else:
        opponent = 1
    matched = 0
    pattern = r'%d%d{2}%d' % (opponent, current, opponent)
    horizon = ''.join(composition[pos_x - 1])
    m = re.search(pattern, horizon)
    if m:
        matched += 1
    vertical = ''.join([composition[i][pos_y - 1] for i in range(15)])
    m = re.search(pattern, vertical)
    if m:
        matched += 1
    main_diagonal = ''.join([composition[pos_x + i][pos_y + i]
                             for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
    m = re.search(pattern, main_diagonal)
    if m:
        matched += 1
    anti_diagonal = ''.join([composition[pos_x - 1 + i][pos_y - 1 - i]
                             for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
    m = re.search(pattern, anti_diagonal)
    if m:
        matched += 1
    return matched


def heuristic_value(composition, pos_x, pos_y, current):
    lianwu_num_current = lianwu(composition, pos_x, pos_y, current)
    huosi_num_current = huosi(composition, pos_x, pos_y, current)
    chongsi_num_current = chongsi(composition, pos_x, pos_y, current)
    huosan_num_current = huosan(composition, pos_x, pos_y, current)
    miansan_num_current = miansan(composition, pos_x, pos_y, current)
    huoer_num_current = huoer(composition, pos_x, pos_y, current)
    mianer_num_current = mianer(composition, pos_x, pos_y, current)
    sisi_num_current = sisi(composition, pos_x, pos_y, current)
    sisan_num_current = sisan(composition, pos_x, pos_y, current)
    sier_num_current = sier(composition, pos_x, pos_y, current)

    value = 0
    if lianwu_num_current >= 1:
        value += 100000 * 5
    elif huosi_num_current >= 1:
        value += 100000 * 5
    elif chongsi_num_current >= 2 or (chongsi_num_current >= 1 and huosan_num_current >= 1):
        value += 50000
    elif huosan_num_current >= 2:
        value += 5000
    elif huosan_num_current >= 1 and miansan_num_current >= 1:
        value += 1000
    elif huosan_num_current >= 1:
        value += 200
    elif huoer_num_current >= 2:
        value += 100
    elif miansan_num_current >= 1:
        value += 50
    elif huoer_num_current >= 1 and mianer_num_current >= 1:
        value += 10
    elif huoer_num_current >= 1:
        value += 5
    elif mianer_num_current >= 1:
        value += 3
    elif sisi_num_current >= 1 or sisan_num_current >= 1 or sier_num_current >= 1:
        value += -5

    opponent = 1 if current == 2 else 2
    lianwu_num_other = lianwu(composition, pos_x, pos_y, opponent)
    huosi_num_other = huosi(composition, pos_x, pos_y, opponent)
    chongsi_num_other = chongsi(composition, pos_x, pos_y, opponent)
    huosan_num_other = huosan(composition, pos_x, pos_y, opponent)
    miansan_num_other = miansan(composition, pos_x, pos_y, opponent)
    huoer_num_other = huoer(composition, pos_x, pos_y, opponent)
    mianer_num_other = mianer(composition, pos_x, pos_y, opponent)
    sisi_num_other = sisi(composition, pos_x, pos_y, opponent)
    sisan_num_other = sisan(composition, pos_x, pos_y, opponent)
    sier_num_other = sier(composition, pos_x, pos_y, opponent)

    if lianwu_num_other >= 1:
        value -= 100000
    elif huosi_num_other >= 1:
        value -= 100000
    elif chongsi_num_other >= 2 or (chongsi_num_other >= 1 and huosan_num_other >= 1):
        value -= 50000
    elif huosan_num_other >= 2:
        value -= 5000
    elif huosan_num_other >= 1 and miansan_num_other >= 1:
        value -= 1000
    elif huosan_num_other >= 1:
        value -= 200
    elif huoer_num_other >= 2:
        value -= 100
    elif miansan_num_other >= 1:
        value -= 50
    elif huoer_num_other >= 1 and mianer_num_other >= 1:
        value -= 10
    elif huoer_num_other >= 1:
        value -= 5
    elif mianer_num_other >= 1:
        value -= 3
    elif sisi_num_other >= 1 or sisan_num_other >= 1 or sier_num_other >= 1:
        value -= -5

    copy_composition = copy.deepcopy(composition)
    copy_composition[pos_x - 1][pos_y - 1] = str(opponent)
    lianwu_num_opponent = lianwu(copy_composition, pos_x, pos_y, opponent)
    huosi_num_opponent = huosi(copy_composition, pos_x, pos_y, opponent)
    chongsi_num_opponent = chongsi(copy_composition, pos_x, pos_y, opponent)
    huosan_num_opponent = huosan(copy_composition, pos_x, pos_y, opponent)
    miansan_num_opponent = miansan(copy_composition, pos_x, pos_y, opponent)
    huoer_num_opponent = huoer(copy_composition, pos_x, pos_y, opponent)
    mianer_num_opponent = mianer(copy_composition, pos_x, pos_y, opponent)
    sisi_num_opponent = sisi(copy_composition, pos_x, pos_y, opponent)
    sisan_num_opponent = sisan(copy_composition, pos_x, pos_y, opponent)
    sier_num_opponent = sier(copy_composition, pos_x, pos_y, opponent)

    if lianwu_num_opponent >= 1:
        value += 100000 * 10
    elif huosi_num_opponent >= 1:
        value += 100000 * 10
    elif chongsi_num_opponent >= 2 or (chongsi_num_opponent >= 1 and huosan_num_opponent >= 1):
        value += 50000 * 2
    elif huosan_num_opponent >= 2:
        value += 5000 * 2
    elif huosan_num_opponent >= 1 and miansan_num_opponent >= 1:
        value += 1000 * 2
    elif huosan_num_opponent >= 1:
        value += 200 * 2
    elif huoer_num_opponent >= 2:
        value += 100 * 2
    elif miansan_num_opponent >= 1:
        value += 50 * 2
    elif huoer_num_opponent >= 1 and mianer_num_opponent >= 1:
        value += 10 * 2
    elif huoer_num_opponent >= 1:
        value += 5 * 2
    elif mianer_num_opponent >= 1:
        value += 3 * 2
    elif sisi_num_opponent >= 1 or sisan_num_opponent >= 1 or sier_num_opponent >= 1:
        value += -5 * 2

    value += position_value[pos_x - 1][pos_y - 1]

    return value
