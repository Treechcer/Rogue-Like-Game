import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    x = 0
    y = 0
    z = 0

    pygame.display.set_caption("Rogue-Like game")
    width = 800
    height = 600
    window = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        xyz = (x % 256,y % 256,z % 256)

        window.fill(xyz)

        x += 1
        z += 1
        y += 1

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main() #tak to je crazy