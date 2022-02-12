import sys
import pygame
import ctypes

pygame.init()

speed = [10, 10]
size = width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

logos = ["logo/DVD_logo_1.png", "logo/DVD_logo_2.png", "logo/DVD_logo_3.png",
         "logo/DVD_logo_4.png", "logo/DVD_logo_5.png"]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
logo = pygame.image.load(logos[0])
rect = logo.get_rect()

fps = 60
i = 0
count = 0
count_corner = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            last_speed = speed
            speed = [0, 0]
        if pygame.key.get_pressed()[pygame.K_f]:
            speed = [15, 15]
        if i > 0 and ((rect.left == 0 and rect.top == 0) or (rect.right == width and rect.top == 0) or
                      (rect.left == 0 and rect.bottom == height) or (rect.right == width and rect.bottom == height)):
            speed = [0, 0]
            count_corner += 1
    if rect.left < 0:
        speed[0] = -speed[0]
        i += 1
        logo = pygame.image.load(logos[i % len(logos)])
        count += 1
    if rect.right > width:
        speed[0] = -speed[0]
        i += 1
        logo = pygame.image.load(logos[i % len(logos)])
        count += 1

    if rect.top < 0:
        speed[1] = -speed[1]
        i += 1
        logo = pygame.image.load(logos[i % len(logos)])
        count += 1
    if rect.bottom > height:
        speed[1] = -speed[1]
        i += 1
        logo = pygame.image.load(logos[i % len(logos)])
        count += 1

    count_view = pygame.font.SysFont("", 48).render("Счётчик ударов: {}".format(count), True, (255, 255, 255))
    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logo, rect)
    screen.blit(count_view, (0, 0))
    pygame.display.update()
    clock.tick(fps)
