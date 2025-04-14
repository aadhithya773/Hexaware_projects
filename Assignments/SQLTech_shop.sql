create database tech_shop;
go
use tech_shop;
go

---TASK 1 creating tables-----------
create table customers (
    customerid int primary key identity(1,1),
    firstname varchar(50),
    lastname varchar(50),
    email varchar(100),
    phone varchar(20),
    address varchar(255));

create table products (
    productid int primary key identity(1,1),
    productname varchar(100),
    description varchar(255),
    price decimal(10, 2));

create table orders (
    orderid int primary key identity(1,1),
    customerid int,
    orderdate datetime,
    totalamount decimal(10, 2),
    foreign key (customerid) references customers(customerid));

create table orderdetails (
    orderdetailid int primary key identity(1,1),
    orderid int,
    productid int,
    quantity int,
    foreign key (orderid) references orders(orderid),
    foreign key (productid) references products(productid));

create table inventory (
    inventoryid int primary key identity(1,1),
    productid int,
    quantityinstock int,
    laststockupdate datetime,
    foreign key (productid) references products(productid));

------------------inserting records---------------------------
insert into customers (firstname, lastname, email, phone, address) values
('arjun', 'kumar', 'arjun.kumar@email.com', '9876543210', '123 street, chennai'),
('meera', 'singh', 'meera.singh@email.com', '9876543211', '45 avenue, bangalore'),
('ravi', 'sharma', 'ravi.sharma@email.com', '9876543212', '67 road, mumbai'),
('divya', 'rao', 'divya.rao@email.com', '9876543213', '89 cross, hyderabad'),
('karthik', 'menon', 'karthik.menon@email.com', '9876543214', '23 main st, delhi'),
('anita', 'joshi', 'anita.joshi@email.com', '9876543215', '12 park st, pune'),
('suresh', 'patel', 'suresh.patel@email.com', '9876543216', '98 hill rd, ahmedabad'),
('pooja', 'nair', 'pooja.nair@email.com', '9876543217', '34 east st, kochi'),
('rahul', 'gupta', 'rahul.gupta@email.com', '9876543218', '56 west st, kolkata'),
('neha', 'verma', 'neha.verma@email.com', '9876543219', '78 garden rd, noida');

insert into products (productname, description, price) values
('laptop', '15-inch i5 laptop', 55000.00),
('smartphone', 'android 5G phone', 20000.00),
('headphones', 'wireless noise-cancelling', 3500.00),
('keyboard', 'mechanical keyboard', 1500.00),
('mouse', 'bluetooth mouse', 800.00),
('monitor', '24-inch LED monitor', 7000.00),
('printer', 'inkjet color printer', 6000.00),
('router', 'dual band wifi router', 2500.00),
('webcam', 'hd 1080p webcam', 1200.00),
('tablet', '10-inch android tablet', 18000.00);

insert into orders (customerid, orderdate, totalamount) values
(1, '2024-03-01', 75500.00),
(2, '2024-03-02', 38500.00),
(3, '2024-03-03', 800.00),
(4, '2024-03-04', 18000.00),
(5, '2024-03-05', 20000.00),
(6, '2024-03-06', 13500.00),
(7, '2024-03-07', 1500.00),
(8, '2024-03-08', 2500.00),
(9, '2024-03-09', 4700.00),
(10, '2024-03-10', 61200.00);

insert into orderdetails (orderid, productid, quantity) values
(1, 1, 1),
(1, 3, 1),
(2, 2, 1),
(2, 4, 1),
(3, 5, 1),
(4, 10, 1),
(5, 2, 1),
(6, 6, 1),
(6, 3, 1),
(10, 1, 1);

insert into inventory (productid, quantityinstock, laststockupdate) values
(1, 10, '2024-03-01'),
(2, 20, '2024-03-01'),
(3, 50, '2024-03-01'),
(4, 30, '2024-03-01'),
(5, 40, '2024-03-01'),
(6, 15, '2024-03-01'),
(7, 25, '2024-03-01'),
(8, 35, '2024-03-01'),
(9, 45, '2024-03-01'),
(10, 12, '2024-03-01');

-----TASK 2 select,where,Between and Like:-----------
--1.Write an SQL query to retrieve the names and emails of all customers.  
select firstname,lastname,email
from customers;

--2. List all orders with order dates and corresponding customer names----
select o.orderid,o.orderdate,c.firstname,c.lastname
from orders o
join customers c on o.customerid=c.customerid;

--3. Insert a new customer record into the customers table--
insert into customers (firstname, lastname, email, phone, address) 
values ('akash', 'reddy', 'akash.reddy@email.com', '9876543220', '100 new street, chennai');

--4. Update prices of all electronic gadgets by increasing them by 10%
update products
set price=price*1.10
where productname like '%laptop%' 
   or productname like '%smartphone%' 
   or productname like '%tablet%' 
   or productname like '%router%' 
   or productname like '%printer%' 
   or productname like '%monitor%';
/* another way
update products
set price = price * 1.10
where productname in ('laptop', 'smartphone', 'tablet', 'router', 'printer', 'monitor');
*/

--5. Delete a specific order and its associated order details--
declare @orderid int = 2;
delete from orderdetails where orderid = @orderid;
delete from orders where orderid = @orderid;

--6.Insert a new order into the orders table
insert into orders (customerid, orderdate, totalamount)
values (3, getdate(), 15000.00);

--7. Update contact info (email and address) for a specific customer--
declare @customerid int = 5;
declare @newemail varchar(100) = 'new.email@example.com';
declare @newaddress varchar(255) = '500 modern colony, bangalore';
update customers
set email = @newemail, address = @newaddress
where customerid = @customerid;

--8. Recalculate and update total cost of each order based on orderdetails
select*from orders;
select * from orderdetails;
update o
set totalamount = (
    select sum(p.price * od.quantity)
    from orderdetails od
    join products p on od.productid = p.productid
    where od.orderid = o.orderid
)
from orders o;

--9. Delete all orders and orderdetails for a specific customer
declare @custid int = 4;
delete od
from orderdetails od
join orders o on od.orderid = o.orderid
where o.customerid = @custid;
delete from orders where customerid = @custid;

--10. Insert a new electronic gadget product
insert into products (productname, description, price)
values ('smartwatch', 'bluetooth fitness smartwatch', 3500.00);

--11. Update order status 
alter table orders add order_status varchar(50);
declare @orderid int = 3;
declare @newstatus varchar(20) = 'shipped';
update orders
set order_status = @newstatus
where orderid = @orderid;

--12. Calculate and update number of orders placed by each customer
alter table customers add order_count int;
update customers
set order_count=(
    select count(*)
	from orders
	where orders.customerid=customers.customerid);

/*Task 3. Aggregate functions, Having, Order By, GroupBy and Joins: */

--1.List all orders along with customer information
select o.orderid, o.orderdate, c.firstname, c.lastname, c.email, c.phone
from orders o
join customers c on o.customerid = c.customerid;

--2.Total revenue by each electronic gadget product
alter table products
add category varchar(50);
update products
set category = 'electronics'
where productname like '%laptop%' 
   or productname like '%smartphone%' 
   or productname like '%tablet%' 
   or productname like '%router%' 
   or productname like '%monitor%' 
   or productname like '%printer%';

select p.productname, sum(od.quantity * p.price) as total_revenue
from orderdetails od
join products p on od.productid = p.productid
where p.category = 'electronics'
group by p.productname;
select*from products;

--3.List all customers who made at least one purchase
select distinct c.firstname, c.lastname, c.email, c.phone
from customers c
join orders o on c.customerid = o.customerid;

--4.Most popular electronic gadget by quantity
select top 1 p.productname, sum(od.quantity) as total_quantity
from orderdetails od
join products p on od.productid = p.productid
where p.category = 'electronics'
group by p.productname
order by total_quantity desc;

--5.Electronic gadgets with their categories
select productname, category
from products
where category = 'electronics';

--6.Average order value per customer
select c.firstname, c.lastname, avg(o.totalamount) as average_order_value
from customers c
join orders o on c.customerid = o.customerid
group by c.firstname, c.lastname;

--7.Order with the highest total revenue
select top 1 o.orderid, c.firstname, c.lastname, o.totalamount
from orders o
join customers c on o.customerid = c.customerid
order by o.totalamount desc;

--8.Electronic gadgets and number of times each was ordered
select p.productname, count(od.orderdetailid) as times_ordered
from orderdetails od
join products p on od.productid = p.productid
where p.category = 'electronics'
group by p.productname;

--9.Customers who purchased a specific electronic gadget
declare @product_name varchar(100) = 'laptop';
select distinct c.firstname, c.lastname, c.email
from customers c
join orders o on c.customerid = o.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where p.productname like '%' + @product_name + '%';

--10. Total revenue for orders in a specific time period
declare @start_date date = '2024-01-01';
declare @end_date date = '2024-12-31';
select sum(totalamount) as total_revenue
from orders
where orderdate between @start_date and @end_date;

/* Sub query and its types*/
--1.
select firstname,lastname,email
from customers 
where customerid not in(
               select distinct customerid
			   from orders);

--2.
select count(*) as total_sale_prod
from inventory
where quantityinstock > 0;

--3.Total revenue generated by TechShop
select sum(od.quantity*p.price)as total_revenue
from orderdetails od
join products p on od.productid=p.productid;

--4. Average quantity ordered for products in a specific category
select avg(od.quantity) as average_quantity
from orderdetails od
join products p on od.productid = p.productid
where p.productname like '%laptop%';  

--5.
select sum(od.quantity * p.price) as customer_revenue
from orders o
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where o.customerid =6;

--6. Customers who placed the most orders
select firstname, lastname, order_count
from (
    select c.customerid, c.firstname, c.lastname, count(o.orderid) as order_count
    from customers c
    join orders o on c.customerid = o.customerid
    group by c.customerid, c.firstname, c.lastname
) as customer_orders
where order_count = (
select max(order_count)
from (
      select count(orderid) as order_count
      from orders
      group by customerid
    ) as order_counts);

--7.Most popular product category by quantity
select top 1 p.productname, sum(od.quantity) as total_quantity
from orderdetails od
join products p on od.productid = p.productid
where p.productname like '%laptop%' 
   or p.productname like '%smartphone%' 
   or p.productname like '%tablet%'
group by p.productname
order by total_quantity desc;

--8.Customer who spent the most on electronic gadgets
select top 1 c.firstname, c.lastname, sum(od.quantity * p.price) as total_spent
from customers c
join orders o on c.customerid = o.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where p.productname like '%laptop%'
   or p.productname like '%smartphone%'
   or p.productname like '%tablet%'
group by c.firstname, c.lastname
order by total_spent desc;

--9. Average order value (total revenue / number of orders)
select avg(order_value) as average_order_value
from (
select o.orderid, sum(od.quantity * p.price) as order_value
from orders o
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
group by o.orderid) as order_totals;

--10.Number of orders placed by each customer
select c.firstname,c.lastname,count(o.orderid)as total_orders
from customers c
join orders o on c.customerid=o.customerid
group by c.firstname,c.lastname;



