from typing import Dict, Optional

from logic.resources import *
from objects.base import BaseObject


class Image(BaseObject):
    def __init__(self, path: str, x: int, y: int, resize_params: Optional[Dict[str, int]] = None):
        self.image = ResourceLoader.load_image(path).resource
        if resize_params is not None:
            self.__resize(resize_params['width'], resize_params['height'])
        r = self.image.get_rect()
        BaseObject.__init__(self, x, y, r.width, r.height)

    def __resize(self, width: int, height: int):
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen):
        screen.blit(self.image, self.rect)