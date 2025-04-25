create database Ticket_booking_system;
go
use Ticket_booking_system;
go

-- 1. venue table
create table venue (
    venue_id int primary key identity(1,1),
    venue_name varchar(100),
    address varchar(255)
);

-- 2. booking table
create table booking (
    booking_id int primary key identity(1,1),
    customer_id int,
    event_id int,
    num_tickets int,
    total_cost decimal(10,2),
    booking_date date
);

-- 3. event table
create table event (
    event_id int primary key identity(1,1),
    event_name varchar(100),
    event_date date,
    event_time time,
    venue_id int,
    total_seats int,
    available_seats int,
    ticket_price decimal(10,2),
    event_type varchar(20) check (event_type in ('Movie', 'Sports', 'Concert')),
    booking_id int,
    foreign key (venue_id) references venue(venue_id),
    foreign key (booking_id) references booking(booking_id)
);

-- 4. customer table
create table customer (
    customer_id int primary key identity(1,1),
    customer_name varchar(100),
    email varchar(100),
    phone_number varchar(15),
    booking_id int,
    foreign key (booking_id) references booking(booking_id)
);

insert into venue (venue_name, address) values
('Grand Hall', '123 Main St'),
('Sky Arena', '456 Park Ave'),
('Cineplex 21', '789 Broadway'),
('Concert Dome', '101 Center Blvd'),
('Metro Sports Center', '202 Stadium Rd'),
('Sunset Theater', '303 Sunset Blvd'),
('Green Field', '404 Grassland Dr'),
('Civic Auditorium', '505 Downtown Ln'),
('Lakeview Pavilion', '606 Lake Rd'),
('Galaxy Mall Theater', '707 Galaxy Blvd');

insert into booking (customer_id, event_id, num_tickets, total_cost, booking_date) values
(null, null, 2, 100.00, '2025-04-01'),
(null, null, 3, 150.00, '2025-04-02'),
(null, null, 1, 50.00, '2025-04-03'),
(null, null, 4, 200.00, '2025-04-04'),
(null, null, 2, 120.00, '2025-04-05'),
(null, null, 3, 180.00, '2025-04-06'),
(null, null, 1, 60.00, '2025-04-07'),
(null, null, 5, 300.00, '2025-04-08'),
(null, null, 2, 110.00, '2025-04-09'),
(null, null, 1, 55.00, '2025-04-10');

insert into event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, booking_id) values
('Rock Night', '2025-05-01', '19:00', 1, 500, 300, 50.00, 'Concert', 1),
('Football Match', '2025-05-03', '18:30', 2, 800, 500, 40.00, 'Sports', 2),
('Avengers: Reassembled', '2025-05-04', '20:00', 3, 300, 200, 30.00, 'Movie', 3),
('Jazz Evening', '2025-05-05', '21:00', 4, 400, 350, 45.00, 'Concert', 4),
('Basketball Finals', '2025-05-06', '17:00', 5, 600, 400, 60.00, 'Sports', 5),
('Romantic Comedy Fest', '2025-05-07', '19:30', 6, 250, 100, 25.00, 'Movie', 6),
('Country Music Gala', '2025-05-08', '20:30', 7, 350, 320, 55.00, 'Concert', 7),
('Cricket Night', '2025-05-09', '18:00', 8, 1000, 750, 35.00, 'Sports', 8),
('Sci-Fi Weekend', '2025-05-10', '22:00', 9, 200, 80, 20.00, 'Movie', 9),
('Pop Fiesta', '2025-05-11', '19:45', 10, 450, 430, 48.00, 'Concert', 10);

insert into customer (customer_name, email, phone_number, booking_id) values
('Alice Smith', 'alice@example.com', '1234567890', 1),
('Bob Johnson', 'bob@example.com', '2345678901', 2),
('Charlie Lee', 'charlie@example.com', '3456789012', 3),
('Diana Ross', 'diana@example.com', '4567890123', 4),
('Ethan Clark', 'ethan@example.com', '5678901234', 5),
('Fiona Green', 'fiona@example.com', '6789012345', 6),
('George Brown', 'george@example.com', '7890123456', 7),
('Hannah White', 'hannah@example.com', '8901234567', 8),
('Ian Black', 'ian@example.com', '9012345678', 9),
('Jenny Blue', 'jenny@example.com', '0123456789', 10);
