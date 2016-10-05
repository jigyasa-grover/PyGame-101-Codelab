# Adding a background to the game scene. 

#3, after loading the Player image
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")


# Tile the grass over the screen area to cover it completely

#6 (before the player is drawn on screen):
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    

