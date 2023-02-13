import pygame

from logic import ResourceLoader
from objects.base import BaseObject
from objects.button import Button as InternalButton
from settings import Settings


class Button(BaseObject):
    BUTTON_STYLE = {
        "hover_color": pygame.Color('darkgray'),
        "clicked_color": pygame.Color('black'),
        "clicked_font_color": pygame.Color('white'),
        "hover_font_color": pygame.Color('white'),
    }

    def __init__(self, x: int | str, y: int | str, width: int, height: int, title: str, action, hover_sound, image=None, **kwargs):
        if isinstance(x, str):
            x = Settings.BASE_WINDOW_WIDTH * float(x.strip("%")) / 100 - width / 2
        if isinstance(y, str):
            y = Settings.BASE_WINDOW_HEIGHT * float(y.strip("%")) / 100 - height / 2
        self.image = image
        if self.image:
            self.image = ResourceLoader.load_image(self.image).resource
        super(Button, self).__init__(x, y, width, height)
        self.internal_button = InternalButton(self.rect, pygame.Color('gray'), action, text=title, hover_sound=hover_sound, **kwargs,
                                              **self.BUTTON_STYLE)

    def event(self, event: pygame.event.Event) -> None:
        self.internal_button.check_event(event)

    def draw(self, screen: pygame.Surface) -> None:
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            self.internal_button.update(screen)
