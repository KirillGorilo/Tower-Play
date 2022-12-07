import pygame

pygame.init()

# словарь, который содержит цвета
colors_lists = {
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
}

W = 600
H = 900

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Игра - башенки")
# pygame.display.set_icon(pygame.image.load("icon.bmp")) # иконка игры

FPS = 60
clock = pygame.time.Clock()

# ПОВЕРХНОСТИ
surf = pygame.Surface((300, 200))
surf.fill(colors_lists.get("BLUE"))
# константы перемещения объекта
x = 300
y = 200

# скорость перемещения и падения
speed = 5
fall_objects = 10

space_key = False
# главный цикл программы
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_key = True

    keys = pygame.key.get_pressed()
    surf.fill(colors_lists.get("BLUE"))

    if space_key:
        if y >= 720:
            space_key = False
        y += fall_objects
    elif keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    sc.fill(colors_lists.get("WHITE"))
    pygame.draw.rect(sc, colors_lists.get("BLUE"), (x, y, 20, 20))
    surf.blit(surf, (300, 200))
    pygame.display.update()
    clock.tick(FPS)
