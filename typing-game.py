# Simple pygame program

# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Establish screen size
screenWidth = 800
screenHeight = 600

# Colors to be used
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

# Set up the drawing window
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the escape key?  If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button?  If so, stop the loop.
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background with white
    screen.fill((255,255,255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50,50))

    # Give the surface a color to separate it from the background
    surf.fill(black)
    rect = surf.get_rect()

    # Put the center of surf at the center of the display
    surf_center = (
        (screenWidth-surf.get_width())/2,
        (screenHeight-surf.get_height())/2
    )

    # This line says "Draw surf onto the screen at the center"
    screen.blit(surf, surf_center)
    pygame.display.flip()

# Done! Time to quit
pygame.quit()