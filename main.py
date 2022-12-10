import pygame

W, H = 600, 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("моя первая программа на pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


FPS = 60
clock = pygame.time.Clock()

sp = None

sc.fill(WHITE)
pygame.display.update()

x = W // 2
y = H // 2
speed = 5

pygame.mouse.set_visible(False)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(WHITE)

    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        pygame.draw.circle(sc, BLUE, pos, 7)

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:

        if sp is None:
            sp = pos

        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        sc.fill(WHITE)
        pygame.draw.rect(sc, RED, (sp[0], sp[1], width, height ))
    else:
        sp = None
    pygame.display.update()









    clock.tick(FPS)


