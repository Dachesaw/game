import pygame
from pygame.sprite import _Group, Sprite

class Bullet(Sprite):
    """Класс для управления пулями вылетающими из корабля"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Создание пули в позиции (0, 0) и назначение начальной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # позиция пули в вещесвенной переменной
        self.y = float(self.rect.y)