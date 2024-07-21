
import mysql.connector
from tkinter import *
from pathlib import Path
from tkinter.tix import *


OUTPUT_PATH2 = Path(__file__).parent
ASSETS_PATH2 = OUTPUT_PATH2 / Path(r"assets\frame2")


def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)

def clearselectedhotel(): # Clear Hotel Label and Icon
    htl_label.destroy()
    basecanvas1.delete(htl_image)
    if 'htlcancelbutton' in globals():
        htlcancelbutton.destroy()
        confirmhtlbutton.destroy() 

def choose_hotel(hotel_name): # Display hotel name and Icon upon Hotel click event 
    global htl_label
    global htl_image
    
    if 'htl_label' in globals():
        clearselectedhotel()
        
    htl_image = basecanvas1.create_image(
        320,
        290,
        image = Hotel_image_1)
    
    htl_label = Label(basecanvas1,
                  border = 10,
                  highlightthickness= 10,
                  bg = '#E6C197',
                  width = 25,
                  height = 1,
                  text = hotel_name,
                  font = ('Times New Roman',18))
    htl_label.place(x = 165, y = 270) 
    
def confirm_hotel(hotel_id):  # Even -- Button clck - Confirm Hotel
    global Selected_Restaurant
    Selected_Restaurant = hotel_id
    print(Selected_Restaurant)
    clearselectedhotel()  
    basecanvas1.destroy()
    canvas2.destroy()
    scrollbar.destroy()

    
def hotel_selected(hotel_name,hotel_id):  #called Upon Hotel Click Event
    global htlcancelbutton, confirmhtlbutton
    choose_hotel(hotel_name)
    
    htlcancelbutton = Button(basecanvas1,
                
                         width = 10,
                         text = 'Clear',
                         font = ('Times New Roman',18),
                         command = clearselectedhotel )
    htlcancelbutton.place(x = 180, y = 500)
    

    confirmhtlbutton = Button(basecanvas1,
                         width = 10,
                         text = 'Confirm',
                         font = ('Times New Roman',18),
                         command = lambda id = hotel_id: confirm_hotel(id))
    confirmhtlbutton.place(x = 330, y = 500)

# User Options - Previous Orders, Edit Profile, Logout 
def useroptions():
    
    X = 469; Y = 5
    global ButtonImage0,ButtonImage1,ButtonImage2
    tip = Balloon(root)
    for i in tip.subwidgets_all():
        i.configure(bg='white')

    ButtonImage0 = PhotoImage( 
            file=relative_to_assets2("Orders.png"))
    ButtonImage1 = PhotoImage(
            file=relative_to_assets2("Logout.png"))
    ButtonImage2 = PhotoImage(
            file=relative_to_assets2("Profile.png"))

    View_orders = Button(basecanvas1,image =ButtonImage0 ,border=0 ,bg = '#FF9700',activebackground='#FF9700'  )
    tip.bind_widget(View_orders,balloonmsg="Veiw previous orders")
    View_orders.place (x = X, y = Y)

    Profile_btn = Button(basecanvas1,image =ButtonImage2 ,border=0 ,bg = '#FFE89F',activebackground='#FFE89F'  )
    tip.bind_widget(Profile_btn,balloonmsg="View and Edit Profile")
    Profile_btn.place (x = X + 55, y = Y)

    Logout_btn = Button(basecanvas1,image =ButtonImage1 ,border=0 ,bg = '#FF9700',activebackground='#FF9700'  )
    tip.bind_widget(Logout_btn,balloonmsg="Logout")
    Logout_btn.place (x = X+111 , y = Y)
    
def hotelcanvas():
    
    global basecanvas1 ,Hotel_image_1,image_image_1,canvas2,scrollbar
    
    
    cursor.execute("SELECT hotelid, hotel_name FROM Hotel_details") 
    hotels = cursor.fetchall()

    Hotel_image_1 = PhotoImage(
        file=relative_to_assets2("label_bg.png"))

    image_image_1 = PhotoImage(
        file=relative_to_assets2("image_1.png"))

    # Create a canvas
    canvas2 = Canvas(
        root,
        bg = "orange",
        height = 600,
        width = 360,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas2.pack(side=LEFT, fill=BOTH, expand=TRUE)

 

    basecanvas1 = Canvas(
        root,
        bg = "orange",
        height = 600,
        width = 630,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )


    image_1 = basecanvas1.create_image(
        150.0,
        300.0,
        image=image_image_1
    )


    basecanvas1.pack(side = RIGHT)

    useroptions()

    # Create a frame inside the canvas to hold the buttons
    frame1 = Frame(canvas2,width =360,height = 650,bg= "#371F11")

    #Text inside Canvas
    htltext = Label(basecanvas1,text = 'Select your desired Restaurant to proceed !',font = ('Arial',18,'bold'),bg = '#DECBBA')
    htltext.place(x = 80, y = 70)


    # Add a scrollbar
    scrollbar = Scrollbar(root, command=canvas2.yview)
    scrollbar.place(x=355, y=0, height=600)

    # Configure canvas to use scrollbar
    canvas2.configure(yscrollcommand=scrollbar.set)
    canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

    # Create buttons for each hotel
    Y = 30
    for index,hotel in enumerate(hotels):
        hotel_id, hotel_name = hotel
    
        if index == 0 : 
            #creating a Window inside canvas and assigning the window as Frame 
            window_height = 102 * (len(hotels))
            canvas2.create_window((0, 0),
                         height = window_height,
                         width=360,
                         window=frame1,
                         anchor='se')
            
        htl_button = Button(frame1,
                      bg = '#E6C197',
                      font = ('Arial',12),
                      text = hotel_name,           
                      command=lambda htlname=hotel_name,htlid = hotel_id : hotel_selected(htlname,htlid),
                      relief="flat",
                      highlightthickness=5  # Add a border around the button
                      )
    
        htl_button.config(padx=10, pady=10)

        htl_button.place(
            width=338.0,
            height=74.0,
            x = 10,
           y = Y)
        Y+= 100
    
       



##################################################################################################################################
    

# Start Tkinter event loop
    
root = Tk()
root.config(background='#E6C197')
root.title("Hotel Selection")
root.geometry("1000x600")
root.configure(bg = "#FFFFFF")
root.resizable(False,False)

Selected_Restaurant = ''


# Connect to 
# MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlrootpwd",
    database="food_delivery_application"
)
cursor = db.cursor()



# Fetch hotel details from MySQL

hotelcanvas()
    

root.mainloop()

# Close database connection
db.close()
