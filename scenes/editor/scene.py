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
        self.btn1 = Button("4%", "10%", 80, 80, "", self.btn1, None, "data/images/btn1.png" )
        self.objects.append(self.background)
        self.objects.append(self.btn1)

    def hide(self):
        ...

    def btn1(self):
        ...
