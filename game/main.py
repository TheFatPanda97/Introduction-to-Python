import pygame, os
from random import randint
from object import Object
from player import Player
from bullet import Bullet

screen_width = 1200
screen_height = 850
pygame.font.init()
myfont = pygame.font.SysFont("Times New Roman", 40)
score = 0
number_of_bullets = 15
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
    70, 40)
all_bullets = []
all_obs = []
screen = pygame.display.set_mode((screen_width, screen_height))
red = 255, 0, 0
running = True
has_object = False
speed = 1
bu_speed = 1
obs_speed = 1
ufo_width = 100
ufo_height = 100
pos_x = screen_width // 2 - ufo_width // 2
pos_y = 0
ufo = Player(pos_x, pos_y, ufo_width, ufo_height,
             "ufo.png")
bu1 = Bullet(pos_x, pos_y)
shoot = False
spawn_rate = 0
bullet_rate = 0


def hit(b1, b2):
    b2_range = [range(b2.pos_x - b1.width, b2.pos_x + b2.width),
                range(b2.pos_y - b1.height, b2.pos_y + b2.height)]
    if b1.pos_x in b2_range[0] and b1.pos_y in b2_range[1]:
        return True
    else:
        return False


while running:
    score_txt = myfont.render(f"score: {score}", False, (255, 255, 255))
    bullet_txt = myfont.render(f"bullet: {number_of_bullets}", False,
                               (255, 255, 255))
    spawn_rate += 1
    bullet_rate += 1
    print(bullet_rate, number_of_bullets)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            shoot = False

    pressedKeys = pygame.key.get_pressed()

    if bullet_rate == 500 and number_of_bullets < 15:
        number_of_bullets += 1
        bullet_rate = 0

    if spawn_rate == 100:
        spawn_rate = 0
        curr_obj = Object(screen)
        curr_obj.generate_loc()
        all_obs.append(curr_obj)

    if pressedKeys[pygame.K_LEFT]:
        pos_x -= speed
    elif pressedKeys[pygame.K_RIGHT]:
        pos_x += speed
    elif pressedKeys[pygame.K_UP]:
        pos_y -= speed
    elif pressedKeys[pygame.K_DOWN]:
        pos_y += speed

    if pressedKeys[pygame.K_SPACE] and not shoot and number_of_bullets > 0:
        all_bullets.append(
            Bullet(randint(ufo.pos_x + 15, ufo.pos_x + ufo.width - 30),
                   pos_y))
        shoot = True
        number_of_bullets -= 1

    if pos_x > screen_width - ufo.width:
        pos_x = screen_width - ufo.width
    elif pos_x < 0:
        pos_x = 0
    elif pos_y > screen_height - ufo_height:
        pos_y = screen_height - ufo_height
    elif pos_y < 0:
        pos_y = 0

    screen.fill((0, 0, 0))
    screen.blit(score_txt, (5, 0))
    screen.blit(bullet_txt, (1040, 0))

    ufo.pos_x = pos_x
    ufo.pos_y = pos_y

    for i in range(len(all_bullets) - 1, -1, -1):
        bullet = all_bullets[i]
        if bullet.pos_y < 0:
            all_bullets.pop(i)
            break
        for j in range(len(all_obs) - 1, -1, -1):
            curr_obj = all_obs[j]
            if hit(bullet, curr_obj):
                curr_obj.generate_loc()
                score += 1
                all_obs.pop(j)
                all_bullets.pop(i)
                break
            elif curr_obj.pos_y >= screen_height:
                all_obs.pop(j)

        bullet.pos_y -= bu_speed
        screen.blit(bullet.img, (bullet.pos_x, bullet.pos_y))

    for obs in all_obs:
        if hit(ufo, obs):
            pos_y += 3
            if pressedKeys[pygame.K_LEFT]:
                pos_x += 10
            elif pressedKeys[pygame.K_RIGHT]:
                pos_x -= 3
            elif pressedKeys[pygame.K_UP]:
                pos_y += 3
            elif pressedKeys[pygame.K_DOWN]:
                pos_y -= 3
            if pos_y > screen_height - ufo_height:
                obs.generate_loc()
                # running = False
                all_bullets = []
                all_obs = []
                pos_x = screen_width // 2 - ufo_width // 2
                pos_y = 0
                score = 0
                number_of_bullets = 15
                spawn_rate = 0
                bullet_rate = 0
        obs.pos_y += obs_speed
        obs.generate_object()

    screen.blit(ufo.img, (pos_x, pos_y))

    pygame.display.update()
