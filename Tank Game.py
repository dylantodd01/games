import random
import pygame
import time
import math
pygame.init()

screen = pygame.display.set_mode((1192,670))
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
green = (0,139,69)
blue = (99,130,255)
red = (238,0,0)
image0 = pygame.image.load("background.png")
image1 = pygame.image.load("gold.png")
image2 = pygame.image.load("tank1_0.png")
image3 = pygame.image.load("tank1_15.png")
image4 = pygame.image.load("tank1_30.png")
image5 = pygame.image.load("tank1_45.png")
image6 = pygame.image.load("tank1_60.png")
image7 = pygame.image.load("tank1_75.png")
image8 = pygame.image.load("tank1_90.png")
image9 = pygame.image.load("tank_explosion.png")
pygame.mixer.music.load("bomb.mp3")


def background():
    screen.blit(image0,(0,0))
def gold():
    screen.blit(image1,(400,400))
def draw_tank1_0(screen):
    screen.blit(image2,(x1, y))
def draw_tank1_15(screen):
    screen.blit(image3,(x1 - 3, y - 9))
def draw_tank1_30(screen):
    screen.blit(image4,(x1 - 3, y - 21))
def draw_tank1_45(screen):
    screen.blit(image5,(x1 - 4, y - 31))
def draw_tank1_60(screen):
    screen.blit(image6,(x1 - 4, y - 39))
def draw_tank1_75(screen):
    screen.blit(image7,(x1 - 7, y - 43))
def draw_tank1_90(screen):
    screen.blit(image8,(x1 - 5, y - 45))

def draw_tank1(angle):
    if angle < 7.5:
        draw_tank1_0(screen)
    elif angle >= 7.5 and angle < 22.5:
        draw_tank1_15(screen)
    elif angle >= 22.5 and angle < 37.5:
        draw_tank1_30(screen)
    elif angle >= 37.5 and angle < 52.5:
        draw_tank1_45(screen)
    elif angle >= 52.5 and angle < 67.5:
        draw_tank1_60(screen)
    elif angle >= 67.5 and angle < 82.5:
        draw_tank1_75(screen)
    elif angle >= 82.5 and angle <= 90:
        draw_tank1_90(screen)
    
#def draw_tank2(screen):
#    screen.blit(image3,(x2, y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def display_angle(angle):
    largeText = pygame.font.Font("freesansbold.ttf",20)
    s = "Angle: " + str(angle)
    TextSurf, TextRect = text_objects(s, largeText)
    TextRect.center = (596,40)
    screen.blit(TextSurf, TextRect)
def display_power(power):
    largeText = pygame.font.Font("freesansbold.ttf",20)
    s = "Power: " + str(round(power, 1))
    TextSurf, TextRect = text_objects(s, largeText)
    TextRect.center = (596,80)
    screen.blit(TextSurf, TextRect)
    
x1 = 180
x2 = 970
y = 480
angle = 0
x1_change = 0
power = 5.0
power_change = 0


speed = 1
shoot1 = False
done = False
while done == False:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shoot1 = True
                done = True

    while shoot1 == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shoot1 = True
                done = True
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -speed
                elif event.key == pygame.K_RIGHT:
                    x1_change = speed

                if event.key == pygame.K_UP:
                    power_change = +0.04
                elif event.key == pygame.K_DOWN:
                    power_change = -0.04

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x1_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                power_change = 0

        mousex1, mousey1 = pygame.mouse.get_pos()
        mousex1 -= x1 + 40
        mousey1 = (670 - mousey1) - 170
        
        if mousex1 > 0 and mousey1 > 0:
            angle = math.degrees(math.atan(mousey1/mousex1))
            angle = round(angle, 1)
        elif mousex1 < 0 and mousey1 > 0:
            angle = 90.0
        elif mousex1 > 0 and mousey1 < 0:
            angle = 0.0
        
        x1 += x1_change
        power += power_change
        if power < 5:
            power = 5.0
        if power > 8:
            power = 8.0
        
        if x1 < 0:
            x1 = 0
        if x1 > 327:
            x1 = 327

        xpower = 12 * power * math.cos(math.radians(angle))
        ypower = 12 * power * math.sin(math.radians(angle))

        
        background()
        gold()
        draw_tank1(angle)

        for i in range(1,7):
            if i > 1 or power > 6.5:
                pygame.draw.rect(screen,(255,0,0),(x1 + 40 + xpower * i, y + 12 + ((3 * i**2) - (ypower * i)),6,6))
        p = 1
        bally = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                while bally <= y + 25:
                    
                    ballx = round(x1 + 40 + (xpower * p))
                    bally = round(y + 12 + ((3 * p**2) - (ypower * p)))
                    
                    background()
                    gold()
                    draw_tank1(angle)
                    pygame.draw.circle(screen, blue, (ballx, bally),5)
                    pygame.display.update()
                    p += 0.2
                    time.sleep(0.002)
                
                screen.blit(image9, (ballx - 35, bally - 30))
                pygame.mixer.music.play(0)
                time.sleep(0.2)
                pygame.display.update()
                time.sleep(0.8)
                #shoot1 = True
        
        display_angle(angle)
        display_power(power)
        pygame.display.update()
        clock.tick(60)
    

pygame.quit()
quit()
