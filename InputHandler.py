import pygame

def inputHandler(position):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        position[0] -= 1
        return position
    elif keys[pygame.K_RIGHT]:
        position[0] += 1
        return position
    elif keys[pygame.K_UP]:
        position[1] -= 1
        return position
    elif keys[pygame.K_DOWN]:
        position[1] += 1
        return position
    else:
        return position
#should work now
