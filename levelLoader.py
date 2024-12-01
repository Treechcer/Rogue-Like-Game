import pygame
from classes import Character
import random

tile = 48

def loadLevel(window, level, frameCount, position, enemies):
    wall = []
    enemiesDone = 0
    test = True
    for row in range(22):
        for col in range(12):
            enemyCount = countEnemy(level)
            if level[col][row] == "w":
                drawObj(row, col, "sprites/wall.png", window)
                wall.append((col, row))
            elif level[col][row] == "ENEMY":
                if enemyCount != len(enemies):
                    enemies = makeEnemyObjects(enemies, 10, 5, 60.0, 30.0, 10, row, col)
                    wall.append((col, row))

            elif level[col][row] == " ":
                drawObj(row, col, "sprites/ground.png", window)
            elif level[col][row] == "player":
                drawObj(row, col, "sprites/ground.png", window)

    for obj in enemies:
        #enemiesDone = 0
        frameCount, level, wall, enemiesDone = enemyMove(obj.getPositionRow(), obj.getPositionCol(), window, frameCount, position, level, wall, enemyCount, enemiesDone, obj)
        #print(obj.getPositionRow(), obj.getPositionCol())

    for row in range(22):
        for col in range(12):
            if level[col][row] == "ENEMYm":
                level[col][row] = "ENEMY"

    if wall != []:
        return wall, frameCount, enemies

def makeEnemyObjects(enemies, health, strenght, speed, attackSpeed, regenspeed, row, col):
    enemy = Character(health, strenght, speed, attackSpeed, regenspeed, row, col)
    enemies.append(enemy)
    return enemies

def enemyMove(row, col, window, frameCount, position, level, wall, enemyCount, enemiesDone, obj):
    drawObj(row, col, "sprites/ground.png", window)
    drawObj(row, col, "sprites/goblin.png", window)
    if col > position[1] and frameCount % 60 == 0:
        if level[col - 1][row] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col - 1][row] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
        obj.setPositionCol(-1)
    elif col < position[1] and frameCount % 60 == 0:
        if level[col + 1][row] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col + 1][row] = "ENEMYm"
        level[col][row] = " "
        obj.setPositionCol(1)
        enemiesDone += 1
    elif row < position[0] and frameCount % 60 == 0:
        if level[col][row + 1] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col][row + 1] = "ENEMYm"
        level[col][row] = " "
        obj.setPositionRow(1)
        enemiesDone += 1
    elif row > position[0] and frameCount % 60 == 0:
        if level[col][row - 1] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col][row - 1] = "ENEMYm"
        level[col][row] = " "
        obj.setPositionRow(-1)
        enemiesDone += 1

    return frameCount, level, wall, enemiesDone

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