import pygame 

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Author Game!!")

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   # these codes are telling the computer to close the while loop when running is False (clicking the "x")

    pygame.draw.rect(screen, "red", (100, 100, 50, 50))   # the top left corner of the rectangle will be on the coordinates (first two numbers) you tell the computer, and the next two numbers tells the size of the rectangle

    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to my cool game!", True, "white")
    screen.blit(text, (200, 300))

    image = pygame.image.load("IRT_Perc_PostDD.png")
    
    screen.blit(image, (300,300, 50, 50))

    pygame.display.flip()   # refresh your screen, like flipping a whiteboard that being drawed by the computer
pygame.quit()

