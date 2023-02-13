from enum import Enum

import pygame

from logic.field import Field
from particles import ParticleContainer


class SceneIndexes(Enum):
    MENU = 0
    EDITOR = 1


class Settings:
    BASE_WINDOW_WIDTH = window_width = 1280
    BASE_WINDOW_HEIGHT = window_height = 720
    CELL_SIZE = 40
    SCENES = SceneIndexes
    BACKGROUND_COLOR = pygame.Color('white')
    PARTICLES = ParticleContainer()
    scene_changed = True
    scene_index = 0
    VOLUME = 10
    nickname = "Player"

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.scene_index = index.value

    @staticmethod
    def update_settings():
        ...

    @staticmethod
    def set_scene_no_activate(index):
        Settings.scene_index = index.value

    @staticmethod
    def translate_coords(x, y):
        return x * Settings.BASE_WINDOW_WIDTH / Settings.window_width, y * Settings.BASE_WINDOW_HEIGHT / Settings.window_height


Settings.field = Field("data/levels/field.txt", Settings)
