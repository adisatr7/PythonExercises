from tkinter import *
from tkinter import filedialog, ttk

# -- Configs ---

app_name = "Demo Program"
app_icon = "app_icon.ico"
file_extension = [("TXT files", "*txt")]


# -- Functions ---

# Function: Returns file type
def get_file_type(file):
    return "*" + file.name[file.name.find("."):]


# Function: Returns file name without directory
def get_file_name(file):
    return file.name[file.name.find("/"):]


# Function: Returns file directory
def get_file_dir(file):
    return file.name


# Function: Reads an opened file
def read_file(file):
    print(f"Opened a file: {get_file_dir(file)}")
    bx_box.delete(0.0, END)
    bx_box.insert(INSERT, file.read())


# Button: bt_save_file
def save_file(saved_value):
    print("Opening file dialog...")
    file = filedialog.asksaveasfile(title="Save File", mode='w',
                                    filetypes=file_extension,
                                    defaultextension=file_extension)
    if file is not None:
        file.write(saved_value.get(1.0, END))
        print(f"File saved: {get_file_dir(file)}")
    else:
        print("No file was saved")


# Button: bt_safe_vile
def open_file():
    print("Opening file dialog...")
    opened_file = filedialog.askopenfile(title="Open File",
                                         multiple=False,
                                         filetypes=file_extension)
    if opened_file is not None:
        read_file(opened_file)
    else:
        print("No file was selected")


# Checkbox: Demo
def checkbox(v):
    print(is_checked.get())


# -- Main ---

gui = Tk()
gui.title(app_name)
gui.iconbitmap(app_icon)

# What to do with the box
Label(text=" Input a string:").grid(row=0, column=0, sticky=W)

# Slider test
vertical_slider = Scale(gui, from_=0, to=10, orient=VERTICAL)
vertical_slider.grid(row=0, column=1, rowspan=2)

# Write box
bx_box = Text(gui, height=4, width=32)
bx_box.grid(row=1, column=0)

# Save file button
bt_save_file = ttk.Button(gui, text="Save File", command=lambda: save_file(bx_box))
bt_save_file.grid(row=2, column=0, columnspan=2)

# Open file button
bt_open_file = ttk.Button(gui, text="Open File", command=open_file)
bt_open_file.grid(row=3, column=0, columnspan=2)

# Demo checkbox button
is_checked = IntVar()
bt_demo_checkbox = ttk.Checkbutton(gui, text="Demo textbox", variable=is_checked)
bt_demo_checkbox.grid(row=4, column=0, columnspan=2)

# -- End ---
gui.mainloop()
