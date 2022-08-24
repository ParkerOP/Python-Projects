import random
import time
import pygame

# Initialization
pygame.init()
screen_length = 500
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
# Variables

x = screen_width/2
y = screen_length/2
x_change = 0
y_change = 0
gameOver = False
snakeSpeed = 20
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue2 = (00, 200, 213)
snakeList = []
snakeLength = 1
collided = False
currentScore = 0
# To generate message on display screen
def message(msg,color):
    font_style = pygame.font.SysFont('bahnschrift', 30)
    mesg = font_style.render(msg, True, color)
    getRect = mesg.get_rect()
    getRect.center = (screen_width/2, screen_length/2)
    screen.blit(mesg, getRect)
# To generate the current score on display screen
def scoreMessage(score) :
    font_style = pygame.font.SysFont("comicsansms", 25)
    mesg = font_style.render(f"Your Score : {score}", True, yellow)
    getRect = mesg.get_rect()
    getRect.center = (90, 10)
    screen.blit(mesg, getRect)
# Food coordinates
x_food = round(random.randrange(10, screen_width - 20) /10) *10 
y_food = round(random.randrange(10, screen_length - 20) /10) *10 


# Main Loop
while(gameOver == False) :
    
    for events in pygame.event.get() :
        if(events.type == pygame.QUIT) :
            gameOver = True
        elif(events.type == pygame.KEYDOWN) :
            if(events.key == pygame.K_RIGHT) :
                x_change = 10
                y_change = 0
            elif(events.key == pygame.K_LEFT) :
                x_change = -10
                y_change = 0
            elif(events.key == pygame.K_UP) :
                x_change = 0
                y_change = -10
            elif(events.key == pygame.K_DOWN) :
                x_change = 0
                y_change = 10
    
    x += x_change
    y += y_change

    if(x >= screen_width or x < 0 or y >= screen_length or y < 0) :
        gameOver = True
    pygame.draw.circle(screen, red, [x_food,y_food], radius=3.5)

    snakeHead = [x, y]
    snakeList.append(snakeHead)

    if(len(snakeList) > snakeLength) :
        del snakeList[0]

    for x1 in snakeList[:-1] :
        if(x1 == snakeHead) :
            gameOver = True
            collided = True
            
    if(x == x_food and y == y_food) :
        message("Yummy!", yellow)
        x_food = round(random.randrange(10, screen_width - 20)/10) *10
        y_food = round(random.randrange(10, screen_length - 20)/10) *10
        snakeLength += 1
        currentScore += 1
    
    for z in snakeList :
        pygame.draw.rect(screen, green, [z[0], z[1], 10, 10])

    scoreMessage(currentScore)

    pygame.display.update()
    clock.tick(snakeSpeed)
    screen.fill(blue)
if(x >= screen_width or x < 0 or y >= screen_length or y < 0) :
    message("It's Game Over!", yellow)
    pygame.display.update()
    time.sleep(2) 
if(collided == True) :
    message("Game Over! You collided with yourself.", yellow)
    pygame.display.update()
    time.sleep(2)
pygame.quit()
# quit()