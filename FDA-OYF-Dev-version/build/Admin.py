
import re                               # Regular Expressions
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.tix import *
import mysql.connector as sql
from tkinter import ttk 
from tkcalendar import Calendar
from datetime import datetime
from math import ceil                   # Math - Ceil 

#Establish MySql Connection and Cursor 
con = sql.connect(host='localhost',user = 'root',password = 'mysqlrootpwd',database='food_delivery_application')
cur = con.cursor()

#validate password for Signup :
def validatepwd(x):
    lower = 0 ; upper = 0 ; number = 0; special = 0;special_chars = '!@#$%^&*'
    for i in x :
        if i.isdigit(): 
            number +=1 
        elif i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i in special_chars:
            special += 1

    if lower >= 1 :
        if upper >= 1 :
            if number >= 1 :
                if special  >= 1 :
                    if lower >= 1 and upper >= 1 and upper >= 1 and special  >= 1 :
                        return True 
                    else :
                        return False  
                else :
                    messagebox.showwarning('Password Warning',"Password must contanin at least 1 special character (!@#$%^&*) ")
                    entry_9.delete(0,'end')
                    entry_10.delete(0,'end') 
            else :
                messagebox.showwarning('Password Warning',"Password must contanin at least 1 number")
                entry_9.delete(0,'end')
                entry_10.delete(0,'end')
        else :
            messagebox.showwarning('Password Warning',"Password must contanin at least 1 uppercase character ")
            entry_9.delete(0,'end')
            entry_10.delete(0,'end')         
    else :
        messagebox.showwarning('Password Warning',"Password must contanin at least 1 lowercase character ")
        entry_9.delete(0,'end')
        entry_10.delete(0,'end')

# Validate PhoneNumber:
def validatephno(x):
    number = 0 
    for i in x:
        if i.isdigit():
            number+=1
    if number == len(x):
        return True
    else :
        return False
    
#validate Email
def validateemail(x):
    # Regular expression pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$' # ^ = start , $  = end ,\w = alphanumeric and _, \. = dot ,- hyphen   
    # Using re.match() to check if the email matches the pattern
    if re.match(pattern, x):
        return True
    else:
        return False

# To validate length of data (Str) 
def validatelen(x,Min,Max) : # pass arguements for minumum length and maximum length 
    if len(x)> (Min -1) and len(x) < (Max +1):
        return True
    else:
        return False 

#Validate name : Usage -  (name,city,state)
def validatename(x,name): 
    # if the feild is name, check for pauses (.), else, Don't .
    letters = 0;spaces = 0; pauses = 0
    for i in x :
        if i.isalpha():
            letters += 1
        elif i.isspace():
            spaces +=1
        if name == 'name':
            if i == '.':
                pauses +=1 
        else:
            pass
    if letters + spaces + pauses == len(x):
        return True
    else :
        return False

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

# To return baseprice of an Item
def returnbaseprice(itemid):
    
    cur.execute('select BasePrice from items where ItemId = %s',(itemid,))
    (baseprice,)= cur.fetchone()
   
    return baseprice
      
##########################################################################

OUTPUT_PATH8 = Path(__file__).parent
ASSETS_PATH8 = OUTPUT_PATH8 / Path(r"assets\frame8")

def relative_to_assets8(path: str) -> Path:
    return ASSETS_PATH8 / Path(path)

# Display Report 6 
def display_report_6(report_6):
    
    global canvas34,frame15,scrollbar13
    if "canvas34" in globals():
        canvas34.destroy()
        scrollbar13.destroy()
        frame15.destroy()
        
    canvas34 = Canvas(window,highlightthickness=0,height = 410,width = 980,bg ='#FFFFFF',borderwidth=0)
    canvas34.place(x = 17,y = 150)

    #Creating scrollbar
    scrollbar13 = Scrollbar(window,command=canvas34.yview)
    scrollbar13.place(x=977, y=150)
    scrollbar13.place(height=410)
   
    # Creating Frame
    frame15 = Frame(canvas34, width=985, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas34.configure(yscrollcommand=scrollbar13.set)
    canvas34.bind('<Configure>', lambda e: canvas34.configure(scrollregion=canvas34.bbox("all")))
        
    window_height = 50*len(report_6) +110
    canvas34.create_window((0, 0),   
                     height =window_height,
                     width=980,
                     window=frame15,
                     anchor='nw')
        
    Ycoor = 10
    for name,hotel_name,orderid in report_6 :
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
        
        if Ycoor == 10 :
            item_name_label = Label(frame15,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Order Amount',anchor=CENTER)
            item_name_label.place(x = 590,y = Ycoor)

            cust_name_label = Label(frame15,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Customer Name',anchor=CENTER)
            cust_name_label.place(x = 10,y = Ycoor)
        
            email_address_label = Label(frame15,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel Name')
            email_address_label.place(x = 300,y = Ycoor)
        
            Order_count_label = Label(frame15,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='View Bill')
            Order_count_label.place(x = 820,y = Ycoor)

            Ycoor+=60
         
        if len(name)>15:
            name = name[:13]+'...'
        
        if len(hotel_name)>15:
            hotel_name = hotel_name[:13]+'...'
        
        orderamt = str(computeamount(orderid))
        
        if len(orderamt) > 9:
            orderamt = orderamt[:]+'...'
            
        label0 = Label(frame15,bg ='#FFFFFF',font = Font,foreground= Foreground, text =orderamt,anchor=CENTER)
        label0.place(x = 660,y = Ycoor+15,anchor= CENTER)

        label1 = Label(frame15,bg ='#FFFFFF',font = Font,foreground= Foreground, text =name,anchor=CENTER)
        label1.place(x = 10,y = Ycoor)
        
        label2 = Label(frame15,bg ='#FFFFFF',font = Font,foreground= Foreground, text =hotel_name)
        label2.place(x = 300,y = Ycoor)
        
        generatebill_btn = Button(frame15,
            font = Font,
            text = 'View Bill',
            activebackground= '#FFD4BD',                          
            borderwidth=0,
            highlightthickness=0,
            #command=lambda i = orderid:bill(i),
            relief="flat"
        )
        generatebill_btn.place( x=870.0,
                               y=Ycoor + 10,
                               anchor= CENTER)
        
        Ycoor += 50   
        
# genreate report 6 from sql 
def generate_report_6(start_date,end_date,user_option):
    
    if user_option == 'Select All' :
        query = '''SELECT 
        pd.Name,hd.Hotel_Name,o.OrderId
	    FROM orders o
	    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	    JOIN login_credentials lc ON o.custid = lc.CustId
	    JOIN personal_details pd ON lc.CustId = pd.Custid
        where  o.OrderDatetime >  %s  and o.OrderDatetime <= %s 
	    ORDER BY o.OrderDatetime DESC;
        '''    
        value_tuple= (start_date,end_date)
        
    else :  
        index = dropdown_menu.current()
        cust_id = menu_custid[index-1]
        query = '''SELECT 
        pd.Name,hd.Hotel_Name,o.OrderId
	    FROM orders o
	    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	    JOIN login_credentials lc ON o.custid = lc.CustId
	    JOIN personal_details pd ON lc.CustId = pd.Custid
        where  o.OrderDatetime >  %s  and o.OrderDatetime <= %s and  o.custid = %s
	    ORDER BY o.OrderDatetime DESC;
        '''
        value_tuple= (start_date,end_date,cust_id)
    
    cur.execute(query,value_tuple)
    report_6 = cur.fetchall()
    
    if report_6 == []:
       messagebox.showinfo('No Orders ','No Orders were made by selected user in the given timespan')
    else : 
       display_report_6(report_6)

# Generate Report btn - Go btn - click event 
def report_6_go_btn():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    user_option = dropdown_menu.get()
    user_option = user_option.strip()
    if start_date > end_date :
        messagebox.showerror('Date Error','Start date connot be later then End Date')
    elif user_option == '' or  user_option not in menu:
        messagebox.showerror('User Error','Invalid User Option')
    else :
        generate_report_6(start_date,end_date,user_option)        

# create menu for report 6 : tuple of all hotels with All option
def report6_create_menu():
    global menu,menu_custid
    
    cur.execute('Select Name,Address,Custid from personal_details')
    
    hotels = cur.fetchall()
    menu = ['Select All']
    menu_custid = []
    
    for name,address,custid in hotels:
        menu.append(str(name+' | '+address))
        menu_custid.append(custid)
        
# report 6 - user wise - recent order
def report_6():
    
    global canvas33,report_button_image_4,report_button_image_3,report_button_image_2,report_button_image_1
    global today,start_date_var,end_date_var,dropdown_menu,menu
    
    admn_home_btn()
  
    canvas33 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas33.place(x = 0, y = 0)
    
    start_date_var = StringVar(canvas33)
    start_date_var.set("2024-01-01")

    end_date_var = StringVar(canvas33)
    today = datetime.today().date()
    end_date_var.set(today.strftime("%Y-%m-%d"))   
    
    report6_create_menu()
    
    dropdown_menu = ttk.Combobox(canvas33,width =120)
    dropdown_menu['values'] = menu
    dropdown_menu.current(0)
    dropdown_menu.place(x = 90, y= 63) 

    
    go_btn = Button(canvas33,
                    text = 'Go',
                    width = 15,
                    command = report_6_go_btn)
    go_btn.place(x = 840, y = 60)

    entry_1 = Entry(canvas33,
        textvariable=end_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=609.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    entry_2 = Entry(canvas33,
        textvariable=start_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=159.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    canvas33.create_text(
        99.0,
        22.0,
        anchor="nw",
        text="Start date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    canvas33.create_text(
        556.0,
        22.0,
        anchor="nw",
        text="End date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_26.png"))
    button_1 = Button(canvas33,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_start_calendar,
        relief="flat"
    )
    button_1.place(
        x=432.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_27.png"))
    button_2 = Button(canvas33,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_end_calendar,
        relief="flat"
    )
    button_2.place(
        x=882.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    button_3 = Button(canvas33,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    button_3.place(
        x=6.0,
        y=6.0,
        width=45.0,
        height=45.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    button_4 = Button(canvas33,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    button_4.place(
        x=963.0,
        y=6.0,
        width=32.0,
        height=41.0
    )

# Display Report 5 
def display_report_5(report_5):
    
    global canvas32,frame14,scrollbar12
    if "canvas32" in globals():
        canvas32.destroy()
        scrollbar12.destroy()
        frame14.destroy()
        
    canvas32 = Canvas(window,highlightthickness=0,height = 410,width = 980,bg ='#FFFFFF',borderwidth=0)
    canvas32.place(x = 17,y = 150)

    #Creating scrollbar
    scrollbar12 = Scrollbar(window,command=canvas32.yview)
    scrollbar12.place(x=977, y=150)
    scrollbar12.place(height=410)
   
    # Creating Frame
    frame14 = Frame(canvas32, width=985, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas32.configure(yscrollcommand=scrollbar12.set)
    canvas32.bind('<Configure>', lambda e: canvas32.configure(scrollregion=canvas32.bbox("all")))
        
    window_height = 50*len(report_5) +110
    canvas32.create_window((0, 0),   
                     height =window_height,
                     width=980,
                     window=frame14,
                     anchor='nw')
        
    Ycoor = 10
    for name,hotel_name,hotel_address ,Order_count in report_5 :
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
        
        if Ycoor == 10 :
            item_name_label = Label(frame14,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel Address',anchor=CENTER)
            item_name_label.place(x = 590,y = Ycoor)

            cust_name_label = Label(frame14,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Customer Name',anchor=CENTER)
            cust_name_label.place(x = 10,y = Ycoor)
        
            email_address_label = Label(frame14,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel Name')
            email_address_label.place(x = 300,y = Ycoor)
        
            Order_count_label = Label(frame14,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Order Count')
            Order_count_label.place(x = 800,y = Ycoor)

            Ycoor+=60
         
        if len(name)>15:
            name = name[:13]+'...'
        
        if len(hotel_name)>15:
            hotel_name = hotel_name[:13]+'...'
        
        if len(hotel_address)>17:
            hotel_address = hotel_address[:14]+'...'
        
        label0 = Label(frame14,bg ='#FFFFFF',font = Font,foreground= Foreground, text =hotel_address,anchor=CENTER)
        label0.place(x = 590,y = Ycoor)

        label1 = Label(frame14,bg ='#FFFFFF',font = Font,foreground= Foreground, text =name,anchor=CENTER)
        label1.place(x = 10,y = Ycoor)
        
        label2 = Label(frame14,bg ='#FFFFFF',font = Font,foreground= Foreground, text =hotel_name)
        label2.place(x = 300,y = Ycoor)
        
        label3 = Label(frame14,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =Order_count)
        label3.place(x = 870,y = Ycoor + 15 ,anchor= CENTER)

        Ycoor += 50   
        
# genreate report 5 from sql 
def generate_report_5(start_date,end_date,user_option):
    
    if user_option == 'Select All' :
        query = '''	SELECT 
        pd.Name,hd.Hotel_Name,hd.address,COUNT(o.OrderId)
	    FROM orders o
	    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	    JOIN login_credentials lc ON o.custid = lc.CustId
	    JOIN personal_details pd ON lc.CustId = pd.Custid
	    WHERE o.OrderDatetime > %s  and o.OrderDatetime <= %s
	    GROUP BY pd.Name, hd.Hotel_Name,hd.address;
    ;
        '''    
        value_tuple= (start_date,end_date)
        
    else :
        index = dropdown_menu.current()
        cust_id = menu_custid[index-1]
        query = '''	SELECT 
        pd.Name,hd.Hotel_Name,hd.address,COUNT(o.OrderId)
	    FROM orders o
	    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	    JOIN login_credentials lc ON o.custid = lc.CustId
	    JOIN personal_details pd ON lc.CustId = pd.Custid
	    WHERE o.OrderDatetime >  %s  and o.OrderDatetime <= %s and lc.CustId = %s
	    GROUP BY pd.Name, hd.Hotel_Name,hd.address;

        '''
        value_tuple= (start_date,end_date,cust_id)
    
    cur.execute(query,value_tuple)
    report_5 = cur.fetchall()
    
    if report_5 == []:
       messagebox.showinfo('No Hotels ','No Hotels were Ordered from by selected user in the given timespan')
    else : 
       display_report_5(report_5)

# Generate Report btn - Go btn - click event 
def report_5_go_btn():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    user_option = dropdown_menu.get()
    user_option = user_option.strip()
    if start_date > end_date :
        messagebox.showerror('Date Error','Start date connot be later then End Date')
    elif user_option == '' or  user_option not in menu:
        messagebox.showerror('User Error','Invalid User Option')
    else :
        generate_report_5(start_date,end_date,user_option)        

# create menu for report 5 : tuple of all hotels with All option
def report5_create_menu():
    global menu,menu_custid
    
    cur.execute('Select Name,Address,Custid from personal_details')
    
    hotels = cur.fetchall()
    menu = ['Select All']
    menu_custid = []
    
    for name,address,custid in hotels:
        menu.append(str(name+' | '+address))
        menu_custid.append(custid)
        
# report 5 - User Wise hotel  - order count report
def report_5():
    
    global canvas31,report_button_image_4,report_button_image_3,report_button_image_2,report_button_image_1
    global today,start_date_var,end_date_var,dropdown_menu,menu
    
    admn_home_btn()
  
    canvas31 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas31.place(x = 0, y = 0)
    
    start_date_var = StringVar(canvas31)
    start_date_var.set("2024-01-01")

    end_date_var = StringVar(canvas31)
    today = datetime.today().date()
    end_date_var.set(today.strftime("%Y-%m-%d"))   
    
    report5_create_menu()
    
    dropdown_menu = ttk.Combobox(canvas31,width =120)
    dropdown_menu['values'] = menu
    dropdown_menu.current(0)
    dropdown_menu.place(x = 90, y= 63) 

    
    go_btn = Button(canvas31,
                    text = 'Go',
                    width = 15,
                    command = report_5_go_btn)
    go_btn.place(x = 840, y = 60)

    entry_1 = Entry(canvas31,
        textvariable=end_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=609.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    entry_2 = Entry(canvas31,
        textvariable=start_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=159.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    canvas31.create_text(
        99.0,
        22.0,
        anchor="nw",
        text="Start date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    canvas31.create_text(
        556.0,
        22.0,
        anchor="nw",
        text="End date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_26.png"))
    button_1 = Button(canvas31,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_start_calendar,
        relief="flat"
    )
    button_1.place(
        x=432.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_27.png"))
    button_2 = Button(canvas31,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_end_calendar,
        relief="flat"
    )
    button_2.place(
        x=882.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    button_3 = Button(canvas31,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    button_3.place(
        x=6.0,
        y=6.0,
        width=45.0,
        height=45.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    button_4 = Button(canvas31,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    button_4.place(
        x=963.0,
        y=6.0,
        width=32.0,
        height=41.0
    )
 
# Display Report 4 
def display_report_4(report_4):
    
    global canvas30,frame13,scrollbar11
    if "canvas30" in globals():
        canvas30.destroy()
        scrollbar11.destroy()
        frame13.destroy()
        
    canvas30 = Canvas(window,highlightthickness=0,height = 410,width = 980,bg ='#FFFFFF',borderwidth=0)
    canvas30.place(x = 17,y = 150)

    #Creating scrollbar
    scrollbar11 = Scrollbar(window,command=canvas30.yview)
    scrollbar11.place(x=977, y=150)
    scrollbar11.place(height=410)
   
    # Creating Frame
    frame13 = Frame(canvas30, width=985, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas30.configure(yscrollcommand=scrollbar11.set)
    canvas30.bind('<Configure>', lambda e: canvas30.configure(scrollregion=canvas30.bbox("all")))
        
    window_height = 50*len(report_4) +110
    canvas30.create_window((0, 0),   
                     height =window_height,
                     width=980,
                     window=frame13,
                     anchor='nw')
        
    Ycoor = 10
    for name,email_id,Item_name ,Order_count in report_4 :
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
        
        if Ycoor == 10 :
            item_name_label = Label(frame13,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Item Name',anchor=CENTER)
            item_name_label.place(x = 590,y = Ycoor)

            cust_name_label = Label(frame13,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Customer Name',anchor=CENTER)
            cust_name_label.place(x = 10,y = Ycoor)
        
            email_address_label = Label(frame13,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Emai address')
            email_address_label.place(x = 300,y = Ycoor)
        
            Order_count_label = Label(frame13,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Order Count')
            Order_count_label.place(x = 800,y = Ycoor)

            Ycoor+=60
         
        if len(name)>15:
            name = name[:13]+'...'
        
        if len(Item_name)>15:
            Item_name = Item_name[:13]+'...'
        
        if len(email_id)>17:
            email_id = email_id[:14]+'...'
        
        label0 = Label(frame13,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Item_name,anchor=CENTER)
        label0.place(x = 590,y = Ycoor)

        label1 = Label(frame13,bg ='#FFFFFF',font = Font,foreground= Foreground, text =name,anchor=CENTER)
        label1.place(x = 10,y = Ycoor)
        
        label2 = Label(frame13,bg ='#FFFFFF',font = Font,foreground= Foreground, text =email_id)
        label2.place(x = 300,y = Ycoor)
        
        label3 = Label(frame13,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =Order_count)
        label3.place(x = 870,y = Ycoor + 15 ,anchor= CENTER)

        Ycoor += 50   
        
# genreate report 4 from sql 
def generate_report_4(start_date,end_date,user_option):
    
    if user_option == 'Select All' :
        query = '''	SELECT pd.Name,pd.emailid,i.Item_Name,SUM(od.Quantity)
	    FROM orders o
	    JOIN order_details od ON o.OrderId = od.OrderId
	    JOIN items i ON od.ItemId = i.ItemId
	    JOIN login_credentials lc ON o.custid = lc.CustId
	    JOIN personal_details pd ON lc.CustId = pd.Custid
	    WHERE o.OrderDatetime > %s and o.OrderDatetime <= %s 
	    GROUP BY pd.Name, i.Item_Name, pd.emailid ;
        '''    
        value_tuple= (start_date,end_date)
        
    else :
        index = dropdown_menu.current()
        cust_id = menu_custid[index-1]
        query = '''	SELECT pd.Name,pd.emailid,i.Item_Name,SUM(od.Quantity)
	    FROM orders o
	    JOIN order_details od ON o.OrderId = od.OrderId
	    JOIN items i ON od.ItemId = i.ItemId
	    JOIN login_credentials lc ON o.custid = lc.CustId
	    JOIN personal_details pd ON lc.CustId = pd.Custid
	    WHERE o.OrderDatetime >  %s  and o.OrderDatetime <= %s and lc.CustId = %s
	    GROUP BY pd.Name, i.Item_Name, pd.emailid ;
        '''
        value_tuple= (start_date,end_date,cust_id)
    
    cur.execute(query,value_tuple)
    report_4 = cur.fetchall()
    
    if report_4 == []:
       messagebox.showinfo('No Items','No Items were Ordered by selected user in the given timespan')
    else : 
       display_report_4(report_4)

# Generate Report btn - Go btn - click event 
def report_4_go_btn():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    user_option = dropdown_menu.get()
    user_option = user_option.strip()
    if start_date > end_date :
        messagebox.showerror('Date Error','Start date connot be later then End Date')
    elif user_option == '' or  user_option not in menu:
        messagebox.showerror('User Error','Invalid User Option')
    else :
        generate_report_4(start_date,end_date,user_option)        

# create menu for report 4 : tuple of all users with All option
def report4_create_menu():
    global menu,menu_custid
    
    cur.execute('Select Name,Address,Custid from personal_details')
    
    hotels = cur.fetchall()
    menu = ['Select All']
    menu_custid = []
    
    for name,address,custid in hotels:
        menu.append(str(name+' | '+address))
        menu_custid.append(custid)
        
# report 4 - user wise item - order count report
def report_4():
    
    global canvas29,report_button_image_4,report_button_image_3,report_button_image_2,report_button_image_1
    global today,start_date_var,end_date_var,dropdown_menu,menu
    
    #admn_home_btn()
  
    canvas29 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas29.place(x = 0, y = 0)
    
    start_date_var = StringVar(canvas29)
    start_date_var.set("2024-01-01")

    end_date_var = StringVar(canvas29)
    today = datetime.today().date()
    end_date_var.set(today.strftime("%Y-%m-%d"))   
    
    report4_create_menu()
    
    dropdown_menu = ttk.Combobox(canvas29,width =120)
    dropdown_menu['values'] = menu
    dropdown_menu.current(0)
    dropdown_menu.place(x = 90, y= 63) 

    
    go_btn = Button(canvas29,
                    text = 'Go',
                    width = 15,
                    command = report_4_go_btn)
    go_btn.place(x = 840, y = 60)

    entry_1 = Entry(canvas29,
        textvariable=end_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=609.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    entry_2 = Entry(canvas29,
        textvariable=start_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=159.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    canvas29.create_text(
        99.0,
        22.0,
        anchor="nw",
        text="Start date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    canvas29.create_text(
        556.0,
        22.0,
        anchor="nw",
        text="End date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_26.png"))
    button_1 = Button(canvas29,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_start_calendar,
        relief="flat"
    )
    button_1.place(
        x=432.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_27.png"))
    button_2 = Button(canvas29,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_end_calendar,
        relief="flat"
    )
    button_2.place(
        x=882.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    button_3 = Button(canvas29,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    button_3.place(
        x=6.0,
        y=6.0,
        width=45.0,
        height=45.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    button_4 = Button(canvas29,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    button_4.place(
        x=963.0,
        y=6.0,
        width=32.0,
        height=41.0
    )
 
# Display Report 3 
def display_report_3(report_3):
    
    global canvas28,frame12,scrollbar10
    if "canvas28" in globals():
        canvas28.destroy()
        scrollbar10.destroy()
        frame12.destroy()
        
    canvas28 = Canvas(window,highlightthickness=0,height = 410,width = 980,bg ='#FFFFFF',borderwidth=0)
    canvas28.place(x = 17,y = 150)

    #Creating scrollbar
    scrollbar10 = Scrollbar(window,command=canvas28.yview)
    scrollbar10.place(x=977, y=150)
    scrollbar10.place(height=410)
   
    # Creating Frame
    frame12 = Frame(canvas28, width=985, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas28.configure(yscrollcommand=scrollbar10.set)
    canvas28.bind('<Configure>', lambda e: canvas28.configure(scrollregion=canvas28.bbox("all")))
        
    window_height = 50*len(report_3) +110
    canvas28.create_window((0, 0),   
                     height =window_height,
                     width=980,
                     window=frame12,
                     anchor='nw')
    
    Ycoor = 10
    for Hotel_name,Hotel_address,name,Order_count in report_3 :
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
        
        if Ycoor == 10 :
            cust_name_label = Label(frame12,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Item Name',anchor=CENTER)
            cust_name_label.place(x = 530,y = Ycoor)

            hotel_name_label = Label(frame12,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel Name',anchor=CENTER)
            hotel_name_label.place(x = 10,y = Ycoor)
        
            Hotel_address_label = Label(frame12,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel address')
            Hotel_address_label.place(x = 270,y = Ycoor)
        
            Order_count_label = Label(frame12,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Order Count')
            Order_count_label.place(x = 800,y = Ycoor)

            Ycoor+=60
         
        if len(name)>15:
            name = name[:13]+'...'
        
        if len(Hotel_name)>15:
            Hotel_name = Hotel_name[:13]+'...'
        if len(Hotel_address)>20:
            Hotel_address = Hotel_address[:18]+'...'
        
        label0 = Label(frame12,bg ='#FFFFFF',font = Font,foreground= Foreground, text =name,anchor=CENTER)
        label0.place(x = 530,y = Ycoor)

        label1 = Label(frame12,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Hotel_name,anchor=CENTER)
        label1.place(x = 10,y = Ycoor)
        
        label2 = Label(frame12,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Hotel_address)
        label2.place(x = 270,y = Ycoor)
        
        label3 = Label(frame12,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =Order_count)
        label3.place(x = 870,y = Ycoor,anchor= CENTER)

        Ycoor += 50   
        
# genreate report 3 from sql 
def generate_report_3(start_date,end_date,htl_option):
    
    if htl_option == 'Select All' :
        query = '''SELECT 
    hd.Hotel_Name,hd.address,i.Item_Name,SUM(od.Quantity)
	FROM orders o 
	JOIN order_details od ON o.OrderId = od.OrderId
	JOIN items i ON od.ItemId = i.ItemId
    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	where o.OrderDatetime > %s and o.OrderDatetime <= %s 
	GROUP BY hd.Hotel_Name, i.Item_Name, hd.address;
        ''' 
        value_tuple = (start_date,end_date)
    else :
        [hotelname,address] = htl_option.split(' | ')
        query = '''SELECT 
    hd.Hotel_Name,hd.address,i.Item_Name,SUM(od.Quantity)
	FROM orders o 
	JOIN order_details od ON o.OrderId = od.OrderId
	JOIN items i ON od.ItemId = i.ItemId
    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	where o.OrderDatetime > %s and o.OrderDatetime <= %s
    and hd.hotel_name = %s and hd.address = %s
	GROUP BY hd.Hotel_Name, i.Item_Name, hd.address;
        '''
        value_tuple = (start_date,end_date,hotelname,address)
    
    cur.execute(query,value_tuple)
    report_3 = cur.fetchall()
    
    if report_3 == []:
        messagebox.showinfo('No Items','No Items were Ordered by users from the selected hotel or in the given timespan')
    else : 
        display_report_3(report_3)

# Generate Report btn - Go btn - click event 
def report_3_go_btn():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    htl_option = dropdown_menu.get()
    htl_option = htl_option.strip()
    if start_date > end_date :
        messagebox.showerror('Date Error','Start date connot be later then End Date')
    elif htl_option == '' or  htl_option not in menu:
        messagebox.showerror('Hotel Error','Invalid Hotel Option')
    else :
        generate_report_3(start_date,end_date,htl_option)        

# create menu for report 3 : tuple of all hotels with All option
def report3_create_menu():
    global menu
    
    cur.execute('Select hotel_name,address from hotel_details')
    
    hotels = cur.fetchall()
    menu = ['Select All']
    for name,address in hotels:
        menu.append(str(name+' | '+address))
    
# report 3 - hotel wise user - order count report
def report_3():
    
    global canvas27,report_button_image_4,report_button_image_3,report_button_image_2,report_button_image_1
    global today,start_date_var,end_date_var,dropdown_menu,menu
    
    #admn_home_btn()
  
    canvas27 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas27.place(x = 0, y = 0)
    
    start_date_var = StringVar(canvas27)
    start_date_var.set("2024-01-01")

    end_date_var = StringVar(canvas27)
    today = datetime.today().date()
    end_date_var.set(today.strftime("%Y-%m-%d"))   
    
    report3_create_menu()
    
    dropdown_menu = ttk.Combobox(canvas27,width =120)
    dropdown_menu['values'] = menu
    dropdown_menu.current(0)
    dropdown_menu.place(x = 90, y= 63) 

    
    go_btn = Button(canvas27,
                    text = 'Go',
                    width = 15,
                    command = report_3_go_btn)
    go_btn.place(x = 840, y = 60)

    entry_1 = Entry(canvas27,
        textvariable=end_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=609.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    entry_2 = Entry(canvas27,
        textvariable=start_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=159.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    canvas27.create_text(
        99.0,
        22.0,
        anchor="nw",
        text="Start date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    canvas27.create_text(
        556.0,
        22.0,
        anchor="nw",
        text="End date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_26.png"))
    button_1 = Button(canvas27,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_start_calendar,
        relief="flat"
    )
    button_1.place(
        x=432.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_27.png"))
    button_2 = Button(canvas27,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_end_calendar,
        relief="flat"
    )
    button_2.place(
        x=882.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    button_3 = Button(canvas27,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    button_3.place(
        x=6.0,
        y=6.0,
        width=45.0,
        height=45.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    button_4 = Button(canvas27,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    button_4.place(
        x=963.0,
        y=6.0,
        width=32.0,
        height=41.0
    )
    
# Display Report 2 
def display_report_2(report_2):
    
    global canvas26,frame11,scrollbar9
    
    if "canvas26" in globals():
        canvas26.destroy()
        scrollbar9.destroy()
        frame11.destroy()
        
    canvas26 = Canvas(window,highlightthickness=0,height = 410,width = 980,bg ='#FFFFFF',borderwidth=0)
    canvas26.place(x = 17,y = 150)

    #Creating scrollbar
    scrollbar9 = Scrollbar(window,command=canvas26.yview)
    scrollbar9.place(x=977, y=150)
    scrollbar9.place(height=410)
   
    # Creating Frame
    frame11 = Frame(canvas26, width=985, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas26.configure(yscrollcommand=scrollbar9.set)
    canvas26.bind('<Configure>', lambda e: canvas26.configure(scrollregion=canvas26.bbox("all")))
        
    window_height = 50*len(report_2) +110
    canvas26.create_window((0, 0),   
                     height =window_height,
                     width=980,
                     window=frame11,
                     anchor='nw')
    
    Ycoor = 10
    for name,Hotel_name,Hotel_address ,Order_count in report_2 :
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
        
        if Ycoor == 10 :
            cust_name_label = Label(frame11,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Customer Name',anchor=CENTER)
            cust_name_label.place(x = 530,y = Ycoor)

            hotel_name_label = Label(frame11,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel Name',anchor=CENTER)
            hotel_name_label.place(x = 10,y = Ycoor)
        
            Hotel_address_label = Label(frame11,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel address')
            Hotel_address_label.place(x = 270,y = Ycoor)
        
            Order_count_label = Label(frame11,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Order Count')
            Order_count_label.place(x = 800,y = Ycoor)

            Ycoor+=60
         
        if len(name)>15:
            name = name[:13]+'...'
        
        if len(Hotel_name)>15:
            Hotel_name = Hotel_name[:13]+'...'
        if len(Hotel_address)>20:
            Hotel_address = Hotel_address[:18]+'...'
        
        label0 = Label(frame11,bg ='#FFFFFF',font = Font,foreground= Foreground, text =name,anchor=CENTER)
        label0.place(x = 530,y = Ycoor)

        label1 = Label(frame11,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Hotel_name,anchor=CENTER)
        label1.place(x = 10,y = Ycoor)
        
        label2 = Label(frame11,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Hotel_address)
        label2.place(x = 270,y = Ycoor)
        
        label3 = Label(frame11,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =Order_count)
        label3.place(x = 870,y = Ycoor+ 15,anchor= CENTER)

        Ycoor += 50   
        
# genreate report 2 from sql 
def generate_report_2(start_date,end_date,htl_option):
    
    if htl_option == 'Select All' :
        query = '''SELECT 
	    personal_details.name, hotel_details.hotel_name,hotel_details.address, COUNT(orders.custid) AS order_count
        FROM orders
	    JOIN personal_details ON personal_details.custid = orders.custid
	    JOIN hotel_details ON hotel_details.hotelid = orders.hotelid
        where orders.OrderDatetime > %s and orders.OrderDatetime <= %s
        GROUP BY personal_details.name, hotel_details.hotel_name, hotel_details.address, orders.custid, orders.hotelid;
        ''' 
        value_tuple = (start_date,end_date)
    else :
        [hotelname,address] = htl_option.split(' | ')
        query = '''SELECT 
	    personal_details.name, hotel_details.hotel_name,hotel_details.address, COUNT(orders.custid) AS order_count
	    FROM orders
	    JOIN personal_details ON personal_details.custid = orders.custid
	    JOIN hotel_details ON hotel_details.hotelid = orders.hotelid
        where orders.OrderDatetime > %s and orders.OrderDatetime <= %s and hotel_details.hotel_name = %s and hotel_details.address = %s
        GROUP BY personal_details.name, hotel_details.hotel_name, hotel_details.address, orders.custid, orders.hotelid;
        '''
        value_tuple = (start_date,end_date,hotelname,address)
    
    cur.execute(query,value_tuple)
    report_2 = cur.fetchall()
    
    if report_2 == []:
        messagebox.showinfo('No Orders','No orders were made by users from the selected hotel or in the given timespan')
    else : 
        display_report_2(report_2)

# Generate Report btn - Go btn - click event 
def report_2_go_btn():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    htl_option = dropdown_menu.get()
    htl_option = htl_option.strip()
    if start_date > end_date :
        messagebox.showerror('Date Error','Start date connot be later then End Date')
    elif htl_option == '' or  htl_option not in menu:
        messagebox.showerror('Hotel Error','Invalid Hotel Option')
    else :
        generate_report_2(start_date,end_date,htl_option)        

# create menu for report 2 : tuple of all hotels with All option
def report2_create_menu():
    global menu
    
    cur.execute('Select hotel_name,address from hotel_details')
    
    hotels = cur.fetchall()
    menu = ['Select All']
    for name,address in hotels:
        menu.append(str(name+' | '+address))
    
# report 2 - hotel wise user - order count report
def report_2():
    
    global canvas25,report_button_image_4,report_button_image_3,report_button_image_2,report_button_image_1
    global today,start_date_var,end_date_var,dropdown_menu,menu
    
    admn_home_btn()
  
    canvas25 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas25.place(x = 0, y = 0)
    
    start_date_var = StringVar(canvas25)
    start_date_var.set("2024-01-01")

    end_date_var = StringVar(canvas25)
    today = datetime.today().date()
    end_date_var.set(today.strftime("%Y-%m-%d"))   
    
    report2_create_menu()
    
    dropdown_menu = ttk.Combobox(canvas25,width =120)
    dropdown_menu['values'] = menu
    dropdown_menu.current(0)
    dropdown_menu.place(x = 90, y= 63) 

    
    go_btn = Button(canvas25,
                    text = 'Go',
                    width = 15,
                    command = report_2_go_btn)
    go_btn.place(x = 840, y = 60)

    entry_1 = Entry(canvas25,
        textvariable=end_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=609.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    entry_2 = Entry(canvas25,
        textvariable=start_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=159.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    canvas25.create_text(
        99.0,
        22.0,
        anchor="nw",
        text="Start date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    canvas25.create_text(
        556.0,
        22.0,
        anchor="nw",
        text="End date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_26.png"))
    button_1 = Button(canvas25,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_start_calendar,
        relief="flat"
    )
    button_1.place(
        x=432.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_27.png"))
    button_2 = Button(canvas25,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_end_calendar,
        relief="flat"
    )
    button_2.place(
        x=882.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    button_3 = Button(canvas25,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    button_3.place(
        x=6.0,
        y=6.0,
        width=45.0,
        height=45.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    button_4 = Button(canvas25,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    button_4.place(
        x=963.0,
        y=6.0,
        width=32.0,
        height=41.0
    )
 
# Display Report 1 
def display_report_1(report_1):
    
    global canvas24,frame10,scrollbar8
    if "canvas24" in globals():
        canvas24.destroy()
        scrollbar8.destroy()
        frame10.destroy()
        
    canvas24 = Canvas(window,highlightthickness=0,height = 410,width = 920,bg ='#FFFFFF',borderwidth=0)
    canvas24.place(x = 77,y = 150)

    #Creating scrollbar
    scrollbar8 = Scrollbar(window,command=canvas24.yview)
    scrollbar8.place(x=977, y=150)
    scrollbar8.place(height=410)
   
    # Creating Frame
    frame10 = Frame(canvas24, width=925, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas24.configure(yscrollcommand=scrollbar8.set)
    canvas24.bind('<Configure>', lambda e: canvas24.configure(scrollregion=canvas24.bbox("all")))
        
    window_height = 50*len(report_1) +110
    canvas24.create_window((0, 0),   
                     height =window_height,
                     width=920,
                     window=frame10,
                     anchor='nw')
    Ycoor = 10
    for order_count,Hotel_name,Hotel_address in report_1 :
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
        
        if Ycoor == 10 :
            hotel_name_label = Label(frame10,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel Name',anchor=CENTER)
            hotel_name_label.place(x = 30,y = Ycoor)
        
            Hotel_address_label = Label(frame10,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Hotel address')
            Hotel_address_label.place(x = 350,y = Ycoor)
        
            Order_count_label = Label(frame10,bg ='#FFFFFF',font = ('Inika',18,'bold'),foreground= Foreground, text ='Order Count')
            Order_count_label.place(x = 700,y = Ycoor)
        
            Ycoor+=60
        
        if len(Hotel_name)>15:
            Hotel_name = Hotel_name[:13]+'...'
        if len(Hotel_address)>20:
            Hotel_address = Hotel_address[:18]+'...'
        
        label1 = Label(frame10,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Hotel_name,anchor=CENTER)
        label1.place(x = 30,y = Ycoor)
        
        label2 = Label(frame10,bg ='#FFFFFF',font = Font,foreground= Foreground, text =Hotel_address)
        label2.place(x = 350,y = Ycoor)
        
        label3 = Label(frame10,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =order_count)
        label3.place(x = 770,y = Ycoor+ 15,anchor = CENTER)
        
        Ycoor += 50   
        
# genreate report 1 from sql 
def generate_report_1(start_date,end_date,htl_option):
    
    if htl_option == 'Select All' :
        query = '''select count(orders.hotelid),hotel_details.hotel_name,hotel_details.address 
        from hotel_details left join orders on orders.hotelid = hotel_details.hotelid 
        where orders.OrderDatetime > %s and orders.OrderDatetime <= %s
        group by  orders.hotelid,hotel_details.hotel_name,hotel_details.address ;'''
        value_tuple = (start_date,end_date)
    else :
        [hotelname,address] = htl_option.split(' | ')
        query = '''select count(orders.hotelid) , hotel_details.hotel_name,hotel_details.address 
        from hotel_details left join orders on orders.hotelid = hotel_details.hotelid 
        where orders.OrderDatetime > %s and orders.OrderDatetime <= %s  
        and hotel_details.hotel_name = %s and hotel_details.address = %s
        group by  orders.hotelid,hotel_details.hotel_name,hotel_details.address ;'''
        value_tuple = (start_date,end_date,hotelname,address)
    
    cur.execute(query,value_tuple)
    report_1 = cur.fetchall()
    
    if report_1 == []:
        messagebox.showinfo('No Orders','No orders were made from the selected hotel or in the given timespan')
    else : 
        display_report_1(report_1)

# Generate Report btn - Go btn - click event 
def report_1_go_btn():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    htl_option = dropdown_menu.get()
    htl_option = htl_option.strip()
    if start_date > end_date :
        messagebox.showerror('Date Error','Start date connot be later then End Date')
    elif htl_option == '' or htl_option not in menu:
        messagebox.showerror('Hotel Error','Invalid Hotel Option')
    else :
        generate_report_1(start_date,end_date,htl_option)
        
# Check date on start date selected
def on_start_date_selected():
    
    selected_date = cal.selection_get()
    
    if selected_date > today:
        messagebox.showerror("Invalid Date", "You can't select a date later than today's date.")
        cal.selection_set(today) 

    else:
        start_date_var.set(selected_date.strftime("%Y-%m-%d"))
        top_level.destroy()

# Check date on end date selected
def on_end_date_selected():
    selected_date = cal.selection_get()
    if selected_date > today:
        messagebox.showerror("Invalid Date", "You can't select a date later than today's date.")
        cal.selection_set(today)
    else:
        end_date_var.set(selected_date.strftime("%Y-%m-%d"))
        top_level.destroy()

# Calnder fot end Date
def open_end_calendar():
    global cal, top_level

    if 'top_level' in globals():
        top_level.destroy()
        
    top_level = Toplevel()
    top_level.wm_attributes('-topmost',True)
    cal = Calendar(top_level, selectmode='day', year=int(end_date_var.get()[:4]), month=int(end_date_var.get()[5:7]), day=int(end_date_var.get()[8:]))
    cal.pack(padx=20, pady=20)
    cal_button = Button(top_level, text="Select End Date", command=on_end_date_selected)
    cal_button.pack(pady=10)

# Calender for start date
def open_start_calendar():
    global cal, top_level
    
    if 'top_level' in globals():
        top_level.destroy()
        
    top_level = Toplevel()
    top_level.wm_attributes('-topmost',True)
    cal = Calendar(top_level, selectmode='day', year=int(start_date_var.get()[:4]), month=int(start_date_var.get()[5:7]), day=int(start_date_var.get()[8:]))
    cal.pack(padx=20, pady=20)
    cal_button = Button(top_level, text="Select Start Date", command=on_start_date_selected)
    cal_button.pack(pady=10)

# create menu for report 1 : tuple of all hotels with All option
def report1_create_menu():
    global menu
    
    cur.execute('Select hotel_name,address from hotel_details')
    
    hotels = cur.fetchall()
    menu = ['Select All']
    for name,address in hotels:
        menu.append(str(name+' | '+address))
    
# report 1 - hotel wise order count report
def report_1():
    
    global canvas23,report_button_image_4,report_button_image_3,report_button_image_2,report_button_image_1
    global today,start_date_var,end_date_var,dropdown_menu,menu
    
    admn_home_btn()
  
    canvas23 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas23.place(x = 0, y = 0)
    
    start_date_var = StringVar(canvas23)
    start_date_var.set("2024-01-01")

    end_date_var = StringVar(canvas23)
    today = datetime.today().date()
    end_date_var.set(today.strftime("%Y-%m-%d"))   
    
    report1_create_menu()
    
    dropdown_menu = ttk.Combobox(canvas23,width =120)
    dropdown_menu['values'] = menu
    dropdown_menu.current(0)
    dropdown_menu.place(x = 90, y= 63) 

    
    go_btn = Button(canvas23,
                    text = 'Go',
                    width = 15,
                    command = report_1_go_btn)
    go_btn.place(x = 840, y = 60)

    entry_1 = Entry(canvas23,
        textvariable=end_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=609.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    entry_2 = Entry(canvas23,
        textvariable=start_date_var,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=159.0,
        y=14.0,
        width=268.0,
        height=30.0
    )

    canvas23.create_text(
        99.0,
        22.0,
        anchor="nw",
        text="Start date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    canvas23.create_text(
        556.0,
        22.0,
        anchor="nw",
        text="End date",
        fill="#000000",
        font=("Inika", 12 * -1)
    )

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_26.png"))
    button_1 = Button(canvas23,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_start_calendar,
        relief="flat"
    )
    button_1.place(
        x=432.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_27.png"))
    button_2 = Button(canvas23,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_end_calendar,
        relief="flat"
    )
    button_2.place(
        x=882.0,
        y=11.0,
        width=33.0,
        height=35.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    button_3 = Button(canvas23,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    button_3.place(
        x=6.0,
        y=6.0,
        width=45.0,
        height=45.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    button_4 = Button(canvas23,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    button_4.place(
        x=963.0,
        y=6.0,
        width=32.0,
        height=41.0
    )

# view Reports btn
def view_reports():
    global report_button_image_1,report_button_image_2,report_button_image_3,report_button_image_4,report_button_image_5,report_button_image_6
    global canvas22

    admn_home_btn()

    canvas22 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 410,
        width = 920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas22.place(x = 37,y = 150)

    report_button_image_1 = PhotoImage(
        file=relative_to_assets8("button_20.png"))

    button_1 = Button(canvas22,
        image=report_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=report_3,
        relief="flat"
    )
    button_1.place(
        x=48.0,
        y=150.0,
        width=826.0,
        height=46.0
    )

    report_button_image_2 = PhotoImage(
        file=relative_to_assets8("button_21.png"))
    button_2 = Button(canvas22,
        image=report_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=report_4,
        relief="flat"
    )
    button_2.place(
        x=48.0,
        y=209.0,
        width=826.0,
        height=46.0
    )

    report_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_22.png"))
    button_3 = Button(canvas22,
        image=report_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=report_6,
        relief="flat"
    )
    button_3.place(
        x=48.0,
        y=326.0,
        width=826.0,
        height=46.0
    )

    report_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_23.png"))
    button_4 = Button(canvas22,
        image=report_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=report_5,
        relief="flat"
    )
    button_4.place(
        x=48.0,
        y=267.0,
        width=826.0,
        height=46.0
    )

    report_button_image_5 = PhotoImage(
        file=relative_to_assets8("button_24.png"))
    button_5 = Button(canvas22,
        image=report_button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=report_1,
        relief="flat"
    )
    button_5.place(
        x=48.0,
        y=34.0,
        width=826.0,
        height=46.0
    )

    report_button_image_6 = PhotoImage(
        file=relative_to_assets8("button_25.png"))
    button_6 = Button(canvas22,
        image=report_button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=report_2,
        relief="flat"
    )
    button_6.place(
        x=48.0,
        y=93.0,
        width=826.0,
        height=46.0
    )

# create category string 
def create_category_str():
    global Category_String
    Category_String = ''
    
    if breakfast :
        Category_String+='breakfast'+'/'
    if lunch:
        Category_String+='lunch'+'/'
    if dinner:
        Category_String+='dinner'+'/'
    if chaat:
        Category_String+='chaat'+'/'
    if beverage:
        Category_String+='beverage'+'/'
        
    Category_String = Category_String[:-1]

# sql add new Item 
def sql_admn_add_new_item():
    query = 'insert into items (Item_Name, BasePrice,category,IsDeleted ) values (%s,%s,%s,%s)'
    update_tuple = (admn_edit_itemname,admn_edit_itembaseprice,Category_String,'False')
    cur.execute(query,update_tuple)
    
    con.commit()
   
    messagebox.showinfo('New Item','New Item Added !')
    
    manage_items()    

# Sql Update hotel details 
def sql_update_admn_edit_item(itemid):
    query = 'update items set Item_Name = %s, BasePrice = %s ,category = %s,IsDeleted = %s where itemid = %s '
    update_tuple = (admn_edit_itemname,admn_edit_itembaseprice,Category_String,Item_inactive,itemid)
    cur.execute(query,update_tuple)
    con.commit()
    
    messagebox.showinfo('Item Update','Changes Made !')
    
    manage_items()

# get edit item values 
def get_edit_item_values():
    global admn_edit_itemname,admn_edit_itembaseprice
    
    admn_edit_itemname = admn_itm_entry_1.get()
    admn_edit_itembaseprice = admn_itm_entry_2.get()

# Validate Add New Item values - Admin canvas
def validate_admn_add_item():   
    
    get_edit_item_values()
    
    cur.execute("select item_name,baseprice,itemid from items where item_name = %s ",(admn_edit_itemname,))
    try :
        (itemname,baseprice,Item_Id) = cur.fetchone()
        unique = False
    except :
        unique = True
        
    if admn_edit_itemname == '': #Ckecking htlname if it's an empty String
        messagebox.showerror('Item Name Error','Enter a Valid Item Name')
        admn_itm_entry_1.delete(0,'end')
        
    elif unique == False:
        # checking whether the admin didn't change name or address 
        messagebox.showerror('Item Error','Item Already Exists')
        admn_itm_entry_1.delete(0,'end')
        
    else :
        #As hotelname is now unique, Ckecking the length of hotelname 
        if validatelen(admn_edit_itemname,2,30): 
            if validateint(admn_edit_itembaseprice,'Item Base Price'):
                # validate category
                if validatecategory():
                   sql_admn_add_new_item()
            else :
                admn_itm_entry_2.delete(0,'end')                             
        else :
            messagebox.showwarning('Item Name Warning',"Item Name must contain minimum 2 and not more than 30 characters !")
            admn_itm_entry_1.delete(0,'end')      

# validate item edit - admin canvas
def validate_admn_edit_item(itemid):
    get_edit_item_values()
    
    cur.execute("select item_name,baseprice,itemid from items where item_name = %s ",(admn_edit_itemname,))
    try :
        (itemname,baseprice,Item_Id) = cur.fetchone()
        unique = False
    except :
        unique = True
        
    if admn_edit_itemname == '': #Ckecking htlname if it's an empty String
        messagebox.showerror('Item Name Error','Enter a Valid Item Name')
        admn_itm_entry_1.delete(0,'end')
        
    elif unique == False and  itemid != Item_Id:
        # checking whether the admin didn't change name or address 
        messagebox.showerror('Item Error','Item Already Exists')
        admn_itm_entry_1.delete(0,'end')
        
    else :
        #As hotelname is now unique, Ckecking the length of hotelname 
        if validatelen(admn_edit_itemname,2,30): 
            if validateint(admn_edit_itembaseprice,'Item Base Price'):
                # validate category
                if validatecategory():
                   sql_update_admn_edit_item(itemid)
            else :
                admn_itm_entry_2.delete(0,'end')                             
        else :
            messagebox.showwarning('Item Name Warning',"Item Name must contain minimum 2 and not more than 30 characters !")
            admn_itm_entry_1.delete(0,'end')  

# Validate category Checkboxes
def validatecategory():
    global breakfast,lunch,dinner,chaat,beverage
    
    breakfast = admn_itm_sv_breakfast.get()
    lunch = admn_itm_sv_lunch.get()
    dinner = admn_itm_sv_dinner.get()
    chaat = admn_itm_sv_chaat.get() 
    beverage = admn_itm_sv_beverage.get() 

    if breakfast or lunch or dinner:
        food = 1
    else : 
        food = 0
    
    if (food and beverage) or (chaat and beverage) or (food and chaat):
        messagebox.showerror('Category Error','Invalid combination of Item Category !')
        return False
    elif not(food or beverage or chaat):
        messagebox.showerror('Category Error','Choose appropriate Item Category !')
        return False
    else :
        create_category_str()
        return True        
  
# Button Click Event - Delete Item
def delete_item():
    global Item_inactive
    Item_inactive = 'True'
    item_status()

# Button Click Event - Delete Item
def enable_item(): 
    global Item_inactive
    Item_inactive = 'False'
    item_status()
    
# Item Status - Correcponding Buttons :
def item_status():
    global del_itm_img,enable_itm_img
    
    if Item_inactive == 'False':
        del_itm_img = PhotoImage(
            file=relative_to_assets8("button_16.png"))
        del_itm_btn = Button(canvas19,
            image=del_itm_img,
            borderwidth=0,
            highlightthickness=0,
            command=delete_item,
            relief="flat"
        )
        del_itm_btn.place(
            x=151.0,
            y=354.0,
        )
    else :
        
        enable_itm_img = PhotoImage(
            file=relative_to_assets8("button_17.png"))
        enable_itm_btn = Button(canvas19,
            image=enable_itm_img,
            borderwidth=0,
            highlightthickness=0,
            command=enable_item,
            relief="flat"
        )
        enable_itm_btn.place(
            x=151.0,
            y=355.0,
        )
        
#set Item strvar 
def set_admn_item_edit_strvar(itemid):
    
    global admn_itm_svname,admn_itm_svbaseprice,admn_itm_sv_breakfast,admn_itm_sv_lunch,admn_itm_sv_dinner,admn_itm_sv_chaat,admn_itm_sv_beverage
    global Item_inactive
    
    cur.execute('select item_name,baseprice,category,isdeleted from items where itemid = %s',(itemid,))
    item_details = cur.fetchone()
     
    Item_inactive =  item_details[-1]

    # String Variables for Text extries
    admn_itm_svname = StringVar(window)
    admn_itm_svbaseprice = StringVar(window)
    
    # Int Variables for Checkboxes
    admn_itm_sv_breakfast = IntVar(window)
    admn_itm_sv_lunch = IntVar(window)
    admn_itm_sv_dinner = IntVar(window)
    admn_itm_sv_chaat = IntVar(window)
    admn_itm_sv_beverage = IntVar(window)
    
    # assigning Strin/Int variables
    admn_itm_svname.set(item_details[0])
    admn_itm_svbaseprice.set(item_details[1])
    
    Category_List = item_details[2].split('/')
    
    for i in Category_List :
        if i == 'breakfast' :
            admn_itm_sv_breakfast.set(1)
        elif i == 'lunch':
            admn_itm_sv_lunch.set(1)
        elif i == 'dinner':
            admn_itm_sv_dinner.set(1)
        elif i == 'chaat':
            admn_itm_sv_chaat.set(1)
        elif i == 'beverage':
            admn_itm_sv_beverage.set(i)
        else:
            pass

# set null intvar for checkbox - add item
def set_admn_add_item_intvar():
    global admn_itm_sv_breakfast,admn_itm_sv_lunch,admn_itm_sv_dinner,admn_itm_sv_chaat,admn_itm_sv_beverage  
    # Int Variables for Checkboxes
    admn_itm_sv_breakfast = IntVar(window)
    admn_itm_sv_lunch = IntVar(window)
    admn_itm_sv_dinner = IntVar(window)
    admn_itm_sv_chaat = IntVar(window)
    admn_itm_sv_beverage = IntVar(window)   
    
# Admin - Add Item - Btn Click Event 
def add_item():
    
    global canvas21,bg_image_1,cancel_btn_img,save_btn_img
    global admn_itm_entry_1,admn_itm_entry_2
    
    admn_home_btn()
    
    set_admn_add_item_intvar()
    
    canvas21 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 410,
        width = 920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas21.place(x = 37,y = 150)


    admn_itm_entry_1 = Entry(canvas21,
        bd=0,
        font = ('Inka',16),
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    admn_itm_entry_1.place(
        x=133.0,
        y=97.0,
        width=351.0,
        height=53.0
    )


    admn_itm_entry_2 = Entry(canvas21,
        bd=0,
        font = ('Inka',16),
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    admn_itm_entry_2.place(
        x=133.0,
        y=227.0,
        width=350.0,
        height=52.0
    )

    breakfast_checkbtn = Checkbutton(canvas21,
                                     variable = admn_itm_sv_breakfast)
    breakfast_checkbtn.place(x = 585, y = 75)
    
    lunch_checkbtn = Checkbutton(canvas21,
                                     variable = admn_itm_sv_lunch)
    lunch_checkbtn.place(x = 585, y = 125) 
    
    dinner_checkbtn = Checkbutton(canvas21,
                                     variable = admn_itm_sv_dinner)
                                  
    dinner_checkbtn.place(x = 585, y = 175)  
    
    chaat_checkbtn = Checkbutton(canvas21,
                                     variable = admn_itm_sv_chaat)
                                 
    chaat_checkbtn.place(x = 585, y = 225)
    
    beverage_checkbtn = Checkbutton(canvas21,
                                     variable = admn_itm_sv_beverage)
                                    
    beverage_checkbtn.place(x = 585, y = 280)
    

    #cancel Button
    cancel_btn_img = PhotoImage(
        file=relative_to_assets8("button_19.png"))
    cancel_itm_btn = Button(canvas21,
        image=cancel_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=manage_items,
        relief="flat"
    )
    cancel_itm_btn.place(
        x=536.0706787109375,
        y=358.28521728515625    
    )
    # SAVE Button
    save_btn_img = PhotoImage(
        file=relative_to_assets8("button_18.png"))
    save_itm_btn = Button(canvas21,
        image=save_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=validate_admn_add_item,
        relief="flat"
    )
    save_itm_btn.place(
        x=667.4732055664062,
        y=355.9932861328125
    )
    bg_image_1 = PhotoImage(
        file=relative_to_assets8("bg_image_1.png"))
    image_1 = canvas21.create_image(
        657.0,
        191.0,
        image=bg_image_1
    )

    canvas21.create_text(
        134.0,
        74.0,
        anchor="nw",
        text="Item Name",
        fill="#000000",
        font=("Inika", 19 * -1)
    )

    canvas21.create_text(
        133.0,
        204.0,
        anchor="nw",
        text="Base Price",
        fill="#000000",
        font=("Inika", 19 * -1)
    )
    canvas21.create_text(
        617.0,
        15.0,
        anchor="nw",
        text="Category",
        fill="#000000",
        font=("Inika", 19 * -1)
    )



    canvas21.create_text(
        619.0,
        70.0,
        anchor="nw",
        text="Breakfast",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas21.create_text(
        618.0,
        120.0,
        anchor="nw",
        text="Lunch",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas21.create_text(
        617.0,
        171.0,
        anchor="nw",
        text="Dinner",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas21.create_text(
        619.0,
        222.0,
        anchor="nw",
        text="Chaat",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas21.create_text(
        617.0,
        273.0,
        anchor="nw",
        text="Beverage",
        fill="#000000",
        font=("Inika", 26 * -1)
    )
         
#  Admin - Edit Item - Button Click Event
def edit_item(itemid):
    
    global canvas19,bg_image_1,cancel_btn_img,save_btn_img
    global admn_itm_entry_1,admn_itm_entry_2
    
    admn_home_btn()
    
    set_admn_item_edit_strvar(itemid)
    
    canvas19 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 410,
        width = 920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas19.place(x = 37,y = 150)

    item_status()


    admn_itm_entry_1 = Entry(canvas19,
        bd=0,
        textvariable= admn_itm_svname,
        font = ('Inka',16),
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    admn_itm_entry_1.place(
        x=133.0,
        y=97.0,
        width=351.0,
        height=53.0
    )


    admn_itm_entry_2 = Entry(canvas19,
        bd=0,
        textvariable=admn_itm_svbaseprice,
        font = ('Inka',16),
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    admn_itm_entry_2.place(
        x=133.0,
        y=227.0,
        width=350.0,
        height=52.0
    )

    breakfast_checkbtn = Checkbutton(canvas19,
                                     variable = admn_itm_sv_breakfast)
    breakfast_checkbtn.place(x = 585, y = 75)
    
    lunch_checkbtn = Checkbutton(canvas19,
                                     variable = admn_itm_sv_lunch)
    lunch_checkbtn.place(x = 585, y = 125) 
    
    dinner_checkbtn = Checkbutton(canvas19,
                                     variable = admn_itm_sv_dinner)
                                  
    dinner_checkbtn.place(x = 585, y = 175)  
    
    chaat_checkbtn = Checkbutton(canvas19,
                                     variable = admn_itm_sv_chaat)
                                 
    chaat_checkbtn.place(x = 585, y = 225)
    
    beverage_checkbtn = Checkbutton(canvas19,
                                     variable = admn_itm_sv_beverage)
                                    
    beverage_checkbtn.place(x = 585, y = 280)
    

    #cancel Button
    cancel_btn_img = PhotoImage(
        file=relative_to_assets8("button_19.png"))
    cancel_itm_btn = Button(canvas19,
        image=cancel_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=manage_items,
        relief="flat"
    )
    cancel_itm_btn.place(
        x=536.0706787109375,
        y=358.28521728515625    
    )
    # SAVE Button
    save_btn_img = PhotoImage(
        file=relative_to_assets8("button_18.png"))
    save_itm_btn = Button(canvas19,
        image=save_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda i = itemid: validate_admn_edit_item(i),
        relief="flat"
    )
    save_itm_btn.place(
        x=667.4732055664062,
        y=355.9932861328125
    )
    bg_image_1 = PhotoImage(
        file=relative_to_assets8("bg_image_1.png"))
    image_1 = canvas19.create_image(
        657.0,
        191.0,
        image=bg_image_1
    )

    canvas19.create_text(
        134.0,
        74.0,
        anchor="nw",
        text="Item Name",
        fill="#000000",
        font=("Inika", 19 * -1)
    )

    canvas19.create_text(
        133.0,
        204.0,
        anchor="nw",
        text="Base Price",
        fill="#000000",
        font=("Inika", 19 * -1)
    )
    canvas19.create_text(
        617.0,
        15.0,
        anchor="nw",
        text="Category",
        fill="#000000",
        font=("Inika", 19 * -1)
    )



    canvas19.create_text(
        619.0,
        70.0,
        anchor="nw",
        text="Breakfast",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas19.create_text(
        618.0,
        120.0,
        anchor="nw",
        text="Lunch",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas19.create_text(
        617.0,
        171.0,
        anchor="nw",
        text="Dinner",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas19.create_text(
        619.0,
        222.0,
        anchor="nw",
        text="Chaat",
        fill="#000000",
        font=("Inika", 26 * -1)
    )

    canvas19.create_text(
        617.0,
        273.0,
        anchor="nw",
        text="Beverage",
        fill="#000000",
        font=("Inika", 26 * -1)
    )
 
# manage Items canas in Admin canvas
def manage_items():
    global edit_btn_image,canvas18,scrollbar7
    
    admn_home_btn()
    

    canvas18 = Canvas(window,highlightthickness=0,height = 410,width = 920,bg ='#FFFFFF',borderwidth=0)
    canvas18.place(x = 37,y = 150)
  

    #Creating scrollbar
    scrollbar7 = Scrollbar(window,command=canvas18.yview)
    scrollbar7.place(x=947, y=150)
    scrollbar7.place(height=410)
   
    # Creating Frame
    frame9 = Frame(canvas18, width=925, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas18.configure(yscrollcommand=scrollbar7.set)
    canvas18.bind('<Configure>', lambda e: canvas18.configure(scrollregion=canvas18.bbox("all")))
    
    edit_btn_image = PhotoImage(
        file = relative_to_assets8('button_6.png'))
    
    cur.execute('select item_name,category,isdeleted,itemid from items order by itemid desc ')
    items = cur.fetchall() # List of Tuples 
    
    window_height = 50*len(items) +110
    canvas18.create_window((0, 0),   
                     height =window_height,
                     width=920,
                     window=frame9,
                     anchor='nw')
    Ycoor = 10
    for itemname,category,isdeleted ,itemid in items :
        
        if Ycoor == 10 :
            New_htl_btn = Button(frame9,
                                 command = add_item,
                                 font = ('Inika',16),
                                 text = ' + New Item')
            New_htl_btn.place(x = 30, y = Ycoor)
            Ycoor+=60
         
        Foreground = '#000000'
        Font = ('Inika',18)
                 
        Foreground = '#000000'
        Font = ('Inika',18)
            
        if isdeleted == 'True':
            Foreground = '#7D7D7D'
            Font = strikethrough_font
            status = 'Inactive'
        else :
            status = 'Active'
        
        if len(itemname)>15:
            itemname = itemname[:13]+'...'
        if len(category)>20:
            category = category[:18]+'...'
        
        label1 = Label(frame9,bg ='#FFFFFF',font = Font,foreground= Foreground, text =itemname,anchor=CENTER)
        label1.place(x = 30,y = Ycoor)
        
        label2 = Label(frame9,bg ='#FFFFFF',font = Font,foreground= Foreground, text =category)
        label2.place(x = 350,y = Ycoor)
        
        label3 = Label(frame9,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =status)
        label3.place(x = 700,y = Ycoor)
        
        btn = Button(frame9,bg ='#FFFFFF',image = edit_btn_image,borderwidth=0,command = lambda i = itemid:edit_item(i))
        btn.place(x = 850,y = Ycoor)

        Ycoor += 50    

# Update Sql values for Edit hotel in Admin Canvas
def admin_update_hotel_details(hotelid):
    query = "Update hotel_details set Hotel_name = %s,Address = %s,City = %s,state = %s,pricepercent = %s,taxpercent = %s,isdeleted = %s where hotelid = %s"
    value_tuple = (admn_edit_htlname,admn_edit_htladdress,admn_edit_htlcity,admn_edit_htlstate,admn_edit_htlpricepercent,admn_edit_htltaxpercent,Hotel_Inactive,hotelid)
    cur.execute(query,value_tuple)
    
    con.commit()
    
    messagebox.showinfo('Hotel Update','Changes made !')
    manage_hotels()

# Set Sql values for New Hotel Creation 
def admin_add_hotel():
    query = "insert into hotel_details (Hotel_name,Address,City,state,pricepercent,taxpercent,isdeleted) values (%s,%s,%s,%s,%s,%s,'False')"
    value_tuple = (admn_edit_htlname,admn_edit_htladdress,admn_edit_htlcity,admn_edit_htlstate,admn_edit_htlpricepercent,admn_edit_htltaxpercent)
    
    cur.execute(query,value_tuple)
    
    con.commit()
    
    messagebox.showinfo('Add New Hotel','Hotel Registered Successfully !')
    
    manage_hotels()
    
# button CLick event - Delete Hotel in Admin canvas
def delete_hotel():
    global Hotel_Inactive 
    Hotel_Inactive = 'True'
    hotel_status()

# button CLick event - Delete Hotel in Admin canvas
def enable_hotel():
    global Hotel_Inactive
    Hotel_Inactive = 'False'
    hotel_status()
    
#Update Hotel Status - Correcponding buttons 
def hotel_status():
    global htl_button_image_1,htl_button_image_2,del_htl_btn
    global Hotel_Inactive 
    
    if "del_htl_btn" in globals() :
        del_htl_btn.destroy()
    if "enable_htl_btn" in globals():
        enable_htl_btn.destroy()
        
    if Hotel_Inactive == 'False' :
        # Delete Button
        htl_button_image_1 = PhotoImage(
            file=relative_to_assets8("button_13.png"))
        del_htl_btn = Button(canvas17,
            image=htl_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=delete_hotel,
            relief="flat"
        )
        del_htl_btn.place(
            x=36.0,
            y=351.0,
            width=163.0,
            height=27.84583282470703
        )
    else :
        # Enable Hotel Button
        htl_button_image_2 = PhotoImage(
            file=relative_to_assets8("button_14.png"))
        enable_htl_btn = Button(canvas17,
            image=htl_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=enable_hotel,
            relief="flat"
        )
        enable_htl_btn.place(
            x=36.0,
            y=351.0,
            width=163.0,
            height=27.84583282470703
        )
    
#fetch Edit - Hotel details from sql
def sqlfetch_edit_htl(hotelid):
    global htl_details , Hotel_Inactive
    
    cur.execute('select Hotel_Name,Address,City,state,pricepercent,taxpercent,isdeleted from hotel_details where hotelid = %s',(hotelid,))
    htl_details = cur.fetchone()
    Hotel_Inactive = htl_details[-1]
    
# set string var for admin edit hotel 
def admin_hotel_setstrvar():
    global admn_svhtlname,admn_svhtladdress,admn_svhtlcity,admn_svhtlstate,admn_svhtlpricepercent,admn_svhtltaxpercent
    # create String variables
    admn_svhtlname          = StringVar(window)
    admn_svhtladdress       = StringVar(window)
    admn_svhtlcity          = StringVar(window)
    admn_svhtlstate         = StringVar(window)
    admn_svhtlpricepercent  = StringVar(window)
    admn_svhtltaxpercent    = StringVar(window)
    
    # set string Variables
    
    admn_svhtlname.set(htl_details[0])
    admn_svhtladdress.set(htl_details[1])
    admn_svhtlcity.set(htl_details[2])
    admn_svhtlstate.set(htl_details[3])
    admn_svhtlpricepercent.set(htl_details[4])
    admn_svhtltaxpercent.set(htl_details[5])

# get admin entered values - edit hotel
def get_edit_hotel_values():
    
    global admn_edit_htlname , admn_edit_htladdress,admn_edit_htlcity,admn_edit_htlstate,admn_edit_htlpricepercent,admn_edit_htltaxpercent 
    
    admn_edit_htlname = htl_entry_1.get()
    admn_edit_htladdress = htl_entry_2.get("1.0", "end-1c")
    admn_edit_htlcity = htl_entry_3.get()
    admn_edit_htlstate  = htl_entry_4.get()
    admn_edit_htlpricepercent  = htl_entry_5.get()
    admn_edit_htltaxpercent = htl_entry_6.get()

# Validate integer values 
def validateint(string,arg):
    try :
        integer = int(string)
        return True
    except:
        text = arg + ' can only take up valid integer values'
        messagebox.showerror('Value Error',text)
        
        return False

# Validate Admin - Add hotel Values 
def validate_admin_add_hotel():
    get_edit_hotel_values()
    
    cur.execute("select hotel_name,address,hotelid from hotel_details where hotel_name = %s ",(admn_edit_htlname,))
    try :
        (htlname,htladdress,htl_id) = cur.fetchone()
        unique = False
    except :
        unique = True
        
    if admn_edit_htlname == '': #Ckecking htlname if it's an empty String
        messagebox.showerror('Hotel Name Error','Enter a Valid Hotel Name')
        htl_entry_1.delete(0,'end')
        
    elif unique == False and  admn_edit_htladdress == htladdress:
        # checking whether the admin didn't change name or address 
        messagebox.showerror('Hotel Error','Hotel Already Exists')
        htl_entry_1.delete(0,'end')
        htl_entry_2.delete('1.0','end')
        
    else :
        #As hotelname is now unique, Ckecking the length of hotelname 
        if validatelen(admn_edit_htlname,5,30):
            if validatelen(admn_edit_htladdress,1,200):#validate address
                if validatelen(admn_edit_htlcity,1,30) and validatename(admn_edit_htlcity,'city'):#validate City
                    if validatelen(admn_edit_htlstate,1,30) and validatename(admn_edit_htlstate,'state'): #validate state
                        if validateint(admn_edit_htlpricepercent,'Price Percent'):
                            if validateint(admn_edit_htltaxpercent,'Tax Percent'):
                                # Update to sql table 
                                admin_add_hotel()
                            else:
                                htl_entry_6.delete(0,'end')
                        else :
                            htl_entry_5.delete(0,'end')                             
                    else:
                        messagebox.showwarning('State Error','State field should ONLY contain letters and spaces and should not exceed 30 characters')
                        htl_entry_4.delete(0,'end')                                                   
                else:
                    messagebox.showwarning('City Error','City field should ONLY contain letters and spaces and should not exceed 30 characters')
                    htl_entry_3.delete(0,'end')
            else:
                messagebox.showerror('Address Error','Address field should not be empty and should not exceed 200 characters')
                htl_entry_2.delete('1.0','end')
        else :
            messagebox.showwarning('Hotel Name Warning',"Hotel Name must contain minimum 5 and not more than 30 characters !")
            htl_entry_1.delete(0,'end')        

# validate Admin - Edit Hotel Details Values - btn click event - save hotel edit - admin canvas
def valivdate_admin_edit_hotels(hotelid):
    get_edit_hotel_values()
    
    cur.execute("select hotel_name,address,hotelid from hotel_details where hotel_name = %s ",(admn_edit_htlname,))
    try :
        (htlname,htladdress,htl_id) = cur.fetchone()
        unique = False
    except :
        unique = True
        
    if admn_edit_htlname == '': #Ckecking htlname if it's an empty String
        messagebox.showerror('Hotel Name Error','Enter a Valid Hotel Name')
        htl_entry_1.delete(0,'end')
        
    elif unique == False and  hotelid != htl_id and admn_edit_htladdress == htladdress:
        # checking whether the admin didn't change name or address 
        messagebox.showerror('Hotel Error','Hotel Already Exists')
        htl_entry_1.delete(0,'end')
        htl_entry_2.delete('1.0','end')
        
    else :
        #As hotelname is now unique, Ckecking the length of hotelname 
        if validatelen(admn_edit_htlname,5,30):
            if validatelen(admn_edit_htladdress,1,200):#validate address
                if validatelen(admn_edit_htlcity,1,30) and validatename(admn_edit_htlcity,'city'):#validate City
                    if validatelen(admn_edit_htlstate,1,30) and validatename(admn_edit_htlstate,'state'): #validate state
                        if validateint(admn_edit_htlpricepercent,'Price Percent'):
                            if validateint(admn_edit_htltaxpercent,'Tax Percent'):
                                # Update to sql table 
                                admin_update_hotel_details(hotelid)
                            else:
                                htl_entry_6.delete(0,'end')
                        else :
                            htl_entry_5.delete(0,'end')                             
                    else:
                        messagebox.showwarning('State Error','State field should ONLY contain letters and spaces and should not exceed 30 characters')
                        htl_entry_4.delete(0,'end')                                                   
                else:
                    messagebox.showwarning('City Error','City field should ONLY contain letters and spaces and should not exceed 30 characters')
                    htl_entry_3.delete(0,'end')
            else:
                messagebox.showerror('Address Error','Address field should not be empty and should not exceed 200 characters')
                htl_entry_2.delete('1.0','end')
        else :
            messagebox.showwarning('Hotel Name Warning',"Hotel Name must contain minimum 5 and not more than 30 characters !")
            htl_entry_1.delete(0,'end')    
            
# Edit Hotel Canvas - Button Click event - edit hotel in admin canvas    
def edit_hotel(hotelid):
    global canvas17,htl_button_image_3,htl_button_image_4
    global htl_entry_1,htl_entry_2,htl_entry_3,htl_entry_4,htl_entry_5,htl_entry_6
   
    sqlfetch_edit_htl(hotelid)
    admin_hotel_setstrvar()
    
    admn_home_btn()
  
    Font = ('Inika',14)
    
    canvas17 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 410,
        width = 925,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas17.place(x = 37,y = 150)
   
    hotel_status()

    htl_entry_1 = Entry(canvas17,
        bd=0,
        font = Font ,
        bg="#D9D9D9",
        textvariable= admn_svhtlname,
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_1.place(
        x=27.0,
        y=52.0,
        width=403.0,
        height=36.0
    )

    htl_entry_2 = Text(canvas17,
        bd=0,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_2.insert('1.0', admn_svhtladdress.get())
    htl_entry_2.place(
        x=30.0,
        y=138.0,
        width=403.0,
        height=190.0
    )
    
    htl_entry_3 = Entry(canvas17,
        bd=0,
        textvariable = admn_svhtlcity,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_3.place(
        x=493.0,
        y=52.0,
        width=403.0,
        height=36.0
    )

    htl_entry_4 = Entry(canvas17,
        bd=0,
        textvariable = admn_svhtlstate,
        bg="#D9D9D9",
        font = Font ,
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_4.place(
        x=490.0,
        y=138.0,
        width=403.0,
        height=36.0
    )
    htl_entry_5 = Entry(canvas17,
        bd=0,
        textvariable = admn_svhtlpricepercent,
        bg="#D9D9D9",
        font = Font ,
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_5.place(
        x=493.0,
        y=217.0,
        width=403.0,
        height=36.0
    )

    htl_entry_6 = Entry(canvas17,
        bd=0,
        textvariable = admn_svhtltaxpercent,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_6.place(
        x=493.0,
        y=292.0,
        width=403.0,
        height=36.0
    )

    canvas17.create_text(
        27.0,
        30.0,
        anchor="nw",
        text="Hotel Name",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas17.create_text(
        33.0,
        112.0,
        anchor="nw",
        text="Hotel Address",
        fill="#000000",
        font=("Inika", 17 * -1)
    )



    canvas17.create_text(
        496.0,
        30.0,
        anchor="nw",
        text="City\n",
        fill="#000000",
        font=("Inika", 17 * -1)
    )


    canvas17.create_text(
        493.0,
        116.0,
        anchor="nw",
        text="State",
        fill="#000000",
        font=("Inika", 17 * -1)
    )


    canvas17.create_text(
        496.0,
        195.0,
        anchor="nw",
        text="Item Price - Percent (%)",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas17.create_text(
        496.0,
        270.0,
        anchor="nw",
        text="Tax Percent (%)",
        fill="#000000",
        font=("Inika", 17 * -1)
    )


    # save Button
    htl_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_12.png"))
    button_3 = Button(canvas17,
        image=htl_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda h = hotelid: valivdate_admin_edit_hotels(h),
        relief="flat"
    )
    button_3.place(
        x=729.0,
        y=353.0,
        width=163.0,
        height=27.84583282470703
    )

    #cancel Button
    htl_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_10.png"))
    button_4 = Button(canvas17,
        image=htl_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=manage_hotels,
        relief="flat"
    )
    button_4.place(
        x=546.0,
        y=353.0,
        width=163.0,
        height=27.84583282470703
    )

# Add New Hotel
def add_hotel():
    global canvas20,htl_button_image_3,htl_button_image_4
    global htl_entry_1,htl_entry_2,htl_entry_3,htl_entry_4,htl_entry_5,htl_entry_6
   
    
    admn_home_btn()
  
    Font = ('Inika',14)
    
    canvas20 = Canvas(
        window,
        bg = "#FFFFFF",
        height = 410,
        width = 925,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas20.place(x = 37,y = 150)
   

    htl_entry_1 = Entry(canvas20,
        bd=0,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_1.place(
        x=27.0,
        y=52.0,
        width=403.0,
        height=36.0
    )

    htl_entry_2 = Text(canvas20,
        bd=0,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_2.place(
        x=30.0,
        y=138.0,
        width=403.0,
        height=190.0
    )
    
    htl_entry_3 = Entry(canvas20,
        bd=0,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_3.place(
        x=493.0,
        y=52.0,
        width=403.0,
        height=36.0
    )

    htl_entry_4 = Entry(canvas20,
        bd=0,
        bg="#D9D9D9",
        font = Font ,
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_4.place(
        x=490.0,
        y=138.0,
        width=403.0,
        height=36.0
    )
    htl_entry_5 = Entry(canvas20,
        bd=0,
        bg="#D9D9D9",
        font = Font ,
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_5.place(
        x=493.0,
        y=217.0,
        width=403.0,
        height=36.0
    )

    htl_entry_6 = Entry(canvas20,
        bd=0,
        font = Font ,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    htl_entry_6.place(
        x=493.0,
        y=292.0,
        width=403.0,
        height=36.0
    )

    canvas20.create_text(
        27.0,
        30.0,
        anchor="nw",
        text="Hotel Name",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas20.create_text(
        33.0,
        112.0,
        anchor="nw",
        text="Hotel Address",
        fill="#000000",
        font=("Inika", 17 * -1)
    )



    canvas20.create_text(
        496.0,
        30.0,
        anchor="nw",
        text="City\n",
        fill="#000000",
        font=("Inika", 17 * -1)
    )


    canvas20.create_text(
        493.0,
        116.0,
        anchor="nw",
        text="State",
        fill="#000000",
        font=("Inika", 17 * -1)
    )


    canvas20.create_text(
        496.0,
        195.0,
        anchor="nw",
        text="Item Price - Percent (%)",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas20.create_text(
        496.0,
        270.0,
        anchor="nw",
        text="Tax Percent (%)",
        fill="#000000",
        font=("Inika", 17 * -1)
    )


    # save Button
    htl_button_image_3 = PhotoImage(
        file=relative_to_assets8("button_12.png"))
    button_3 = Button(canvas20,
        image=htl_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=validate_admin_add_hotel,
        relief="flat"
    )
    button_3.place(
        x=729.0,
        y=353.0,
        width=163.0,
        height=27.84583282470703
    )

    #cancel Button
    htl_button_image_4 = PhotoImage(
        file=relative_to_assets8("button_10.png"))
    button_4 = Button(canvas20,
        image=htl_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=manage_hotels,
        relief="flat"
    )
    button_4.place(
        x=546.0,
        y=353.0,
        width=163.0,
        height=27.84583282470703
    )

# Manage Hotels Canvas in Admin canvas
def manage_hotels():
    
    global edit_btn_image,canvas16,scrollbar6
    
    admn_home_btn()
    

    canvas16 = Canvas(window,highlightthickness=0,height = 410,width = 920,bg ='#FFFFFF',borderwidth=0)
    canvas16.place(x = 37,y = 150)
  

    #Creating scrollbar
    scrollbar6 = Scrollbar(window,command=canvas16.yview)
    scrollbar6.place(x=947, y=150)
    scrollbar6.place(height=410)
   
    # Creating Frame
    frame8 = Frame(canvas16, width=925, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas16.configure(yscrollcommand=scrollbar6.set)
    canvas16.bind('<Configure>', lambda e: canvas16.configure(scrollregion=canvas16.bbox("all")))
    edit_btn_image = PhotoImage(
        file = relative_to_assets8('button_6.png'))
    
    cur.execute('select hotel_name,address,isdeleted,HotelId from hotel_details  order by hotelid desc')
    hotels = cur.fetchall() # List of Tuples 
    
    window_height = 50*len(hotels) + 110
    canvas16.create_window((0, 0),   
                     height =window_height,
                     width=920,
                     window=frame8,
                     anchor='nw')
    Ycoor = 10
    for hotelname,address,isdeleted ,hotelid in hotels :
        
        if Ycoor == 10 :
            New_htl_btn = Button(frame8,
                                 command = add_hotel,
                                 font = ('Inika',16),
                                 text = ' + New Hotel')
            New_htl_btn.place(x = 30, y = Ycoor)
            Ycoor+=60
         
        Foreground = '#000000'
        Font = ('Inika',18)
            
        if isdeleted == 'True':
            Foreground = '#7D7D7D'
            Font = strikethrough_font
            status = 'Inactive'
        else :
            status = 'Active'
        
        if len(hotelname)>15:
            hotelname = hotelname[:13]+'...'
        if len(address)>20:
            address = address[:18]+'...'
        
        label1 = Label(frame8,bg ='#FFFFFF',font = Font,foreground= Foreground, text =hotelname,anchor=CENTER)
        label1.place(x = 30,y = Ycoor)
        
        label2 = Label(frame8,bg ='#FFFFFF',font = Font,foreground= Foreground, text =address)
        label2.place(x = 350,y = Ycoor)
        
        label3 = Label(frame8,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =status)
        label3.place(x = 700,y = Ycoor)
        
        btn = Button(frame8,bg ='#FFFFFF',image = edit_btn_image,borderwidth=0,command = lambda h = hotelid:edit_hotel(h))
        btn.place(x = 850,y = Ycoor)

        Ycoor += 50

# Button Click Event - Save  in edit user details 
def admn_save_user_edits(custid):
    get_admin_edit_user_values()
    if validate_admin_edit_user_detaisl(custid):
        query = " Update personal_details set Name=%s,PhoneNo=%s,EmailId=%s,Address=%s,City=%s,state=%s  where custid = %s "
        Update_tuple = (adm_edit_name,adm_edit_phno,adm_edit_emailaddress,adm_edit_address,adm_edit_city,adm_edit_state,custid)
        cur.execute(query,Update_tuple)
        cur.execute('update login_credentials set password = %s,username = %s,is_admin = %s, isdeleted = %s where custid = %s',(adm_edit_password,adm_edit_username,admin,inactive,custid))
        con.commit()
        edit_user(custid)
        messagebox.showinfo('User Information','Changes Done !')
        manage_users()

#Get Admin- Edit users  Page Values :
def get_admin_edit_user_values():
    # put the variables as global
    global adm_edit_name,adm_edit_phno,adm_edit_emailaddress,adm_edit_address,adm_edit_username,adm_edit_password,adm_edit_confirmpassword,adm_edit_city,adm_edit_state
    
    adm_edit_name = entry_6.get()
    adm_edit_phno = entry_7.get()
    adm_edit_emailaddress = entry_8.get()
    adm_edit_addressln1 = entry_9.get()
    adm_edit_addressln2 = entry_10.get()
    adm_edit_username = entry_1.get()
    adm_edit_password = entry_2.get()
    adm_edit_confirmpassword = entry_3.get()
    adm_edit_city = entry_4.get()
    adm_edit_state = entry_5.get()
    
    #strip the values
    adm_edit_name = adm_edit_name.strip()
    adm_edit_phno = adm_edit_phno.strip()
    adm_edit_emailaddress = adm_edit_emailaddress.strip()
    adm_edit_addressln1 = adm_edit_addressln1.strip()
    adm_edit_addressln2 = adm_edit_addressln2.strip()
    adm_edit_username = adm_edit_username.strip()
    adm_edit_password = adm_edit_password.strip()
    adm_edit_confirmpassword = adm_edit_confirmpassword.strip()
    adm_edit_city = adm_edit_city.strip()
    adm_edit_state = adm_edit_state.strip()
  
    # Concatenating Addressln1 and Addressln2 into same variable 'address' (separated with a ' | ' )
    adm_edit_address = adm_edit_addressln1 + ' | ' + adm_edit_addressln2  

# Validate Admin - Edit - User Details Values :  
def validate_admin_edit_user_detaisl(custid):
    #Ckecking Username
    cur.execute("select custid from login_credentials where username = %s and Isdeleted = 'False'",(adm_edit_username,))
    
    try :
        (exists,) = cur.fetchone()
    except :
        exists = 0 
        
    if adm_edit_username == '': #Ckecking username if it's an empty String
        messagebox.showerror('Username Error','Enter a Valid Username')
        
    elif exists and exists != custid : #checking if user already exists
        messagebox.showwarning('User Exists',"Username already exixts. Press Cancel if you dont want to make changes")
        
    else :
        #As username is now unique, Ckecking the length of username 
        if validatelen(adm_edit_username,5,25):
            #As username is now unique, Ckecking the passwords
            if validatelen(adm_edit_password,8,15): #ckecking if pwd is lengthy enough
                if adm_edit_password == adm_edit_confirmpassword :# if passwords match
                    if validatepwd(adm_edit_password):#Validating Passwords
                        if validatelen(adm_edit_name,1,25):#Checking Name length
                            if validatename(adm_edit_name,'name'):#validate name
                                if validatelen(adm_edit_phno,10,10):#Validate lenth of phno
                                    if validatephno (adm_edit_phno):#validate phno
                                        if validateemail(adm_edit_emailaddress):#validate email
                                            if validatelen(adm_edit_address,2,200):#validate address
                                                if validatelen(adm_edit_city,1,30) and validatename(adm_edit_city,'city'):#validate City
                                                    if validatelen(adm_edit_state,1,30) and validatename(adm_edit_state,'state'): #validate state
                                                        # add values to sql table - login_credentials and personal_details
                                                        return True
                                                    else:
                                                        messagebox.showwarning('State Error','State field should ONLY contain letters and spaces and should not exceed 30 characters')
                                                        entry_5.delete(0,'end')                                                   
                                                else:
                                                    messagebox.showwarning('City Error','City field should ONLY contain letters and spaces and should not exceed 30 characters')
                                                    entry_4.delete(0,'end')
                                            else:
                                                messagebox.showerror('Address Error','Address field should not be empty and should not exceed 200 characters')
                                                entry_8.delete(0,'end')
                                                entry_10.delete(0,'end')
                                        else :
                                            messagebox.showerror('Email Error','Enter a valid Email')
                                            entry_8.delete(0,'end')
                                    else:
                                        messagebox.showerror('PhNo Error','Phone number should contain Numbers ONLY !')
                                        entry_7.delete(0,'end')
                                else:
                                    messagebox.showerror('PhNo Error','Enter a valid 10 digit Phno')   
                                    entry_7.delete(0,'end')
                            else :
                                messagebox.showwarning('Name Error','Name cannot contain numbers and special characters except (.) and whitespaces !')
                                entry_6.delete(0,'end')
                        else :
                            messagebox.showwarning('Name Error','Enter your name. Do not exceed 25 characters')
                            entry_6.delete(0,'end')            
                elif len(adm_edit_confirmpassword) == 0 : # if confirmPassword is Left empty
                    messagebox.showerror('Password Error',"Confirm Password")
                else:
                    messagebox.showerror('Password Error',"Passwords don't match")
                    entry_2.delete(0,'end')
                    entry_3.delete(0,'end')
            else :
                messagebox.showwarning('Password Warning',"Password must contain minimum 8 and not more than 15 characters !")
                entry_2.delete(0,'end')
                entry_3.delete(0,'end')
        else :
            messagebox.showwarning('Username Warning',"Username must contain minimum 5 and not more than 25 characters !")
            entry_1.delete(0,'end')

# make admin - user    
def makeadmin(custid):
    global admin
    admin = 'True'
    user_status(custid)
  
# revoke admin user    
def revokeadmin(custid):
    global admin
    admin = 'False'
    user_status(custid)
 
# delete (disable) user    
def deleteuser(custid):
   global inactive
   inactive = 'True'
   user_status(custid)
 
# enable user    
def enableuser(custid):
    global inactive
    inactive = 'False'
    user_status(custid)

# Update user satus - corresponding buttons
def user_status(custid):
    global button_image_7,button_image_8,button_image_9,button_image_11

    # Checking if Admin
    if admin == 'True':
        # Revoke Admin Button
        button_image_11 = PhotoImage(
            file=relative_to_assets8("button_11.png"))
        button_11 = Button(canvas15,
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda c= custid: revokeadmin(c),
            relief="flat"
        )
        if Current_CustID == custid or custid == 14:
            button_11.config(state = DISABLED)
            
        button_11.place(
            x=30.0,
            y=380.0,
            width=163.0,
            height=27.84583282470703
        )
        
    else :
        # Make Admin Button
        button_image_9 = PhotoImage(
            file=relative_to_assets8("button_9.png"))
        button_9 = Button(canvas15,
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda c = custid: makeadmin(c),
            relief="flat"
        )
        button_9.place(
            x=30.0,
            y=380.0,
            width=163.0,
            height=27.84583282470703
        )

    # Checking if Deleted 
    if inactive == 'True' :
        # Enable User Button
        button_image_8 = PhotoImage(
            file=relative_to_assets8("button_8.png"))
        button_8 = Button(canvas15,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command= lambda c = custid: enableuser(c),
            relief="flat"
        )
        button_8.place(
            x=200.0,
            y=380.0,
            width=163.0,
            height=27.84583282470703
        )
    else :
        # delete user button
        button_image_7 = PhotoImage(
            file=relative_to_assets8("button_7.png"))
        button_7 = Button(canvas15,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command= lambda c = custid: deleteuser(c),
            relief="flat"
        )
        if Current_CustID == custid or custid == 14: 
            button_7.config(state = DISABLED)
            
        button_7.place(
            x=200.0,
            y=380.0,
            width=163.0,
            height=27.84583282470703
        )

# Manage Users canvas in admincanvas
def manage_users():
    global edit_btn_image,canvas14,scrollbar5
    
    admn_home_btn()
    
    # show all users, show an option to delete the user, make them the admin, change their info
    canvas14 = Canvas(window,highlightthickness=0,height = 410,width = 920,bg ='#FFFFFF',borderwidth=0)
    canvas14.place(x = 37,y = 150)
  

    #Creating scrollbar
    scrollbar5 = Scrollbar(window,command=canvas14.yview)
    scrollbar5.place(x=947, y=150)
    scrollbar5.place(height=410)
   
    # Creating Frame
    frame7 = Frame(canvas14, width=925, height=410,borderwidth = 0,highlightthickness = 0,bg = '#FFFFFF')

    # Canvas Config
    canvas14.configure(yscrollcommand=scrollbar5.set)
    canvas14.bind('<Configure>', lambda e: canvas14.configure(scrollregion=canvas14.bbox("all")))


    #admin_user_controls()
    
    edit_btn_image = PhotoImage(
        file = relative_to_assets8('button_6.png'))
    
    cur.execute('select login_credentials.username,login_credentials.is_Admin ,login_credentials.IsDeleted,login_credentials.CustId,personal_details.name from login_credentials,personal_details where login_credentials.custid = personal_details.custid')
    users = cur.fetchall() # List of Tuples 
    
    window_height = 50*len(users) +20
    canvas14.create_window((0, 0),   
                     height =window_height,
                     width=920,
                     window=frame7,
                     anchor='nw')
    Ycoor = 10
    for username,isadmin,isdeleted,custid,name in users :
        
        Foreground = '#000000'
        Font = ('Inika',18)
        if isdeleted == 'True' :
            Foreground = '#7D7D7D'
            Font = strikethrough_font
            
        if isadmin == 'True':
            status = 'Admin'
        else :
            status = 'Customer'
        
        if len(name)>20:
            name = name[:18]+'...'
        label1 = Label(frame7,bg ='#FFFFFF',font = Font,foreground= Foreground, text =username,anchor=CENTER)
        label1.place(x = 30,y = Ycoor)
        
        label2 = Label(frame7,bg ='#FFFFFF',font = Font,foreground= Foreground, text =name)
        label2.place(x = 350,y = Ycoor)
        
        label3 = Label(frame7,bg ='#FFFFFF',font = ('Inika',18),foreground= Foreground, text =status)
        label3.place(x = 700,y = Ycoor)
        
        btn = Button(frame7,bg ='#FFFFFF',image = edit_btn_image,borderwidth=0,command = lambda c = custid: edit_user(c))
        btn.place(x = 850,y = Ycoor)

        Ycoor += 50

 # Creating String Variable 
  
# Set string var for admin user - editing  
def admin_user_setstrvar():
    global admn_svname, admn_svphno,admn_svemail,admn_svaddressln1,admn_svaddressln2,admn_username,admn_svpwd,admn_svconfirmpwd,admn_svcity,admn_svstate
    
    #Creating StingVars 
    admn_svname    = StringVar(window)
    admn_svphno    = StringVar(window)
    admn_svemail  = StringVar(window)
    admn_svaddressln1      = StringVar(window)
    admn_svaddressln2 = StringVar(window)
    admn_username = StringVar(window)
    admn_svpwd = StringVar(window)
    admn_svconfirmpwd = StringVar(window)
    admn_svcity = StringVar(window)
    admn_svstate = StringVar(window)
    
    #Assigning (Setting) StringVars - Parent tuple is Profile_Details
    
    admn_svname.set(user_details[0])
    admn_svphno.set(user_details[1])
    admn_svemail.set(user_details[2])
        # Personal_Details[4] contains both addressln1 and addressln2 separated by a '|'
        # we have to .split('|') and set the respective StringVar 
    admn_svaddressln1.set( user_details[3].split(' | ')[0] )
    admn_svaddressln2.set( user_details[3].split(' | ')[1] )
    admn_username.set(user_details[6])
    admn_svpwd.set(user_details[7])
    admn_svconfirmpwd.set(user_details[7])
    admn_svcity.set(user_details[4])
    admn_svstate.set(user_details[5])

# Button Click event - Edit user
def edit_user(custid):
    
    global button_image_10,button_image_12,canvas15
    global user_details,admin,inactive
    global entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9,entry_10
    
    admn_home_btn()
        
    # Fetch Account Details
    cur.execute("select personal_details.Name ,personal_details.PhoneNo,personal_details.EmailId,personal_details.Address,personal_details.City,personal_details.state,login_credentials.username,login_credentials.Password from personal_details,login_credentials where login_credentials.Custid = personal_details.Custid and login_credentials.custid = %s",(custid,))
    user_details = cur.fetchone()
     
    # Fetch admin / active details 
    cur.execute('select is_admin,isdeleted from login_credentials where custid = %s',(custid,))
    (admin,inactive) = cur.fetchone()
     
    admin_user_setstrvar()
    
    if "canvas15" in globals():
        canvas15.destroy()
        
    canvas15 = Canvas(window,height = 410,width = 920,bg ='#FFFFFF',borderwidth= 0,highlightthickness=0)
    canvas15.place(x = 37,y = 150)
  
    user_status(custid)



    entry_1 = Entry(canvas15,
        bd=0,
        textvariable= admn_username,
        font = ('Inika',16),
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=520.0,
        y=30.0,
        width=399.0,
        height=38.0
    )

    entry_2 = Entry(canvas15,
        bd=0,
        show = '*',
        font = ('Inika',16),
        textvariable= admn_svpwd,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=520.0,
        y=105.0,
        width=399.0,
        height=38.0
    )

    entry_3 = Entry(canvas15,
        textvariable= admn_svconfirmpwd,
        show ='*',
        font = ('Inika',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=520.0,
        y=180.0,
        width=399.0,
        height=38.0
    )

    entry_4 = Entry(canvas15,
        bd=0,
        font = ('Inika',16),
        textvariable= admn_svcity,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=520.0,
        y=255.0,
        width=399.0,
        height=38.0
    )

    entry_5 = Entry(canvas15,
        bd=0,
        font = ('Inika',16),
        textvariable= admn_svstate,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=520.0,
        y=330.0,
        width=399.0,
        height=38.0
    )
   
    entry_6 = Entry(canvas15,
        bd=0,
        textvariable=  admn_svname,
        bg="#D9D9D9",
        font = ('Inika',16),
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=20.0,
        y=30.0,
        width=399.0,
        height=38.0
    )

    entry_7 = Entry(canvas15,
        font = ('Inika',16),
        bd=0,
        bg="#D9D9D9",
        textvariable= admn_svphno,
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=20.0,
        y=105.0,
        width=399.0,
        height=38.0
    )

    entry_8 = Entry(canvas15,
        bd=0,
        textvariable= admn_svemail,
        font = ('Inika',16),
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=20.0,
        y=180.0,
        width=399.0,
        height=38.0
    )

    entry_9 = Entry(canvas15,
        bd=0,
        bg="#D9D9D9",
        textvariable= admn_svaddressln1,
        font = ('Inika',16),
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=20.0,
        y=255.0,
        width=403.0,
        height=36.0
    )

    entry_10 = Entry(canvas15,
        bd=0,
        font = ('Inika',16),
        bg="#D9D9D9",
        textvariable= admn_svaddressln2,
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=20.0,
        y=330.0,
        width=403.0,
        height=36.0
    )

    canvas15.create_text(
        20.0,
        10.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas15.create_text(
        20.0,
        85.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas15.create_text(
        20.0,
        160.0,
        anchor="nw",
        text="Email ",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas15.create_text(
        20.0,
        235.0,
        anchor="nw",
        text="Address Line 1",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas15.create_text(
        20.0,
        310.0,
        anchor="nw",
        text="Address Line 2",
        fill="#000000",
        font=("Inika", 17 * -1)
    )
    canvas15.create_text(
        520.0,
        10.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Inika", 17 * -1)
    )
 

    canvas15.create_text(
        520.0,
        85.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas15.create_text(
        520.0,
        160.0,
        anchor="nw",
        text="Confirm Pasword",
        fill="#000000",
        font=("Inika", 17 * -1)
    )
    canvas15.create_text(
        520.0,
        235.0,
        anchor="nw",
        text="City",
        fill="#000000",
        font=("Inika", 17 * -1)
    )

    canvas15.create_text(
        520.0,
        310.0,
        anchor="nw",
        text="State",
        fill="#000000",
        font=("Inika", 17 * -1)
    )
     
    # cancel Button
    button_image_10 = PhotoImage(
        file=relative_to_assets8("button_10.png"))
    button_10 = Button(canvas15,
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=manage_users,
        relief="flat"
    )
    button_10.place(
        x=570.0,
        y=380.0,
        width=163.0,
        height=27.84583282470703
    )
    
    # save Button 
    button_image_12 = PhotoImage(
        file=relative_to_assets8("button_12.png"))
    button_12 = Button(canvas15,
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda c = custid:  admn_save_user_edits(c),
        relief="flat"
    )
    if custid == 14: # primary Admin 
        button_12.config(state = DISABLED)
        
    button_12.place(
        x=740.0,
        y=380.0,
        width=163.0,
        height=27.84583282470703
    )

# Button Click Event - Close btn in admincanvas
def closebutton():
    
    admn_home_btn()
    canvas13.destroy()

# Button Click Event - Close btn in Admincanvas
def admn_home_btn():
    
    if "canvas14" in globals():
        canvas14.destroy()
        scrollbar5.destroy()
    if "canvas15" in globals():
        canvas15.destroy()
    if "canvas16" in globals():
        canvas16.destroy()
        scrollbar6.destroy()
    if "canvas17" in globals():
        canvas17.destroy()    
    if "canvas18" in globals():
        canvas18.destroy()
        scrollbar7.destroy()
    if "canvas19" in globals():
        canvas19.destroy()
    if "canvas20" in globals():
        canvas20.destroy()
    if "canvas21" in globals():
        canvas21.destroy()
    if "canvas22" in globals():
        canvas22.destroy()
    if "canvas23" in globals():
        canvas23.destroy()
    if "canvas24" in globals():
        canvas24.destroy()
        scrollbar8.destroy()
        frame10.destroy()
    if "canvas25" in globals():
        canvas25.destroy()  
    if "canvas26" in globals():
        canvas26.destroy()
        scrollbar9.destroy()
        frame11.destroy()    
    if "canvas27" in globals():
        canvas27.destroy()  
    if "canvas28" in globals():
        canvas28.destroy()
        scrollbar10.destroy()
        frame12.destroy() 
    if "canvas29" in globals():
        canvas29.destroy()  
    if "canvas30" in globals():
        canvas30.destroy()
        scrollbar11.destroy()
        frame13.destroy() 
    if "canvas31" in globals():
        canvas31.destroy()  
    if "canvas32" in globals():
        canvas32.destroy()
        scrollbar12.destroy()
        frame14.destroy() 
    if "canvas33" in globals():
        canvas33.destroy()  
    if "canvas34" in globals():
        canvas34.destroy()
        scrollbar13.destroy()
        frame15.destroy() 
                     
# Admin Canvas    
def admincanvas():
    
    global canvas13,button_image_1,button_image_2,button_image_3,button_image_4,button_image_5,image_image_1,button_image_15
    
    tooltip = Balloon(window)
    for i in tooltip.subwidgets_all():
        i.configure(bg='white')
   
    canvas13 = Canvas(
        window,
        bg = "#D5D5D5",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas13.place(x = 0, y = 0)
    canvas13.create_text(
        403.0,
        22.0,
        anchor="nw",
        text="oyFood - Admin",
        fill="#000000",
        font=("Inika Bold", 27 * -1)
    )

    # Manage Hotels Btn
    button_image_1 = PhotoImage(
        file=relative_to_assets8("button_1.png"))
    manage_htl_btn = Button(canvas13,
        image=button_image_1,
        borderwidth=0,
        activebackground= '#D5D5D5',
        highlightthickness=0,
        command=manage_hotels,
        relief="flat"
    )
    manage_htl_btn.place(
        x=348.0,
        y=72.0,
        width=240.0,
        height=41.0
    )
    
    # Manage Users Btn
    button_image_2 = PhotoImage(
        file=relative_to_assets8("button_2.png"))
    manage_users_btn = Button(canvas13,
        image=button_image_2,
        borderwidth=0,
        activebackground= '#D5D5D5',
        highlightthickness=0,
        command=manage_users,
        relief="flat"
    )
    manage_users_btn.place(
        x=63.0,
        y=72.0,
        width=240.0,
        height=41.0
    )
    
    # Manage Items Btn
    button_image_3 = PhotoImage(
        file=relative_to_assets8("button_3.png"))
    manage_items_btn = Button(canvas13,
        image=button_image_3,
        borderwidth=0,
        activebackground= '#D5D5D5',
        highlightthickness=0,
        command=manage_items,
        relief="flat"
    )
    manage_items_btn.place(
        x=631.0,
        y=72.0,

        width=240.0,
        height=41.0
    )

    # Close Btn
    button_image_4 = PhotoImage(
        file=relative_to_assets8("button_4.png"))
    closebtn = Button(canvas13,
        image=button_image_4,
        borderwidth=0,
        activebackground= '#D5D5D5',
        highlightthickness=0,
        command=closebutton,
        relief="flat"
    )
    closebtn.place(
        x=950.0,
        y=7.0,
        width=45.0,
        height=45.0
    )
    tooltip.bind_widget(closebtn,balloonmsg = 'Logout')
    
    # Home Btn
    button_image_15 = PhotoImage(
        file=relative_to_assets8("button_15.png"))
    homebtn = Button(canvas13,
        image=button_image_15,
        borderwidth=0,
        activebackground= '#D5D5D5',
        highlightthickness=0,
        command=admn_home_btn,
        relief="flat"
    )
    homebtn.place(
        x=10.0,
        y=7.0,
        width=45.0,
        height=45.0
    )
    tooltip.bind_widget(homebtn,balloonmsg = 'Logout')

    # View Reports Btn
    button_image_5 = PhotoImage(
        file=relative_to_assets8("button_5.png"))
    reports_btn = Button(canvas13,
        image=button_image_5,
        borderwidth=0,
        activebackground= '#D5D5D5',
        highlightthickness=0,
        command=view_reports,
        relief="flat"
    )
    reports_btn.place(
        x=902.0,
        y=72.0,
        width=32.0,
        height=41.0
    )
    tooltip.bind_widget(reports_btn,balloonmsg = 'View Reports')
    # rounded rectangle
    image_image_1 = PhotoImage(
        file=relative_to_assets8("image_1.png"))
    image_1 = canvas13.create_image(
        500.0,
        357.0,
        image=image_image_1
    )

###########################################################################
    
window = Tk()
window.geometry("1000x600")
window.configure(bg = "#D5D5D5")
    
strikethrough_font = font.Font(window, family="Inika", size=18, overstrike=1)


admincanvas()
Current_CustID = 14
window.resizable(False, False)
window.mainloop()


