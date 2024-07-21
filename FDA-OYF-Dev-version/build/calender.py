from tkcalendar import Calendar
from datetime import datetime
from tkinter import *
from tkinter import messagebox

def on_date_change(event):
    selected_date = cal.selection_get()
    if selected_date > today:
        messagebox.showerror("Invalid Date", "You can't select a date later than today's date.")
        # Reset to today's date
        create_calender()
    else :
        print(selected_date)
def create_calender():
    global cal,today

    if "cal" in globals():
        cal.destroy()
    # Get today's date
    today = datetime.today().date()
    print(today)
    cal = Calendar(window, selectmode='day', year=today.year, month=today.month, day=today.day)
    cal.pack()

    # Bind the date change event
    cal.bind("<<CalendarSelected>>", on_date_change)


window = Tk()
create_calender()
window.mainloop()
