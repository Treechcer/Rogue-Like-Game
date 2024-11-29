import pygame

def inputHandler(position, wall, t1, t2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and t2 - t1 >= 0.15:
        if position[0] != 0:
            for i in range(len(wall)):
                if position[0] - 1 == wall[i][1] and position[1] == wall[i][0]:
                    return position
            position[0] -= 1
            position[2] = True
        return position
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and t2 - t1 >= 0.15:
        if position[0] < 15:
            for i in range(len(wall)):
                if position[0] + 1 == wall[i][1] and position[1] == wall[i][0]:
                    return position
            position[0] += 1
            position[2] = True
        return position
    elif keys[pygame.K_UP] or keys[pygame.K_w] and t2 - t1 >= 0.15:
        if position[1] != 0:
            for i in range(len(wall)):
                if position[0] == wall[i][1] and position[1] - 1 == wall[i][0]:
                    return position
            position[1] -= 1
            position[2] = True
        return position
    elif keys[pygame.K_DOWN] or keys[pygame.K_s] and t2 - t1 >= 0.15:
        if position[1] < 11:
            for i in range(len(wall)):
                if position[0] == wall[i][1] and position[1] + 1 == wall[i][0]:
                    return position
            position[1] += 1
            position[2] = True
        return position
    else:
        return position