import pygame

def inputHandler(position, wall):
    new_position = position[:]
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]: 
        if new_position[0] > 0 and not any(new_position[0] - 1 == w[1] and new_position[1] == w[0] for w in wall):
            new_position[0] -= 1
    elif keys[pygame.K_d]: 
        if new_position[0] < 15 and not any(new_position[0] + 1 == w[1] and new_position[1] == w[0] for w in wall):
            new_position[0] += 1
    elif keys[pygame.K_w]: 
        if new_position[1] > 0 and not any(new_position[0] == w[1] and new_position[1] - 1 == w[0] for w in wall):
            new_position[1] -= 1
    elif keys[pygame.K_s]: 
        if new_position[1] < 11 and not any(new_position[0] == w[1] and new_position[1] + 1 == w[0] for w in wall):
            new_position[1] += 1

    return new_position
