import pygame

pygame.display.set_mode((600, 400))

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

print ("программа продолжает работу")

