import pygame

def inputHandler(position, wall):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if position[0] != 0:
            for i in range(len(wall)):
                if position[0] - 1 == wall[i][1] and position[1] == wall[i][0]:
                    return position
            position[0] -= 1
        return position
    elif keys[pygame.K_RIGHT]:
        if position[0] < 15:
            for i in range(len(wall)):
                if position[0] + 1 == wall[i][1] and position[1] == wall[i][0]:
                    return position
            position[0] += 1
        return position
    elif keys[pygame.K_UP]:
        if position[1] != 0:
            for i in range(len(wall)):
                if position[0] == wall[i][1] and position[1] - 1 == wall[i][0]:
                    return position
            position[1] -= 1
        return position
    elif keys[pygame.K_DOWN]:
        if position[1] < 11:
            for i in range(len(wall)):
                if position[0] == wall[i][1] and position[1] + 1 == wall[i][0]:
                    return position
            position[1] += 1
        return position
    else:
        return position