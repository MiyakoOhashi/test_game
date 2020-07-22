"""draw_image3.jp"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Draw Image3")
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    logo = pygame.image.load("pythonlogo.jpg")
    theta = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        theta += 1

        SURFACE.fill((255, 255, 255))
        #ロゴを回転し、左上が(100, 30)の位置にロゴを描画
        new_logo = pygame.transform.rotate(logo, theta)
        SURFACE.blit(new_logo, (100, 30))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()