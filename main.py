import sys
import random
import pygame

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 446, 780
SPEED = 1
REC_WIDTH, REC_HEIGHT = 111, 260
SCORE = 0
PLAY = False

def random_y_positions_generator():
    """Generate a list of random y positions for rectangles."""
    # Generate a list of random numbers between -WINDOW_HEIGHT and -1
    numbers = [random.randint(-WINDOW_HEIGHT, -1) for _ in range(4)]
    # Choose a random index to replace with 0
    index = random.randint(0, 3)
    # Replace the number at the chosen index with 0
    numbers[index] = 0
    return numbers

# Initial positions and colors of rectangles
x_positions = [0, 2 + REC_WIDTH, 2 + (REC_WIDTH * 2), 2 + (REC_WIDTH * 3)]
y_positions = random_y_positions_generator()
colors = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

def update_colors(mouse):
    """Update colors of rectangles based on mouse position."""
    global colors
    mouse_x, mouse_y = mouse
    for idx in range(4):
        c1 = mouse_x >= x_positions[idx] 
        c2 = mouse_x <= x_positions[idx] + REC_WIDTH
        c3 = mouse_y >= y_positions[idx] 
        c4 = mouse_y <= y_positions[idx] + REC_HEIGHT
        if c1 and c2 and c3 and c4:
            colors[idx] = (116, 52, 235)  # Change color if mouse is over the rectangle
        else:
            colors[idx] = (0, 0, 0)

def update_y_positions(mouse=None):
    """Update y positions of rectangles."""
    global y_positions, SCORE, PLAY, SPEED
    if mouse:
        mouse_x, mouse_y = mouse
    for idx in range(4):
        if (y_positions[idx] + REC_HEIGHT) >= WINDOW_HEIGHT:
            # Print the final score
            print(f"\n\nSCORE: {SCORE}\n\n")
            PLAY = False
            y_positions = random_y_positions_generator()  # Reset positions if rectangle reaches bottom
            return
        else:
            if mouse:
                c1 = mouse_x >= x_positions[idx] 
                c2 = mouse_x <= x_positions[idx] + REC_WIDTH
                c3 = mouse_y >= y_positions[idx] 
                c4 = mouse_y <= y_positions[idx] + REC_HEIGHT
                if c1 and c2 and c3 and c4:
                    y_positions[idx] = random.randint(-WINDOW_HEIGHT, -1)
                    SCORE += 1  # Increment score if mouse clicks the rectangle
            else:
                y_positions[idx] += SPEED  # Move rectangle down

# Load background image and fonts
bg = pygame.image.load('Assets/bg.png')  # Load background image
score_font = pygame.font.SysFont('Arial', 35)  # Define score font
start_font = pygame.font.SysFont('Arial', 15)  # Define start font

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Piano Tiles")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Print the final score
                print(f"/n/nSCORE: {SCORE}\n\n")
                pygame.quit()
                sys.exit()

    # Clear the screen with the background image and draw divider lines
    screen.blit(bg, (0, 0))  # Draw background image
    pygame.draw.rect(screen, (255, 255, 255), (REC_WIDTH, 0, 2, WINDOW_HEIGHT))  # Draw divider lines
    pygame.draw.rect(screen, (255, 255, 255), (REC_WIDTH * 2, 0, 2, WINDOW_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (REC_WIDTH * 3, 0, 2, WINDOW_HEIGHT))

    # Update the position of the rectangles
    mouse = pygame.mouse.get_pos()
    update_colors(mouse)  # Update colors based on mouse position
    if PLAY:
        # Draw rectangles if game is running
        pygame.draw.rect(screen, colors[0], (x_positions[0], y_positions[0], REC_WIDTH, REC_HEIGHT))
        pygame.draw.rect(screen, colors[1], (x_positions[1], y_positions[1], REC_WIDTH - 2, REC_HEIGHT))
        pygame.draw.rect(screen, colors[2], (x_positions[2], y_positions[2], REC_WIDTH - 2, REC_HEIGHT))
        pygame.draw.rect(screen, colors[3], (x_positions[3], y_positions[3], REC_WIDTH, REC_HEIGHT))
        
        # Render and display score text
        text = score_font.render(f"Score: {SCORE}", False, (209, 77, 112))
        screen.blit(text, (WINDOW_WIDTH / 4, WINDOW_HEIGHT - 100))
        
        # Check for mouse clicks and update positions
        click = pygame.mouse.get_pressed()
        if click[0]:
            update_y_positions(mouse)
        else:
            update_y_positions(None)
        SPEED += 0.0005  # Increase speed gradually
    else:
        # Draw start button if game is not running
        pygame.draw.rect(screen, colors[2], (x_positions[2], WINDOW_HEIGHT - REC_HEIGHT, REC_WIDTH - 2, REC_HEIGHT))
        text = start_font.render("START", False, (255, 255, 255))
        screen.blit(text, (WINDOW_WIDTH / 1.75, WINDOW_HEIGHT - (REC_HEIGHT / 2)))
        # Check for mouse click on start button and start the game
        click = pygame.mouse.get_pressed()
        if click[0]:
            mouse_x, mouse_y = mouse
            c1 = mouse_x >= x_positions[2] 
            c2 = mouse_x <= x_positions[2] + REC_WIDTH
            c3 = mouse_y >= WINDOW_HEIGHT - REC_HEIGHT
            c4 = mouse_y <= WINDOW_HEIGHT
            if c1 and c2 and c3 and c4:
                PLAY = True  # Start the game if the start button is clicked

    # Update the display
    pygame.display.update()
