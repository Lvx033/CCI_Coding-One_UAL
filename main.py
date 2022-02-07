import sys
from Trash import *
from Player import *
from constants import *
import pygame

pygame.init()

timeFont = pygame.font.SysFont('Timesnewroman', 20)
font = pygame.font.SysFont('Timesnewroman', 21)
game_end_font = pygame.font.SysFont('Timesnewroman', 40)

initial_pos_x = 100
initial_pos_y = 120

seg = 1
step = 1

trash_group = pygame.sprite.Group()
run = True


def create_trash():
    global step, seg
    while step <= 3:
        if step == 1:
            obj = Trash(initial_pos_x * seg * 1.1, initial_pos_y * step, 2)

            trash_group.add(obj)
            seg += 1
        if step == 2:
            obj = Trash(initial_pos_x * seg + 160, initial_pos_y * step, 3)
            trash_group.add(obj)
            seg += 1
        if step == 3:
            obj = Trash(initial_pos_x * seg + 170, initial_pos_y * step, 1)
            trash_group.add(obj)
            seg += 1

        if seg > 6 and step == 1:
            seg = 0
            step = 2
        if seg > 5 and step == 2:
            seg = 0
            step = 3
        if seg > 5 and step == 3:
            seg = 0
            step = 4
    step = seg = 1


create_trash()

player_group = pygame.sprite.Group()

p1 = player(x=100, y=700, opt=1, speed=8)
p2 = player(x=400, y=700, opt=2, speed=8)

player_group.add(p1, p2)

stars = pygame.sprite.Group()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
x = []
y = trash_group.copy()

game_over = True


def game_end():
    global game_over, font, clock

    while game_over:
        screen.fill(BLACK)

        level_text = font.render(f'Level {constants.current_level}', True, WHITE)
        screen.blit(level_text, (345, 10))

        p1_score = game_end_font.render(f'P1 Score: {p1.score}', True, WHITE)
        p2_score = game_end_font.render(f'P2 Score: {p2.score}', True, WHITE)

        screen.blit(p1_score, (280, 250))
        screen.blit(p2_score, (280, 450))

        for event in pygame.event.get():

            # game exit
            if event.type == pygame.QUIT:
                game_over = False
                pygame.quit()
                sys.exit()

        clock.tick(10)
        pygame.display.flip()


def main():
    time_elapsed = 0

    global run, time_limit, timex, fresh, trash_group, ADDENEMY, x, stars, player_group, clock

    switch = 0
    while run:

        screen.fill(BLACK)

        level_text = font.render(f'Level {constants.current_level}', True, WHITE)
        screen.blit(level_text, (345, 10))

        time_left_text = font.render(f'Time Left: {constants.total_time_left}s', True, (WHITE))
        screen.blit(time_left_text, (310, 50))

        # screen.blit(bubble_player, (0, 250))

        # ******************EVENT***********************

        for event in pygame.event.get():

            # game exit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == ADDENEMY:
                x_pos = random.randrange(10, WIDTH, 10)
                factor = random.randrange(2, 5, 1)
                o = Star(x_pos, factor)
                stars.add(o)

        # ----------------------------draw--------------------------------------------
        stars.draw(screen)
        stars.update()

        trash_group.draw(screen)
        trash_group.update()

        player_group.draw(screen)
        player_group.update()

        p1.player_bullets.draw(screen)
        p1.player_bullets.update()

        p2.player_bullets.draw(screen)
        p2.player_bullets.update()

        # -------------------------move trash---------------------------------------------

        for i in trash_group:
            if i.rect.x + i.rect.width >= WIDTH:
                switch = 1
                for j in trash_group:
                    j.rect.y += 2 * constants.current_level  # keep y growth according to requirement

        for i in trash_group:
            if i.rect.x <= 0:
                switch = 0
                for j in trash_group:
                    j.rect.y += 2 * constants.current_level  # keep y growth according to requirement

        if switch == 1:
            for i in trash_group:
                i.rect.x -= 1 * constants.current_level  # keep x growth according to requirement

        if switch == 0:
            for i in trash_group:
                i.rect.x += 1 * constants.current_level  # keep x growth according to requirement

        # -----------------------bullet hit trash---------------------------------------------
        p1_shot_trash = pygame.sprite.groupcollide(trash_group, p1.player_bullets, False, True)

        for i in p1_shot_trash:
            i.hp -= 1
            if i.hp <= 0:
                p1.score += i.score

        p2_shot_trash = pygame.sprite.groupcollide(trash_group, p2.player_bullets, False, True)
        for i in p2_shot_trash:
            i.hp -= 1
            if i.hp <= 0:
                p2.score += i.score

        # -------------------------trash hit player---------------------------------------------
        p1_did_get_hit_by_trash = pygame.sprite.spritecollide(p1, trash_group, True)
        if p1_did_get_hit_by_trash:
            for i in p1_did_get_hit_by_trash:
                p1.hp -= i.hp
                if p1.hp <= 0:
                    p1.lives -= 1
                    p1.hp = 15
                    if p1.lives == 0:
                        print('P1 DEAD 0 lives')
                        run = False

        p2_did_get_hit_by_trash = pygame.sprite.spritecollide(p2, trash_group, True)
        if p2_did_get_hit_by_trash:
            for i in p2_did_get_hit_by_trash:
                p2.hp -= i.hp
                if p2.hp <= 0:
                    p2.lives -= 1
                    p2.hp = 15
                    if p2.lives == 0:
                        print('P2 DEAD 0 lives')
                        run = False

        # -----------------------time ended----------------------------------------------------
        time_elapsed += 1
        if time_elapsed % 30 == 0:
            constants.total_time_left -= 1
        #            print(constants.total_time_left)

        if constants.total_time_left == 0:
            run = False

        # -----------------------trash killed-------------------------------------------------

        if len(trash_group) == 0:
            constants.current_level += 1
            print(f'Advancing to {constants.current_level}')
            create_trash()
            constants.total_time_left = 120

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()
    game_end()
