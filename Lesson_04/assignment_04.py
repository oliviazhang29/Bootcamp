# build on assignment_03
# have three people to play before tomorrow's class

# at the end, put the codes into AI and ask it to comment on the codes 
# ask whether it has any suggestions to realize some functions I want

# something extra: ask AI how to add time to the game

import pygame
import tkinter as tk
import pandas as pd

root = tk.Tk()   # start an instance of tkinter, called root
root.title("Awesome drawing game!")   # name the window 
tk.Label(root, text = "Type your name:").pack()   # whatever we pack, it will be on the top left of the screen by default, and the next
id_username = tk.Entry(root)
id_username.pack()

name = ""
running = False
data = pd.DataFrame()
drawn_points = []

def start_game():
    global name, screen, running   # global makes the variable available for the whole script 
    name = id_username.get()
    root.destroy()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cool Drawing Game!") #set window title
    running = True

tk.Button(root, text = "Start Game", command = start_game).pack()
root.mainloop()

# define some variables before starting the while loop will make the computer fun faster
box = pygame.Rect(200, 300, 100, 100)
font = pygame.font.Font(None, 36) #default font, size 36
state = "instruction0" #initial state
img = pygame.image.load("IRT_Perc_PostDD.png")
drawing = False
last_pos = None
just_entered_draw_state = False

while running:
    mouse_pos = pygame.mouse.get_pos()

    # event log: all inputs to computer
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #exit on window close
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state == "instruction0":
                state = "instruction1" #transition to the instruction1 state
            elif state == "instruction1":
                state = "display" # transition to the display state, different tasks should be named differently, so that we can reference and distinguish them, e.g., when we want to go back to a state
            elif state == "display":
                state = "instruction2" #transition to the instruction2 state
            elif state == "instruction2":
                state = "draw" # transition to draw state
                just_entered_draw_state = True
            elif state == "draw":
                state = "finished" # transition to the finished state
                data = pd.DataFrame(drawn_points, columns=["x", "y"])   # ✅ Save points to dataframe
                print(data)  # Optional: confirm it's working
                data.to_excel("drawing_data01.xlsx", index=False)
            elif state == "finished":
                running = False #exit game

        # ✅ Mouse event handling ONLY during draw state
    if state == "draw":
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            mouse_pos = event.pos
            if last_pos:
                pygame.draw.line(screen, "white", last_pos, mouse_pos, 3)
                drawn_points.append(mouse_pos)   # ✅ Record current coordinate
            last_pos = mouse_pos

    if state == "instruction0":
        screen.fill((0, 0, 0)) #black background
        font = pygame.font.Font(None, 36)
        text = font.render("Press space to move forward.", True, "white")
        screen.blit(text, (200, 300))

    elif state == "instruction1":
        screen.fill((0, 0, 0)) 
        #add your text/shapes/images here (e.g., game task elements)
        font = pygame.font.Font(None, 36)
        text = font.render("Memorize the following plot as much as possible.", True, "white")
        screen.blit(text, (100, 300))

    elif state == "display":
        screen.fill((0, 0, 0)) 
        screen.blit(img, (50,100, 50, 50))

    elif state == "instruction2":
        screen.fill((0, 0, 0))  
        font = pygame.font.Font(None, 36)
        text = font.render("On the next page, draw the plot you just saw using your mouse.", True, "white")
        screen.blit(text, (50, 300))

    elif state == "draw":
        if just_entered_draw_state:
            screen.fill((0, 0, 0))  # Clear screen just once when entering
            just_entered_draw_state = False   # do not clear the screen again — lines will accumulate as drawn

    elif state == "finished":
        screen.fill((0, 100, 0)) #green background
        font = pygame.font.Font(None, 36)
        text = font.render("Game over!", True, "white")
        screen.blit(text, (350, 300))

    pygame.display.flip() #refresh screen, has to be in the while loop
pygame.quit() #exit pygame

root = tk.Tk()
root.title("Game over!")
text = tk.Text(root, height=100, width=50)
text.insert(tk.END, f"Data backup: {data}")
text.pack()
root.mainloop()