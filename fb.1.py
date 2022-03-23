import pygame
import sys #what is sys for
import random
pygame.init()

width = 800
height = 600
red = 255,0,0
blue = 0,0,255
yellow = (255,255,0)
black = 0,0,0
speed = 15
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 35)
player_size = 50
player_pos = [width/2 , height-2 * player_size]
movement = 50 #has to be correlated with size
enemy_size = 50
enemy_pos = [random.randint(0,width - enemy_size), 50 ]
enemy_list = [enemy_pos]
score = 0
screen = pygame.display.set_mode((width, height)) #set the display

game_over = False #Boolean variable set to false

def set_level(score, speed):
    if score < 20:
        speed = 8
    elif score < 50:
        speed = 10
    elif score < 70:
        speed = 15
    elif score > 100:
        speed = 25



    return speed


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1 :
        x_pos = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([ x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos  in enemy_list:
        pygame.draw.rect(screen, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def update_enemy_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False


while not game_over: #While loop that is going to run until game over becomes true

    #QUESTIONS: why does it run if event is not inizialized (know what event does)
    for event in pygame.event.get():
       # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0] # this two keys are for making things easier
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= movement #to make the rec move left
            elif event.key == pygame.K_RIGHT:
                x += movement #to make the rec move right

            player_pos = [x, y] #the player_pos variable is set to have the new value of x and y
    screen.fill(black) #Built in function so the background be filled black and make the illusion of the rectangle moving



    clock.tick(30)#To set the framerate of the game

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    drop_enemies(enemy_list)
    score = update_enemy_pos(enemy_list, score)
    speed = set_level(score, speed)
    text = "score: " + str(score)
    label = myfont.render(text, 1, yellow)
    screen.blit(label,  (width - 200, height - 40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, red, (player_pos[0], player_pos [1], player_size, player_size))
    pygame.display.update() #it is so that the rectangle appear
