import pygame
import constants

class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, max_width_bullet_can_go, opt):
        super(Player_Bullet, self).__init__()
        if opt == 1:
            self.image = pygame.image.load('assets/laserBlue03.png')  # get the img
        elif opt == 2:
            self.image = pygame.image.load('assets/laserGreen05.png')  # get the img

        self.image = pygame.transform.flip(self.image, True, False)  # flip the img as its the other way round raw
        self.key = self.image.get_at((0, 0))  # get the mask to remove from the img (the white stuff) at the top corner
        self.image.set_colorkey(self.key)  # set the key from above to remove, the key color in the img gets deleted
        self.rect = self.image.get_rect(center=pos)  # get the rect of the img for collision detection
        self.speed = speed  # set the bullet speed which you get from params
        self.width_constraint = max_width_bullet_can_go  # max width after which the bullet is deleted

    def destroy(self):
        if self.rect.x < 0:
            self.kill()

    def update(self):
        self.rect.y -= self.speed  # move the bullet along
        self.destroy()




class player(pygame.sprite.Sprite):
    def __init__(self, x, y, opt, speed):
        super(player, self).__init__()

        if opt == 1:
            self.image = pygame.image.load('assets/playerShip1_blue.png')
            self.image = pygame.transform.scale(self.image,(self.image.get_width()/2 + 20,self.image.get_height() /2 + 20))
            self.life = pygame.image.load('assets/playerLife1_blue.png')
        elif opt == 2:
            self.image = pygame.image.load('assets/playerShip1_green.png')
            self.image = pygame.transform.scale(self.image,(self.image.get_width()/2 + 20,self.image.get_height() /2 + 20))
            self.life = pygame.image.load('assets/playerLife1_green.png')


        self.hp = 15
        self.hp_pics = []
        for i in range(16):
            bar = pygame.image.load(f'assets/Health bar/Health bar{i}.png')
            bar = pygame.transform.scale(bar,(bar.get_width() * 0.3, bar.get_height() * 0.3))
            self.hp_pics.append(bar)



        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.x = self.rect.x
        self.y = self.rect.y

        self.opt = opt

        self.speed = speed

        self.score = 0

        self.lives = 2
        self.font = pygame.font.SysFont('Timesnewroman', 21)


        self.can_shoot = True  # A var that decides if we can shoot

        # We want some cool down for which we are allowed to shoot again, if we dont have it, if you press space it'll emit a stream of bullets
        self.cooldown = 10  # Max cooldown(cd) we have to count to, to be able to shoot again, bigger val = longer wait time

        self.current_cooldown_count = 0  # Var used to see where we are in our count to the cd, if curr cd == cd we can shoot again

        self.player_bullets = pygame.sprite.Group()


    def draw_hp(self):
        if self.opt == 1:
            constants.screen.blit(self.hp_pics[self.hp],(10,80))
        elif self.opt == 2:
            constants.screen.blit(self.hp_pics[self.hp],(680,80))




    def shoot(self):
        # fire the bullet, add the bullet to the sprite group, pos is rect.center because we want the bullet to come
        # from the plane speed = speed at which the player bullet travels max width = the max dist after which to
        # kill the bullet you will see the pygame.mixer.Channel(2).play(XYZ) line again shortly, we need to have
        # channels to play out from if we have several sounds playing at once we wont hear them as they'll cancel out
        # hence we need different channels to play audio from so they don't cancel, default is 7
        print('fired bullet')
        self.player_bullets.add(Player_Bullet(pos=self.rect.center, speed=20, max_width_bullet_can_go=constants.WIDTH, opt=self.opt))
        self.can_shoot = False

    def reload(self):
        # so here we start our count from 0...cd, when we reach cd we can shoot again, you can
        # print(self.current_cooldown_count) to see the counting process
        if self.current_cooldown_count <= self.cooldown:
            self.current_cooldown_count += 1
            self.can_shoot = False
        else:
            self.can_shoot = True
            self.current_cooldown_count = False



    def show_text(self):
        titleScore = f'P1 Score: {self.score}'if self.opt == 1 else f'P2 Score: {self.score}'
        text1 = self.font.render(titleScore,True,(constants.WHITE))

        titleLives = 'P1 Lives'if self.opt == 1 else 'P2 Lives'
        text2 = self.font.render(titleLives,True,(constants.WHITE))

        if self.opt == 1:
            constants.screen.blit(text1,(10,10))
            constants.screen.blit(text2,(10,50))
        elif self.opt == 2:
            constants.screen.blit(text1,(630,10))
            constants.screen.blit(text2, (630, 50))


    def show_lives(self):

        if self.opt == 1:
            if self.lives == 2:
                constants.screen.blit(self.life,(90,50))
                constants.screen.blit(self.life,(130,50))
            elif self.lives == 1:
                constants.screen.blit(self.life,(90,50))

        if self.opt == 2:
            if self.lives == 2:
                constants.screen.blit(self.life,(750,50))
                constants.screen.blit(self.life,(710,50))
            elif self.lives == 1:
                constants.screen.blit(self.life,(710,50))





    def update(self):

        self.draw_hp()

        self.show_lives()

        self.show_text()

        constants.screen.blit(self.image, (self.rect.x, self.rect.y))

#        pygame.draw.rect(constants.screen,(constants.WHITE),self.rect,1)

        pressed_key = pygame.key.get_pressed()

        if self.opt == 2:
            if pressed_key[pygame.K_LEFT]:
                self.rect.x -= self.speed
            elif pressed_key[pygame.K_RIGHT]:
                self.rect.x += self.speed

        if self.opt == 1:
            if pressed_key[pygame.K_a]:
                self.rect.x -= self.speed
            elif pressed_key[pygame.K_d]:
                self.rect.x += self.speed


        if self.opt == 1:
            if pressed_key[pygame.K_SPACE] and self.can_shoot:  # if space is pressed and you can shoot, SHOOT!
                self.shoot()
        elif self.opt == 2:
            if pressed_key[pygame.K_RETURN] and self.can_shoot:  # if space is pressed and you can shoot, SHOOT!
                self.shoot()

        if self.can_shoot == False:  # if we cant shoot we reload our gun
            self.reload()


       # **************** loc **********************
        # reset the loc if you exceed the window (Y)
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y + self.rect.height >= constants.WIDTH:
            self.rect.y = constants.WIDTH - self.rect.height

        # reset the loc if you exceed the window (X)
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width >=constants.WIDTH:
            self.rect.x = constants.WIDTH - self.rect.width


