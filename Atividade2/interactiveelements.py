import pygame
import sys

# This code is a simple implementation of an interactive square in a window. Press any arroy key to see it move

# Pygame initialization and window configuration
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Graphic Application (Activity 2 - Pygame)")

# Colors (RGB format)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Interactive object settings
object_x, object_y = 400, 300  # Initial position
object_size = 50
speed = 5

# Main game loop
running = True
while running:
    # Fill screen with white
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Real-time keyboard input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_x -= speed
    if keys[pygame.K_RIGHT]:
        object_x += speed
    if keys[pygame.K_UP]:
        object_y -= speed
    if keys[pygame.K_DOWN]:
        object_y += speed

    # Keep object within screen boundaries
    object_x = max(0, min(object_x, WIDTH - object_size))
    object_y = max(0, min(object_y, HEIGHT - object_size))

    # Draw object on screen
    pygame.draw.rect(screen, BLUE, (object_x, object_y, object_size, object_size))

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Cap at 60 FPS

pygame.quit()
sys.exit()
