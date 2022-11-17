show databases;

create database vsearchlogDB;

use vsearchlogDB;

show tables;

grant all on vsearchlogDB.* to 'vsearch' identified by 'password';

create table log(
id int auto_increment primary key,
ts timestamp default current_timestamp,
phrase varchar(128) not null,
letters varchar(32) not null,
ip varchar(16) not null,
browser_string varchar(256) not null,
results varchar(64) not null);


select * from log;

select 
	id 
from
	log
where ip = '127.0.0.1'
order by ts desc;
