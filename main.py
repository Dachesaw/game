import sys
import pygame
from settings import Settings
from ship import Ship

class AliensInvasion:
    """Класс для управления ресурасами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_widht = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = (self.settings.bg_color)
        pygame.display.set_caption('ANIME ALIENS')
        
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # Отслеживание клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            # Отображение последнего отрисованного экрана
            pygame.display.flip()    


if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AliensInvasion()
    ai.run_game()