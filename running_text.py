import asyncio
# import mcpi.minecraft as minecraft

import letters as letters


async def main():
    # task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(start_running_text_in_mc())

    await asyncio.gather(task2)


async def print_nums():
    num = 1
    while True:
        print("Прошло 5 секунд")
        num += 1
        await asyncio.sleep(5)


async def start_running_text_in_terminal():
    await run_let.start()


async def start_running_text_in_mc():
    run_let = MCRunningLine(-222, 143, 100, ("xy", -10, -9))
    run_let.set_timeout(0.2)
    run_let.set_color(back=[0, 0], letter=[35, 1])
    run_let.draw_board()
    run_let.set_text('ннннннннннн')
    await run_let.start()


class RunningLine:
    def __init__(self, width, height, pause):
        self.width = width
        self.height = height
        self.pause = pause

        self.pixels_of_text = []

    def set_timeout(self, timeout: float):
        self.pause = timeout

    def set_text(self, text: str) -> None:
        # обновляем список пикселей
        self.pixels_of_text = []

        # добавляем нужные пиксели букв в общий список
        for letter in text:
            letter = letter.lower()
            # проверяем, все ли буквы есть в алфавите
            assert letter in letters.ALPHABET, f"Символа '{letter}' нет в словаре доступных символов"

            pixel_of_letter = self._convert_letter_to_size(letter)

            for lt in pixel_of_letter:
                self.pixels_of_text.append(lt)
            self.pixels_of_text.append(letters.ALPHABET.get(" ")[0])  # пробел между буквами

    def _convert_letter_to_size(self, letter):
        pixel_of_letter = []
        instruction = letters.ALPHABET.get(letter)
        width_ins = instruction['width'].split(' ')

        if width_ins[0] == '-':
            width_letter = self.height - int(width_ins[1])
        elif width_ins[0] == '*':
            width_letter = self.height * int(width_ins[1])

        edge_ins = instruction['edge'].split(' ')
        center_ins = instruction['center'].split(' ')
        width_without_edge = width_letter - 2

        for w in range(width_letter):
            pixel_of_letter.append([])
            if w == 0 or w == width_letter - 1:
                if edge_ins[0] == '*':
                    for _ in range(self.height):
                        pixel_of_letter[w].append(1)
                else:
                    pass

            else:
                if center_ins[0] == '*':
                    pass
                elif center_ins[0] == '//':
                    for h in range(self.height):
                        if h == self.height // int(center_ins[1]):
                            pixel_of_letter[w].append(1)
                        else:
                            pixel_of_letter[w].append(0)

        return pixel_of_letter


class ConsoleRunningLine(RunningLine):
    def __init__(self, width, height, pause):
        super().__init__(width, height, pause)

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


class MCRunningLine(RunningLine):
    def __init__(self, right_x, up_y, right_z, coord_width_height: tuple, pause: float = 0.5):

        # self.craft = minecraft.Minecraft.create()

        self._check_parametrize(coord_width_height)

        self._width = coord_width_height[1]
        self._height = coord_width_height[2]

        super().__init__(abs(self._width), abs(self._height), pause)

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
        if block:  # пиксель буквы
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
