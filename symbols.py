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


def from_up_to_bottom(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == order_col:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


def t_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    for h in range(height):
        if h == 0:
            pix_column.append(symbol_id[0])
        else:
            pix_column.append(symbol_id[1])
    return pix_column


def from_up_and_bottom_to_center(pix_column: list, height: int, symbol_id, order_col) -> list:
    print('fupabottocen')
    print(order_col, (height // 2))
    if order_col > (height // 2):
        for h in range(height):
            if h == ((height // 2) - (height - order_col)):
                pix_column.append(symbol_id[0])
            elif h == ((height // 2) + (height - order_col)):
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
        return pix_column


def from_center_to_up_and_bottom(pix_column: list, height: int, symbol_id, order_col) -> list:
    print('fcenttoupandb')
    print(height - order_col, (height // 2))
    if height - order_col > (height // 2):
        for h in range(height):
            if h == ((height // 2) - order_col):
                pix_column.append(symbol_id[0])
            elif h == ((height // 2) + order_col):
                pix_column.append(symbol_id[1])
            else:
                pix_column.append(0)
        return pix_column


def up_and_bottom(pix_column: list, height: int, symbol_id, order_col) -> list:
    print('upandbot')
    for h in range(height):
        if h == 0:
            pix_column.append(symbol_id)
        elif h == height - 1:
            pix_column.append(symbol_id)
        else:
            pix_column.append(0)
    return pix_column


ID_SYMBOLS = {0: '.',
              1: '|',
              2: '-',
              3: '/',
              4: '\\',
              5: '~',
              6:'{'}

INSTRUCT = {'all': all_fill,
            'center': center_place,
            'up': up_place,
            't-center': t_center,
            'from_bottom_to_up': from_bottom_to_up,
            'from_center_to_up_and_bottom': from_center_to_up_and_bottom,
            'from_up_and_bottom_to_center': from_up_and_bottom_to_center,
            'up_and_bottom': up_and_bottom}

# in instruction
#   first list: percent of all width
#   second list: id added symbols
#   third list: instruction added symbols

ALPHABET = {' ': [[1], [0], ['all']],

            '!': [[1, 1, 1, 0, 1]],
            ',': [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0]],
            '-': [[1], [2], ['center']],

            'а': [[0, 1, 1, 1, 1], [1, 0, 1, 0, 0], [0, 1, 1, 1, 1]],
            'б': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1]],
            'в': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1]],
            'г': [[0.2, 2], [1, 2], ['all', 'up']],
            'д': [[0, 0, 0, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 1]],
            'е': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]],

            'и': [[0.2, 1, 0.2], [1, 3, 1], ['all', 'from_bottom_to_up', 'all']],
            'к': [[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 1], [1, 0, 0, 0, 1]],
            'л': [[0, 0, 0, 0, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]],
            'м': [[1, 1, 1, 1, 1], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1]],

            'н': [[0.2, 2, 0.2], [1, 2, 1], ['all', 'center', 'all']],
            #
            'о': [[0.2, 0.8, 0.6, 0.8, 0.2], [1, [3, 4], 2, [4, 3], 1],
                  ['center', 'from_center_to_up_and_bottom', 'up_and_bottom', 'from_up_and_bottom_to_center',
                   'center']],
            'п': [[0.2, 2, 0.2], [1, 2, 1], ['all', 'up', 'all']],
            'р': [[1, 1, 1, 1, 1], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0]],
            'с': [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]],
            'т': [[1, 0.2, 1], [2, [2, 1], 2], ['up', 't-center', 'up']],
            'у': [[1, 1, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 1, 1, 1]],
            'ф': [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0]],
            'х': [[1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 1]],
            'ч': [[1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1]],
            'ь': [[1, 1, 1, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 1]],
            'я': [[0, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 1, 1, 1]],

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
