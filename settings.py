class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """инициализация параметров игры"""
        #параметры экрана
        self.screen_widht = 1920
        self.screen_height = 1080
        self.bg_color = (23, 36, 53) 
        # параметры корабля
        self.ship_speed = 1.5
        # Параметры стрельбы
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bulet_color = (60, 60, 60)
        