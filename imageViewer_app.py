from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# images
img1 = ImageTk.PhotoImage(Image.open('g1.jpeg'))
img2 = ImageTk.PhotoImage(Image.open('g2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('g3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('g4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('g5.jpeg'))
list_image = [img1, img2, img3, img4, img5]

# labeling image
myLabel = Label(root, image=list_image[0])
myLabel.grid(columnspan=3)

# forward function
def forward(number):
    global myLabel
    global button_forward
    global button_back
    myLabel.grid_forget()
    myLabel = Label(root, image=list_image[number - 1])
    myLabel.grid(row=0, columnspan=3)
    print(number)
    button_back = Button(root, text="<<", command=lambda: back(number - 1)).grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(number + 1)).grid(row=1, column=2)
    if number == 5:
        button_forward = Button(root, text=">>", state=DISABLED).grid(row=1, column=2)

# backward function
def back(number):
    global myLabel
    global button_forward
    global button_back
    myLabel.grid_forget()
    myLabel = Label(root, image=list_image[number - 1])
    myLabel.grid(row=0, columnspan=3)
    print(number)

    button_back = Button(root, text="<<", command=lambda: back(number - 1))
    button_back.grid(row=1, column=0)

    button_forward = Button(root, text=">>", command=lambda: forward(number + 1)).grid(row=1, column=2)
    if number == 1:
        button_back = Button(root, text="<<", state=DISABLED).grid(row=1, column=0)


button_back = Button(root, text="<<", state=DISABLED, command=back).grid(row=1, column=0)
button_exit = Button(root, text="Exit", command=root.quit).grid(row=1, column=1)
button_forward = Button(root, text=">>", command=lambda: forward(2)).grid(row=1, column=2)
root.mainloop()
