from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os

# -- Configs ---

TITLE = "Database Demo Program"
ICON = "app_icon.ico"


# -- Functions ---

# Function: Clear all forms
def clear_forms():
    bx_name.delete(0.0, END)
    bx_id.delete(0.0, END)
    bx_address.delete(0.0, END)


# Function: Create 'addresses' table
def database_setup():
    print(f"Creating table addresses...")
    database = sqlite3.connect("user_info.db")
    cursor = database.cursor()
    cursor.execute(f"CREATE TABLE addresses ("
                   "name text, "
                   "id text,"
                   "address text )")
    print("Table addresses has been created!")
    database.commit()
    database.close()


# Function: Insert inputted data to database
def database_push():
    is_exist = os.path.isfile("user_info.db")

    print("Establishing connection to database...")
    database = sqlite3.connect("user_info.db")

    print("Connected to database!")
    cursor = database.cursor()

    if not is_exist:
        print("First run detected!")
        database_setup()

    print("Uploading user info...")
    cursor.execute("INSERT INTO addresses VALUES ("
                   ":dm_name,"
                   ":dm_id,"
                   ":dm_address)", {
                       "dm_name": bx_name.get(0.0, "end-1c"),
                       "dm_id": bx_id.get(0.0, "end-1c"),
                       "dm_address": bx_address.get(0.0, "end-1c")
                   })
    print("Process finished!")

    print("Committing changes...")
    database.commit()

    print("All changes have been saved!")
    database.close()


# Function: Prints out database records
def database_print():
    is_exist = os.path.isfile("user_info.db")

    print("Establishing connection to database...")
    database = sqlite3.connect("user_info.db")

    print("Connected to database!")
    cursor = database.cursor()

    if not is_exist:
        print("First run detected!")
        messagebox.showerror(TITLE, "Database is empty!")
        database_setup()

    else:
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()
        print(records)

        print_record = ""

        for record in records:
            print_record += str(record) + "\n"

        lb_query = Label(GUI, text=print_record)
        lb_query.grid(row=5, column=0, columnspan=2)

    database.commit()
    database.close()


# -- Buttons ---

# Button: Submit
def bt_submit():
    database_push()
    clear_forms()
    messagebox.showinfo("Data Submitted!",
                        "Your data has been submitted!")


# Button: Show Records
def bt_show_records():
    database_print()


# -- Main ---

if __name__ == '__main__':
    # GUI Initialization
    GUI = Tk()
    GUI.title(TITLE)
    # GUI.iconbitmap(ICON)

    # Form: Name
    lb_name = Label(GUI, text="Name: ")
    lb_name.grid(row=0, column=0, sticky=W)
    bx_name = Text(GUI, height=1, width=20)
    bx_name.grid(row=0, column=1, columnspan=3)

    # Form: ID
    lb_id = Label(GUI, text="ID: ")
    lb_id.grid(row=1, column=0, sticky=W)
    bx_id = Text(GUI, height=1, width=20)
    bx_id.grid(row=1, column=1, columnspan=3)

    # Form: Address
    lb_address = Label(GUI, text="Address: ")
    lb_address.grid(row=2, column=0, sticky=W + N)
    bx_address = Text(GUI, height=3, width=20)
    bx_address.grid(row=2, column=1, columnspan=3)

    # Button: Submit
    bt_submit = ttk.Button(GUI, text="Submit", command=bt_submit)
    bt_submit.grid(row=3, column=0, columnspan=2, sticky=E+W)

    # Button: Query
    bt_show_records = ttk.Button(GUI, text="Show Records", command=database_print)
    bt_show_records.grid(row=3, column=2, columnspan=2, sticky=E+W)

    # -- End of the Line ---
    GUI.mainloop()
