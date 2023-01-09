# LIBRARIES

import tkinter as tk
import customtkinter as ctk
import requests
from PIL import Image

from FormatFuncs import push


class APIExplore(ctk.CTk):  # inheritence
    def __init__(self, *args, **kwargs):
        super().__init__()  # access to other class init

        # API ROOT
        self.API_ROOT = "https://www.tateapi.com/api/quote"

        # Aesthetics
        
        ctk.set_appearance_mode("Dark")
        
        self.QUOTE_FONT = ("nirmala ui semilight", 20, "normal")
        self.BUTTON_COLOR = "#CC334F"


        # Initialize title
        self.title("Andrew Tate Quotes")

        # Initialize frame and icon
        self.iconbitmap("images/chess.ico")
        self.geometry("512x640")
        self.maxsize(width=512, height=640)
        self.minsize(width=512, height=640)
        
        self.string = ctk.StringVar(name='')
        self.string.set('')


        print(self.string.get()) # debug

        # Initialize Background Image
        self.APP_BACKGROUND_IMAGE = ctk.CTkImage(dark_image=Image.open("images/andrew_chess.jpg"), light_image=Image.open("images/andrew_chess.jpg"), size=(512, 640))
        self.APP_BACKGROUND = ctk.CTkLabel(image=self.APP_BACKGROUND_IMAGE, master=self, text=self.string.get(), font=self.QUOTE_FONT)
        self.APP_BACKGROUND.place(relx=0, rely=0)  # w.r.t frame



        # Initialize button
        self.quote_button = ctk.CTkButton(
                master=self,
                fg_color=self.BUTTON_COLOR,
                text="Tate Speaks",
                hover_color="#A8263E",
                width=120,
                height=30,
                hover=True,
                corner_radius=0,
                command= self.new_quote
                )
        self.quote_button.place(relx=.5, rely=.9, anchor=tk.CENTER)   # w.r.t frame, centered so its 50% of x and 90% of y (from 0 to 1)

    def new_quote(self):
        # I have to ping the site every time for a new quote 
        get_raw_quote = requests.get(self.API_ROOT).json()["quote"]
        self.clean_quote = push(get_raw_quote, length=30, force_space=True)
        self.string.set(self.clean_quote)
        self.APP_BACKGROUND.configure(text=self.string.get())  # had to use stack overflow and read the actual code in ctk_label.py to figure this out




        







