"""draw_image_subregion1.jp"""
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((700, 200))
pygame.display.set_caption("Draw Image subregion1")
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    logo = pygame.image.load("pythonlogo.png")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))
        SURFACE.blit(logo, (0, 0))
        SURFACE.blit(logo, (350, 50), Rect(50, 50, 100, 100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()