# Simple pygame program using the tutorial found at https://realpython.com/pygame-a-primer/

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

# Define a player object by extending pygame.sprite.Sprite
# The surface that is drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(white)
        self.rect = self.surf.get_rect()

# Initiate player.  Right now, it's just a rectangle
player = Player()
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
    
    # Fill the background with black
    screen.fill(black)

    # Draw the player on the screen
    screen.blit(player.surf, (screenWidth/2,screenHeight/2))
    pygame.display.flip()

# Done! Time to quit
pygame.quit()