
from dataclasses import dataclass
import datetime
import mysql.connector as sql           # MySql Connector
from pathlib import Path
from tkinter import Tk, Canvas, Label, Button, PhotoImage,Frame,Scrollbar,CENTER,Toplevel
from math import ceil                   # Math - Ceil 

OUTPUT_PATH6 = Path(__file__).parent
ASSETS_PATH6 = OUTPUT_PATH6 / Path(r"assets\frame6")

OUTPUT_PATH7 = Path(__file__).parent
ASSETS_PATH7 = OUTPUT_PATH7 / Path(r"assets\frame7")
#existing functions :
def relative_to_assets6(path: str) -> Path:
    return ASSETS_PATH6 / Path(path)

# To return baseprice of an Item
def returnbaseprice(itemid):
    
    cur.execute('select BasePrice from items where ItemId = %s',(itemid,))
    (baseprice,)= cur.fetchone()
   
    return baseprice

def bill(order_id):
    
    global Bill_window,canvas9,billbg,oyfoodimg
    
    if 'Bill_window' in globals():
        Bill_window.destroy()

    Bill_window = Toplevel()
    Bill_window.title("Jishnu's Food Delivery Application - oyFood - Bill")
    Bill_window.geometry("450x700")
    Bill_window.configure(bg = "#FFFFFF")
    Bill_window.resizable(False, False)
    
    Total = 0 
    GST = 0 
    Grand_Total = 0 
    Platform_Fee = 0 
    #Get Order Id and HotelId from orders , using userid and datetime
    cur.execute('select HotelId from orders where OrderId = %s',(order_id,))
    (HotelId,)  = cur.fetchone()
    
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

    Bill_window_height = 490 + 30*len(Items) 
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
                         text = htl_details[1]+'\n'+htl_details[2]+','+htl_details[3],
                         font=("GlassAntiqua Regular", 15 * -1))
    hoteladdress.place(x = 169, y = 110, anchor = CENTER)                     

    Line = Label(frame5,
        text=".....................................",
        font=("Inter", 29 * -1)
        )
    Line.place(x = 169, y = 150, anchor = CENTER)
    
    Ycoor = 200
    
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

# Return Itemname from itemid 
def return_itemname(itemid):
   cur.execute('select Item_Name from items where itemid = %s ',(itemid,))
   item_name, = cur.fetchone()
   return item_name 
  
#-------------


       
# Return hotel Name from hotelId
def returnhotelname(hotelid):
    cur.execute('select Hotel_Name from hotel_details where HotelId = %s',(hotelid,))
    (hotelname,) = cur.fetchone()
    return (hotelname)

#compute amount with orderId
def computeamount(orderid):
    cur.execute('select HotelId from orders where OrderId = %s',(orderid,))
    (hotelid,) = cur.fetchone()
    cur.execute('select pricepercent,taxpercent from hotel_details where HotelId = %s',(hotelid,))
    price_percent,Tax_percent = cur.fetchone()
    cur.execute('select ItemId,Quantity from order_details where OrderId = %s ',(orderid,))
    items = cur.fetchall()
    total = 0
    for itemid,quantity in items :
        price = int(returnbaseprice(itemid)*((100+price_percent)/100)*quantity)   
        total += price
    GST = (Tax_percent/100)*total
    tempValue = ceil(GST*100)/100
    GST = tempValue        
    Platform_Fee = 0.05*total
    tempValue = ceil(Platform_Fee*100)/100
    Platform_Fee = tempValue 
    
    amount = total + GST + Platform_Fee
    tempValue = ceil(amount*100)/100
    amount = tempValue

    return str(amount)
    
def relative_to_assets7(path: str) -> Path:
    return ASSETS_PATH7 / Path(path)


def yourorderscanvas():
    global bgimage,rectangle_img,generate_bill_bg
    

    window.title("Jishnu's Food Delivery Application - oyFood - YourOrders")
    
    cur.execute('select OrderId,OrderDatetime,HotelId from orders where CustId = %s ',(Current_CustId,))
    orders = cur.fetchall()
    
    for Id,d,htlid in orders :
        date = d.strftime('%Y-%m-%d %H:%M')
        
    canvas11 = Canvas(
        window,
        bg = "#FFD4BD",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas11.place(x = 0, y = 0)
    bgimage = PhotoImage(
        file=relative_to_assets7("image_1.png"))
    image_1 = canvas11.create_image(
        500.0,
        300.0,
        image=bgimage
    )

    rectangle_img = PhotoImage(
        file=relative_to_assets7("image_2.png"))
    image_2 = canvas11.create_image(
        500.0,
        322.0,
        image=rectangle_img
    )
    # Creating a canvas, Scrollbar, Framw to make a scrollable bill 
    
    canvas12 = Canvas(window,
                 width = 925,         
                 height = 400,
                 )             
    canvas12.place(x = 28, y = 140)
 
    # Creating Framw
    #frame6 = Frame(canvas12, width=925, height=400, bg='#FFD4BD', highlightbackground='#FFD4BD',highlightcolor='')
    frame6 = Frame(canvas12, width=925, height=400, bg='#FFD4BD',borderwidth = 0,highlightthickness = 0)

    #Creating scrollbar
    scrollbar3 = Scrollbar(window,command=canvas12.yview)
    scrollbar3.place(x=955, y=140)
    scrollbar3.place(height=404)

    # Set canvas to scroll
    canvas12.configure(yscrollcommand=scrollbar3.set)
    canvas12.bind('<Configure>', lambda e: canvas12.configure(scrollregion=canvas12.bbox("all")))
    
    # default Bill_window height to incorporate htlname, address, Oyfood logo is 180 

    Bill_window_height = 500
    canvas12.create_window((0, 0),   
                     height = Bill_window_height,
                     width=925,
                     window=frame6,
                     anchor='nw')
    
    canvas11.create_text(
        21.0,
        21.0,
        anchor="nw",
        text="Your Orders",
        fill="#FFFFFF",
        font=("Inter", 37 * -1)
    )
    canvas11.create_text(
        640.0,
        98.0,
        anchor="nw",
        text="Amount",
        fill="#000000",
        font=("Inter", 24 * -1)
    )
    canvas11.create_text(
        85.0,
        98.0,
        anchor="nw",
        text="Ordered on ",
        fill="#000000",
        font=("Inter", 24 * -1)
    )
    canvas11.create_text(
        372.0,
        98.0,
        anchor="nw",
        text="Ordered from",
        fill="#000000",
        font=("Inter", 24 * -1)
    )
    generate_bill_bg = PhotoImage(
            file=relative_to_assets7("button_1.png"))   

    Ycoor = 30
    for Id,d,htlid in orders :
        
        date = d.strftime('%Y-%m-%d %H:%M')
        date_label = Label(frame6,
                           bg = "#FFD4BD", 
                           text = date,
                           font = ('Inter',16))
        date_label.place(x = 30, y = Ycoor)
        
        htlname = returnhotelname(htlid)
        if len(htlname) > 24 :
            htlname = htlname[:22]+'...'
        name = Label (frame6,
                      bg = '#FFD4BD',
                      text = htlname,
                      font = ('Inter',16))
        name.place(x = 280, y = Ycoor)
        
        amount_label = Label(frame6,
                         bg = '#FFD4BD',
                         text ='Rs '+str(computeamount(Id)),
                         font = ('Inter',16))  
        amount_label.place(x = 600, y = Ycoor,anchor='nw')
        

        generatebill_btn = Button(frame6,
            activebackground= '#FFD4BD',                          
            image=generate_bill_bg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda i = Id: bill(i),
            relief="flat"
        )
        generatebill_btn.place(
            x=750.0,y=Ycoor-15,anchor= 'nw')

        Ycoor += 80
        

    

window = Tk()
window.geometry("1000x600")
window.configure(bg = "#FFD4BD")

con = sql.connect(host='localhost',user = 'root',password = 'mysqlrootpwd',database='food_delivery_application')
cur = con.cursor()

Current_UserID = 'jishnu.one'  
Current_CustId = 1
yourorderscanvas()

window.resizable(False, False)
window.mainloop()
