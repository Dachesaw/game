import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        
        self._create_fleet()
        
        pygame.display.set_caption('ANIME ALIENS')


    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_ivents()
            self.ship.update()
            self._update_screen()
            self._update_bullets()

            

    def _check_ivents(self):
        # Отслеживание клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _fire_bullet(self):
        """Создание нового снаряда и включения его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_alowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)        
   
   
    def _update_bullets(self):
        """Обновляет позиции снарядов и удаляет старые"""
        # Обновление позиции снарядов
        self.bullets.update()
        # Удаление снарядов вышедший за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) 

        

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)
        
        pygame.display.flip()  # Отображение последнего отрисованного экрана    
        
    
    def _create_fleet(self):
        """Создание флота вторжения"""
        # Создание пришельца и вычисление количвеста пришельцев в ряду
        # интервал между пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width = alien.rect.width
        awaible_space_x = self.settings.screen_widht - (2 * alien_width)
        number_aliens_x = awaible_space_x // (2 * alien_width)
        # Создание первого ряда пришельцев
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.alien.add(alien)

if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AliensInvasion()
    ai.run_game()