import tkinter as tk
import pygame
import pandas as pd

root = tk.Tk()   # start an instance of tkinter, called root
root.title("Awesome clicking game!")   # name the window 
tk.Label(root, text = "Type your name:").pack()   # whatever we pack, it will be on the top left of the screen by default, and the next
id_username = tk.Entry(root)
id_username.pack()

name = ""
running = False
df = pd.DataFrame(columns=["Time", 
                           "Click_X", 
                           "Click_Y", 
                           "In_Box"])

def start_game():
    global name, screen, running   # global makes the variable available for the whole script 
    name = id_username.get()
    root.destroy()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True

tk.Button(root, text = "Start Cool Game", command = start_game).pack()
root.mainloop()

# define some variables before starting the while loop will make the computer fun faster
box = pygame.Rect(200, 300, 100, 100)
font = pygame.font.Font(None, 36)

while running:
    mouse_position = pygame.mouse.get_pos()

    # event log: all inputs to computer
    for event in pygame.event.get():   # event log only registers keyboard keys, not mouse
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            data.append(event.pos)
            print(f"You clicked the mouse button at coords {event.pos}!")   # not showing up in the window, only in the terminal
            if box.collidepoint(event.pos):
                print("Yayy, you clicked the box!")
                trial_data = {
                    "Time": pygame.time.get_ticks(), 
                    "Click_X": event.pos[0]
                    "Click_Y": event.pos[1]
                    "In_Box": True
                }
            else:


    if box.collidepoint(mouse_position):
        box_color = "red"
    else:
        box_color = "purple"

    pygame.draw.rect(screen, box_color, box)

    if box.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:   # [0] for left mouse click and [1] for right mouse click
        text = font.render("Yayy, you can click!!", True, "teal")
        screen.blit(text, (300, 300))

    pygame.display.flip()
pygame.quit()

root = tk.Tk()
root.title("Game over!")
text = tk.Text(root, height=2, width=50)
text.insert(tk.END, f"Data backup: {df["Time"]}")
text.pack()
root.mainloop()

df.to_excel("Cool_Game_Data.xlsx", index = False)

# in reality, we should always have at least two ways of saving the data: saving while the task is running and at the end
# for the assignment, have at least three ways saving the data:
# happening during the task 
# text file at the end 
# excel sheet at the end 
# copy and paster at the end
# print it to the terminal, using append in-between game states

