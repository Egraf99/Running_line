import cv2
import time
from mcpi.minecraft import Minecraft
from symbols import COLOURS


def take_img(size: tuple, img=None, from_video=False):
    assert any([img, from_video]), "Показывать фото img= или брать фото от видеокамеры from_video=True"
    if from_video:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, img = cap.read()
    else:
        img = cv2.imread(img)
    resize_img = cv2.resize(img, size)
    cv2.imwrite('photo/obrab.jpg', resize_img)
    rgb_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)
    return rgb_img


class MineServ:
    def __init__(self):
        self.mc = Minecraft.create()
        self.mc.postToChat('create')
        self.x, self.y, self.z = -130, 200, 202
        size_img = (200, 160)
        self.img = take_img(size_img, img='photo/love.jpg')

    def print_img(self):
        all_colors = list(COLOURS.keys())
        for i, img_column in enumerate(self.img):
            for j, img_pixel in enumerate(img_column):
                block_color = self.find_color_of_block(all_colors, img_pixel)
                block = COLOURS[block_color]

                self.mc.setBlock(self.x - j, self.y - i + 60, self.z + 5, block)

    def clear(self):
        for i in range(500):
            for j in range(200):
                self.mc.setBlock(self.x - j, self.y - i + 60, self.z + 5, (0, 0))

    @staticmethod
    def find_color_of_block(all_rgb, rgb):
        delta = 10000000
        nearest_i = None
        for i, color_rgb in enumerate(all_rgb):
            d = abs(color_rgb[0] - rgb[0]) ** 2 + abs(color_rgb[1] - rgb[1]) ** 2 + abs(color_rgb[2] - rgb[2]) ** 2
            if d < delta:
                delta = d
                nearest_i = i
        return all_rgb[nearest_i]


if __name__ == '__main__':
    m = MineServ()
    time.sleep(3)
    m.print_img()
    time.sleep(30)
    m.clear()