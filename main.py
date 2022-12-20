import tkinter, customtkinter, requests
from PIL import Image, ImageTk, ImageOps
import re
from wills_filter_funcs import len_clean, add_linebreaks_even
import time
# API 
API = "https://www.tateapi.com/api/quote"

# CHECKLIST 
# TODO Place code in Classes 🟩
# TODO Get icon 🟩
# TODO add formatting 
    # version 1.0 ✅
    # add 'copywrite' style space function - check
    # add a function to roughly divide strings in two with optional recursive functionality - check
    # version 1.1
    # add "averages" filter func 🟩
    # add only doubles for sentances longer than a given value 🟩


# FUNCTIONS 

# tk Functions
def new_quote():
    rec = time.time()
    # string format functions 

    # GET API 
    get_raw_quote = requests.get(API)
    raw_quote = get_raw_quote.json()["quote"]
    print(raw_quote, get_raw_quote.json())
    sub_period = len_clean(raw_quote, doubles=True)
    print(sub_period)
   
    print(len(sub_period))
    compiled = add_linebreaks_even(sub_period, recursive=True, length=40)


        
    tate_img_canvas.itemconfigure(canvas_text, text=compiled.strip()) # 👀 dynamically configure 
    print(compiled)
    print(f"speed: {time.time() - rec}")

# APPEARANCE

QUOTE_FONT = ("nirmala ui semilight", 20, "normal")

# Appearance Mode
customtkinter.set_appearance_mode("Dark")

# Button Color(s)
BUTTON_COLOR = "#992D48"

# MAIN WINDOW
root = customtkinter.CTk()
root.geometry("512x640")
root.maxsize(width=512, height=640)
root.minsize(width=512, height=640)

root.title("Andrew Tate Quotes")


# IMAGE 
tate_chess = customtkinter.CTkImage(dark_image=Image.open("images/andrew_chess.jpg"), size=(512, 640))  # 1024, 1280  # w, l
tate_chess_pil = Image.open("images/andrew_chess.jpg")
tate_chess_pil = ImageOps.scale(tate_chess_pil, factor=0.5)
tate_chess_tk = ImageTk.PhotoImage(tate_chess_pil)


# CANVAS
tate_img_canvas = tkinter.Canvas(root, width=512, height=640, highlightthickness=0)
tate_img_canvas.grid(column=0, row=0, rowspan=8, columnspan=8)
tate_img_canvas.create_image(256, 320, image=tate_chess_tk)
canvas_text = tate_img_canvas.create_text(256, 450, text='', font=QUOTE_FONT, fill="white", anchor="s", justify="center")

#background = customtkinter.CTkLabel(image=tate_chess, master=root, text='')
#background.grid(column=0, row=0, rowspan=8, columnspan=8)

#background.configure(text='', font=("nirmala ui semilight", 20, "normal"))  # hardcode

# BUTTON 
quote_button = customtkinter.CTkButton(
        master=root,
        fg_color=BUTTON_COLOR,
        text="Tate Speech",
        hover_color="#A64F59",
        width=120,
        height=30,
        command=new_quote
        )
quote_button.grid(column=4, row=7)


root.mainloop()
