import pygame


class Ship():
    """класс для управления кораблем"""
    def __init__(self, ai_game):
        """инициализация атрибутов корабля и его позиции"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/test_ufo.bmp')
        self.rect = self.image.get_rect()
        # Корабль появляеться у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom
    

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)