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
        self.screen = pygame.display.set_mode((self.settings.screen_widht, self.settings.screen_height))
        self.settings.screen_widht = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = (self.settings.bg_color)
        self.ship = Ship(self)
        
        
        pygame.display.set_caption('ANIME ALIENS')


    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_ivents()
            self.ship.update()
            self._update_screen()


    def _check_ivents(self):
        # Отслеживание клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                
            
    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()  # Отображение последнего отрисованного экрана    


if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AliensInvasion()
    ai.run_game()