import sys

import pygame
import ctypes


def default_settings():
    speed = [10, 10]
    logos = ["logo/DVD_logo_1.png", "logo/DVD_logo_2.png", "logo/DVD_logo_3.png",
             "logo/DVD_logo_4.png", "logo/DVD_logo_5.png"]
    fps = 60
    count = 0
    screen = pygame.display.set_mode(get_size_window())
    clock = pygame.time.Clock()
    rect = pygame.image.load(logos[count % len(logos)]).get_rect()
    return speed, logos, screen, clock, rect, fps, count


def get_size_window():
    return ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)


def dvd_fly():
    speed, logos, screen, clock, rect, fps, count = default_settings()
    last_speed = speed
    logo = pygame.image.load(logos[count % len(logos)])
    while True:
        width, height = get_size_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                speed = [0, 0]
            if pygame.key.get_pressed()[pygame.K_f]:
                speed = last_speed
            if count > 0 and ((rect.left == 0 and rect.top == 0) or (rect.right == width and rect.top == 0) or
                              (rect.left == 0 and rect.bottom == height) or (
                                      rect.right == width and rect.bottom == height)):
                speed = [0, 0]
        if rect.left < 0:
            speed[0] = -speed[0]
            count += 1
            logo = pygame.image.load(logos[count % len(logos)])

        if rect.right > width:
            speed[0] = -speed[0]
            count += 1
            logo = pygame.image.load(logos[count % len(logos)])

        if rect.top < 0:
            speed[1] = -speed[1]
            count += 1
            logo = pygame.image.load(logos[count % len(logos)])

        if rect.bottom > height:
            speed[1] = -speed[1]
            count += 1
            logo = pygame.image.load(logos[count % len(logos)])
        count_view = pygame.font.SysFont("", 48).render("Счётчик ударов: {}".format(count), True, (255, 255, 255))

        rect.left += speed[0]
        rect.top += speed[1]
        screen.fill((0, 0, 0))
        screen.blit(logo, rect)
        screen.blit(count_view, (0, 0))
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    dvd_fly()
