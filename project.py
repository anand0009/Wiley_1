import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.pyplot import title




win = tk.Tk()

# Set the geometry of Tkinter Frame
win.geometry("900x650")

# Open the Image File
bg = ImageTk.PhotoImage(file="bg.jpg")


# Create a Canvas
canvas = tk.Canvas(win, width=2560, height=1440)
canvas.pack(expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("bg.jpg")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)

# def open_file():
#     browse_file.set("Loading...")


# browse_file = tk.StringVar()
# browse_btn = tk.Button(textvariable = browse_file, command= open_file(), font= "Raleway", bg="#20bebe", fg="white", height=2,width=15 )
# browse_file.set("Choose a File")
# browse_btn.grid(column=2,row=2)

win.mainloop()