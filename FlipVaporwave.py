import pygame, random
from pygame.locals import *

pygame.init()

SCREEN_COMPRIMENTO = 400
SCREEN_ALTURA = 680
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

GROUND_COMPRIMENTO = 2 * SCREEN_COMPRIMENTO
GROUND_ALTURA = 150

PIPE_COMPRIMENTO = 250
PIPE_ALTURA = 500
PIPE_GAP = 80


class State(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('estatua.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_COMPRIMENTO / 5
        self.rect[1] = SCREEN_ALTURA / 4
        self.speed = SPEED
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.speed += GRAVITY

        # Update height
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -SPEED


class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('pilastra1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_COMPRIMENTO, PIPE_ALTURA))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_ALTURA - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= GAME_SPEED


class Ground(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('chão.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_COMPRIMENTO, GROUND_ALTURA))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_ALTURA - GROUND_ALTURA

    def update(self):
        self.rect[0] -= GAME_SPEED


def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


def get_random_pipes(xpos):
    size = random.randint(300, 500)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_ALTURA - size - PIPE_GAP)
    return (pipe, pipe_inverted)


screen = pygame.display.set_mode((SCREEN_COMPRIMENTO, SCREEN_ALTURA))

TELADEFUNDO = pygame.image.load('Fundo.jpg')
TELADEFUNDO = pygame.transform.scale(TELADEFUNDO, (SCREEN_COMPRIMENTO, SCREEN_ALTURA))

state_group = pygame.sprite.Group()
state = State()
state_group.add(state)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_COMPRIMENTO * i)
    ground_group.add(ground)

pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(SCREEN_COMPRIMENTO * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

clock = pygame.time.Clock()

while True:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                state.bump()
    screen.blit(TELADEFUNDO, (0, 0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_group = Ground(GROUND_COMPRIMENTO - 20)
        ground_group.add(new_group)

    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])

        pipes = get_random_pipes(SCREEN_COMPRIMENTO * 2)

        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    state_group.update()
    ground_group.update()
    pipe_group.update()

    state_group.draw(screen)
    pipe_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update()

    if (pygame.sprite.groupcollide(state_group, ground_group, False, False, pygame.sprite.collide_mask) or
            pygame.sprite.groupcollide(state_group, pipe_group, False, False, pygame.sprite.collide_mask)):
        # Game over
        pygame.display.update()
        break