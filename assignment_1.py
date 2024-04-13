import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0,0,255)
green = (0,255,0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])    


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 280
    snake_y = 280
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, 450)
    food_y = random.randint(20, 300)
    score = 0
    init_velocity = 3
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(black)
            text_screen("GAME OVER!!",red,290,240)
            text_screen("Press S To Continue To Play Again", blue, 110, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_a:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                if score<50:
                    score+=1
                elif 50<score and score<100:
                    score+=2
                else :
                    score+=3        
                food_x = random.randint(20, 450)
                food_y = random.randint(20, 300)
                snk_length +=8

            gameWindow.fill(black)
            text_screen("Respect: " + str(score * 5), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0:
                snake_x=screen_width
                # snake_y=0

            if snake_x>screen_width:
                snake_x=0
                # snake_y=screen_height

            if snake_y<0:
                snake_y=screen_height
                # snake_x=0

            if snake_y>screen_height:
                snake_y=0
                # snake_x=screen_height


                # game_over = True
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()
