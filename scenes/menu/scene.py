import pygame

from logic.sound import Sound
from objects.buttons import Button
from scenes.base import BaseScene
from settings import Settings


class MenuScene(BaseScene):
    PROCESS_ESCAPE = False

    def set_up_objects(self):
        self.button_editor = Button("50%", "50%", 200, 50,
                                    "Editor",
                                    lambda: Settings.set_scene(Settings.SCENES.EDITOR), hover_sound=Sound("data/sounds/select_sound.wav"),
                                    font=pygame.font.Font(None, 30))
        self.objects.append(self.button_editor)

    def additional_process_event(self, event):
        self.mouse_particle_event(event)
