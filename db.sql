create database db_books;
use db_books;

create table libros(
	id int primary key auto_increment,
    nombre varchar(100) not null,
    autor varchar(100) not null,
    imagen varchar(100) not null,
    precio decimal(10,2) not null
);