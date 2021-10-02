import pygame
import random
import operator
from colors import color_dict

# Initialize pygame essentials
pygame.init()

# Load the background image
image = pygame.image.load("bg.jpg")
image_rect = image.get_rect()

# Screen settings
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
SCREEN_BG_COLOR = (30, 30, 30)

# Time / FPS
FPS = 1000

# Set the main preview display/window with width and height
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Draw the display shape sized and positioned as display
# so we can use it's coordinates for positioning other elements
display_rect = display.get_rect()

pygame.display.set_caption("Sorting algorithm")
clock = pygame.time.Clock()

# Width of the line (change for the total number of lines)
line_width = 1

# Total number of lines in the screen
total_lines = int(display.get_width() / line_width)

# Store all drawn lines in the list
drawn_lines = []


class Line():
    """A class to manage a single line parameters"""

    def __init__(self, color):
        self.width = line_width  # 10
        self.height = random.randint(-400, 0)
        self.color = color
        self.surface = pygame.Surface((self.width, abs(self.height)))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect()
        self.rect.bottom = display_rect.bottom


def generate_lines():
    """Generate lines across the screen"""
    line_x_position = 0
    # Set the random color for every line generation cycle
    new_color = random.choice(list(color_dict))
    new_color = str(new_color)

    # Create the total_lines amount of objects and fill the line list with them
    for _ in range(total_lines):
        line = Line(new_color)
        line.rect.x += line_x_position
        drawn_lines.append(line)
        line_x_position += line_width


def draw_lines():
    """Draw the generated lines from the line list"""
    for line in drawn_lines:
        display.blit(line.surface, line.rect)


def redraw_lines():
    """Empty the list filled with line objects.
    Generate new lines and redraw them on the screen again."""
    drawn_lines.clear()
    generate_lines()
    draw_lines()


def sort():
    """Sort the objects inside the line list by height"""
    drawn_lines.sort(key=operator.attrgetter('height'))
    line_x_position = 0
    for line in drawn_lines:
        line.rect.x = line_x_position
        line_x_position += line_width


def draw_sorted():
    for line in drawn_lines:
        display.blit(line.surface, line.rect)


def main():
    """The main loop"""

    is_generated = False
    is_sorted = False

    while True:
        # Handle the user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    redraw_lines()
                elif event.key == pygame.K_RIGHT:
                    sort()
                    is_sorted = True

        # Generate lines in list
        if not is_generated:
            generate_lines()
            is_generated = True

        # Draws the background image
        display.fill(SCREEN_BG_COLOR)

        if not is_sorted:
            draw_lines()
        else:
            draw_sorted()

        # Refresh/update the images on the display
        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
