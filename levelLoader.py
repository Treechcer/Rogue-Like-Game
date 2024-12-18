import pygame
from classes import Character

tile = 48

def loadLevel(window, level, frameCount, position):
    wall = []
    enemies = []
    enemiesDone = 0
    for row in range(22):
        for col in range(12):
            enemyCount = countEnemy(level)
            if level[col][row] == "w":
                drawObj(row, col, "sprites/wall.png", window)
                wall.append((col, row))
            elif level[col][row] == "ENEMY":
                #if enemyCount != len(enemies):
                #    enemies = []
                #else:
                #    makeObjectsEnemy(row, col, enemies)
                wall.append((col, row))
                if enemiesDone == enemyCount:
                    enemiesDone = 0
                frameCount, level, wall, enemiesDone = enemyMove(row, col, window, frameCount, position, level, wall, enemyCount, enemiesDone)
            elif level[col][row] == " ":
                drawObj(row, col, "sprites/ground.png", window)
            elif level[col][row] == "player":
                drawObj(row, col, "sprites/ground.png", window)
        
    for row in range(22):
        for col in range(12):
            if level[col][row] == "ENEMYm":
                level[col][row] = "ENEMY"

    if wall != []:
        return wall, frameCount

def enemyMove(row, col, window, frameCount, position, level, wall, enemyCount, enemiesDone):
    drawObj(row, col, "sprites/ground.png", window)
    drawObj(row, col, "sprites/goblin.png", window)
    if col > position[1] and frameCount % 60 == 0:
        if level[col - 1][row] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col - 1][row] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
    elif col < position[1] and frameCount % 60 == 0:
        if level[col + 1][row] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col + 1][row] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
    elif row < position[0] and frameCount % 60 == 0:
        if level[col][row + 1] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col][row + 1] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
    elif row > position[0] and frameCount % 60 == 0:
        if level[col][row - 1] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col][row - 1] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1

    return frameCount, level, wall, enemiesDone

def makeObjectsEnemy(row, col, enemies):
    enemy = Character(20, 3, 0.20, 0.15, 5, row, col)
    enemies.append(enemy)
    return enemies

def countEnemy(level):
    enemyCount = 0
    for row in range(16):
        for col in range(12):
            if level[col][row] == "ENEMY":
                enemyCount += 1

    return enemyCount

def drawObj(row, col, imagePos, window):
    image = pygame.image.load(f"{imagePos}")
    image = pygame.transform.scale(image, (tile, tile))
    window.blit(image, (row * tile, col * tile))