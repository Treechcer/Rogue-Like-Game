import pygame

tile = 48

def loadLevel(window, level, frameCount, position):
    wall = []
    for row in range(16):
        for col in range(11):
            if level[col][row] == "x":
                pygame.draw.rect(window, (0,0,50), (row * tile, col * tile, tile, tile))
            elif level[col][row] == "y":
                pygame.draw.rect(window, (10,200,10), (row * tile, col * tile, tile, tile))
            elif level[col][row] == "w":
                pygame.draw.rect(window, (0,0,0), (row * tile, col * tile, tile, tile))
                wall.append((col, row))
    
    for row in range(16):
        for col in range(11):
            if level[col][row] == "ENEMY" and frameCount >= 20:
                if col > position[1]:
                    enemyMove([row, col-1], row, col, window, level)
                    frameCount = 0

    if wall != []:
        return wall

def enemyMove(position, row, col, window, level):
    pygame.draw.rect(window, (0,0,0), (row * tile, col * tile, tile, tile))
    level[col+1][row] = " "
    level[col][row] = "ENEMY"
    print("moved?")