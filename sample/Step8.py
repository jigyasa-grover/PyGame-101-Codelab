# Adding a Health Meter and Clock

# Adding the clock.

    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)
    
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    
    textRect = survivedtext.get_rect()
    
    textRect.topright=[635,5]
    
    screen.blit(survivedtext, textRect)
    

# Adding the health bar.

healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")

# The first is the red image used for the full health bar. The second is the green image used to show the current health level.

    # 6.5 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))
        
# The code first draws the all-red health bar. Then it draws a certain amount of green over the bar, according to how much life the castle has remaining.
