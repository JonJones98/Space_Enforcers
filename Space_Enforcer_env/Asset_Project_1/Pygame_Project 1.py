import os
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")

WHITE =(255,255,255)
FPS = 60
YELLOW_SHACESHIP_IMAGE = pygame.image.load(os.path.join('Space_Enforcer_env/Asset_Project_1','spaceship_yellow'))
RED_SHACESHIP_IMAGE = pygame.image.load(os.path.join('Space_Enforcer_env/Asset_Project_1','spaceship_red'))

def draw_window():
    WIN.fill(WHITE, rect=None, special_flags=0)
    #WIN.blit(YELLOW_SHACESHIP_IMAGE,(300,250))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            draw_window()
            if event.type == pygame.quit:
                run = False

    pygame.quit()


if _name_ == " _main_":
    main()

