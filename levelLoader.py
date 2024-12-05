import pygame

image_cache = {}

tile = 48

def loadImage(imagePath):
    """Load and cache images to avoid reloading multiple times."""
    if imagePath not in image_cache:
        image = pygame.image.load(imagePath)
        image = pygame.transform.scale(image, (tile, tile))
        image_cache[imagePath] = image
    return image_cache[imagePath] 

def drawObj(row, col, imagePos, window):
    """Draw an object on the window using the cached image."""
    image = loadImage(imagePos)
    window.blit(image, (row * tile, col * tile)) 

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
    if col > position[1] and frameCount % 30 == 0:
        if level[col - 1][row] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col - 1][row] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
    elif col < position[1] and frameCount % 30 == 0:
        if level[col + 1][row] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col + 1][row] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
    elif row < position[0] and frameCount % 30 == 0:
        if level[col][row + 1] in ["w", "player", "ENEMY", "ENEMYm"]:
            enemiesDone += 1
            return frameCount, level, wall, enemiesDone
        level[col][row + 1] = "ENEMYm"
        level[col][row] = " "
        enemiesDone += 1
    elif row > position[0] and frameCount % 30 == 0:
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
    for row in range(22):
        for col in range(12):
            if level[col][row] == "ENEMY":
                enemyCount += 1
    return enemyCount
