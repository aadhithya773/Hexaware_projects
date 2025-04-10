create database sisdb;
go
use sisdb;
go

create table students (
    student_id int identity(1,1) primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    date_of_birth date not null,
    email varchar(100) unique not null,
    phone_number varchar(15) not null
);
insert into students (first_name, last_name, date_of_birth, email, phone_number) values
('alice', 'smith', '2000-05-10', 'alice.smith@example.com', '9876543210'),
('bob', 'johnson', '1999-03-20', 'bob.johnson@example.com', '8765432109'),
('charlie', 'lee', '2001-07-15', 'charlie.lee@example.com', '7654321098'),
('david', 'brown', '2000-11-22', 'david.brown@example.com', '6543210987'),
('eve', 'davis', '1998-12-30', 'eve.davis@example.com', '5432109876'),
('frank', 'miller', '1999-01-05', 'frank.miller@example.com', '4321098765'),
('grace', 'wilson', '2000-09-09', 'grace.wilson@example.com', '3210987654'),
('hank', 'moore', '2001-04-17', 'hank.moore@example.com', '2109876543'),
('ivy', 'taylor', '1997-10-08', 'ivy.taylor@example.com', '1098765432'),
('jack', 'anderson', '2002-06-01', 'jack.anderson@example.com', '9988776655');

create table teacher (
teacher_id int identity(1,1) primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(100) unique not null
);
insert into teacher (first_name, last_name, email) values
('john', 'mathews', 'john.mathews@univ.edu'),
('sarah', 'connor', 'sarah.connor@univ.edu'),
('alan', 'turing', 'alan.turing@univ.edu'),
('ada', 'lovelace', 'ada.lovelace@univ.edu'),
('elon', 'musk', 'elon.musk@univ.edu'),
('marie', 'curie', 'marie.curie@univ.edu'),
('steve', 'jobs', 'steve.jobs@univ.edu'),
('jane', 'goodall', 'jane.goodall@univ.edu'),
('richard', 'feynman', 'richard.feynman@univ.edu'),
('nikola', 'tesla', 'nikola.tesla@univ.edu');

create table courses (
    course_id int identity(1,1) primary key,
    course_name varchar(100) not null,
    credits int not null check (credits > 0),
    teacher_id int null,
    foreign key (teacher_id) references teacher(teacher_id)
);
insert into courses (course_name, credits, teacher_id) values
('data structures', 4, 1),
('operating systems', 3, 2),
('database systems', 3, 3),
('software engineering', 3, 4),
('ai and ml', 4, 5),
('computer networks', 3, 6),
('compiler design', 4, 7),
('cybersecurity', 3, 8),
('iot applications', 2, 9),
('embedded systems', 3, 9);

create table enrollments (
    enrollment_id int identity(1,1) primary key,
    student_id int not null,
    course_id int not null,
    enrollment_date date not null,
    foreign key (student_id) references students(student_id),
    foreign key (course_id) references courses(course_id)
);
insert into enrollments (student_id, course_id, enrollment_date) values
(1, 1, '2024-06-10'),
(1, 2, '2024-06-11'),
(2, 3, '2024-06-12'),
(3, 1, '2024-06-13'),
(4, 4, '2024-06-14'),
(5, 5, '2024-06-15'),
(6, 6, '2024-06-16'),
(7, 7, '2024-06-17'),
(8, 8, '2024-06-18'),
(9, 9, '2024-06-19');

create table payments (
    payment_id int identity(1,1) primary key,
    student_id int not null,
    amount decimal(10,2) not null check (amount > 0),
    payment_date date not null,
    foreign key (student_id) references students(student_id)
);
insert into payments (student_id, amount, payment_date) values
(1, 1500.00, '2025-06-20'),
(2, 1800.50, '2024-06-21'),
(3, 1300.75, '2025-06-22'),
(4, 2000.00, '2025-06-23'),
(5, 2500.00, '2024-06-24'),
(6, 1200.00, '2024-06-25'),
(7, 1600.00, '2025-06-26'),
(8, 1450.00, '2024-06-27'),
(9, 1750.00, '2024-06-28'),
(10, 1900.00, '2025-06-29');
select*from students;
select*from teacher;
select*from courses;
select*from enrollments;
select*from payments ;
--Task 2 select ,where,between and like:-----------
--1.
insert into students (first_name, last_name, date_of_birth, email, phone_number)
values ('john', 'doe', '1995-08-15', 'john.doe@example.com', '1234567890');

--2.enroll a student in a course
insert into enrollments (student_id, course_id, enrollment_date)
values (1, 2, '2025-04-08');
select * from students;
select * from courses;
--3.updating records
update teacher
set email='abc@example.com'
where teacher_id=1;
--4.deleting the records
delete from enrollments
where student_id=2 and course_id=3;
--5.update course
update courses
set teacher_id=2
where course_id=5;
--6.delete specific student and enroll
delete from enrollments
where student_id=3;
-----this cant be done because Before deleting a student, you must delete all dependent records in child tables — like enrollments and payments.
delete from students
where student_id=3;

--7.
update payments
set amount = 5500.00
where payment_id = 3;

---Task 3 aggregate functions-----
--1.writing a query to calc total payments---
select s.first_name,s.last_name,sum(p.amount)as total_payment
from students s
join payments p on s.student_id=p.student_id
where s.student_id =1
group by s.first_name,s.last_name;

--2.count of students---
select c.course_name, count(e.student_id) as student_count
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_name
order by student_count desc;

--3.students not enroll in any course
select s.student_id, s.first_name, s.last_name
from students s
left join enrollments e on s.student_id = e.student_id
where e.enrollment_id is null;

--4.stud and names of course enrolled--
select s.first_name, s.last_name, c.course_name
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id;

--5.teachers and the courses--
select t.first_name, t.last_name, c.course_name
from teacher t
join courses c on t.teacher_id = c.teacher_id;

--6. stuents and their enrollments dates for a specific course
select s.first_name,s.last_name,c.course_name,e.enrollment_date
from students s
join enrollments e on s.student_id=e.student_id
join courses c on e.course_id=c.course_id
where c.course_id=2;

--7.students not made any payments---
select s.student_id, s.first_name, s.last_name
from students s
left join payments p on s.student_id = p.student_id
where p.payment_id is null;

--8.courses that have no enrollments
select c.course_id, c.course_name
from courses c
left join enrollments e on c.course_id = e.course_id
where e.enrollment_id is null;

--9.stud enroll in more than 1 course
select s.student_id, s.first_name, s.last_name, count(e.course_id) as course_count
from students s
join enrollments e on s.student_id = e.student_id
group by s.student_id, s.first_name, s.last_name
having count(e.course_id) > 1;

--10.teachers not assigned to any courses
select t.teacher_id, t.first_name, t.last_name
from teacher t
left join courses c on t.teacher_id = c.teacher_id
where c.course_id is null;

--Task 4 subquery and its types
--1. Average number of students enrolled in each course--
select avg(enrollment_count) as avg_students_per_course
from (
    select course_id, count(student_id) as enrollment_count
    from enrollments
    group by course_id
) as course_enrollments;


--2. Student(s) who made the highest payment--
select s.first_name, s.last_name, p.amount
from students s
join payments p on s.student_id = p.student_id
where p.amount = (
select max(amount)
from payments);

--4.Total payments made to courses taught by each teacher
select t.first_name, t.last_name, 
( select sum(p.amount)
  from payments p
  join enrollments e on p.student_id = e.student_id
  join courses c2 on e.course_id = c2.course_id
  where c2.teacher_id = t.teacher_id) 
  as total_payment
from teacher t;

--5.Students enrolled in all available courses--
select s.student_id, s.first_name, s.last_name
from students s
where (
select count(distinct e.course_id)
from enrollments e
where e.student_id = s.student_id) = (select count(*)from courses);

--6.Teachers not assigned to any courses
select first_name, last_name
from teacher
where teacher_id not in (
select distinct teacher_id
from courses
where teacher_id is not null);

--7. avg of all stud
select avg(datediff(year, date_of_birth, getdate())) as avg_age
from students;

--8.courses with no enrollments
select course_name
from courses
where course_id not in (
    select distinct course_id
    from enrollments
);
--9.total payments made by each student
select s.first_name, s.last_name, c.course_name, sum(p.amount) as total_payment
from payments p
join students s on s.student_id = p.student_id
join enrollments e on e.student_id = p.student_id
join courses c on c.course_id = e.course_id
group by s.first_name, s.last_name, c.course_name;

--10.stude made more than 1 payment
select s.first_name, s.last_name, count(p.payment_id) as payment_count
from students s
join payments p on s.student_id = p.student_id
group by s.first_name, s.last_name
having count(p.payment_id) > 1;

--11.Total payments made by each student--
select s.first_name, s.last_name, sum(p.amount) as total_payment
from students s
join payments p on s.student_id = p.student_id
group by s.first_name, s.last_name;

--12.course and count of enrolled students--
select c.course_name, count(e.student_id) as total_enrolled
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_name;

--13.Average payment amount made by students--
select s.first_name, s.last_name, avg(p.amount) as avg_payment
from students s
join payments p on s.student_id = p.student_id
group by s.first_name, s.last_name;

select*from courses;
select*from enrollments;
select*from teacher;

select course_id, enrollment_count
from (
    select course_id, count(student_id) as enrollment_count
    from enrollments e
    group by course_id
) as sub;


