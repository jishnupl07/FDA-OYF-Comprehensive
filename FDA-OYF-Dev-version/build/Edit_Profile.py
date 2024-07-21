
import mysql.connector as sql
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import re  #Regular Expressions
from tkinter import messagebox


OUTPUT_PATH1 = Path(__file__).parent
ASSETS_PATH1 = OUTPUT_PATH1 / Path(r"assets\frame1")


def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

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
                    profile_entry_9.delete(0,'end')
                    profile_entry_10.delete(0,'end') 
            else :
                messagebox.showwarning('Password Warning',"Password must contanin at least 1 number")
                profile_entry_9.delete(0,'end')
                profile_entry_10.delete(0,'end')
        else :
            messagebox.showwarning('Password Warning',"Password must contanin at least 1 uppercase character ")
            profile_entry_9.delete(0,'end')
            profile_entry_10.delete(0,'end')         
    else :
        messagebox.showwarning('Password Warning',"Password must contanin at least 1 lowercase character ")
        profile_entry_9.delete(0,'end')
        profile_entry_10.delete(0,'end')

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

def validateeditprofile():
        getprofilevalues()
        #As username is now unique, Ckecking the passwords
        if validatelen(edit_password,8,15): #ckecking if pwd is lengthy enough
            if edit_password == edit_confirmpassword :# if passwords match
                if validatepwd(edit_password):#Validating Passwords
                    if validatelen(edit_name,1,25):#Checking Name length
                        if validatename(edit_name,'name'):#validate name
                            if validatelen(edit_phno,10,10):#Validate lenth of phno
                                if validatephno (edit_phno):#validate phno
                                    if validateemail(edit_emailaddress):#validate email
                                        if validatelen(edit_address,2,200):#validate address
                                            if validatelen(edit_city,1,30) and validatename(edit_city,'city'):#validate City
                                                if validatelen(edit_state,1,30) and validatename(edit_state,'state'): #validate state
                                                    # add values to sql table - login_credentials and personal_details
                                                    #sqlsignup()
                                                    messagebox.showinfo('Profile - Status','Update Successful. Return to Hotels page.')
                                                    #returntologin()

                                                else:
                                                    messagebox.showwarning('State Error','State field should ONLY contain letters and spaces and should not exceed 30 characters')
                                                    profile_entry_12.delete(0,'end')                                                   
                                            else:
                                                messagebox.showwarning('City Error','City field should ONLY contain letters and spaces and should not exceed 30 characters')
                                                profile_entry_11.delete(0,'end')
                                        else:
                                            messagebox.showerror('Address Error','Address field should not be empty and should not exceed 200 characters')
                                            profile_entry_6.delete(0,'end')
                                            profile_entry_7.delete(0,'end')
                                    else :
                                        messagebox.showerror('Email Error','Enter a valid Email')
                                        profile_entry_5.delete(0,'end')
                                else:
                                    messagebox.showerror('PhNo Error','Phone number should contain Numbers ONLY !')
                                    profile_entry_4.delete(0,'end')
                            else:
                                messagebox.showerror('PhNo Error','Enter a valid 10 digit Phno')   
                                profile_entry_4.delete(0,'end')
                        else :
                            messagebox.showwarning('Name Error','Name cannot contain numbers and special characters except (.) and whitespaces !')
                            entry_3.delete(0,'end')
                    else :
                        messagebox.showwarning('Name Error','Enter your name. Do not exceed 25 characters')
                        entry_3.delete(0,'end')            
            elif len(edit_confirmpassword) == 0 : # if confirmPassword is Left empty
                messagebox.showerror('Password Error',"Confirm Password")
            else:
                messagebox.showerror('Password Error',"Passwords don't match")
                profile_entry_9.delete(0,'end')
                profile_entry_10.delete(0,'end')
        else :
            messagebox.showwarning('Password Warning',"Password must contain minimum 8 and not more than 15 characters !")
            profile_entry_9.delete(0,'end')
            profile_entry_10.delete(0,'end')

def getprofilevalues():
    # put the variables as global
    global edit_name,edit_phno,edit_emailaddress,edit_address,edit_password,edit_confirmpassword,edit_city,edit_state
    
    edit_name = entry_3.get()
    edit_phno = profile_entry_4.get()
    edit_emailaddress = profile_entry_5.get()
    edit_addressln1 = profile_entry_6.get()
    edit_addressln2 = profile_entry_7.get()
    edit_password = profile_entry_9.get()
    edit_confirmpassword = profile_entry_10.get()
    edit_city = profile_entry_11.get()
    edit_state = profile_entry_12.get()
    
    #strip the values
    edit_name = edit_name.strip()
    edit_phno = edit_phno.strip()
    edit_emailaddress = edit_emailaddress.strip()
    edit_addressln1 = edit_addressln1.strip()
    edit_addressln2 = edit_addressln2.strip()
    edit_password = edit_password.strip()
    edit_confirmpassword = edit_confirmpassword.strip()
    edit_city = edit_city.strip()
    edit_state = edit_state.strip()
  
    # Concatenating Addressln1 and Addressln2 into same variable 'address' (separated with a ' | ' )
    edit_address = edit_addressln1 + ' | ' + edit_addressln2  

#Fetches Current User Details from Sql Table - Personal_Details
def sqlfetchdatails():
    
    global Personal_Details,Password
    
    cur.execute("Select name,Phoneno,Emailid,Address,city,state from personal_details where custid = %s",(Current_CustID,))
    Details = cur.fetchall()
    [Personal_Details] = Details
    cur.execute("Select Password from login_credentials where custid = %s",(Current_CustID,))
    Pwd = cur.fetchall()   
    [(Password,)] = Pwd
    
    #Personal_Details is a tuple !
    #Password is a String
   


def setstrvar():
    global svname, svphno,svemail,svaddressln1,svaddressln2,svpwd,svconfirmpwd,svcity,svstate
    
    #Creating StingVars 
    svname    = StringVar(window)
    svphno    = StringVar(window)
    svemail  = StringVar(window)
    svaddressln1      = StringVar(window)
    svaddressln2 = StringVar(window)
    svpwd = StringVar(window)
    svconfirmpwd = StringVar(window)
    svcity = StringVar(window)
    svstate = StringVar(window)
    
    #Assigning (Setting) StringVars - Parent tuple is Profile_Details
    
    svname.set(Personal_Details[0])
    svphno.set(Personal_Details[1])
    svemail.set(Personal_Details[2])
        # Personal_Details[4] contains both addressln1 and addressln2 separated by a '|'
        # we have to .split('|') and set the respective StringVar 
    svaddressln1.set( Personal_Details[3].split(' | ')[0] )
    svaddressln2.set( Personal_Details[3].split(' | ')[1] )
    svpwd.set(Password)
    svconfirmpwd.set(Password)
    svcity.set(Personal_Details[4])
    svstate.set(Personal_Details[5])

def profilecanvas():
    global entry_3,profile_entry_4,profile_entry_5,profile_entry_6,profile_entry_7,profile_entry_9,profile_entry_10,profile_entry_11,profile_entry_12 #to get values in other funtions
    global image_image_3,button_image_3,button_image_4,entry_image_3

    sqlfetchdatails()
    setstrvar()
    
    strvariables = (svname, svphno,svemail,svaddressln1,svaddressln2,svpwd,svconfirmpwd,svcity,svstate)

    canvas_5 = Canvas(
        window,
        bg = "#FFFDFD",
        height = 596,
        width = 996,
        bd = 0,
        highlightthickness = 0,
        relief = "flat"
    )

    canvas_5.place(x = 0, y = 0)

    image_image_3 = PhotoImage(
        file=relative_to_assets1("image_1.png"))
    image_1 = canvas_5.create_image(
        498.0,
        298.0,
        image=image_image_3
    )
    #Save Button

    button_image_3 = PhotoImage(
        file=relative_to_assets1("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command= validateeditprofile,
        relief="flat"
    )
    button_3.place(
        x=579.0,
        y=519.0,
        width=176.0,
        height=35.98222351074219
    )
    #Cancel Button

    button_image_4 = PhotoImage(
        file=relative_to_assets1("button_2.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=767.0,
        y=519.0,
        width=175.0,
        height=36.0
    )

    #Text of all the required fields for Personal Information

    canvas_5.create_text(
        558.0,
        436.0,
        anchor="nw",
        text="State :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        558.0,
        345.0,
        anchor="nw",
        text="City :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        558.0,
        266.0,
        anchor="nw",
        text="Confirm Password :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        558.0,
        180.0,
        anchor="nw",
        text="Password :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        558.0,
        92.0,
        anchor="nw",
        text="Username:",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        44.0,
        436.0,
        anchor="nw",
        text="Address Line 2 :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        44.0,
        349.0,
        anchor="nw",
        text="Address Line 1 :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        44.0,
        266.0,
        anchor="nw",
        text="Email Address : ",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        44.0,
        180.0,
        anchor="nw",
        text="Phone No :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    canvas_5.create_text(
        44.0,
        92.0,
        anchor="nw",
        text="Name :",
        fill="#000000",
        font=("Inter Bold", 18 * -1)
    )

    #All the TextBoxes are of same size and therfore, I'm using the Same variable for all of it
    #There are 10 Such TextBoxes in the current canvas. 

    #  entry_image_3 can be considered as the entry image for all the other TextBoxes too .

    ##

    entry_image_3 = PhotoImage(
        file=relative_to_assets1("entry_1.png"))

    ##

    #Name Entry 
    entry_bg_3 = canvas_5.create_image(
        245.5,
        135.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        font = ('Times New Roman',16),
        textvariable= strvariables[0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=53.0,
        y=116.0,
        width=390.0,
        height=36.0
    )

    #phone Number 

    entry_bg_4 = canvas_5.create_image(
        245.5,
        223.0,
        image=entry_image_3
    )
    profile_entry_4= Entry(
        textvariable= strvariables[1],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_4.place(
        x=55.0,
        y=204.0,
        width=390.0,
        height=36.0
    )



    #email Address

    entry_bg_5 = canvas_5.create_image(

        247.5,
        311.0,
        image=entry_image_3
    )
    profile_entry_5 = Entry(
        textvariable= strvariables[2],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_5.place(
        x=55.0,
        y=291.0,
        width=394.0,
        height=38.0
    )




    #Address Line 1

    entry_bg_6 = canvas_5.create_image(
        247.5,
        396.0,
        image=entry_image_3
    )
    profile_entry_6 = Entry(
        textvariable= strvariables[3],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_6.place(
        x=55.0,
        y=376.0,
        width=392.0,
        height=38.0
    )

    #Address Line 2

    entry_bg_7 = canvas_5.create_image(
        247.5,
        483.0,
        image=entry_image_3
    )
    profile_entry_7 = Entry(
        textvariable= strvariables[4],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_7.place(
        x=55.0,
        y=463.0,
        width=392.0,
        height=38.0
    )

    #Username is Freezed as label - It cannot and Should not be changed 
    
    Username = Label( 
        text = Current_UserID,
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )

    Username.place(
        x=565.0,
        y=115.0,
        width=387.0,
        height=40.0
    )
    


    #Password
    entry_bg_9 = canvas_5.create_image(
        759.5,
        223.0,
        image=entry_image_3
    )
    profile_entry_9 = Entry(
        show = '*',
        textvariable= strvariables[5],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_9.place(
        x=570.0,
        y=204.0,
        width=390.0,
        height=36.0
    )



    #confirm Password 
    entry_bg_10 = canvas_5.create_image(
        761.5,
        311.0,
        image=entry_image_3
    )
    profile_entry_10 = Entry(
        show = '*',
        textvariable= strvariables[6],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_10.place(
        x=567.0,
        y=291.0,
        width=392.0,
        height=38.0
    )


    #City Entry

    entry_bg_11 = canvas_5.create_image(
        757.5,
        396.0,
        image=entry_image_3
    )
    profile_entry_11 = Entry(
        textvariable= strvariables[7],
        font = ('Times New Roman',16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_11.place(
        x=565.0,
        y=376.0,
        width=392.0,
        height=38.0
    )

    #State Entry

    entry_bg_12 = canvas_5.create_image(
        757.5,
        483.0,
        image=entry_image_3
    )
    profile_entry_12 = Entry(
        textvariable= strvariables[8],
        font=("Times New Roman", 16),
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    profile_entry_12.place(
        x=565.0,
        y=463.0,
        width=392.0,
        height=38.0
    )



    # Line 
    canvas_5.create_rectangle(
        44.0,#distance from left 
        63.0, #distance from top (of 1 of the parallel sides)
        340.0,#length
        70.0,#distance from top (of the other parallel side)
        fill="#50261F",
        outline="")


    canvas_5.create_text(
        45.0,
        27.0,
        anchor="nw",
        text="View and Edit Your Profile ",
        fill="#50261F",
        font=("Times New Roman",25 * -1,'bold')
    )

########################################################################################################################################

window = Tk()
window.geometry("996x596")
window.configure(bg = "#FFFDFD")

con = sql.connect(host='localhost',user = 'root',password = 'mysqlrootpwd',database='food_delivery_application')
cur = con.cursor()

Current_UserID = 'jishnu.one'
Current_CustID =1
profilecanvas()

# StringVar, StringVar.set

        #var = StringVar(window) #Setting a Stringvar - special variable to hold textvariable - Default value of a widget
        #var.set(dict_items[i]) #setting to hold the previous value of SpinBox
        # textvariable  = var 

window.resizable(False, False)
window.mainloop()
