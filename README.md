# Vsearch Application

## Overview
<br>

xxxxxxxxxxxxxxxxx

## Data model

**log table**

| COLUMN  		| TYPE  	| CONSTRAINT  	|
|	---			|	---		|	---			|	
| id |  int auto_increment  	|   PRIMARY KEY	| 
|ts		|  timestamp	|   	| 
|phrase		|  varchar(128)		|   NOT NULL	| 
|letters			|  varchar(32) 	|   			| 
|ip		|  varchar(16)	|   			| 
|browser_string		|  varchar(256)	|   			| 
|results		|  varchar(64)		|   			| 


## Project Architecture
```
.
├── Makefile
├── README.md
├── config
│   └── .env.example
├── docker
│   └── docker-compose.yml
├── help
│   └── sql_query.sql
├── requirements.txt
├── tests
└── webapp
    ├── main.py
    ├── src
    │   ├── DBcm.py
    │   ├── decorator.py
    │   └── vsearch.py
    ├── static
    │   └── hf.css
    └── templates
        ├── base.html
        ├── entry.html
        ├── message.html
        ├── results.html
        └── viewlog.html
```

## Python File:

1. weabbp/
	- main.py: xxxxxxx

2. src/ 
	- DBcm.py : xxxxxxxx

	- decorator.py: xxxxxxxx

	- vsearch.py: xxxxxxxxxx 

## How to run scripts
<br>

First of all, initialize a virtual environment with project dependency, using the script bellow.
Then set the `.env` in config file (if you have some problem, there is `.env.example` for support):

``` bash
make install && source venv/bin/activate
```

``` bash
docker-compose -f docker/docker-compose.yml up -d 
```

``` bash
docker ps
```

``` bash
docker exec -it 'id_docker' bash
```

``` bash
mysql -u root -p 
```
after inform password


In the help folder, copy the database command and execute:
``` bash
create database vsearchlogDB;
```

```bash
use vsearchlogDB;
```

``` bash 
grant all on vsearchlogDB.* to 'vsearch' identified by 'password';
```

```bash
create table log(
id int auto_increment primary key,
ts timestamp default current_timestamp,
phrase varchar(128) not null,
letters varchar(32) not null,
ip varchar(16) not null,
browser_string varchar(256) not null,
results varchar(64) not null);
```

Run python script that consist in execute application:
``` bash
python3 webapp/main.py
```
