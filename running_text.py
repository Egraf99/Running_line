import asyncio
import itertools
# import mcpi.minecraft as minecraft

import symbols


async def main():
    pass
    # task1 = asyncio.create_task(app.App(50, 6))
    # task2 = asyncio.create_task(start_running_text_in_mc())

    # await asyncio.gather(task1)


async def print_nums():
    num = 1
    while True:
        print("Прошло 5 секунд")
        num += 1
        await asyncio.sleep(5)


async def start_running_text_in_mc():
    run_let = MCRunningLine(-222, 143, 100, ("xy", -10, -9))
    run_let.set_timeout(0.2)
    run_let.set_color(back=[0, 0], letter=[35, 1])
    run_let.draw_board()
    run_let.set_text('нннн')
    await run_let.start()


class RunningLine:
    def __init__(self, width, height, indent):
        self.width = width
        self.height = height
        self.indent = indent

        self.pixels_of_text = []

    def set_text(self, text: str) -> None:
        # обновляем список пикселей
        self.text = text
        self.pixels_of_text = []

        # добавляем нужные пиксели букв в общий список
        for letter in text:
            letter = letter.lower()
            # проверяем, все ли буквы есть в алфавите
            assert letter in symbols.ALPHABET, f"Символа '{letter}' нет в словаре доступных символов"

            # подстраисваем под размер
            pixel_of_letter = self._convert_letter_to_size(letter)

            for lt in pixel_of_letter:
                self.pixels_of_text.append(lt)

            self.add_whitespace(self.indent)

        self._width_of_text = len(self.pixels_of_text)  # запоминаем ширину теста в пикселях

    def add_whitespace(self, count):
        for _ in range(count):
            # добавление пикселей пробела
            whitespace = self._convert_letter_to_size(" ")
            self.pixels_of_text.append(whitespace[0])

    def _read_ins(self, instruction):
        pass

    def _get_pixels_from_instruction(self, width, ins):
        # через пропорцию от ширины определяем, сколько столбцов занимает отдельная интсрукция столбца
        proportion = list(map(int, map(lambda x: x * width, ins[0])))
        print(proportion)
        proportion = list(itertools.accumulate(proportion))
        print(proportion)
        print()
        pixels_of_text = []

        _i = []
        for n, limit in enumerate(proportion):
            column_in_order = 0
            for i in range(limit):
                if i not in _i:
                    column_in_order += 1
                    _i.append(i)
                    column_pixels = self._place_pixel(ins[1:], n, column_in_order)
                    if column_pixels:
                        pixels_of_text.append(column_pixels)

        return pixels_of_text

    def _place_pixel(self, ins, n, order_column):
        # ins[0] - id символа
        # ins[1] - имя ключа для выполняемой функции

        pixels_column = []

        # добавляем id символа по инструкции, если она есть
        if symbols.INSTRUCT[ins[1][n]]:
            symbols.INSTRUCT[ins[1][n]](pixels_column, self.height, ins[0][n], order_column)

        # если нет, добавляем id символа-пробела
        else:
            for h in range(self.height):
                pixels_column.append(0)

        return pixels_column

    def _return_width_from_height(self, instruction) -> int:
        width_letter = 0

        if instruction[0] == '-':
            width_letter = self.height - int(instruction[1])

        elif instruction[0].isdigit():
            width_letter = self.height * int(instruction[0])

        return width_letter

    def _convert_letter_to_size(self, letter):
        instruction = symbols.ALPHABET.get(letter)

        # если что-то пойдет не так с размерами букв, верни
        # width_ins = instruction['w_from_h'].split(' ')
        # width_letter = self._return_width_from_height(width_ins)

        # letter_instruction = instruction['instruction']

        pixels_of_text = self._get_pixels_from_instruction(self.height, instruction)

        return pixels_of_text


class QTRunningLine(RunningLine):
    def __init__(self, width, height, indent):
        super().__init__(width, height, indent)

        self.symbol_place = "|"
        self.symbol_back = "."

        self.first_column = 0
        self.width_text = 1

        self.board = []

    def update_board(self):
        for _ in range(self.height):
            self.board.append(self.symbol_back * self.width)

    def _what_symbol_place(self, place):
        return symbols.ID_SYMBOLS[place]

    def change_row_with_column(self):
        pt = self.pixels_of_text[self.first_column:self.width_text]

        if self.width_text >= self.width:
            self.first_column += 1

        # добавляем последнюю строку в область видимости
        self.width_text += 1

        if self.width_text >= len(self.pixels_of_text):
            # добавляем в конец пробел
            self.add_whitespace(self.indent)

        if self.width_text > self._width_of_text + abs(self.width):  # даем тексту уйти с поля видимости и
            # обновляем
            self.first_column, self.width_text = 0, 1
            self.set_text(self.text)

        # проходим по списку пикселей, ограниченных толькой той областью, которую нужно показывать
        for n_column, column in enumerate(pt):
            for n_row, block in enumerate(column):
                # задаем показываемый символ
                symbol = self._what_symbol_place(block)

                # и устанавливаем на необходимое место
                place = self.width - len(pt) + n_column
                self.board[n_row] = self.board[n_row][:place] + symbol + self.board[n_row][place + 1:]


class MCRunningLine(RunningLine):
    def __init__(self, right_x, up_y, right_z, coord_width_height: tuple, pause: float = 0.5, indent=1):
        self.indent = indent

        self.craft = minecraft.Minecraft.create()

        self._check_parametrize(coord_width_height)

        self._width = coord_width_height[1]
        self._height = coord_width_height[2]

        super().__init__(abs(self._width), abs(self._height), self.indent)

        self.pause = pause

        self.color_back_block = [0, 0]
        self.color_letter_block = [35, 2]

        self.x, self.y, self.z = right_x, up_y, right_z
        self._first_coord_change = coord_width_height[0][0].lower()
        self._second_coord_change = coord_width_height[0][1].lower()

    @staticmethod
    def _check_parametrize(coord_width_height):
        for i in coord_width_height[0]:
            assert i.lower() in ['x', 'y', 'z', 'х', 'у'], "Изменяемые координаты должны быть X, Y или Z"
        assert len(coord_width_height[0]) == 2, "Должно быть только 2 изменяемых координат"
        assert coord_width_height[0][0] != coord_width_height[0][1], \
            "Изменяемые координаты должны быть разные"
        assert coord_width_height[1] != 0, "Ширина дисплея не может быть 0"
        assert coord_width_height[2] != 0, "Высота дисплея не может быть 0"

    def set_color(self, back: list = None, letter: list = None) -> None:
        assert any([back, letter]), "Задайте цвет фона back или цвет букв letter"
        if back:
            assert len(back) == 2, "Цвет задается двумя числами: id блока и data блока"
            self.color_back_block = back

        if letter:
            assert len(letter) == 2, "Цвет задается двумя числами: id блока и data блока"
            self.color_letter_block = letter

    def draw_board(self) -> None:
        for height in range(self.height):
            for width in range(self.width):
                self._set_block((width,), height, self.color_back_block)

    def _what_block_place(self, block):
        if block != 0:  # пиксель буквы
            block_color = self.color_letter_block
        else:  # пустой пиксель
            block_color = self.color_back_block

        return block_color

    def _set_block(self, row: tuple, change_coord_column: int, block):
        change_coord_row = 0
        x, y, z = self.z, self.y, self.z

        if self._width < 0:
            for r in row:
                change_coord_row -= r
        elif self._width > 0:
            for r in row:
                change_coord_row += r

        if self._height < 0:
            change_coord_column = -change_coord_column

        if self._first_coord_change in ["x", "х"]:
            x = self.x + change_coord_row
        elif self._first_coord_change in ["y", "у"]:
            y = self.y + change_coord_row
        elif self._first_coord_change == "z":
            z = self.z + change_coord_row

        if self._second_coord_change in ["x", "х"]:
            x = self.x + change_coord_column
        elif self._second_coord_change in ["y", "у"]:
            y = self.y + change_coord_column
        elif self._second_coord_change in "z":
            z = self.z + change_coord_column

        self.craft.setBlock(x, y, z, block)

    def set_timeout(self, timeout: float):
        self.pause = timeout

    async def start(self):
        width_text = 1
        first_column = 0
        while True:
            await asyncio.sleep(self.pause)

            # проходим по списку пикселей, ограниченных толькой той областью, которую нужно показывать
            for n_row, column in enumerate(self.pixels_of_text[first_column:width_text]):
                for n_column, block in enumerate(column):

                    block_color = self._what_block_place(block)

                    if width_text <= self.width:  # показываемый текст меньше общей ширины
                        coord_row = (self.width, n_row, -width_text)

                    else:
                        coord_row = (n_row,)

                    self._set_block(coord_row, n_column, block_color)

            if width_text >= self.width:  # текст дошел до начала показываемой области
                # убираем первую строку за область видимости
                first_column += 1

            # добавляем последнюю строку в область видимости
            width_text += 1

            if width_text > len(self.pixels_of_text) + abs(self.width):  # даем тексту уйти с поля видимости и
                # обновляем
                first_column, width_text = 0, 0


if __name__ == "__main__":
    asyncio.run(main())
