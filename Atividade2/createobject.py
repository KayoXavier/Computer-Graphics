import pygame
import sys
import math
# This code implements a simple interactive program that allows you to create and move diferent objects with your mouse
# Pygame initialization
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Graphic Application")

# Colors
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (128, 0, 128)   # Purple
]

# Predefined objects
objects = [
    {
        'type': 'circle',
        'color': COLORS[0],
        'position': (200, 300),
        'radius': 50
    },
    {
        'type': 'rectangle',
        'color': COLORS[2],
        'rect': pygame.Rect(500, 200, 120, 80)
    },
    {
        'type': 'circle',
        'color': COLORS[4],
        'position': (400, 450),
        'radius': 70
    },
    {
        'type': 'rectangle',
        'color': COLORS[3],
        'rect': pygame.Rect(100, 100, 200, 150)
    }
]

# State variables
current_color = 0
shape_type = "circle"
dragging = False
selected_object = None
offset = (0, 0)
creating = False
initial_pos = (0, 0)

def draw():
    screen.fill((255, 255, 255))  # White background
    
    # Draw all objects
    for obj in objects:
        if obj['type'] == 'circle':
            pygame.draw.circle(screen, obj['color'], obj['position'], obj['radius'])
        elif obj['type'] == 'rectangle':
            pygame.draw.rect(screen, obj['color'], obj['rect'])
    
    # Draw temporary shape during creation
    if creating:
        if shape_type == 'circle':
            radius = int(math.hypot(initial_pos[0]-pygame.mouse.get_pos()[0], 
                                  initial_pos[1]-pygame.mouse.get_pos()[1]))
            pygame.draw.circle(screen, COLORS[current_color], initial_pos, radius, 2)
        else:
            rect = pygame.Rect(initial_pos, (pygame.mouse.get_pos()[0]-initial_pos[0], 
                                           pygame.mouse.get_pos()[1]-initial_pos[1]))
            pygame.draw.rect(screen, COLORS[current_color], rect, 2)
    
    pygame.display.flip()

def main():
    global current_color, shape_type, dragging, selected_object, offset, creating, initial_pos
    
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left button
                    pos = pygame.mouse.get_pos()
                    
                    # Check if clicked on existing object
                    for obj in reversed(objects):
                        if obj['type'] == 'circle':
                            distance = math.hypot(pos[0]-obj['position'][0], pos[1]-obj['position'][1])
                            if distance <= obj['radius']:
                                selected_object = obj
                                offset = (obj['position'][0] - pos[0], obj['position'][1] - pos[1])
                                dragging = True
                                break
                        elif obj['type'] == 'rectangle' and obj['rect'].collidepoint(pos):
                            selected_object = obj
                            offset = (pos[0] - obj['rect'].x, pos[1] - obj['rect'].y)
                            dragging = True
                            break
                    else:  # If didn't click any object
                        creating = True
                        initial_pos = pygame.mouse.get_pos()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if creating:
                        # Create final object
                        final_pos = pygame.mouse.get_pos()
                        if shape_type == 'circle':
                            radius = int(math.hypot(initial_pos[0]-final_pos[0], initial_pos[1]-final_pos[1]))
                            if radius > 0:
                                objects.append({
                                    'type': 'circle',
                                    'color': COLORS[current_color],
                                    'position': initial_pos,
                                    'radius': radius
                                })
                        else:
                            width = final_pos[0] - initial_pos[0]
                            height = final_pos[1] - initial_pos[1]
                            if width != 0 and height != 0:
                                rect = pygame.Rect(initial_pos, (width, height))
                                rect.normalize()
                                objects.append({
                                    'type': 'rectangle',
                                    'color': COLORS[current_color],
                                    'rect': rect
                                })
                        creating = False
                    dragging = False
                    selected_object = None
            
            elif event.type == pygame.MOUSEMOTION and dragging:
                if selected_object:
                    if selected_object['type'] == 'circle':
                        new_x = pygame.mouse.get_pos()[0] + offset[0]
                        new_y = pygame.mouse.get_pos()[1] + offset[1]
                        selected_object['position'] = (new_x, new_y)
                    else:
                        new_x = pygame.mouse.get_pos()[0] - offset[0]
                        new_y = pygame.mouse.get_pos()[1] - offset[1]
                        selected_object['rect'].x = new_x
                        selected_object['rect'].y = new_y
            
            # Keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_color = (current_color + 1) % len(COLORS)
                elif event.key == pygame.K_c:
                    shape_type = "circle"
                elif event.key == pygame.K_r:
                    shape_type = "rectangle"
        
        draw()

if __name__ == "__main__":
    main()
