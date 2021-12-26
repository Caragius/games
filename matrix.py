import pygame as pg
import random


class Matrixletters:
    def __init__(self, app):
        self.app = app
        self.letters = [chr(int('0x30a0', 16) + 1) for i in range(1, 95)]
        self.font_size = 15
        self.font = pg.font.Font("MS Mincho.ttf", self.font_size, bold=False)
        self.colums = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.colums)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (55, 200, 100))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] += 1

    def run(self):
        self.draw()


class Matrixapp:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1000
        pg.init()
        self.screen = pg.display.set_mode(self.RES)  # display
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        ''
        self.matrixletters = Matrixletters(self)

    def draw(self):
        self.surface.fill((0, 0, 0, 15))
        self.matrixletters.run()  # sqap
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()  # obnovlenie
            self.clock.tick(30)


if __name__ == "__matrix__":
    print(555)
else:
    app = Matrixapp()
    app.run()
