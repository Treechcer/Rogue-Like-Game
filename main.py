import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Rogue-Like game")
    width = 800
    height = 600
    okno = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()