# Ian's file

# File Name : {required}
# Student Name: {required}
# email:  {required}
# Assignment Number: Assignment nn  {required}
# Due Date:   {required}
# Course #/Section:   {required}
# Semester/Year:   {required}
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

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

