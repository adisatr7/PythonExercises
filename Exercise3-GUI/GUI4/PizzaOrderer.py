from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# -- Initialization ---
root = Tk()
root.title("Pizza Orderer™")
root.iconbitmap("icon.ico")

# -- Order form ---
Label(root, text="Enter your info here:").grid(row=0, column=0, columnspan=2, padx=5, pady=3)

# Form: Name
Label(root, text="Recipient's Name").grid(row=1, column=0, padx=3, sticky=W)
user_name = StringVar(value=" Enter your full name")
Entry(root, textvariable=user_name, width=23).grid(row=1, column=1, padx=7)

# Form: Address
Label(root, text="Recipient's Address").grid(row=2, column=0, padx=3, sticky=W)
user_street = StringVar(value=" Street Address")
Entry(root, textvariable=user_street, width=23).grid(row=2, column=1, padx=7)
user_city = StringVar(value=" City")
Entry(root, textvariable=user_city, width=23).grid(row=3, column=1, padx=7)
user_state = StringVar(value=" State / Province")
Entry(root, textvariable=user_state, width=23).grid(row=4, column=1, padx=7)

# Form: Phone number
Label(root, text="Phone Number").grid(row=5, column=0, padx=3, sticky=W)
user_phone = StringVar(value=" 0xx-xxx-xxxx")
Entry(root, textvariable=user_phone, width=23).grid(row=5, column=1, padx=7)

# -- Pizza preview image ---
text_preview = Label(root, text="Preview:").grid(row=0, column=3, columnspan=3, padx=5, sticky=W)

# Image: Locate files
img_empty = ImageTk.PhotoImage(Image.open("pizza/empty.png"))
img_bbq = ImageTk.PhotoImage(Image.open("pizza/bbq.png"))
img_cheese = ImageTk.PhotoImage(Image.open("pizza/cheese.png"))
img_hawaiian = ImageTk.PhotoImage(Image.open("pizza/hawaiian.png"))
img_margherita = ImageTk.PhotoImage(Image.open("pizza/margherita.png"))
img_mendoan = ImageTk.PhotoImage(Image.open("pizza/mendoan.png"))
img_pepperoni = ImageTk.PhotoImage(Image.open("pizza/pepperoni.png"))

# Image: List
PREVIEWS = [
    img_bbq,
    img_cheese,
    img_hawaiian,
    img_margherita,
    img_mendoan,
    img_pepperoni
]

# Image: Load an empty pic by default
img_preview = Label(image=img_empty)
img_preview.grid(row=1, column=3, padx=7, pady=2, columnspan=3, rowspan=(7 + len(PREVIEWS)))


# Image: Change image on radio-button click
def preview(img_index):
    global img_preview
    img_preview.grid_forget()
    img_preview = Label(image=PREVIEWS[img_index])
    img_preview.grid(row=1, column=3, padx=7, pady=2, columnspan=3, rowspan=(7 + len(PREVIEWS)))


# -- Pizza Flavor selection ---
user_flavor = IntVar(value=-1)

# Flavor: Text instruction
text_select_flavor = Label(root, text="Choose your flavor:")
text_select_flavor.grid(row=6, column=0, columnspan=2)

# Flavor: List
FLAVORS = ("BBQ", "Cheese", "Hawaiian", "Margherita", "Mendoan", "Pepperoni")

# Flavor: Create radio buttons
for i in range(len(FLAVORS)):
    Radiobutton(root, text=FLAVORS[i], variable=user_flavor, value=i,
                command=lambda: preview(user_flavor.get())). \
        grid(row=(7 + i), column=0, padx=10, sticky=W)


# Function: Returns True if user has picked a flavor
def has_picked():
    return user_flavor.get() > -1


# Function: Order the user a pizza
def place_order(user_name, user_street, user_city, user_state, user_phone, user_flavor):
    # Normally I'd put something here, like from a library or from an API to place the order
    # But since this is just a trial/experiment program for me, so I'll just leave it like
    # this unless sometimes in the future I decided to make an actual program out of this
    return


# -- Checkout ---
def checkout():
    # Checkout: If user has picked a pizza flavor
    if has_picked():
        confirm = messagebox.askyesno("Confirmation",
                                      f"Are you sure you want to buy a {FLAVORS[user_flavor.get()]} Pizza?")

        if confirm == 1:
            messagebox.showinfo("Pizza Ordered", "Thank you for your purchase!"
                                                 " Your order is being processed"
                                                 " and will be delivered to you"
                                                 " as soon as possible!")
            place_order(user_name.get(),
                        user_street.get(),
                        user_city.get(),
                        user_state.get(),
                        user_phone.get(),
                        user_flavor.get())

            root.quit()

    # Checkout: If user has NOT picked any flavor but clicked checkout anyway
    else:
        messagebox.showerror("Checkout Error", "You have not picked a pizza flavor."
                                               " Please pick one first before checking out!")


Button(root, text="Checkout >>", padx=5, command=checkout).grid(row=(8 + len(FLAVORS)), column=5, columnspan=2, pady=4)

# -- End: Infinite loop ---
root.mainloop()
