import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
loaded_apps = []

# To load a previously loaded apps from another session
if os.path.isfile("GUI_Training1_save.txt"):
    with open("save.txt", "r") as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(',')
        print("Loaded apps: " + str(temp_apps))
        loaded_apps = [x for x in temp_apps if x.strip()]


# Add an app to the list
def add_app():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open File",
                                          filetypes=(("Executables", "*.exe"),
                                                     ("All files", "*.*")))

    clear_list()

    loaded_apps.append(filename)
    print("Added an app to the list: " + filename)

    update_label()


# Run those apps that are in the list
def run_apps():
    for app in loaded_apps:
        os.startfile(app)


# Clear loaded apps list
def clear_list():
    loaded_apps.clear()
    print("App list cleared!")

    for widget in frame.winfo_children():
        widget.destroy()


# Updates the app list label
def update_label():
    for app in loaded_apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


canvas = tk.Canvas(root, height=600, width=800, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Open button
open_file = tk.Button(root, text="Open File",
                      padx=10, pady=5,
                      fg="white", bg="#263D42",
                      command=add_app)
open_file.pack()

# Run button
run_app = tk.Button(root, text="Run Apps",
                    padx=10, pady=5,
                    fg="white", bg="#263D42",
                    command=run_apps)
run_app.pack()

# Clear button
clear_app = tk.Button(root, text="Clear App List",
                      padx=10, pady=5,
                      fg="white", bg="#263D42",
                      command=clear_list)
clear_app.pack()

# Update the label
update_label()

# Loop the program
root.mainloop()

# Save the loaded apps list into a file
with open("save.txt", "w") as f:
    for app in loaded_apps:
        f.write(app + ", ")
print("Saving loaded apps list...")