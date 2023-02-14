import pygame
import time

from scenes import *
from logic.resources import *
from settings import Settings
from objects import Button


class Application:
    def __init__(self, screen):
        self.screen = screen
        self.virtual_screen = pygame.Surface(screen.get_size())
        self.game_over = False

        ResourceLoader.setup(ResourceLoader.generate_raw_resource_dict("."))
        ResourceLoader.load()
        self.scenes = [
            MenuScene(),
            EditorScene(),
        ]
        print(ResourceLoader.loaded)

        time.sleep(0.5)

    def scene_activate(self):
        Settings.scene_changed = False
        self.scenes[Settings.scene_index].activate()

    def scene_event(self):
        for event in pygame.event.get():
            Settings.window_width, Settings.window_height = self.screen.get_size()
            if hasattr(event, "pos"):
                event.pos = Settings.translate_coords(*event.pos)
            self.process_application_exit(event)
            self.scenes[Settings.scene_index].process_event(event)

    def process_application_exit(self, event):
        if event.type != pygame.QUIT:
            return
        self.game_over = True

    def scene_logic(self):
        self.scenes[Settings.scene_index].process_logic()

    def scene_draw(self):
        self.virtual_screen.fill(Settings.BACKGROUND_COLOR)
        self.scenes[Settings.scene_index].process_draw(self.virtual_screen)
        scaled = pygame.transform.scale(self.virtual_screen, self.screen.get_size())
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()

    def process_frame(self):
        self.scene_event()
        if Settings.scene_changed:
            self.scene_activate()
            return
        self.scene_logic()
        self.scene_draw()
        pygame.time.wait(3)

    def run(self):
        while not self.game_over:
            self.process_frame()