-- create database University
 -- use university

/*create table student
(id int auto_increment,
name varchar(30),
gmail varchar(30),
primary key(id)
);*/

/*insert into
student(id,name,gmail)
values
(1,'Chaitanya','chaitanya@gmail.com'),(2,'Varshini','varshini@gmail.com'),(3,'durga','durga@gmail.com');*/

/*      alter table student
change column id student_id int;*/
 /* select * from student*/

/*create table certificate
(certificate_id int auto_increment,
year int,
sem int,
primary key(certificate_id)
);*/

/*insert into certificate
(certificate_id,year,sem)
values(101,1,1),(102,1,2);*/

/*insert into certificate
(certificate_id,year,sem)
values(103,2,1),(104,2,2),(105,3,1),(106,3,2),(107,4,1),(108,4,2);*/
/*select * from certificate; */
/*insert into certificate
(year,sem)
values(2,1)*/
/*create table certificate_log
(student_id int,
certificate_id int,
received_date date,
foreign key(student_id) references student(student_id),
foreign key(certificate_id) references certificate(certificate_id)
);*/

/*insert into certificate_log
(student_id,certificate_id,received_date)
values(1,101,'2020-10-28'),(2,102,'2020-10-26');*/
-- select *  from certificate_log
/*truncate table certificate_log;*/

/*select * from certificate_log;*/

/*insert into certificate_log
(student_id,certificate_id,received_date)
values(1,101,'2020-10-28'),(2,102,'2020-10-26');*/

/* select * from certificate_log*/
 
/*insert into certificate_log
(student_id,certificate_id,received_date)
values(4,101,'2020-10-28'),(5,102,'2020-10-26');*/




