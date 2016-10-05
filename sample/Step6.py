# Creating randomly generated badgers

# Add bad guys to a list an array.
# Update the bad guy array each frame and check if they are off screen.

# First, add the following code to the end of section #2:
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

# The above sets up a timer so that the game adds a new badger after some time has elapsed. You decrease the badtimer every frame until it is zero and then you spawn a new badger.

# Now add the following to the end of section #3:
badguyimg1 = pygame.image.load("resources/images/badguy1.png")
badguyimg=badguyimg1

# Update and show the bad guys. 
# Add this code right after section #6.2:

    # 6.3 - Draw badgers
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
        
# The first line checks if badtimer is zero and if it is, creates a badger and sets badtimer up again based on how many times badtimer has run so far. 
# The first for loop updates the x position of the badger, checks if the badger is off the screen, and removes the badger if it is offscreen. The second for loop draws all of the badgers.

# In order to use the random function in the above code, you also need to import the random library. So add the following to the end of section #1:
import random

#Finally, add this line right after the while statement (section #4) to decrement the value of badtimer for each frame:
badtimer-=1

# Stoppingthe badgers crossing over the castle

# Add this code right before the index+=1 on the first for loop in section #6.3:
        # 6.3.1 - Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.3 - Next bad guy
