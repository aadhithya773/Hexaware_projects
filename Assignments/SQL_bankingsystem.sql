use banking_system;
go

create table customers(
  customer_id int identity(1,1) primary key,
  first_name varchar(100),
  last_name varchar(50),
  dob date,
  email_id varchar(100),
  ph_number varchar(50));

create table accounts(
  account_id int primary key,
  customer_id int identity(1,1),
  acc_type varchar(100),
  balance decimal(10,2)
  foreign key (customer_id) references customers(customer_id));

create table Transactions(
  transaction_id int primary key,
  account_id int,
  transaction_type varchar(100),
  amount decimal(10,2),
  tran_date date,
  foreign key(account_id) references accounts(account_id));
  
 insert into customers (first_name, last_name, dob, email_id, ph_number) values
('Aarav', 'Sharma', '1990-04-15', 'aarav.sharma@email.com', '9876543210'),
('Priya', 'Verma', '1985-12-20', 'priya.verma@email.com', '9876543211'),
('Rohan', 'Mehta', '1992-01-05', 'rohan.mehta@email.com', '9876543212'),
('Neha', 'Kumar', '1988-06-10', 'neha.kumar@email.com', '9876543213'),
('Anjali', 'Singh', '1995-07-25', 'anjali.singh@email.com', '9876543214'),
('Vikram', 'Gupta', '1993-03-14', 'vikram.gupta@email.com', '9876543215'),
('Sneha', 'Reddy', '1990-11-11', 'sneha.reddy@email.com', '9876543216'),
('Amit', 'Patel', '1991-08-09', 'amit.patel@email.com', '9876543217'),
('Kavya', 'Jain', '1989-05-22', 'kavya.jain@email.com', '9876543218'),
('Rahul', 'Yadav', '1994-02-18', 'rahul.yadav@email.com', '9876543219');

insert into accounts (account_id, acc_type, balance) values
(101, 'Savings', 25000.00),
(102, 'Current', 55000.50),
(103, 'Savings', 15000.75),
(104, 'Current', 34000.00),
(105, 'Savings', 12000.00),
(106, 'Savings', 47000.90),
(107, 'Current', 9000.00),
(108, 'Savings', 19000.00),
(109, 'Current', 60000.25),
(110, 'Savings', 8000.00);

insert into transactions (transaction_id, account_id, transaction_type, amount, tran_date) values
(1, 101, 'Deposit', 5000.00, '2025-04-01'),
(2, 102, 'Withdrawal', 3000.00, '2025-04-02'),
(3, 103, 'Deposit', 2000.50, '2025-04-03'),
(4, 104, 'Withdrawal', 1000.00, '2025-04-04'),
(5, 105, 'Deposit', 3500.00, '2025-04-05'),
(6, 106, 'Withdrawal', 1500.00, '2025-04-06'),
(7, 107, 'Deposit', 2500.00, '2025-04-07'),
(8, 108, 'Withdrawal', 800.00, '2025-04-08'),
(9, 109, 'Deposit', 7000.00, '2025-04-09'),
(10, 110, 'Withdrawal', 1200.00, '2025-04-10');

--TASK2: Select, Where, Between, AND, LIKE:
--1. query to retrieve the name ,acc_type and email of all cutomers
select*from customers;

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    a.acc_type,
    c.email_id
FROM 
    customers c
JOIN 
    accounts a ON c.customer_id = a.customer_id;

--2.Write a SQL query to list all transaction corresponding customer. 
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.tran_date
FROM 
    customers c
JOIN 
    accounts a ON c.customer_id = a.customer_id
JOIN 
    transactions t ON a.account_id = t.account_id

--3.Write a SQL query to increase the balance of a specific account by a certain amount. 
update accounts
set balance+=500
where account_id=104;
select *from accounts;

--4.Write a SQL query to Combine first and last names of customers as a full_name. 
select 
   concat(first_name,' ',last_name)as full_name
   from customers;
--5.Write a SQL query to remove accounts with a balance of zero where the account type is savings. 
delete from accounts
where balance=0 and acc_type='savings';

--6.Write a SQL query to Find customers living in a specific city. 
alter table customers
add city varchar(100);
UPDATE customers SET city = 'Chennai' WHERE customer_id = 1;
UPDATE customers SET city = 'Mumbai' WHERE customer_id = 2;
UPDATE customers SET city = 'Delhi' WHERE customer_id = 3;
UPDATE customers SET city = 'Chennai' WHERE customer_id = 4;
UPDATE customers SET city = 'Kolkata' WHERE customer_id = 5;
UPDATE customers SET city = 'Mumbai' WHERE customer_id = 6;
UPDATE customers SET city = 'Bangalore' WHERE customer_id = 7;
UPDATE customers SET city = 'Hyderabad' WHERE customer_id = 8;
UPDATE customers SET city = 'Bangalore' WHERE customer_id = 9;
UPDATE customers SET city = 'Hyderabad' WHERE customer_id = 10;

---instead the above way we updated city we can do it like
/*UPDATE customers
SET city = CASE customer_id
    WHEN 1 THEN 'Chennai'
    WHEN 2 THEN 'Mumbai'
    WHEN 3 THEN 'Delhi'
    WHEN 4 THEN 'Chennai'
    WHEN 5 THEN 'Kolkata'
    WHEN 6 THEN 'Mumbai'
    WHEN 7 THEN 'Bangalore'
    WHEN 8 THEN 'Hyderabad'
    WHEN 9 THEN 'Bangalore'
    WHEN 10 THEN 'Hyderabad'
    ELSE city
END;*/

select *from customers
where city='chennai';

--7.Write a SQL query to Get the account balance for a specific account. 
select account_id,balance
from accounts
where
    account_id = 102;  
--8.Write a SQL query to List all current accounts with a balance greater than $1,000.
select *
from accounts
where acc_type = 'Current' and balance > 1000;

--9.Write a SQL query to Retrieve all transactions for a specific account. 
select *
from transactions
where account_id = 101;  

SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_amount
FROM 
    customers c
JOIN 
    accounts a ON c.customer_id = a.customer_id
JOIN 
    transactions t ON a.account_id = t.account_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name;

--10.Write a SQL query to Calculate the interest accrued on savings accounts based on a 
given interest rate. 
select 
account_id,
customer_id,
balance,
balance * 0.05 as interest_accrued
from accounts
where acc_type = 'savings';

--11. Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit. 
select 
    account_id,
    customer_id,
    acc_type,
    balance
from 
    accounts
where 
    balance < 500;

--12.Write a SQL query to Find customers not living in a specific city. 
select 
    customer_id,
    first_name,
    last_name,
    city
from 
    customers
where 
    city <>'chennai'; -- we can also use city not in ('chennai') to exclude it


--Task3  Aggregate functions, Having, Order By, GroupBy and Joins:-----------------
--1. Write a SQL query to Find the average account balance for all customers.   
select 
  concat(c.first_name,' ',c.last_name)as customer_name,
  round( avg (balance),2) as balance
  from customers c
  join accounts a on c.customer_id=a.customer_id
  group by c.customer_id,c.first_name,c.last_name;
--2. Write a SQL query to Retrieve the top 10 highest account balances.  
select top 10
    account_id,
    customer_id,
    acc_type,
    balance
from 
    accounts
order by 
    balance desc;
select *from Transactions;
--3. Write a SQL query to Calculate Total Deposits for All Customers in specific date. 
select sum(amount)as total_deposit
from Transactions
where transaction_type='Deposit'
and tran_date='2025-04-10';

--4.find the oldest and newest customers
--oldest customer based on dob
select top 1
customer_id,
first_name,last_name,
dob from customers
order by
dob asc;
--newest customer
select top 1
customer_id,
first_name,last_name,
dob from customers
order by
dob desc;
--another way
select 
    (select top 1 concat(first_name, ' ', last_name) 
     from customers 
     where dob = (select min(dob) from customers)) as oldest_customer,

    (select top 1 concat(first_name, ' ', last_name) 
     from customers 
     where dob = (select max(dob) from customers)) as newest_customer;

--5. Write a SQL query to Retrieve transaction details along with the account type. 
select *from Transactions;
select*from accounts;
select 
    t.transaction_id,
    t.account_id,
    a.acc_type,
    t.transaction_type,
    t.amount,
    t.tran_date
from 
    transactions t
join 
    accounts a on t.account_id = a.account_id;

--6. Write a SQL query to Get a list of customers along with their account details. 
select 
    c.customer_id,
    concat(c.first_name, ' ', c.last_name) as customer_name,
    c.email_id,
    c.ph_number,
    a.account_id,
    a.acc_type,
    a.balance
from 
    customers c
join 
    accounts a on c.customer_id = a.customer_id;

--7. Transaction details + customer info for a specific account--
select 
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.tran_date,
    c.customer_id,
    concat(c.first_name, ' ', c.last_name) as customer_name,
    c.email_id
from 
    transactions t
join 
    accounts a on t.account_id = a.account_id
join 
    customers c on a.customer_id = c.customer_id
where 
    t.account_id = 101;

--8. Customers with more than one account:
select 
    c.customer_id,
    concat(c.first_name, ' ', c.last_name) as customer_name,
    count(a.account_id) as number_of_accounts
from 
    customers c
join 
    accounts a on c.customer_id = a.customer_id
group by 
    c.customer_id, c.first_name, c.last_name
having 
    count(a.account_id) > 1;

--9. Difference in total deposits and withdrawals:
select 
    sum(
	case when transaction_type = 'deposit' then amount else 0 end) -
    sum(case when transaction_type = 'withdrawal' then amount else 0 end) 
    as difference_in_amount
from 
    transactions;

--10. Average daily balance per account over a period
select 
a.account_id,
round(sum(balance) * 1.0 / count(distinct tran_date), 2) as avg_daily_balance
from 
    accounts a
join 
    transactions t on a.account_id = t.account_id
where 
    t.tran_date between '2025-04-01' and '2025-04-10'
group by 
    a.account_id;

--11.Total balance per account
select 
    acc_type,
    sum(balance) as total_balance
from 
    accounts
group by 
    acc_type;

--12.Accounts with highest number of transactions
select 
    t.account_id,
    count(t.transaction_id) as transaction_count
from 
    transactions t
group by 
    t.account_id
order by 
    transaction_count desc;

--13. Customers with high total balances + account types
select 
    c.customer_id,
    concat(c.first_name, ' ', c.last_name) as customer_name,
    a.acc_type,
    sum(a.balance) as total_balance
from 
    customers c
join 
    accounts a on c.customer_id = a.customer_id
group by 
    c.customer_id, c.first_name, c.last_name, a.acc_type
having 
    sum(a.balance) > 10000;

--14. Duplicate transactions (based on amount, date, and account):
select 
    account_id,
    amount,
    tran_date,
    count(*) as duplicate_count
from 
    transactions
group by 
    account_id, amount, tran_date
having 
    count(*) > 1;

/* Tasks 4: Subquery and its type:*/

--1. Retrieve the customer(s) with the highest account balance
select 
c.customer_id,
concat(c.first_name, ' ', c.last_name) as customer_name,a.balance
from customers c
join accounts a on c.customer_id = a.customer_id
where 
    a.balance = (select max(balance) from accounts);

--2.average balance for customers with more than 1 account
select
round(avg(balance),2)as avg_balance
from accounts
where customer_id in(
   select customer_id
   from accounts
   group by customer_id
   having count(account_id)>1);

--3. Accounts with transactions > average transaction amount
select *
from transactions
where amount > (
    select avg(amount) from transactions);

--4.Customers with no recorded transactions
select
  c.customer_id,
  concat(first_name,' ',last_name) as customer_name
from
   customers c
where
   c.customer_id not in(
    select distinct a.customer_id
	from accounts a
	join transactions t on a.account_id=t.account_id);

--5. Total balance of accounts with no recorded transactions
select sum(balance) as total_balance
from  accounts
where 
    account_id not in (select distinct account_id from transactions);

--6. Transactions for accounts with the lowest balance

select*
from Transactions
where account_id not in(
select account_id
from accounts
where balance=(select min(balance)from accounts));

--7. Customers with accounts of multiple types
select customer_id
from accounts
group by customer_id
having count(distinct acc_type)>1;

--8. Percentage of each account type
select acc_type,
round(cast(count(*) as float) * 100 / (select count(*) from accounts),2) as percentage
from accounts
group by acc_type;

--9. All transactions for a given customer_id 
select t.*
from transactions t
where 
    t.account_id in (
        select account_id from accounts where customer_id = 1);
--10. Total balance for each account type
select acc_type,
(select sum(balance) from accounts a2 where a2.acc_type = a1.acc_type) as total_balance
from accounts a1
group by acc_type;







