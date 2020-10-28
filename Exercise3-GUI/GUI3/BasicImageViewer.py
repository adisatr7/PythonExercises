from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Basic Image Viewer")
root.iconbitmap("app_edit.ico")

img1 = ImageTk.PhotoImage(Image.open("Gallery/01.png"))
img2 = ImageTk.PhotoImage(Image.open("Gallery/02.png"))
img3 = ImageTk.PhotoImage(Image.open("Gallery/03.png"))
img4 = ImageTk.PhotoImage(Image.open("Gallery/04.png"))
img5 = ImageTk.PhotoImage(Image.open("Gallery/05.png"))

img_list = [img1, img2, img3, img4, img5]

img_holder = Label(image=img_list[0])
img_holder.grid(row=0, column=0, columnspan=3)

img_num = Label(root, text=f"Image 1 of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)


def navigate(image_number):
    global img_holder
    global bt_forward
    global bt_back
    global img_num

    img_holder.grid_forget()
    img_holder = Label(image=img_list[image_number - 1])

    bt_forward = Button(root, text=">>", command=lambda: navigate(image_number + 1))
    bt_back = Button(root, text="<<", command=lambda: navigate(image_number-1))
    img_num = Label(root, text=f"Image {image_number} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)

    img_holder.grid(row=0, column=0, columnspan=3)

    if image_number == len(img_list):
        bt_forward = Button(root, text=">>", state=DISABLED)
    if image_number == 1:
        bt_back = Button(root, text="<<", state=DISABLED)

    update_buttons()


def update_buttons():
    bt_back.grid(row=1, column=0, pady=7)
    bt_quit.grid(row=1, column=1, pady=7)
    bt_forward.grid(row=1, column=2, pady=7)
    img_num.grid(row=2, column=0, columnspan=3, sticky=W+E)


bt_back = Button(root, text="<<", state=DISABLED)
bt_quit = Button(root, text="Close", command=root.quit)
bt_forward = Button(root, text=">>", command=lambda: navigate(2))

update_buttons()

root.mainloop()