import sys
import pygame

class AlienInvasion:
    """Класс для управления ресурасами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()


        self.screen = pygame.display.set_mode((1020, 700))
        title = 'AlienBebries'
        pygame.display.set_caption(title)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # Отслеживание клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        #отображение последнего отрисованного экрана
        pygame.display.flip()    
if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()