from typing import Any
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
    
    
    def update(self):
        """Перемещает снаряд по экрану"""
        # Обновление позиции снаряда в вещественном формате
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника
        self.rect.y = self.y
        
    
    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)