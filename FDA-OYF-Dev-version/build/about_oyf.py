


from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def about_oyf() :
    
    global about_window,image_image_1
    
    file = open(r'ReadMe.txt')
    lines = file.readlines()
    
    if 'about_window' in globals():
        about_window.destroy()
        
    about_window = Toplevel()
    about_window.geometry("1000x600")
    about_window.configure(bg = "#AEAEAE")

    canvas35 = Canvas(
        about_window,
        bg = "#AEAEAE",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas35.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("about_logo.png"))
    image_1 = canvas35.create_image(
        500.0,
        36.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("about_image.png"))
    image_2 = canvas35.create_image(
        500.0,
        324.0,
        image=image_image_2
    )
    
    # Creating a canvas, Scrollbar, Framw to make a scrollable bill 
    
    canvas36 = Canvas(about_window,
                         width = 920,
                         bd = 0,
                         highlightthickness = 0,
                         borderwidth= 0,
                         height = 500,
                         )             
    canvas36.place(x = 40, y = 72)
 
    # Creating Frame
    about_frame = Frame(canvas36,
                         width =920,
                         bg = "#D9D9D9",
                         height = 500)
   
    #Creating scrollbar
    about_scrollbar = Scrollbar(about_window, command=canvas36.yview)
    about_scrollbar.place(x=960, y=85)
    about_scrollbar.place(height=480)

    # Set canvas to scroll
    canvas36.configure(yscrollcommand=about_scrollbar.set)
    canvas36.bind('<Configure>', lambda e: canvas36.configure(scrollregion=canvas36.bbox("all")))

    # window height should be accroding to no of lines in txt file.
    Height = len(lines)*30
    canvas36.create_window((0, 0),   
                     height = Height,
                     width=920,
                     window=about_frame,
                     anchor='nw')    
    ycoor = 10
    for i in lines :
        sentence = i[:-1]
                         
        label = Label(about_frame,text = sentence,font = ('Inika',15),bg = "#D9D9D9")
        label.place(x =0, y = ycoor)
        ycoor+=30
    about_window.resizable(False, False)
    about_window.mainloop()

about_oyf()
