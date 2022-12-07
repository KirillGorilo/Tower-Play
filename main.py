import pygame

pygame.init()

# словарь, который содержит цвета
colors_lists = {
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
}

sc = pygame.display.set_mode((700, 900))
pygame.display.set_caption("Игра - башенки")
# pygame.display.set_icon(pygame.image.load("icon.bmp")) # иконка игры

FPS = 60
clock = pygame.time.Clock()

x = 350
y = 200
speed = 5

space_key = False
# главный цикл программы
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y += speed

    sc.fill(colors_lists.get("WHITE"))
    pygame.draw.rect(sc, colors_lists.get("BLUE"), (x, y, 20, 20))
    pygame.display.update()
    clock.tick(FPS)
