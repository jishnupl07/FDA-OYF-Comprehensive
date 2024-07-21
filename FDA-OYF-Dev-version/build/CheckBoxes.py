from tkinter import * 
from pathlib import Path

OUTPUT_PATH8 = Path(__file__).parent
ASSETS_PATH8 = OUTPUT_PATH8 / Path(r"assets\frame8")

def relative_to_assets8(path: str) -> Path:
    return ASSETS_PATH8 / Path(path)


def savebtn():
    isbreakfast = breakfast_var.get()
    islunch = lunch_var.get()
    isdinner  = dinner_var.get()
    s = ''
    if isbreakfast == 1 :
        s+= 'Breakfast '
    if islunch == 1 :
        s+= 'Lunch '
    if isdinner == 1 :
        s+= 'Dinner '
     
    if s == '':    
        print('select one or many that applicable')
    else :
        print(s)
    
window = Tk()

breakfast_var = IntVar(window)
lunch_var = IntVar(window)
dinner_var = IntVar(window)


breakfast_checkbox = Checkbutton(window,font = ('Inika',20),text = 'Breakfast',variable= breakfast_var,highlightbackground = "red", highlightcolor= "red",highlightthickness= 10)
breakfast_checkbox.pack()
lunch_checkbox = Checkbutton(window,font = ('Inika',20),text = 'Lunch',variable= lunch_var)
lunch_checkbox.pack()
dinner_checkbox = Checkbutton(window,font = ('Inika',20),text = 'Dinner',variable= dinner_var)
dinner_checkbox.pack()

save_btn = Button(window, text = 'Save',command = savebtn)
save_btn.pack()

window.geometry("300x300")
window.mainloop()