import pygame

def inputHandler(position):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if position[0] != 0:
            position[0] -= 1
        return position
    elif keys[pygame.K_RIGHT]:
        if position[0] < 15:
            position[0] += 1
        return position
    elif keys[pygame.K_UP]:
        if position[1] != 0:
            position[1] -= 1
        return position
    elif keys[pygame.K_DOWN]:
        if position[1] < 11:
            position[1] += 1
        return position
    else:
        return position