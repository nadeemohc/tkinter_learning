from tkinter import *

import customtkinter

# Set color and theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def button_callback():
    print("Button Pressed ")


app = customtkinter.CTk()
# app.iconbitmap("/home/kenpachi/Nadeem/tkinter_tutorial/images/music.ico")
app.title("First App")
app.geometry("600x350")

button = customtkinter.CTkButton(app, text="My button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()
