
from tkinter import messagebox
import mysql.connector
from tkinter import *
from pathlib import Path



OUTPUT_PATH3 = Path(__file__).parent
ASSETS_PATH3 = OUTPUT_PATH3 / Path(r"assets\frame3")


def relative_to_assets3(path: str) -> Path:
    return ASSETS_PATH3 / Path(path)

#Clear Labels and Spinboxes in canvas4 (frame3) 
def clear_itemlabels():
    global label_list,label2,spinbox_list
    
    for k in label_list.copy():
        label_list.remove(k)
        k.destroy()
        
    for m in spinbox_list:
        m.destroy()
           
# Return Itemname from itemid 
def return_itemname(itemid):
   cur.execute('select ItemId,Item_Name from items  ')
   itemid_and_name = cur.fetchall()
   for i in itemid_and_name :
       item_id , item_name = i
       if item_id == itemid :
           return item_name 
           break
  
# Return Item Price by computing base price and price %
def return_itemprice(itemid):
    cur.execute('select HotelId,pricepercent from hotel_details')
    htlid_and_pricepercent = cur.fetchall()
    Price_Percent = 0 ; Base_Price = 0
    
    for i in htlid_and_pricepercent :
        hotelid,pricepercent = i
        if hotelid == Selected_Restaurant:
            Price_Percent = pricepercent
            break
    cur.execute('select ItemId,BasePrice from items ')
    itemid_and_baseprice =  cur.fetchall()
    for j in itemid_and_baseprice :
        itemId , baseprice = j 
        if itemId == itemid :
            Base_Price = baseprice
    Price_of_item = Base_Price * ((100 + Price_Percent)/100)
    
    return str(int(Price_of_item))

# Return ItemId from Itemname
def return_itemid(itemaname):
    cur.execute('Select ItemId,Item_Name from items')
    itemid_and_itemname = cur.fetchall()
    for i in itemid_and_itemname :
        ItemId, ItemName = i
        if ItemName == itemaname :
            return ItemId
            break

#Event - Place Order Button Click event
def placeorder():
    global dict_items
    
    nil_values = 0    
    for i in range(len(spinbox_list)) :
        
        value = spinbox_list[i].get()
        Itemname =  (label_list[i]['text']).split('(')[0]
        Itemname = Itemname.strip()
        
        dict_items[return_itemid(Itemname)] = value
        
        if value == '0' :
            nil_values += 1
     
        #print(key,value)
        
       
    if nil_values > 0 :
        response = messagebox.askquestion('Empty Values','There are some items with 0 quantity. Do you want to remove them?')
        
        for i in range(len(spinbox_list)) :
            value = spinbox_list[i].get()
            Itemname =  (label_list[i]['text']).split('(')[0]
            Itemname = Itemname.strip()
        
            if value == '0' :
                if response == 'yes':
                    del dict_items[return_itemid(Itemname)]
                    print('Item removed - ',Itemname)
                    print(dict_items)
        createlabelsandspinbox()
        
        if response == 'yes':
            messagebox.showinfo('Order Modified','Your items have been modified based on your selection. verify them and place order !')   
    
    elif len(dict_items) == 0 :
        messagebox.showwarning('Order Error',"Order can't be placed with no items")
    
    else :
        messagebox.showinfo('Success','Move to billing')
        
        frame3.destroy()
        scrollbar1.destroy()
        scrollbar2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        basecanvas2.destroy()
        
#Event - SpinBox value change Event           
def quantity_changed(I,J):  # I is itemId , J is Spinbox index in spinbox_list 
    global dict_items
    value = spinbox_list[J].get()#obtain values from SpinBox
    print('ItemId :',I,'Index:',J,'Quantity:',value)
    dict_items[I] = value #Update Dictionary Values 

    if value == '0':
        clear_itemlabels()
        del dict_items[I]
        createlabelsandspinbox()
       
    else:        
        dict_items[I] = value #Update Dictionary Values   
    
# Clears all the orders in Dictionary        
def clear_orders():
    global dict_items
    
    dict_items.clear()
    createlabelsandspinbox()

# Event - Item Clicked - in canvas3 (frame2).
def item_selected(item_id):  #called Upon Button Click Event
    global dict_items 
    print("Item ID selected:", item_id) 
    if item_id not in list(dict_items.keys()):  # Checking if the itemid/hotelid is already there in listsof_fields
        dict_items[item_id] = 1 #setting default value to 1 
    
    createlabelsandspinbox()

#Create Labels, Spinboxes inside canvas 4 (frame 3) and buttons inside basecanvas2
def createlabelsandspinbox(): 
    
    global label2,label_list,spinbox_list, canvas4 ,scrollbar2,frame3
    
    if 'canvas4' in globals():
        scrollbar2.destroy()
        frame3.destroy()
        canvas4.destroy()

    canvas4 = Canvas(window,
                 bg = '#371F11',
                 width = 450,         
                 height = 400,
                 )             
    canvas4.place(x = 450, y = 100)

    frame3 = Frame(canvas4,width =450,height = 400,bg= "#371F11")
   
    #Creating another scrollbar
    scrollbar2 = Scrollbar(window, command=canvas4.yview)
    scrollbar2.place(x=910, y=100)
    scrollbar2.place(height=400)

    canvas4.configure(yscrollcommand=scrollbar2.set)
    canvas4.bind('<Configure>', lambda e: canvas4.configure(scrollregion=canvas4.bbox("all")))
    #canvas4.pack(side=RIGHT, fill=BOTH, expand=TRUE)
    window2_height = 55 * len(dict_items)
    
    canvas4.create_window((0, 0),   
                     height = window2_height,
                     width=450,
                     window=frame3,
                     anchor='nw')


    if len(dict_items) > 0 :
        clear_itemlabels()
        
    # Creating Labels and SpinBox
    Ycoor = 15   
    spinbox_count = 0
    spinbox_list = list(dict_items.keys())


    for i in dict_items: 
        
        Item_Name = return_itemname(i)
        Item_Price = return_itemprice(i)
        #print(Item_Name,Item_Price)
        
        text_inside_label = Item_Name + ' ( ' + Item_Price+ ' Rs)'
        label2 = Label(frame3,text = text_inside_label , width = 30,height = 2, font = ('Arial', 12)) #Creating Labels List[i] will return the respective string (hotelid/itemid)
        label2.place(x=10,y = Ycoor)
        
        label_list.append(label2) 
        
        var = StringVar(window) #Setting a Stringvar - special variable to hold textvariable - Default value of a widget
        var.set(dict_items[i]) #setting to hold the previous value of SpinBox
        
        
        spinbox_list[spinbox_count]  = Spinbox(frame3, from_=0, to=100,textvariable=var,font = ('Arial',10), command = lambda I = i, J= spinbox_count :quantity_changed(I,J))
        spinbox_list[spinbox_count].place(x = 290, y = Ycoor+10)

        spinbox_count += 1 #Incrementing SpinBox Count 
        Ycoor += 50 # Incrementing Y coordinates
        
        #print(dict_items)
     
    #Place Order Button
    place_order = Button(basecanvas2,
                           width= 10,
                           text = 'Place Order',
                           font = ('Times New Roman',15),
                           command = placeorder
                           )
    place_order.place(x = 420, y = 525)
    
    #Clear Orders Button
    clear_order_button = Button(basecanvas2,
                         width= 10,
                         text = 'Clear',
                         font = ('Times New Roman',15),
                         command = clear_orders
                         )
    clear_order_button.place(x = 85, y = 525)

# Choose - Items Canvas
def itemscanvas():
    global canvas3,basecanvas2, scrollbar1 ,image_image_4
 
    cur.execute("SELECT ItemId, Item_Name FROM items")
    items = cur.fetchall()

    # canvas to hold all the items

    canvas3 = Canvas(
        window,
        bg = "#371F11",
        height = 600,
        width = 360,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas3.pack(side=LEFT, fill=BOTH, expand=TRUE)

    # Canvas to have bg image and other labels
    basecanvas2 = Canvas(
        window,
        bg = "orange",
        height = 600,
        width = 630,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets3("food_bg.png"))

    image_5 = basecanvas2.create_image(
        500.0,
        300.0,
        image=image_image_4
    )
    basecanvas2.pack(side = RIGHT)
    #Back to Hotels Button
    backto_hotels_button = Button(basecanvas2,
                         text = 'Back To Hotels',
                         width= 16,
                         font = ('Times New Roman',15),
                         command = lambda: print('Back to Hotels')
                         )
    backto_hotels_button.place(x = 220, y = 525)


    # Create a frame inside the canvas to hold the buttons
    frame2 = Frame(canvas3,width =360,bg= "#371F11")

    #Text inside Canvas
    items_text = Label(basecanvas2,text = 'What do you want to Eat today ? ',font = ('Arial',18,'bold'),bg = '#E6C197',width = 30)
    items_text.place(x = 100, y = 50)

    # Add a scrollbar
    scrollbar1 = Scrollbar(window, command=canvas3.yview)
    scrollbar1.place(x=355, y=0)
    scrollbar1.place(height=600)

    # Configure canvas to use scrollbar
    canvas3.configure(yscrollcommand=scrollbar1.set)
    canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))

    # Create buttons for each hotel
    Y = 30
    for index, hotel in enumerate(items): #enumerate includes numbers (0,1,2) and the erquired field (hotel)
        item_id, item_name = hotel  
        if index == 0 :
            #creating a Window inside canvas and assigning the window as Frame 
            window_height = 101 * (len(items))
            canvas3.create_window((0, 0),
                         height = window_height,
                         width=360,
                         window=frame2,
                         anchor='se')

        item_button = Button(frame2,
                      bg = '#E6C197',
                      font = ('Arial',12),
                      text = item_name,           
                      command=lambda htlid=item_id: item_selected(htlid),
                      relief="flat",
                      highlightthickness=1  # Add a border around the button
                      )
        item_button.config(padx=10, pady=10)

        item_button.place(
        width=338.0,
        height=74.0,
        x = 10, y = Y)
        Y+= 100

        



##################################################################################################################################
    

# Start Tkinter event loop
    
window = Tk()
window.title("Hotel Selection")
window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
window.resizable(False,False)

# Connect to 
# MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlrootpwd",
    database="food_delivery_application"
)

cur = db.cursor()



Selected_Restaurant = 'htl-ganga'

dict_items = {}    
label_list = []
spinbox_list = []



# Fetch hotel details from MySQL


itemscanvas()
window.mainloop()


# Close database connection
db.close()
