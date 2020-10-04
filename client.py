import pygame
from player import Player
from network import Network

pygame.init()
pygame.display.set_caption('Online Game')

WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def redraw_window(win, player, player2):
    WIN.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def window():
    WIN.fill((255, 255, 255))
    pygame.draw.rect(WIN, (255, 0, 0), (10, 10, 100, 100))
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_player()
    while run:
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(WIN, p, p2)


main()
