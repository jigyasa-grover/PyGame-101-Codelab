# Make the Bunny Move


#2 (after you set the screen height and width):
keys = [False, False, False, False]
playerpos=[100,100]

# Use the "playerpos" variable to draw the player
 
# Change the following line in section #6:
    screen.blit(player, (100,100))
# To:
    screen.blit(player, playerpos)
    
# Update the keys array based on which keys are being pressed.
 
# PyGame makes detecting key presses easy by adding event.key functions.

# At the end of section #8, right after the block checking for event.type==pygame.QUIT, put this code (at the same indentation level as the pygame.QUIT if block):

        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

# Add the following code to the end of game.py (with one indentation level, putting it at the same level as the for loop):

    # 9 - Move player
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
        
# This code simply checks which of the keys are being pressed and adds or subtracts from the player’s x or y position 
# (depending on the key pressed) to move the player.
