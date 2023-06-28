import pygame
from pygame.sprite import _Group, Sprite

class Aliens(Sprite):
    """Класс, Предстовления пришельца"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # Загрузка изображения пришельца и назначения атрибута rect
        self.image = pygame.image.load('img/alien_test.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляеться в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)