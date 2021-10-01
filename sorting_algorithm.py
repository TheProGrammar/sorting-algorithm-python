import pygame
import random

# Initialize pygame essentials
pygame.init()

# Screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
SCREEN_BG_COLOR = (30, 30, 30)

# Time / FPS
FPS = 60

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Draw the display shape sized and positioned as display
# so we can use it's coordinates for positioning other elements
display_rect = display.get_rect()
pygame.display.set_caption("Sorting algorithm")
clock = pygame.time.Clock()

line_width = 10

# Total number of lines in the screen
total_lines = int(display.get_width() / line_width)

# Pygame draws objects from the center/middle of the object
# Shift all lines to the right by half of the line width to fix the issue
line_offset = line_width / 2 - 1

# Store all drawn lines in the list
drawn_lines = []

lines_groups = pygame.sprite.Group()
test = pygame.Surface((line_width, 400))
test.fill('White')


class Line(pygame.sprite.Sprite):
    def __init__(self):
        super(Line, self).__init__()
        self.rect = pygame.Rect()


def generate_lines():
    for _ in range(1):
        line = Line()


def draw_lines():
    for line in lines_groups:
        display.blit(line, (0, 400))


def main():
    is_generated = False
    is_sorted = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass

        if not is_generated:
            generate_lines()
            is_generated = True

        draw_lines()

        # Refresh/update the images on the display
        pygame.display.flip()


main()
pygame.quit()
