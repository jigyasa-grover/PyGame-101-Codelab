# Collisions with Badgers and Arrows

# Looping through all of the bad guys and inside each of those loops, you have to loop through all of the arrows and check if they collide. 
# If they do, then delete the badger, delete the arrow, and add one to your accuracy ratio.

#Right after section #6.3.1, add this:
        #6.3.2 - Check for collisions
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1
