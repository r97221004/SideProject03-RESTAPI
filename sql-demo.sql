create database demo;
use demo;
show tables;
create table user(
 id int AUTO_INCREMENT PRIMARY KEY,
 username VARCHAR(64) NOT NULL UNIQUE,
 password_hash VARCHAR(128) NOT NULL,
 email VARCHAR(64) NOT NULL
 );
 
 show tables;
 desc user;
 
 insert into user(username, password_hash, email) values("Crystal", MD5("demo"), "demo@demo.com");
 
 select * from user;
 
 insert into user(username, password_hash, email) values("Matt", MD5("demo1"), "Matt@demo.com");
 
 select * from user;
 
 insert into user(username, password_hash, email) values("Matt", MD5("demo1"), "Matt@demo.com");
 
 drop database demo;
