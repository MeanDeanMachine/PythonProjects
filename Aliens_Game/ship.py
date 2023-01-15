import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        '''Initialize the ship and set its starting position'''
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom corner of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Ship speed settings
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update ship's position based on if its moving right'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''Center the ship on the screen'''
        self.center = self.screen_rect.centerx