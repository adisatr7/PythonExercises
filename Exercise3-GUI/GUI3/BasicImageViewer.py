from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Basic Image Viewer")
root.iconbitmap("app_edit.ico")

img1 = ImageTk.PhotoImage(Image.open("Gallery/01.jpg"))
img2 = ImageTk.PhotoImage(Image.open("Gallery/02.jpg"))
img3 = ImageTk.PhotoImage(Image.open("Gallery/03.jpg"))
img4 = ImageTk.PhotoImage(Image.open("Gallery/04.jpg"))
img5 = ImageTk.PhotoImage(Image.open("Gallery/05.jpg"))

img_list = [img1, img2, img3, img4, img5]

my_label = Label(image=img_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def navigate(image_number):
    global my_label
    global bt_forward
    global bt_back

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])

    bt_forward = Button(root, text=">>", command=lambda: navigate(image_number + 1))
    bt_back = Button(root, text="<<", command=lambda: navigate(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)

    if image_number == len(img_list):
        bt_forward = Button(root, text=">>", state=DISABLED)
    if image_number == 1:
        bt_back = Button(root, text="<<", state=DISABLED)

    update_buttons()


def update_buttons():
    bt_back.grid(row=1, column=0)
    bt_quit.grid(row=1, column=1)
    bt_forward.grid(row=1, column=2)


bt_back = Button(root, text="<<", state=DISABLED)
bt_quit = Button(root, text="Close", command=root.quit)
bt_forward = Button(root, text=">>", command=lambda: navigate(2))

update_buttons()

root.mainloop()