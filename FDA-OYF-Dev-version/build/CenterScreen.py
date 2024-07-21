import tkinter as tk

def center_screen():
    global window
    global screen_height, screen_width, x_cordinate, y_cordinate
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    #print("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


print('Enter window geometry below :')
#get input or assign
window_width = int(input('Enter Width :'))
window_height= int(input('Enter Height :'))
window = tk.Tk()
#call the funtion
center_screen()
window.mainloop()
