import pygame
import inputHandler as IH
import time

def main():
    pygame.init()
    clock = pygame.time.Clock()

    position = [0,0]

    timerStart = time.time()
    pygame.display.set_caption("Rogue-Like game")
    width = 1920
    height = 1080
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

        pygame.display.flip()
        clock.tick(30)

def moveCharacter(position, window, color):
    tile = 48
    pygame.draw.rect(window, color, (position[0] * tile, position[1] * tile, tile, tile))

if __name__ == "__main__":
    main()
