import pygame


class Ship():
    """класс для управления кораблем"""
    def __init__(self, ai_game):
        """инициализация атрибутов корабля и его позиции"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('img/spaceship_prototype.bmp')
        self.rect = self.image.get_rect()
        # Корабль появляеться у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom
        # Флаги движения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """обновляет позицию корабля с учетом флага"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
