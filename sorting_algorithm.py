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
FPS = 600

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting algorithm")
clock = pygame.time.Clock()

# Draws the rectangular shape sized and positioned as display
# so we can use it's coordinates for positioning
display_rect = display.get_rect()

# bottom left (0, 400)
# top left (0, 0)

line_width = 10

# Total number of lines in the screen
total_lines = int(display.get_width() / line_width)  # 200

# Pygame draws objects from the center/middle of the object
# Shift all lines to the right by half of the line width to fix the issue
line_offset = line_width / 2 - 1

# Store all drawn lines in the list
drawn_lines = []

lines_groups = pygame.sprite.Group()


class Line(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = line_width
        self.height = random.randint(0, 400)
        self.color = WHITE


def generate_lines():
    line_pos = 0
    for _ in range(total_lines):

        # drawn_lines.append(Line())
        lines_groups.add(Line())

        # line = pygame.draw.line(display, WHITE, (display_rect.bottomleft[0] + line_pos + line_offset, 400),
        #                         (display_rect.topleft[0] + line_pos + line_offset, random.randint(0, 400)), line_width)
        # line_pos += line_width
        # drawn_lines.append(line)


# def sort_lines():
#     line_pos = 0
#     for line in drawn_lines:
#         display.blit(display, ((display_rect.topleft[0] + line_pos), (display_rect.topleft[0] + line_pos)))
#         line_pos += line_width

# def randomize_lines():
#     random.shuffle(drawn_lines)


def game():
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
        # sort_lines()
        # if not is_sorted:
        #     sort_lines()
        #     is_sorted = False

        # Refresh/update the images on the display
        pygame.display.flip()


game()
print(lines_groups)
pygame.quit()
