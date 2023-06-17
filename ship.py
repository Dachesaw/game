import pygame


class Ship():
    """класс для управления кораблем"""
    def __init__(self, ai_game):
        """инициализация атрибутов корабля и его позиции"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
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
        # 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """обновляет позицию корабля с учетом флага"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
