import tkinter, customtkinter, requests
from PIL import Image, ImageTk, ImageOps
import re

# API 
API = "https://www.tateapi.com/api/quote"

# CHECKLIST 
# TODO Place code in Classes 🟩
# TODO Get icon 🟩
# TODO add formatting


# FUNCTIONS 

# tk Functions
def new_quote():
    # API 
    get_raw_quote = requests.get(API)
    raw_quote = get_raw_quote.json()["quote"]
    sub_question = re.sub(r"\? ", "?\n", raw_quote)  # break on ?
    sub_period = re.sub(r"\. ", ".\n", sub_question)  # break on .
    print(sub_period)
    print(len(sub_period))

    # if len > 
    # check for commas
    # if not check for space
    # repeat

    find_first_break = sub_period.find("\n")
    half_of_len = len(sub_period[find_first_break]) // 2

    split_sentance = sub_period.splitlines(True)
    print(sub_period)
    print(split_sentance)


    def len_check(input):
        compiled = ''
        for sentance in input:
            if len(sentance) > 50:
                half_of_sentance = len(sentance) // 2
                while sentance[half_of_sentance] != " ":
                    half_of_sentance -= 1
                sentance = sentance[:half_of_sentance + 1] + "\n" + sentance[half_of_sentance + 1:]
            compiled += sentance + "\n"
        return compiled

    compiled = len_check(split_sentance)
    tate_img_canvas.itemconfigure(canvas_text, text=compiled) # 👀 dynamically configure 
    print(compiled)

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
tate_img_canvas.create_image(512/2, 640/2, image=tate_chess_tk)
canvas_text = tate_img_canvas.create_text(512/2, 640/2, text='', font=QUOTE_FONT, fill="white")

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
