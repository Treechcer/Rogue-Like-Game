import pygame

def loadLevel(window, level):
    tile = 48
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
    if wall != []:
        return wall
