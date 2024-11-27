import pygame
import inputHandler as IH
import levelLoader as LL
import time

global image

def main():
    level = [["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
            ["1","2","3","w","5","6","7","8","9","10","11","12","13","14","15","16"],
            ["1","2","3","w","5","6","7","8","9","10","11","12","13","14","15","x"],
            ["1","2","3","w","5","6","7","8","9","10","11","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","9","10","y","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","y","10","x","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"],
            ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]]
    pygame.init()
    clock = pygame.time.Clock()
    position = [3,3]

    wall = []

    position = [0,0]
    
    timerStart = time.time()
    pygame.display.set_caption("Rogue-Like game")
    width = 768  # 16 tileset
    height = 576 # 12 tileset
    window = pygame.display.set_mode((width, height))
    window.fill((255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        moveCharacter(position, window, color=(255,0,0))
        time2 = time.time()

        if time2 - timerStart >= 0.15:
            moveCharacter(position, window, color=(255,255,255))
            position = IH.inputHandler(position)
            moveCharacter(position, window, color=(255,0,0))
            timerStart = time.time()

        if time2 - timerStart >= 0.15:
            moveCharacter(position, window, color=(255,255,255))
            wall = LL.loadLevel(window, level)
            position = IH.inputHandler(position, wall)
            draw_img(window, position)
            timerStart = time.time()


        pygame.display.flip()
        clock.tick(30)

def moveCharacter(position, window, color):
    tile = 48
    pygame.draw.rect(window, color, (position[0] * tile, position[1] * tile, tile, tile))

def moveCharacter(position, window, color):
    tile = 48
    pygame.draw.rect(window, color, (position[0] * tile, position[1] * tile, tile, tile))

def draw_img(window, position):
    tile = 48
    image = pygame.image.load("hero.png")
    image = pygame.transform.scale(image, (tile, tile))
    window.blit(image, (position[0] * tile, position[1] * tile))

if __name__ == "__main__":
    main()
