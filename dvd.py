import sys
import pygame
import ctypes

pygame.init()

speed = [150, 150]
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
    rect_left_view = pygame.font.SysFont("", 48).render("Счётчик слева: {}".format(rect.left), True, (255, 255, 255))
    rect_right_view = pygame.font.SysFont("", 48).render("Счётчик справа: {}".format(rect.right), True, (255, 255, 255))
    rect_top_view = pygame.font.SysFont("", 48).render("Счётчик сверху: {}".format(rect.top), True, (255, 255, 255))
    rect_top_bottom = pygame.font.SysFont("", 48).render("Счётчик снизу: {}".format(rect.bottom), True, (255, 255, 255))
    rect_speed = pygame.font.SysFont("", 48).render("Скорость: {}".format(speed), True, (255, 255, 255))
    rect_count_corner = pygame.font.SysFont("", 48).render("Скорость: {}".format(count_corner), True, (255, 255, 255))
    rect_i = pygame.font.SysFont("", 48).render("I: {}".format(i), True, (255, 255, 255))
    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logo, rect)
    screen.blit(count_view, (0, 0))
    screen.blit(rect_left_view, (0, 50))
    screen.blit(rect_right_view, (350, 50))
    screen.blit(rect_top_view, (0, 100))
    screen.blit(rect_top_bottom, (350, 100))
    screen.blit(rect_speed, (550, 0))
    screen.blit(rect_count_corner, (900, 0))
    screen.blit(rect_i, (900, 100))
    pygame.display.update()
    clock.tick(fps)
