use food_delivery_application ;

select * from login_credentials;
select * from personal_details;
select * from hotel_details;
select * from items;
select * from order_details;
select * from orders;

ALTER TABLE hotel_details
add HotelId int AUTO_INCREMENT PRIMARY KEY;
alter table personal_details
modify column PhoneNo varchar(15);
	
ALTER TABLE orders 
add custid int ,
add  FOREIGN KEY (CustId) REFERENCES login_credentials(CustId);

DELETE FROM order_details;

ALTER TABLE personal_details
add  FOREIGN KEY (CustId) REFERENCES login_credentials(CustId);

UPDATE personal_details SET name = 'Admin (do not edit)' where CustId = 14;  
insert into login_credentials ()values (login_credentials);

insert into login_credentials(username,password,is_admin,isDeleted) values ('admin','admin','True','False');

insert into personal_details values ("Admin One",'0000000000','admin@oyf.com','admin-oyf-hq','chennai','tn',14);

Update Personal_details set name = " Admin (do not edit) "  where custid = 14;
delete from login_credentials where CustId = 9;
	
update items set category = 'lunch/dinner' where itemid = 11;
select * from items;

select count(hotelid) from orders where hotelid = 3;

# Report 1 - hotel wise order count report 

select count(orders.hotelid) , hotel_details.hotel_name,hotel_details.address 
from  
	hotel_details 
    left join orders on orders.hotelid = hotel_details.hotelid 
where orders.OrderDatetime > 'start date' and orders.OrderDatetime < 'end date'  
and hotel_details.hotel_name = 'Hotel Ganga'and hotel_details.address = 'Anna Nagar West'
group by  orders.hotelid,hotel_details.hotel_name,hotel_details.address ;

# Report 2  - Hotel Wise - User order details

SELECT 
	personal_details.name, hotel_details.hotel_name,hotel_details.address, COUNT(orders.custid) AS order_count
	FROM orders
	JOIN personal_details ON personal_details.custid = orders.custid
	JOIN hotel_details ON hotel_details.hotelid = orders.hotelid
where orders.OrderDatetime > '2024-04-18' and orders.OrderDatetime <= '2024-05-25' and hotel_details.hotel_name = 'Hotel Ganga'and hotel_details.address = 'Anna Nagar West'
GROUP BY personal_details.name, hotel_details.hotel_name, hotel_details.address, orders.custid, orders.hotelid;

# Report 3 -  hotel wise item order report 
SELECT 
    hd.Hotel_Name,hd.address,i.Item_Name,SUM(od.Quantity)
	FROM orders o 
	JOIN order_details od ON o.OrderId = od.OrderId
	JOIN items i ON od.ItemId = i.ItemId
    JOIN hotel_details hd ON o.HotelId = hd.HotelId
	where o.OrderDatetime > '2024-04-18' and o.OrderDatetime <= '2024-05-25' 
    and hd.hotel_name = 'Hotel Ganga'and hd.address = 'Anna Nagar West'
	GROUP BY hd.Hotel_Name, i.Item_Name, hd.address;

# report 4 user wise item order count 
	SELECT pd.Name,pd.emailid,i.Item_Name,SUM(od.Quantity)
	FROM orders o
	JOIN order_details od ON o.OrderId = od.OrderId
	JOIN items i ON od.ItemId = i.ItemId
	JOIN login_credentials lc ON o.custid = lc.CustId
	JOIN personal_details pd ON lc.CustId = pd.Custid
	WHERE o.OrderDatetime >  '2024-04-18'  and o.OrderDatetime <= '2024-05-25' and lc.CustId = 1
	GROUP BY pd.Name, i.Item_Name, pd.emailid ;


# report 5 Userwise hotel order count
SELECT 
    pd.Name,hd.Hotel_Name,hd.address,COUNT(o.OrderId)
	FROM orders o
	JOIN hotel_details hd ON o.HotelId = hd.HotelId
	JOIN login_credentials lc ON o.custid = lc.CustId
	JOIN personal_details pd ON lc.CustId = pd.Custid
	WHERE o.OrderDatetime >  '2024-04-18'  and o.OrderDatetime <= '2024-05-26'and lc.CustId = 1
	GROUP BY pd.Name, hd.Hotel_Name,hd.address;

# report 6 Show recent order
SELECT 
    pd.Name,hd.Hotel_Name,o.OrderId
	FROM orders o
	JOIN hotel_details hd ON o.HotelId = hd.HotelId
	JOIN login_credentials lc ON o.custid = lc.CustId
	JOIN personal_details pd ON lc.CustId = pd.Custid
    where  o.OrderDatetime >  '2024-04-18'  and o.OrderDatetime <= '2024-05-27' #and  o.custid = 1
	ORDER BY o.OrderDatetime DESC;
    