import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 505

cur_states = [0] * 400
for i in range(0, len(cur_states), 2):
 cur_states[i] = 1
for i in range(200, len(cur_states), 1):
 cur_states[i] = 0
# for i in cur_states:
#  if cur_states.index(cur_states[i]) % 2 is not 0:
#   cur_states[i] == 1
post_states = []

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    x = 5
    index = 0
    off = 0
    on = 1
    while x < 500:
     y = 5
     index += 1
     while y < 500:
      # Draw based on cur states
      state = cur_states[index]
      # Draw based on values in next state, or post state
      if state is on:
       pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
      elif state is off:
       pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
      y += 25
     x += 25

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
