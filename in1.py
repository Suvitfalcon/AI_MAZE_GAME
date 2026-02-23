import tkinter as tk
from tkinter import PhotoImage
import subprocess
import pygame

# Initialize pygame mixer
pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("button_click.mp3")
    pygame.mixer.music.play()

def call_script():
    play_sound()
    subprocess.run(["python", "d.py"])

def set2():
    play_sound()
    subprocess.run(["python", "d2.py"])

def call():
    play_sound()
    subprocess.run(["python", "d3.py"])

def button1_action():
    play_sound()
    print("Button 1 clicked")

def button2_action():
    play_sound()
    print("Button 2 clicked")

def button3_action():
    play_sound()
    print("Button 3 clicked")

def button4_action():
    play_sound()
    print("Button 4 clicked")

# Create the main window
root = tk.Tk()
root.title("Menu Page")
root.geometry("700x600")

# Load the background image
background_image = PhotoImage(file="539311.png")

# Create a label to hold the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Heading label
heading = tk.Label(root, text="Rampage in Maze", font=("Helvetica", 16), bg="black")
heading.pack(pady=20)

# Create buttons
call_button = tk.Button(root, text="Easy", command=call_script, width=15, height=2)
button2 = tk.Button(root, text="Normal", command=set2, width=15, height=2)
button3 = tk.Button(root, text="Button 3", command=button3_action, width=15, height=2)
button4 = tk.Button(root, text="Button 4", command=button4_action, width=15, height=2)

# Place buttons on the left side of the window
call_button.place(relx=0.1, rely=0.3, anchor=tk.W)
button2.place(relx=0.1, rely=0.4, anchor=tk.W)
button3.place(relx=0.1, rely=0.5, anchor=tk.W)
button4.place(relx=0.1, rely=0.6, anchor=tk.W)

# Add text in the middle of the page
middle_text = tk.Label(root, text="Save the princess!", font=("Helvetica", 18), bg="white")
middle_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main loop
root.mainloop()