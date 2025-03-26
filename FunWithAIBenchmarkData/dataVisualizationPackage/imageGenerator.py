# File Name : imageGenerator.py
# Student Name: Ian McDaniel
# email:  mcdaniip@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Using python packages with assitance of AI to display an image of our team mascot, the Pokemon Oddish

# Brief Description of what this module does. Increases our skills of python code and increased knowledge of python packages
# Citations: https://chatgpt.com

# Anything else that's relevant:

from PIL import Image, ImageTk
import tkinter as tk
import os

def show_team_image():
    """
    Displays a 200x200 pixel image in a Tkinter window called 'Team Logo'.
    """
    root = tk.Tk()
    root.title("Team Logo")

    # Load and resize image (maintaining aspect ratio)
    image_path = os.path.join("images", "team_logo.png")
    img = Image.open("dataPackage/MMLU/img/oddish.png")
    img.thumbnail((200, 200))  # Max size but keeps aspect ratio
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img_tk)
    label.pack()

    root.mainloop()

