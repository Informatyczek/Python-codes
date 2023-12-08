import pygame
import os
from random import*
from main import*
pygame.font.init()
pygame.mixer.init()



WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Odlot!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)



BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 25)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)


#red
red_speed = 5
red_speed_shoot = 4

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))




def draw_window(red_ships_fleat ,yellow, red_bullets, yellow_bullets, yellow_health, POINTS ,elapsed_time,GAME_OVER):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    health_text = ""
    for red in red_ships_fleat:
        health_text = health_text + str(red.health) + " "

    red_health_text = HEALTH_FONT.render(health_text, 1, WHITE)


    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    time_text = HEALTH_FONT.render(
         "Time: "+str(elapsed_time), 1, WHITE)

    points_text = HEALTH_FONT.render("Points: " + str(POINTS), 1, WHITE)
    WIN.blit(time_text, ((WIDTH - time_text.get_width() - 120)/2-points_text.get_width(), 10))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(points_text, (WIDTH / 2 - points_text.get_width() / 2, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    for red in red_ships_fleat:
        WIN.blit(RED_SPACESHIP, (red.rect.x, red.rect.y))


    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    if(GAME_OVER==1):
        draw_text = WINNER_FONT.render("YOUR POINTS: "+str(POINTS), 1, WHITE)
        WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                             2, HEIGHT / 2 - draw_text.get_height() / 2))


    pygame.display.update()
    if(GAME_OVER==1):
        pygame.time.delay(15000)





def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(red_ship_fleet):
    for red in red_ship_fleet:
        keys_pressed = randint(0, 10)  # losowe poruszanie sie statku
        if keys_pressed == 1 and red.rect.x - red.speed > BORDER.x + BORDER.width:  # LEFT
            red.rect.x -= red.speed
        if keys_pressed == 2 and red.rect.x + red.speed + red.rect.width < WIDTH:  # RIGHT
            red.rect.x += red.speed
        if keys_pressed == 3 and red.rect.y - red.speed > 0:  # UP
            red.rect.y -= red.speed
        if keys_pressed == 4 and red.rect.y + red.speed + red.rect.height < HEIGHT - 15:  # DOWN
            red.rect.y += red.speed






def handle_bullets(yellow_bullets, red_bullets, yellow,red_ship_fleet,RED_HITS):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        i=0
        for red in red_ship_fleet:
            if red.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HITS[i]))
                try:
                    yellow_bullets.remove(bullet)
                except:
                    pass
            elif bullet.x > WIDTH:
                try:
                    yellow_bullets.remove(bullet)
                except:
                    pass
            i += 1

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)







def if_game_quit(event, run):
    if event.type == pygame.QUIT:
        pygame.quit()
        run = False
    return run

def shoot_bullet(ship, bullets, max_bullets, bullet_sound):
    if len(bullets) < max_bullets:
        bullet = pygame.Rect(
            ship.x + ship.width, ship.y + ship.height//2 - 2, 10, 5)
        bullets.append(bullet)
        bullet_sound.play()

def shot_red_bullet(red_ship_fleet, red_bullets, MAX_BULLETS, BULLET_FIRE_SOUND):
    for Red in red_ship_fleet:
        losowa_kula = randint(Red.red_speed_shoot, 18)
        if losowa_kula == 18 or losowa_kula == 17:
            bullet = pygame.Rect(
                Red.rect.x, Red.rect.y + Red.rect.height // 2 - 2, 10, 5)
            red_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()


def red_speed_accereration(elapsed_time,red_ships_fleet):
    if(elapsed_time>60 * 2):
        red_ships_fleet[0].speed=20
        red_ships_fleet[1].speed=6
        red_ships_fleet[2].speed=6
        return
    elif (elapsed_time > 60 * 4):
        red_ships_fleet[0].speed = 10
        red_ships_fleet[1].speed = 7
        red_ships_fleet[2].speed = 7
        return
    elif (elapsed_time > 60 * 6):
        red_ships_fleet[0].speed = 12
        red_ships_fleet[1].speed = 7
        red_ships_fleet[2].speed = 7
        return

def red_bullet_accereration(elapsed_time,red_ships_fleet):
    if (elapsed_time > 60 * 2):
        red_ships_fleet[0].red_speed_shoot = 6
        red_ships_fleet[1].red_speed_shoot = 9
        red_ships_fleet[2].red_speed_shoot = 6
        return
    elif (elapsed_time > 60 * 4):
        red_ships_fleet[0].red_speed_shoot = 7
        red_ships_fleet[1].red_speed_shoot = 10
        red_ships_fleet[2].red_speed_shoot = 7
        return
    elif (elapsed_time > 60 * 6):
        red_ships_fleet[0].red_speed_shoot = 7
        red_ships_fleet[1].red_speed_shoot = 12
        red_ships_fleet[2].red_speed_shoot = 7
        return


def move_red(red):
    position_of_comming = randint(1, 5)
    if position_of_comming == 1:#gorny rog
        red.rect.x = WIDTH - 10 - SPACESHIP_WIDTH / 2
        red.rect.y = 10
    elif position_of_comming==2:#dolny rog
        red.rect.x = WIDTH - 10 - SPACESHIP_WIDTH / 2
        red.rect.y = HEIGHT - 10
    elif position_of_comming==3:#srodek
        red.rect.x = (WIDTH + 10)/1.5 + SPACESHIP_WIDTH / 2
        red.rect.y = (HEIGHT + 10)/2
    elif position_of_comming==4:#gorny przedni rog
        red.rect.x = (WIDTH + 10)/2 + SPACESHIP_WIDTH
        red.rect.y = 10
    elif position_of_comming==5:#dolny przedni rog
        red.rect.x = (WIDTH + 10)/2 + SPACESHIP_WIDTH
        red.rect.y = HEIGHT - 10

def handel_death_red(red_ships_fleat,POINTS):
    for red in red_ships_fleat:
        if red.health <= 0:
            POINTS += 1
            move_red(red)
            red.health = 10
            return 1
    return 0




def make_more_enemies(elapsed_time,red_ships_fleet,unused_ships):
    for i in range(1,5):
        if (elapsed_time > i * 20) and (len(red_ships_fleet) == 2+i):  # po 20 sekundach pojawia sie nowy statek
            red_ships_fleet.append(unused_ships[i-1])




class Red:
    def __init__(self,speed,red_speed_shoot, health=10 , x=700, y=300, width=SPACESHIP_WIDTH, height=SPACESHIP_HEIGHT):
        self.rect = pygame.Rect(x, y, width, height)
        self.health = health
        self.speed = speed
        self.red_speed_shoot = red_speed_shoot
