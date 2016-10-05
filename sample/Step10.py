# Music and Sound Effects

# Initializing the mixer by adding this at the end of section #2:
pygame.mixer.init()

# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")

hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)

pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

#"pygame.mixer.music.load"  – it loads the background music for the game and the next line sets the background music to repeat forever.

# section 6.3.1 after if badrect.left<64:
hit.play()

# section 6.3.2 after if badrect.colliderect(bullrect):
enemy.play()

# section 8, after if event.type==pygame.MOUSEBUTTONDOWN:
shoot.play()

