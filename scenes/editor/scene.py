import pygame

from logic import Sound
from objects.buttons import Button
from objects.image import Image
from scenes.base import BaseScene


class EditorScene(BaseScene):
    PROCESS_ESCAPE = True

    def __init__(self):
        super().__init__()
        self.background = Image("data/images/editor_background.png", 0, 0)
        self.hide_right_menu = Button("50%", "50%", 200, 50,
                                      "Спрятать ->",
                                      self.hide, hover_sound=Sound("data/sounds/select_sound.wav"),
                                      font=pygame.font.Font(None, 30))

        self.objects.append(self.background)
        self.objects.append(Button("4%", "10%", 80, 80, "", self.btn1, None, "data/images/btn1.png"))
        self.objects.append(Button("4%", "30%", 80, 80, "", self.btn2, None, "data/images/btn2.png"))
        self.objects.append(Button("4%", "50%", 80, 80, "", self.btn3, None, "data/images/btn3.png"))
        self.objects.append(Button("4%", "70%", 80, 80, "", self.btn4, None, "data/images/btn4.png"))
        self.objects.append(Button("4%", "90%", 80, 80, "", self.btn5, None, "data/images/btn5.png"))

    def hide(self):
        ...

    def btn1(self):
        print(1)

    def btn2(self):
        print(2)

    def btn3(self):
        print(3)

    def btn4(self):
        print(4)

    def btn5(self):
        print(5)
