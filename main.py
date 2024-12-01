import pygame
import inputHandler as IH
import levelLoader as LL
from classes import Character
import time

global image

def main():
    level = [["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," ","ENEMY"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," ","ENEMY"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," ","ENEMY"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ]
    pygame.init()
    clock = pygame.time.Clock()
    position = [3,3, True]
    level[position[1]][position[0]] = "player"

    wall = []

    frameCount = 0

    timerStart = time.time()
    pygame.display.set_caption("Rogue-Like game")
    width = 1056  # 22 tileset
    height = 576 # 12 tileset

    #for testing purposes it's not full in fullscreen, you can enable it tho but un-commenting line after this comment this and commenting two lines after
    #this comment it should work without problems
    #window = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.SCALED)
    window = pygame.display.set_mode((width, height))

    player = Character(100, 5, 0.15, 0.30, 1)

    window.fill((255,255,255))
    while True:
        frameCount += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        time2 = time.time()

        position = IH.inputHandler(position, wall, timerStart, time2, level, player)
        if position[2] == True:
            moveCharacter(position, window, color=(255,255,255))
            wall, frameCount = LL.loadLevel(window, level, frameCount, position)
            draw_img(window, position)
            timerStart = time.time()
            position[2] = False
        else:
            wall, frameCount = LL.loadLevel(window, level, frameCount, position)
            draw_img(window, position)

        pygame.display.flip()
        clock.tick(60)


def moveCharacter(position, window, color):
    tile = 48
    pygame.draw.rect(window, color, (position[0] * tile, position[1] * tile, tile, tile))

def draw_img(window, position):
    tile = 48
    image = pygame.image.load("sprites/hero1.png")
    image = pygame.transform.scale(image, (tile, tile))
    window.blit(image, (position[0] * tile, position[1] * tile))

if __name__ == "__main__":
    main()