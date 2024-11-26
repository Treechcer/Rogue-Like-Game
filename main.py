import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Rogue-Like game")
    okno_sirka = 800
    okno_vyska = 600
    okno = pygame.display.set_mode((okno_sirka, okno_vyska))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()