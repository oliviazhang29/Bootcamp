import pygame
pygame.init() #initialize pygame
screen = pygame.display.set_mode((800, 600))#create 800x600 window
pygame.display.set_caption("Mini Game") #set window title
font = pygame.font.Font(None, 36) #default font, size 36
state = "instructions" #initial state
running = True

while running:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #exit on window close
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state == "instructions":
                state = "task1" #transition to the first task state
            elif state == "task1":
                state = "task2" # transition to the second task state, different tasks should be named differently, so that we can reference and distinguish them, e.g., when we want to go back to a state
            elif state == "task2":
                state = "finished" #transition to finished state
            elif state == "finished":
                running = False #exit game

    if state == "instructions":
        screen.fill((0, 0, 0)) #black background
        #add your text/shapes/images here (e.g., instruction text)
        # pygame.draw.rect(screen, "red", (100, 100, 50, 50))
        font = pygame.font.Font(None, 36)
        text = font.render("Press space to move forward.", True, "white")
        screen.blit(text, (200, 300))

    elif state == "task1":
        screen.fill((0, 0, 100)) #blue background
        #add your text/shapes/images here (e.g., game task elements)
        font = pygame.font.Font(None, 36)
        text = font.render("Press again to see my first year project IRT plot!", True, "white")
        screen.blit(text, (100, 300))

    elif state == "task2":
        screen.fill((0, 0, 100)) #blue background
        image = pygame.image.load("IRT_Perc_PostDD.png")
        screen.blit(image, (50,100, 50, 50))

    elif state == "finished":
        screen.fill((0, 100, 0)) #green background
        #add your text/shapes/images here (e.g., game over text)
        font = pygame.font.Font(None, 36)
        text = font.render("Game over!", True, "white")
        screen.blit(text, (350, 300))

    pygame.display.flip() #refresh screen, has to be in the while loop
pygame.quit() #exit pygame