import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# 1. Create a set of initial states with simple pattern (Ex. blinker)
state_row = [0] * 20
cur_states = [state_row] * 20
# for i in range(0, 400, 2):
#  cur_states[i] = 0

# cur_states[0][0] = 1
# cur_states[30][0] = 1
# cur_states[50][0] = 1
next_states = []
print(cur_states)
print(len(cur_states))
pygame.init()
 # | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
 # | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
 # | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
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
    on = 1
    off = 0
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    for i in range(20):
     
     cur_states[i][i]
     
    # for x in cur_states:
    #  if x is on:
    #   if not cur_states[x - 1]:
    #    val = cur_states[x + 1] % 2
    #    next_states[x] = val
    #   elif cur_states[x - 1]:
    #    val = cur_states[x - 1] + cur_states[x + 1]
    #    next_states[x] = val
    
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    # 3. Work on rules that i) look at all neighbors, ii) save new state
    # in next_states[]

 
    # --- Screen-clearing codecur_states[30][0] = 1
# cur_states[50][0] = 1 goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    # index = 0
    # x = 5
    # while x < 500: 
    #     y = 5
    #     while y < 500:
    #         # 2. Draw based on values in cur_states
    #         state = cur_states[index]
    #         # 4. Draw based on values in next_states
    #         if state == 0:
    #             pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20) )
    #         else:
    #             pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20) )
    #         index += 1
    #         y += 25
    #     x += 25


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()