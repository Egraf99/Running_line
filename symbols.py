def comma(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h >= height - height // 4:
            if h == height - height // 4:
                pix_column.append(symbol_id[0])
            elif h == (height - order_col):
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
        else:
            pix_column.append(0)
    return pix_column


def all_fill(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        pix_column.append(symbol_id)
    return pix_column


def up_place(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == 0:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def bottom_place(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == height - 1:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def bottom_minus_one(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h > height - height // 3 and h != height - 1:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def center_place(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == (height // 2):
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def from_bottom_to_up(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == (height - order_col):
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def from_bottom_to_up_with_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if order_col <= height // 2:
            if h == (height - order_col):
                pix_column.append(symbol_id[0])
            else:
                pix_column.append(0)
        else:
            if h == (height - order_col):
                pix_column.append(symbol_id[0])
            elif h == height // 2:
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
    return pix_column


def from_up_to_bottom(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == order_col - 1:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def from_up_to_bottom_with_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if order_col > height // 2:
            if h == order_col - 1:
                pix_column.append(symbol_id[0])
            else:
                pix_column.append(0)
        else:
            if h == order_col - 1:
                pix_column.append(symbol_id[0])
            elif h == height // 2:
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
    return pix_column


def all_fill_except_first(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == 0:
            pix_column.append(symbol_id[0])
        else:
            pix_column.append(symbol_id[1])
    return pix_column


def from_up_and_bottom_to_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    if height > order_col > (height // 2):
        for h in range(height):
            if h == ((height // 2) - (height - order_col)):
                pix_column.append(symbol_id[0])
            elif h == ((height // 2) + (height - order_col)):
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
        return pix_column


def from_up_and_bottom_to_center_except_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    if height > order_col > (height // 2):
        for h in range(height):
            if h < height // 3 or h >= height - height // 3:
                if h == ((height // 2) - (height - order_col)):
                    pix_column.append(symbol_id[0])
                elif h == ((height // 2) + (height - order_col)):
                    pix_column.append(symbol_id[1])
                else:
                    pix_column.append(0)
            else:
                pix_column.append(0)
        return pix_column

def from_up_and_center_to_third(pix_column: list, height: int, symbol_id, order_col) -> list:
    if height > order_col > (height // 2):
        for h in range(height):
            if h <= height // 2 and height - order_col >= height //4:
                if h == ((height // 2) - (height - order_col)):
                    print(((height // 2) - (height - order_col)))
                    pix_column.append(symbol_id[0])
                elif h == (height - order_col):
                    print('/')
                    print((height - order_col))
                    pix_column.append(symbol_id[1])
                else:
                    pix_column.append(0)
            else:
                pix_column.append(0)
        return pix_column


def from_up_to_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    if height > order_col > (height // 2):
        for h in range(height):
            if h == ((height // 2) - (height - order_col)):
                pix_column.append(symbol_id[0])

            else:
                pix_column.append(0)
        return pix_column


def from_center_to_up_and_bottom(pix_column: list, height: int, symbol_id, order_col) -> list:
    if height - order_col > (height // 2):
        for h in range(height):
            if h == ((height // 2) - order_col):
                pix_column.append(symbol_id[0])
            elif h == ((height // 2) + order_col):
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
        return pix_column


def from_center_to_up(pix_column: list, height: int, symbol_id, order_col) -> list:
    if height - order_col > (height // 2):
        for h in range(height):
            if h == ((height // 2) - order_col):
                pix_column.append(symbol_id)
            else:
                pix_column.append(0)
        return pix_column


def up_and_bottom(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == 0:
            pix_column.append(symbol_id)
        elif h == height - 1:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def up_and_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == 0:
            pix_column.append(symbol_id)
        elif h == height // 2:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


ID_SYMBOLS = {0: '.',
              1: '|',
              2: '-',
              3: '/',
              4: '\\',
              5: 'к'}

INSTRUCT = {'all': all_fill,
            'all_fill_except_first': all_fill_except_first,
            'center': center_place,
            'comma': comma,
            'up': up_place,
            'bottom': bottom_place,
            'bottom_minus_one': bottom_minus_one,
            'from_bottom_to_up': from_bottom_to_up,
            'from_up_to_bottom': from_up_to_bottom,
            'from_bottom_to_up_with_center': from_bottom_to_up_with_center,
            'from_up_to_bottom_with_center': from_up_to_bottom_with_center,
            'from_center_to_up_and_bottom': from_center_to_up_and_bottom,
            'from_up_and_bottom_to_center': from_up_and_bottom_to_center,
            'from_up_and_center_to_third': from_up_and_center_to_third,
            'from_up_and_bottom_to_center_except_center': from_up_and_bottom_to_center_except_center,
            'from_center_to_up': from_center_to_up,
            'up_and_bottom': up_and_bottom,
            'up_and_center': up_and_center}

# in instruction
#   first list: percent of all width
#   second list: id added symbols
#   third list: instruction added symbols

ALPHABET = {' ': [[1], [0], ['all']],

            '!': [[1, 1, 1, 0, 1]],  # !!!

            ',': [[0.2, 0.2], [3, 1], ['bottom', 'bottom_minus_one']],
            '-': [[1], [2], ['center']],

            'а': [[1, 0.2, 1], [[3, 2], 2, [4, 2]],
                  ['from_bottom_to_up_with_center', 'up_and_center', 'from_up_to_bottom_with_center']],
            'б': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1]],  # !!!
            'в': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1]],  # !!!
            'г': [[0.2, 2], [[3, 1], 2], ['all_fill_except_first', 'up']],
            'д': [[0, 0, 0, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 1]],  # !!!
            'е': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]],  # !!!

            'и': [[0.2, 1, 0.2], [1, 3, 1], ['all', 'from_bottom_to_up', 'all']],
            'к': [[0.2, 0.2, 1], [1, 2, [3, 4]],
                  ['all',
                   'center', 'from_center_to_up_and_bottom']],
            'л': [[1, 1, 0.2], [3, 2, [4, 1]],
                  ['from_bottom_to_up',
                   'up', 'all_fill_except_first']],
            'м': [[1, 1, 1, 1, 1], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1]],  # !!!

            'н': [[0.2, 2, 0.2], [1, 2, 1], ['all', 'center', 'all']],

            'о': [[0.2, 1, 0.6, 1, 0.2], [1, [3, 4], 2, [4, 3], 1],
                  ['center', 'from_center_to_up_and_bottom', 'up_and_bottom', 'from_up_and_bottom_to_center',
                   'center']],
            'п': [[0.2, 2, 0.2], [[3, 1], 2, [4, 1]], ['all_fill_except_first', 'up', 'all_fill_except_first']],
            'р': [[0.2, 1,1], [[3, 1], 2, [4,3]], ['all_fill_except_first', 'up_and_center', 'from_up_and_center_to_third']],  # !!!
            'с': [[0.2, 1, 0.6, 1], [1, [3, 4], 2, [4, 3]],
                  ['center', 'from_center_to_up_and_bottom', 'up_and_bottom',
                   'from_up_and_bottom_to_center_except_center']],
            'т': [[1, 0.2, 1], [2, [2, 1], 2], ['up', 'all_fill_except_first', 'up']],
            'у': [[1, 0.2, 1], [[4, 3], 3, 3],
                  ['from_up_and_bottom_to_center',
                   'center', 'from_center_to_up']],
            'ф': [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0]],  # !!!

            'х': [[1, 0.2, 1], [[4, 3], 1, [3, 4]],
                  ['from_up_and_bottom_to_center',
                   'center', 'from_center_to_up_and_bottom']],
            'ч': [[1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1]],  # !!!
            'ь': [[1, 1, 1, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 1]],  # !!!
            'я': [[0, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 1, 1, 1]],  # !!!

            }

COLOURS = {(255, 255, 255): (35, 0),
           (220, 95, 0): (35, 1),
           (170, 47, 160): (35, 2),
           (35, 135, 200): (35, 3),
           (240, 175, 20): (35, 4),
           (95, 170, 25): (35, 5),
           (210, 100, 140): (35, 6),
           (55, 55, 60): (35, 7),
           (124, 124, 114): (35, 8),
           (22, 118, 136): (35, 9),
           (100, 30, 155): (35, 10),
           (45, 45, 140): (35, 11),
           (95, 60, 30): (35, 12),
           (72, 90, 36): (35, 13),
           (140, 32, 32): (35, 14),
           (0, 0, 0): (35, 15)}
