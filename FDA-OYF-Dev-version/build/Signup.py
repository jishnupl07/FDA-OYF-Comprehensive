

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH1 = Path(__file__).parent
ASSETS_PATH1 = OUTPUT_PATH1 / Path(r"assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)


window = Tk()

window.geometry("996x596")
window.configure(bg = "#FFFDFD")

def signupcanvas():
    global image_image_3,button_image_3,button_image_4,button_3,button_4,entry_image_3

    canvas1 = Canvas(
        window,
        bg = "#FFFDFD",
        height = 596,
        width = 996,
        bd = 0,
        highlightthickness = 0,
        relief = "flat"
    )

    canvas1.place(x = 0, y = 0)

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas1.create_image(
        498.0,
        298.0,
        image=image_image_3
    )
    #Submit Button

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=579.0,
        y=519.0,
        width=176.0,
        height=35.98222351074219
    )
    #Cancel Button

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=767.0,
        y=519.0,
        width=175.0,
        height=36.0
    )

    #Text of all the required fields for Personal Information

    canvas1.create_text(
        558.0,
        436.0,
        anchor="nw",
        text="State :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        558.0,
        345.0,
        anchor="nw",
        text="City :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        558.0,
        266.0,
        anchor="nw",
        text="Confirm Password :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        558.0,
        180.0,
        anchor="nw",
        text="Password :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        558.0,
        92.0,
        anchor="nw",
        text="Username:",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        44.0,
        436.0,
        anchor="nw",
        text="Address Line 2 :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        44.0,
        349.0,
        anchor="nw",
        text="Address Line 1 :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        44.0,
        266.0,
        anchor="nw",
        text="Email Address : ",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        44.0,
        180.0,
        anchor="nw",
        text="Phone No :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas1.create_text(
        44.0,
        92.0,
        anchor="nw",
        text="Name :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    #All the TextBoxes are of same size and therfore, I'm using the Same variable for all of it
    #There are 10 Such TextBoxes in the current canvas. 

    #  entry_image_3 can be considered as the entry image for all the other TextBoxes too .

    ##

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_1.png"))

    ##

    #Name Entry 
    entry_bg_3 = canvas1.create_image(
        245.5,
        135.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=53.0,
        y=116.0,
        width=390.0,
        height=36.0
    )

    #phone Number 

    entry_bg_4 = canvas1.create_image(
        245.5,
        223.0,
        image=entry_image_3
    )
    entry_4= Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=55.0,
        y=204.0,
        width=390.0,
        height=36.0
    )



    #email Address

    entry_bg_5 = canvas1.create_image(

        247.5,
        311.0,
        image=entry_image_3
    )
    entry_5 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=55.0,
        y=291.0,
        width=394.0,
        height=38.0
    )




    #Address Line 1

    entry_bg_6 = canvas1.create_image(
        247.5,
        396.0,
        image=entry_image_3
    )
    entry_6 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=55.0,
        y=376.0,
        width=392.0,
        height=38.0
    )

    #Address Line 2

    entry_bg_7 = canvas1.create_image(
        247.5,
        483.0,
        image=entry_image_3
    )
    entry_7 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=55.0,
        y=463.0,
        width=392.0,
        height=38.0
    )

    #username 
    entry_bg_8 = canvas1.create_image(
        759.5,
        135.0,
        image=entry_image_3
    )
    entry_8 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=567.0,
        y=120.0,
        width=387.0,
        height=30.0
    )


    #Password
    entry_bg_9 = canvas1.create_image(
        759.5,
        223.0,
        image=entry_image_3
    )
    entry_9 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=570.0,
        y=204.0,
        width=390.0,
        height=36.0
    )



    #confirm Password 
    entry_bg_10 = canvas1.create_image(
        761.5,
        311.0,
        image=entry_image_3
    )
    entry_10 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=567.0,
        y=291.0,
        width=392.0,
        height=38.0
    )


    #City Entry

    entry_bg_11 = canvas1.create_image(
        757.5,
        396.0,
        image=entry_image_3
    )
    entry_11 = Entry(
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_11.place(
        x=565.0,
        y=376.0,
        width=392.0,
        height=38.0
    )

    #State Entry

    entry_bg_12 = canvas1.create_image(
        757.5,
        483.0,
        image=entry_image_3
    )
    entry_12 = Entry(
        font=("Times New Roman", 16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_12.place(
        x=565.0,
        y=463.0,
        width=392.0,
        height=38.0
    )



    # Line 
    canvas1.create_rectangle(
        44.0,#distance from left 
        63.0, #distance from top (of 1 of the parallel sides)
        340.0,#length
        70.0,#distance from top (of the other parallel side)
        fill="#50261F",
        outline="")


    canvas1.create_text(
        45.0,
        27.0,
        anchor="nw",
        text="Enter your Personal Details ",
        fill="#50261F",
        font=("Times New Roman",25 * -1,'bold')
    )

signupcanvas()
window.resizable(False, False)
window.mainloop()
