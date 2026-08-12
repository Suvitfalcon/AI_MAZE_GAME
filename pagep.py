import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
import subprocess
import pygame  

print("rampage ")


pygame.mixer.init()


pygame.mixer.music.load("god.mp3")
pygame.mixer.music.play(-1)  

def call_script():
    subprocess.run(["python", "d.py"])

def set2():
    subprocess.run(["python", "d2.py"])

def call():
    subprocess.run(["python", "call.py"])
def set():
    subprocess.run(["python", "d3.py"])

def button1_action():
    print("Button 1 clicked")

def button2_action():
    print("Button 2 clicked")

def button3_action():
    print("Button 3 clicked")

def button4_action():
    print("Button 4 clicked")

def exit_application():
    root.destroy()

root = tk.Tk()
root.title("Menu Page")
root.geometry("1600x1200")
heading = tk.Label(root, text="Rampage in Maze", font=("Helvetica", 16))
heading.pack(pady=20)
mylabel=Label(root, text = "rampage")
mylabel.pack()

background_image = PhotoImage(file="539311.png")


background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

heading = tk.Label(root, text="Rampage in Maze", font=("Helvetica", 16), bg="white")
heading.pack(pady=20)


call_button = tk.Button(root, text="Easy", command=call_script, width=15, height=2)
call_button.pack(pady=10)
button2 = tk.Button(root, text="Normal", command=set2, width=15, height=2)
call_button.pack(pady=10)
button3 = tk.Button(root, text="hard", command=set, width=15, height=2)
call_button.pack(pady=10)
exit_button = tk.Button(root, text="Exit", command=exit_application, width=15, height=2)
exit_button.pack(pady=10)
#button4 = tk.Button(root, text="Button 4", command=button4_action, width=15, height=2)
# lkvjnvv

call_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
exit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
#button4.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


root.mainloop()