import pygame
import time
import random
pygame.init()


swidth = 990
sheight = 870
screen = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
green = (0,139,69)
blue = (99,130,255)
red = (238,0,0)
x_values = []
y_values = []



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((swidth/2),(sheight/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

def display_score(score):
    largeText = pygame.font.Font("freesansbold.ttf",20)
    s = "Score: " + str(score)
    TextSurf, TextRect = text_objects(s, largeText)
    TextRect.center = (900,40)
    screen.blit(TextSurf, TextRect)

def welcome():
    screen.fill(white)
    message_display("Welcome To Snake")
    pygame.display.update()
    gameloop()

def game_over():
    screen.fill(white)
    message_display("Game Over")
    pygame.display.update()
    time.sleep(1)
    pygame.quit()

def gameloop():
    x = (480)
    y = (600)
    speed = 30
    foodx = (random.randint(2,31))*30
    foody = (random.randint(2,27))*30
    x_change = 0
    y_change = 0
    score = 0
     
    done = False
    while done == False:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and (x_change <= 0 or score == 0):
                    x_change = -speed
                    y_change = 0
                    
                elif event.key == pygame.K_RIGHT and (x_change >= 0 or score == 0):
                    x_change = speed
                    y_change = 0
                    
                elif event.key == pygame.K_UP and (y_change <= 0 or score == 0):
                    y_change = -speed 
                    x_change = 0
                    
                elif event.key == pygame.K_DOWN and (y_change >= 0 or score == 0):
                    y_change = speed
                    x_change = 0
                    

        if x <= -1 or x >= (swidth - 30) or y <= -1 or y >= (sheight - 30):
            game_over()
        
        x += x_change
        y += y_change
        x_values.append(x)
        y_values.append(y)
        
        if x == foodx and y == foody:
            foodx = (random.randint(2,31))*30
            foody = (random.randint(2,27))*30
            score += 1
            
            
        screen.fill(white)       
        tailx = []
        taily = []
        for i in range(1,score + 1):
            pygame.draw.rect(screen,red,(x_values[(len(x_values) - 1 - i)],y_values[(len(y_values) - 1 - i)],30,
                                         30))
            tailx.append(x_values[(len(x_values) - 1 - i)])
            taily.append(y_values[(len(y_values) - 1 - i)])
        
        pygame.draw.rect(screen,green,(x,y,30,30))
        pygame.draw.rect(screen,blue,(foodx,foody,30,30))
        display_score(score)
        pygame.display.update()
        
        for i in range(0,len(tailx) - 1):
            if x == tailx[i] and y == taily[i]:
                game_over()
        clock.tick(10)
        
        

welcome()
pygame.quit()
quit()
