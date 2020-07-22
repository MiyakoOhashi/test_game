"""draw_ellipse.jp"""
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 250))
pygame.display.set_caption("Drew Ellipse")
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))

        #赤、塗りつぶし
        pygame.draw.ellipse(SURFACE, (255, 0, 0), (50, 50, 140, 60))

        #赤
        pygame.draw.ellipse(SURFACE, (255, 0, 0), (250, 30, 90, 90))

        #緑,線10
        pygame.draw.ellipse(SURFACE, (0, 255, 0), (50, 150, 110, 60), 5)

        #緑、線20
        pygame.draw.ellipse(SURFACE, (0, 255, 0), ((250, 130), (90, 90)), 20)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()