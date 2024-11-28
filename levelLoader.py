import pygame

tile = 48

def loadLevel(window, level, frameCount, position):
    wall = []
    for row in range(16):
        for col in range(12):
            if level[col][row] == "x":
                pygame.draw.rect(window, (0, 0, 50), (row * tile, col * tile, tile, tile))
            elif level[col][row] == "w":
                drawObj(row, col, "wall.png", window)
                wall.append((col, row)) 
            elif level[col][row] == "Enemy":
                drawObj(row, col, "ground.png", window)
                drawObj(row, col, "goblin.png", window)
                if col > position[1] and frameCount >= 35:
                    level[col - 1][row] = "Enemy"
                    level[col][row] = " "
                    frameCount = 0
                elif col < position[1] and frameCount >= 35:
                    level[col + 1][row] = "Enemy"
                    level[col][row] = " "
                    frameCount = 0
                elif row < position[0] and frameCount >= 35:
                    level[col][row + 1] = "Enemy"
                    level[col][row] = " "
                    frameCount = 0
                elif row > position[0] and frameCount >= 35:
                    level[col][row - 1] = "Enemy"
                    level[col][row] = " "
                    frameCount = 0
            elif level[col][row] == " ":
                drawObj(row, col, "ground.png", window)

    return wall, frameCount 

def drawObj(row, col, imagePos, window):
    image = pygame.image.load(f"{imagePos}")
    image = pygame.transform.scale(image, (tile, tile))
    window.blit(image, (row * tile, col * tile))
