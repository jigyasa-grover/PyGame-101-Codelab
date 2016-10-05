# Turning the Bunny

# Steps:
# First you get the mouse and player positions. 
# Then you feed those into the atan2 function. 
# After that, you convert the angle received from the atan2 function from radians to degrees (multiply radians by approximately 57.29 or 360/2π).
# Since the bunny will be rotated, its position will change. 
# So now you calculate the new bunny position and display the bunny on screen.

# The atan2 function comes from the Python math library. So add this to the end of section #1 first:
import math

# Then, replace the last line in section #6 (the player.blit line) with the following :
   
    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()    
    
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    
    screen.blit(playerrot, playerpos1)
    
    

