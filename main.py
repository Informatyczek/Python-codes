# upewnij się ,że masz zainstalowane pygame
#strzelasz alt
from game import *
import pygame
import sys

pygame.font.init()
pygame.mixer.init()

def main():
    RED_HIT_1 = pygame.USEREVENT + 2
    RED_HIT_2 = pygame.USEREVENT + 3
    RED_HIT_3 = pygame.USEREVENT + 4
    RED_HIT_4 = pygame.USEREVENT + 5
    RED_HIT_5 = pygame.USEREVENT + 6
    RED_HIT_6 = pygame.USEREVENT + 7
    RED_HIT_7 = pygame.USEREVENT + 8
    RED_HIT_8 = pygame.USEREVENT + 9
    RED_HIT_9 = pygame.USEREVENT + 10
    RED_HIT_10 = pygame.USEREVENT + 11
    RED_HIT_11 = pygame.USEREVENT + 12
    RED_HIT_12 = pygame.USEREVENT + 13


    RED_HITS = [RED_HIT_1,RED_HIT_2,RED_HIT_3,RED_HIT_4,RED_HIT_5,RED_HIT_6,RED_HIT_7,RED_HIT_8,RED_HIT_9,RED_HIT_10,RED_HIT_11,RED_HIT_12]


    red = Red(red_speed,red_speed_shoot)  #pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red2 = Red(red_speed,red_speed_shoot)
    red3 = Red(red_speed,red_speed_shoot)
    red4 = Red(red_speed,red_speed_shoot)
    red5 = Red(red_speed,red_speed_shoot)
    red6 = Red(red_speed,red_speed_shoot)
    red7 = Red(red_speed,red_speed_shoot)
    red8 = Red(red_speed,red_speed_shoot)
    red9 = Red(red_speed,red_speed_shoot)
    red9 = Red(red_speed,red_speed_shoot)
    red10 = Red(red_speed,red_speed_shoot)
    red11 = Red(red_speed,red_speed_shoot)
    red12 = Red(red_speed,red_speed_shoot)
    unused_ships = [red4,red5,red6,red7]
    red_ships_fleet = [red,red2,red3]


    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []


    yellow_health = 10

    clock = pygame.time.Clock()
    game_start_time = pygame.time.get_ticks()
    run = True
    POINTS = 0
    while run:

        elapsed_time = (pygame.time.get_ticks() - game_start_time) // 1000
        red_speed_accereration(elapsed_time, red_ships_fleet)
        red_bullet_accereration(elapsed_time, red_ships_fleet)

        clock.tick(FPS)
        make_more_enemies(elapsed_time, red_ships_fleet, unused_ships)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

            run = if_game_quit(event, run)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    shoot_bullet(yellow, yellow_bullets, MAX_BULLETS, BULLET_FIRE_SOUND)

            shot_red_bullet(red_ships_fleet, red_bullets, MAX_BULLETS, BULLET_FIRE_SOUND)

            i=0
            for red in red_ships_fleet:
                if event.type == RED_HITS[i]:
                    red.health -= 1
                    BULLET_HIT_SOUND.play()
                i+=1

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        POINTS += handel_death_red(red_ships_fleet,POINTS)




        if yellow_health <= 0:
            draw_window(red_ships_fleet, yellow, red_bullets, yellow_bullets,
                        yellow_health, POINTS, elapsed_time,1)
            return 0


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(red_ships_fleet)
        handle_bullets(yellow_bullets, red_bullets, yellow,red_ships_fleet,RED_HITS)


        draw_window(red_ships_fleet, yellow, red_bullets, yellow_bullets,yellow_health, POINTS,elapsed_time,0)




if __name__ == "__main__":
    main()



