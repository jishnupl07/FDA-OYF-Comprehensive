from math import ceil
from pathlib import Path
from tkinter import CENTER, Button, Tk, Canvas,Label, PhotoImage, Frame, Scrollbar,Toplevel
import mysql.connector as sql
# Requirements = Username , Datetime 
con = sql.connect(host='localhost',user = 'root',password = 'mysqlrootpwd',database='food_delivery_application')
cur = con.cursor()


# Exisiting functions
# Return Itemname from itemid 
def return_itemname(itemid):
   cur.execute('select Item_Name from items where ItemId = %s ',(itemid,))
   (itemname,) = cur.fetchone()
   return itemname 



# newfunctions

OUTPUT_PATH6 = Path(__file__).parent
ASSETS_PATH6 = OUTPUT_PATH6 / Path(r"assets\frame6")

def relative_to_assets6(path: str) -> Path:
    return ASSETS_PATH6 / Path(path)

def returnbaseprice(itemid):
    
    cur.execute('select BasePrice from items where ItemId = %s',(itemid,))
    (baseprice,)= cur.fetchone()
   
    return baseprice

def bill(order_id):
    
    global Bill_window,canvas9,billbg,oyfoodimg
    
    if 'Bill_window' in globals():
        Bill_window.destroy()

    Bill_window = Tk()
    Bill_window.title("Jishnu's Food Delivery Application - oyFood - Bill")
    Bill_window.geometry("450x700")
    Bill_window.configure(bg = "#FFFFFF")
    Bill_window.resizable(False, False)
    
    Total = 0 
    GST = 0 
    Grand_Total = 0 
    Platform_Fee = 0 
    #Get Order Id and HotelId from orders , using userid and datetime
    cur.execute('select custid,OrderDatetime,HotelId from orders where OrderId = %s',(order_id,))
    (custid,Date,HotelId)  = cur.fetchone()
    
    #Get the username of the account 
    cur.execute('select username from login_credentials where custid = %s',(custid,))
    (username,) = cur.fetchone()
    
    # Get Hotel Details 
    cur.execute('select Hotel_Name,Address,City,state,pricepercent,taxpercent from hotel_details where HotelId = %s',(HotelId,))
    htl_details = cur.fetchone()
    
    # Get Itemid and Quantity Ordered
    cur.execute('select ItemId,Quantity from order_details where OrderId = %s',(order_id,))
    
    Items = cur.fetchall()
    
    canvas9 = Canvas(
        Bill_window,
        bg = "#FFFFFF",
        height = 700,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas9.place(x = 0, y = 0)
    
    billbg = PhotoImage(
        file= relative_to_assets6('image_1.png'))
    
    image_1 = canvas9.create_image(
        225.0,
        350.0,
        image=billbg
    )   
    
    # Creating a canvas, Scrollbar, Framw to make a scrollable bill 
    
    canvas10 = Canvas(Bill_window,
                 width = 338,         
                 height = 575,
                 )             
    canvas10.place(x = 51, y = 60)
 
    # Creating Framw
    frame5 = Frame(canvas10,width =338,height = 575)
   
    #Creating scrollbar
    scrollbar3 = Scrollbar(Bill_window, command=canvas10.yview)
    scrollbar3.place(x=375, y=60)
    scrollbar3.place(height=580)

    # Set canvas to scroll
    canvas10.configure(yscrollcommand=scrollbar3.set)
    canvas10.bind('<Configure>', lambda e: canvas10.configure(scrollregion=canvas10.bbox("all")))
    
    # default Bill_window height to incorporate htlname, address, Oyfood logo is 180 

    Bill_window_height = 500 + 30*len(Items) 
    canvas10.create_window((0, 0),   
                     height = Bill_window_height,
                     width=338,
                     window=frame5,
                     anchor='nw')
    
    # OYfood logo
    
    oyfoodimg = PhotoImage(
    file=relative_to_assets6("image_2.png"))
     
    oyfoodimgLabel = Label(frame5 , 
                           image = oyfoodimg)
    
    oyfoodimgLabel.pack()
    
    HotelName = Label(frame5,       
        text=htl_details[0],
        font=("GlassAntiqua Regular", 24 * -1))
    HotelName.place( x = 169 ,y = 70,anchor = CENTER)
    
    hoteladdress = Label(frame5,
                         text = htl_details[1]+'\n'+htl_details[2]+','+htl_details[3]+',\n'+str(Date)+'.'+'\n'+username,
                         font=("GlassAntiqua Regular", 15 * -1))
    hoteladdress.place(x = 169, y = 120, anchor = CENTER)                     

    Line = Label(frame5,
        text=".....................................",
        font=("Inter", 29 * -1)
        )
    Line.place(x = 170, y = 180, anchor = CENTER)
    
    Ycoor = 210
    
    #Labels for Items, Quantity , and Amount
    for itemid, quantity in Items:
        
        amount = int(returnbaseprice(itemid)*((100+htl_details[4])/100)*quantity)
        Total += amount
        
        itm_name =  return_itemname(itemid)
        
        if len(itm_name) > 13 :
            itm_name = itm_name[:11]+'...'
            
        itemname = Label(frame5,
                         text =itm_name,
                         font=("GlassAntiqua Regular", 18 * -1)
                         )
        
        Quantity_label = Label(frame5,
                               text = str(quantity),
                               font=("GlassAntiqua Regular", 18 * -1)
                               )
        Amount_label = Label(frame5,
                             text = 'Rs '+str(amount)+'.00',
                             font=("GlassAntiqua Regular", 18 * -1)
                             )
        
        itemname.place(x = 20,y = Ycoor,anchor = 'w')
        Quantity_label.place(x = 140, y = Ycoor,anchor = 'w')
        Amount_label.place(x = 320, y = Ycoor, anchor = 'e')

        Ycoor += 30
        
    Ycoor+30
    
    Line = Label(frame5,
        text=".....................................",
        font=("Inter", 29 * -1)
        )
    Line .place(x = 169, y = Ycoor , anchor = CENTER)
    
    Ycoor += 33
    
    # Labels for Total
    
    total = Label(frame5,
                       text = 'Total',
                       font=("GlassAntiqua Regular", 18 * -1)
                        )

    Item_Total = Label(frame5,
                       text = 'Rs '+str(Total)+'.00',
                       font=("GlassAntiqua Regular", 18 * -1)
                       )
    total.place(x = 20, y = Ycoor, anchor = 'w')
    Item_Total.place(x = 320, y = Ycoor, anchor = 'e')
    
    Ycoor +=30
    
    # Labels for GST 
    
    GST = ((htl_details[5]/100)*Total)
    tempValue = ceil(GST*100)/100
    GST = tempValue
    
    gst_Label = Label(frame5,
                       text = 'Sales Tax'+' ('+str(htl_details[5])+'%)',
                       font=("GlassAntiqua Regular", 18 * -1)
                        )
    gstamt_label = Label(frame5,
                       text = 'Rs '+str(GST),
                       font=("GlassAntiqua Regular", 18 * -1)
                       )
    gst_Label.place(x = 20, y = Ycoor, anchor = 'w')
    gstamt_label.place(x = 320, y = Ycoor, anchor = 'e')   
    
    Ycoor += 30
    
    # Labels for Platform Fee
    
    Platform_Fee = 0.05*Total
    tempValue = (ceil(Platform_Fee*100)/100)
    Platform_Fee = tempValue

    pltform_fee_label = Label(frame5,
                       text = 'Platform Fee (5%)',
                       font=("GlassAntiqua Regular", 18 * -1)
                        )
    pltfee_amt_label = Label(frame5,
                       text = 'Rs '+str(Platform_Fee),
                       font=("GlassAntiqua Regular", 18 * -1)
                       )
    pltform_fee_label.place(x = 20, y = Ycoor, anchor = 'w')
    pltfee_amt_label.place(x = 320, y = Ycoor, anchor = 'e')   

    # Label for Grand Total 
    
    Grand_Total = GST + Total + Platform_Fee
    tempValue = ceil(Grand_Total*100)/100
    Grand_Total = tempValue

    Ycoor += 30 
    
    grandtotal_label = Label(frame5,
                       text = 'Grand Total',
                       font=("GlassAntiqua Regular", 22 * -1,'bold')
                        )
    grandtotal_amt_label = Label(frame5,
                       text = 'Rs '+str(Grand_Total),
                       font=("GlassAntiqua Regular", 22 * -1,'bold')
                       )
    grandtotal_label.place(x = 20, y = Ycoor, anchor = 'w')
    grandtotal_amt_label.place(x = 320, y = Ycoor, anchor = 'e')   
    
    Ycoor += 28
    
    # Line
    
    Line = Label(frame5,
        text=".....................................",
        font=("Inter", 29 * -1)
        )
    Line .place(x = 169, y = Ycoor , anchor = CENTER)
    
    Ycoor += 60
    
    # Label for Thank You

    ty = Label(frame5,
                       text = 'Thank you for using\n oyFood \n..........',
                       font=("GlassAntiqua Regular", 20* -1)
                       )
    ty.place(x = 169, y = Ycoor, anchor = CENTER)   
       
    Bill_window.mainloop()





bill(57)

