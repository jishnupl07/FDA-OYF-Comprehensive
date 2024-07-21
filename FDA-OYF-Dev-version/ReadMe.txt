Jishnu's Food Delivery Application - oyFood 

oyFood provides a comprehensive solution for managing food orders, from user authentication and
restaurant browsing to detailed billing and order summaries. Its intuitive interface and 
robust backend integration make it a valuable tool for both customers and administrators in 
the food delivery ecosystem.

A Tkinter - MySql Interactive Program. 
This application is a Python-based desktop software designed to facilitate food ordering. 
It leverages the Tkinter library for the graphical user interface (GUI) and connects to a MySQL 
database to manage data related to users, restaurants, menu items, and orders. 

Features

User Authentication:
	Login Page: Allows users to log in to the application. Credentials are verified against
	stored data in the MySQL database.
	SignUp Page: New users can create an account.

Restaurant Listings:
	Displays a list of available restaurants.
	Fetches restaurant details from the Hotel_details table in the database, excluding
	deleted entries.

Menu Display:
	Shows the menu items available at a selected restaurant.
	Items are fetched from the database and displayed with buttons for easy selection.

Order Management:
	Users can select items from the menu and add them to their order.
	The application calculates the total price, including taxes (GST) and a platform fee.

Order Summary and Billing:
	Displays a summary of the user's order.
	Shows detailed billing information, including itemized costs, taxes, platform fee and
	the grand total.

User Options :
	Users can edit their profile, repeat their orders with a click of a button, Logout.

Admin Functions:
	Admin users have access to additional functionalities for managing users, restaurants 
	and menu items.
	Admin-specific features include adding new restaurants, updating existing ones and
	deleting entries.

Graphical User Interface:
	oyFood uses Tkinter for creating a responsive and user-friendly interface.
	Custom Buttons, Labels, Checkboxes, Spinboxes, Comboboxes and Canvases enhance the 
	visual appeal and usability.
	Separate frames and canvases are used for different pages, such as login, restaurant 
	listing, menu display and order summary.

Database Integration:
	oyFood connects to a MySQL database to store and retrieve data.
	Ensures data persistence for user accounts, restaurant details, menu items and orders.

User Interface Components:
	Buttons: Custom-styled for better user interaction.
	Labels and Spinboxes: Used for displaying information and allowing quantity selection 
	for items.
	Canvases and Frames: Manage layout and organization of different sections within the 
	application window.
___________________________________________________________________________________________

Installation Guide :
	open cmd/termial
	change directory to application folder      -   cd <path>
	install required modules :                  -   pip intsall -r requirements.txt
	open main.pyw                               -   python main.pyw 

___________________________________________________________________________________________

Lines of Code - 7510 (Seven Thousand Five Hundred Ten Lines)
oyF - LogoFont - Bauhaus 93

Modules Used :

	mysql.connector # Sql 
	tkinter         # General Widgets
	pathlib	        # Path
	datetime        # DateTime
	tkinter.tix     # ToopTip (Balloon)
	tkcalendar      # Calendersss
	re              # Regular Expressions
	math            # Math - Ceil 
	
Variables Used :

#Path - 9 sets 

	OUTPUT_PATH - OUTPUT_PATH8
	ASSETS_PATH - ASSETS_PATH8

#Canvas - 39

	canvas - canvas 36
	basecanvas1
	basecanvas2

#frames - 16
 
	frame1 - frame 16 

#Window - 1

	window

# Toplevel - 3

	bill_window
	top_level (for calender)
	about_window

Functions Used : 149

	relative_to_assets
	relative_to_assets1
	relative_to_assets2
	relative_to_assets3
	relative_to_assets4
	relative_to_assets5
	relative_to_assets6
	relative_to_assets7
	relative_to_assets8
	display_report_6
	generate_report_6
	report_6_go_btn
	report6_create_menu
	report_6
	display_report_5
	generate_report_5
	report_5_go_btn
	report5_create_menu
	report_5
	display_report_4
	generate_report_4
	report_4_go_btn
	report4_create_menu
	report_4
	display_report_3
	generate_report_3
	report_3_go_btn
	report3_create_menu
	report_3
	display_report_2
	generate_report_2
	report_2_go_btn
	report2_create_menu
	report_2
	display_report_1
	generate_report_1
	report_1_go_btn
	on_start_date_selected
	on_end_date_selected
	open_end_calendar
	open_start_calendar
	report1_create_menu
	report_1
	view_reports
	create_category_str
	sql_admn_add_new_item
	sql_update_admn_edit_item
	get_edit_item_values
	validate_admn_add_item
	validate_admn_edit_item
	validatecategory
	delete_item
	enable_item
	item_status
	set_admn_item_edit_strvar
	set_admn_add_item_intvar
	add_item
	edit_item
	manage_items
	admin_update_hotel_details
	admin_add_hotel
	delete_hotel
	enable_hotel
	hotel_status
	sqlfetch_edit_htl
	admin_hotel_setstrvar
	get_edit_hotel_values
	validateint
	validate_admin_add_hotel
	valivdate_admin_edit_hotels
	edit_hotel
	add_hotel
	manage_hotels
	admn_save_user_edits
	get_admin_edit_user_values
	validate_admin_edit_user_detaisl
	makeadmin
	revokeadmin
	deleteuser
	enableuser
	user_status
	manage_users
	admin_user_setstrvar
	edit_user
	closebutton
	admn_home_btn	
	repeatorder
	homebtn1
	returnhotelname
	computeamount
	homebtn
	returnbaseprice
	finalplaceorder
	sql_addorder
	editItems
	sqlfetch_user_hotel_datails
	clear_orderitemlabels
	create_order_itemlabels
	cancelprofile
	update_profle_values
	validate_editprofile
	getprofilevalues
	sqlfetchdatails
	setstrvar
	clear_itemlabels
	return_itemname
	return_itemprice
	return_itemid
	placeorder
	backtohotels
	updatelabelsandspinbox
	clear_orders
	item_selected
	createlabelsandspinbox
	clearselectedhotel
	choose_hotel
	logout
	confirm_hotel
	viewprofile
	vieworders
	useroptions
	hotel_selected
	validatephno
	validateemail
	validatelen
	validatename
	center_screen
	checklogin
	getsignupvalues
	sqlsignup
	velidatepwd
	validatesignup
	returntologin
	cancelbutton
	submitbutton
	clearloginpage
	getloginvalues
	loginbutton
	signupbutton
	admincanvas
	about_oyf
	yourorderscanvas
	bill
	ordersuccessfulcanvas
	ordercanvas
	profilecanvas
	itemscanvas
	hotelcanvas
	signupcanvas
	logincanvas


