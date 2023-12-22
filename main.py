import pygame
from random import randint

HEAD = (0, 200, 0)
BODY = (0, 255, 0)
APPLE = (255, 0, 0)
BACKGROUND = (20, 20, 20)

pygame.init()
X = 400
Y = 400
screen = pygame.display.set_mode((X, Y))
screen.fill(BACKGROUND)

pos = {'x': 0, 'y': 0}
pos_apple = {'x': randint(-10, 9), 'y': randint(-10, 9)}
pos_of_body = []
length_body = 0
direction = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 2:
                direction = 0
            elif event.key == pygame.K_RIGHT and direction != 3:
                direction = 1
            elif event.key == pygame.K_DOWN and direction != 0:
                direction = 2
            elif event.key == pygame.K_LEFT and direction != 1:
                direction = 3
            elif event.key == pygame.K_q:
                length_body += 10
    screen.fill(BACKGROUND)
    pos_of_body.append(pos.copy())
    if length_body < len(pos_of_body):
        pos_of_body.pop(0)
    match direction:
        case 0:
            pos['y'] -= 1
        case 1:
            pos['x'] += 1
        case 2:
            pos['y'] += 1
        case 3:
            pos['x'] -= 1

    if pos['x'] < -10:
        run = False
    elif pos['x'] > 9:
        run = False
    elif pos['y'] > 9:
        run = False
    elif pos['y'] < -10:
        run = False

    if pos in pos_of_body:
        if length_body == 399:
            print("WIN!")
        else:
            print("LOSER!")
            print(f"score is:{length_body-1}")
        run = False


    if pos == pos_apple:
        while pos_apple in pos_of_body or pos == pos_apple:
            pos_apple = {'x': randint(-10, 9), 'y': randint(-10, 9)}
        length_body += 1

    # print(pos_of_body)

    pygame.draw.rect(screen, APPLE,
                     (X // 2 + pos_apple['x'] * (X // 20), Y // 2 + pos_apple['y'] * (Y // 20), 20, 20))
    for i in pos_of_body:
        pygame.draw.rect(screen, BODY, (X // 2 + i['x'] * (X // 20), Y // 2 + i['y'] * (Y // 20), 20, 20), 5)
    pygame.draw.rect(screen, HEAD,
                     (X // 2 + pos['x'] * (X // 20), Y // 2 + pos['y'] * (Y // 20), 20, 20))
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
