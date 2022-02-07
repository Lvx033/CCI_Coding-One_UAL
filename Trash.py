import pygame, random
import constants


class Trash(pygame.sprite.Sprite):
    def __init__(self, x, y, opt):
        super(Trash, self).__init__()

        if opt == 1:
            self.image = pygame.image.load('assets/can.png')
            self.image = pygame.transform.scale(self.image, (self.image.get_width() + 10, self.image.get_height() + 10))
            self.hp = 1
            self.score = 1
        elif opt == 2:
            self.image = pygame.image.load('assets/satellite.png')
            self.hp = 3
            self.score = 3
        elif opt == 3:
            self.image = pygame.image.load('assets/trash bag.png')
            self.image = pygame.transform.scale(self.image, (self.image.get_width() + 15, self.image.get_height() + 15))
            self.hp = 2
            self.score = 2
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = self.rect.x
        self.y = self.rect.y


    def update(self):

        constants.screen.blit(self.image, (self.rect.x, self.rect.y))
#        pygame.draw.rect(constants.screen, constants.WHITE, self.rect, 1)
        if self.hp == 0:
            self.kill()
        if self.rect.y >= constants.WIDTH:
            self.kill()


# *****************************STARS************************************************************

class Star(pygame.sprite.Sprite):
    def __init__(self, x, factor):
        super(Star, self).__init__()
        self.image = pygame.image.load('assets/star.jpg')
        self.image = pygame.transform.scale(self.image, ((self.image.get_width()/factor), (self.image.get_height()/factor)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, -10)
        self.x = self.rect.x
        self.y = self.rect.y
        self.speed = random.randrange(1, 3, 1)


    def update(self):
        constants.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.y += self.speed
