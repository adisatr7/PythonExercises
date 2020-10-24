from tkinter import *

root = Tk()

root.title("@raddox7's First Basic Calculator")

e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=5)


def calc_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + number)


def calc_clear():
    e.delete(0, END)


def calc_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def calc_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def calc_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def calc_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def calc_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))
    else:
        print("Error: Invalid math operator!")


# Button size
px = 35
py = 35

# Define buttons
button_1 = Button(root, text="1", padx=px, pady=py, command=lambda: calc_click("1"))
button_2 = Button(root, text="2", padx=px, pady=py, command=lambda: calc_click("2"))
button_3 = Button(root, text="3", padx=px, pady=py, command=lambda: calc_click("3"))
button_4 = Button(root, text="4", padx=px, pady=py, command=lambda: calc_click("4"))
button_5 = Button(root, text="5", padx=px, pady=py, command=lambda: calc_click("5"))
button_6 = Button(root, text="6", padx=px, pady=py, command=lambda: calc_click("6"))
button_7 = Button(root, text="7", padx=px, pady=py, command=lambda: calc_click("7"))
button_8 = Button(root, text="8", padx=px, pady=py, command=lambda: calc_click("8"))
button_9 = Button(root, text="9", padx=px, pady=py, command=lambda: calc_click("9"))
button_0 = Button(root, text="0", padx=px, pady=py, command=lambda: calc_click("0"))
button_plus = Button(root, text="+", padx=px, pady=py, command=calc_add)
button_minus = Button(root, text="-", padx=px, pady=py, command=calc_sub)
button_multiply = Button(root, text="X", padx=px, pady=py, command=calc_mul)
button_divide = Button(root, text="/", padx=px, pady=py, command=calc_div)
button_equal = Button(root, text="=", padx=px, pady=py, command=calc_equal)
button_clear = Button(root, text="C", padx=px, pady=py, command=calc_clear)

# Button grids
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_equal.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_clear.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_plus.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_divide.grid(row=4, column=1)
button_minus.grid(row=4, column=2)
button_multiply.grid(row=4, column=3)


root.mainloop()