import cv2
import numpy as np
import time
from mcpi.minecraft import Minecraft

colours = {(255, 255, 255): (35, 0),
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


def take_img(size: tuple):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, img = cap.read()
    resize_img = cv2.resize(img, size)
    rgb_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)
    return rgb_img


class MineServ:
    def __init__(self):
        self.mc = Minecraft.create()
        self.mc.postToChat('create')
        self.x, self.y, self.y = 29, 160, 305
        self.take_img((60, 50))

    def take_img(self, size):
        self.img = take_img(size)

    def print_img(self):
        for i, img_column in enumerate(self.img):
            for j, img_pixel in enumerate(img_column):
                print(j)
                print(img_pixel)


if __name__ == '__main__':
    MineServ().print_img()
