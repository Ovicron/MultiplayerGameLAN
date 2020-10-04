import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.vel
        if keys[pygame.K_s]:
            self.y += self.vel
        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)




