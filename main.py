import pygame
import inputHandler as IH
import levelLoader as LL
import time
import random
import math

global image

class Player:
    def __init__(self, position):
        self.rect = pygame.Rect(position[0] * 48, position[1] * 48, 48, 48)
        
class Enemy:
    def __init__(self, x, y, width, height, image_path, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.speed = speed

    def follow_player(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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
    
    enemy_position = [random.randint(0, 15), random.randint(0, 11)]  #spawne enemaka
    enemy = Enemy(
        x=enemy_position[0] * 48,
        y=enemy_position[1] * 48,
        width=48,
        height=48,
        image_path="goblin.png",
        speed=5
    )
    wall = []

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

        time2 = time.time()

        if time2 - timerStart >= 0.15:
            moveCharacter(position, window, color=(255,255,255))
            wall = LL.loadLevel(window, level)
            position = IH.inputHandler(position, wall)
            draw_img(window, position)
            enemy.follow_player(Player(position))
            enemy.draw(window)
            timerStart = time.time()

        pygame.display.flip()
        clock.tick(60)

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
