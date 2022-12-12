import tkinter, customtkinter, requests
from PIL import Image
from os import getcwd, path

# CHECKLIST 
# TODO Place code in Classes 🟩


# FUNCTIONS
def new_quote():
    pass


# APPEARANCE
customtkinter.set_appearance_mode("Dark")

# MAIN WINDOW
root = customtkinter.CTk()
root.geometry(f"{600}x{600}")
root.title("Andrew Tate Quotes")

pwd = getcwd()
print(pwd)
# IMAGE 


tate_chess = customtkinter.CTkImage(dark_image=Image.open("images/andrew_chess.jpg"), size=(100, 100))
background = customtkinter.CTkLabel(image=tate_chess)
background.grid(column=1, row=0, rowspan=2)

# BUTTON 
quote_button = customtkinter.CTkButton(
        master=root,
        width=120,
        height=30,
        )
quote_button.grid(column=1, row=3)


root.mainloop()
