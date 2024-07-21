


from pathlib import Path

from tkinter import Tk, Canvas, Entry, Button, PhotoImage


#Function to place  the application window to the centre of the screen.
def center_screen():
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Jishnu's Food Delivery Application")
window_height = 703
window_width = 499
center_screen()
#window.geometry("499x703")
window.configure(bg = "#836767")

#main canvas
canvas = Canvas(
    window,
    bg = "#836767",
    height = 703,
    width = 499,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    249.0,
    351.0,
    image=image_image_1
)
#bg Image
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    249.0,
    386.0,
    image=image_image_2
)
#login Text
canvas.create_text(
    205.0,
    270.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Arya Regular", 39 * -1)
)
#password Text
canvas.create_text(
    74.0,
    392.0,
    anchor="nw",
    text="Password: ",
    fill="#000000",
    font=("Inter", 14 * -1)
)
#username Text
canvas.create_text(
    71.0,
    328.0,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("Inter", 14 * -1)
)
#signUp Button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
#signup Button Variable is button_1 
button_1 = Button(canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=324.0,
    y=463.0,
    width=103.18163299560547,
    height=19.720571517944336
)
#login Button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
# login button variable is button_2

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=82.0,
    y=466.0,
    width=81.0,
    height=17.0000057220459
)
#username Textbox
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    249.0,
    361.0,
    image=entry_image_1
)
# Username - Vairable is - entry_1
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=62.0,
    y=347.0,
    width=374.0,
    height=26.0
)
#passsword Textbox
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    250.0,
    425.0,
    image=entry_image_2
)
# Password - Variable is - entry_2

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=63.0,
    y=411.0,
    width=374.0,
    height=26.0
)










window.resizable(False, False)
window.mainloop()
