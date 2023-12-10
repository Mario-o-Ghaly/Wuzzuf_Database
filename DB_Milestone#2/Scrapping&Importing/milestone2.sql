create database if not exists wuzzuf;
use wuzzuf;

-- alter table user
-- modify column phone_num varchar(30);
-- add column experience int,
-- drop column experience_min,
-- drop column experience_max;

create table if not exists user(
	email varchar(50) not null primary key,
    username varchar(50) not null, -- assuming size
    password varchar(50) not null, -- assuming size
    country varchar(50), -- longest country name is Bosnia and Herzegovina
    city varchar(25), -- assuming no city is longer than the longest country
    district varchar(25), -- same assumption as above
    experience int, -- as if it is experience+ years
    no_experience bool, -- true if zero experience
    GPA double, 
    phone_num varchar(20), -- assuming size
    BOD date,
    gender char,
    first_name varchar(15) not null, -- assuming size
	middle_name varchar(15), -- assuming size
	last_name varchar(15) not null -- assuming size
);

create table if not exists user_skill(
	skill varchar(50) not null, -- assuming size
    email varchar(50),
	foreign key (email) references user(email) on update cascade,
    primary key(email, skill)
);

-- drop table apply;
-- drop table saved_jobs;
-- drop table job_posting_type;
-- drop table job_posting_category;
-- drop table job_posting_skill;
-- drop table job_posting;


create table if not exists company(
	company_name varchar(500) not null primary key,
    description varchar(10000) default NULL, -- assuming size
    country varchar(50) not null, -- by default it is Egypt
    city varchar(25) default NULL,
    found_date date default NULL,
    size_min int default NULL,
    size_max int default NULL
);


create table if not exists company_sector(
	company_name varchar(500),
    sector varchar(50) ,
	foreign key (company_name) references company(company_name) on update cascade,
	primary key(company_name, sector)
);

-- ALTER TABLE job_posting
-- MODIFY COLUMN job_title varchar(100);

-- ALTER TABLE job_posting
-- -- drop index jccd;
-- ADD INDEX jccd (job_title, country, city, district, company_name);


create table if not exists job_posting(
    job_title varchar(100) not null, -- assuming size
    country varchar(50) not null,
    city varchar(25) not null,
    district varchar(25),
    description varchar(5000) not null, 
    requirements varchar(2000), -- assuming  size, and it can be emoty
    post_date date not null,
    viewed int, -- #applicatns viewed for this job posting
	considered int, -- #applicants considered for this job posting
    experience_min int,
    experience_max int,
    salary_min int, -- was not null
    salary_max int, -- was not null
    hidden_salary bool not null,
    vacancies int, -- was not null
    career_level varchar(50), -- was not null
    education_level varchar(50),
	company_name varchar(500),
    gender char(1),
    foreign key (company_name) references company(company_name) on update cascade,
	primary key (company_name, job_title, country, city, district)
);


CREATE TABLE IF NOT EXISTS job_posting_type (
	company_name varchar(500),
    job_title varchar(100),
    country varchar(50),
    city varchar(25),
    district varchar(25),
    job_type varchar(20) not null,
    primary key (company_name, job_title, country, city, district, job_type),
    constraint fk1 foreign key (job_title, country, city, district, company_name) references job_posting(job_title, country, city, district, company_name) on update cascade
    );

create table if not exists job_posting_category(
	company_name varchar(500),
    job_title varchar(100), 
    country varchar(50),
    city varchar(25) ,
    district varchar(25),
    job_category varchar(50) not null,
	primary key (company_name, job_title, country, city, district, job_category),
    constraint category_fk1 foreign key (job_title, country, city, district, company_name) references job_posting(job_title, country, city, district, company_name) on update cascade 
);

create table if not exists job_posting_skill(
	company_name varchar(500),
    job_title varchar(100), 
    country varchar(50),
    city varchar(25) ,
    district varchar(25),
    skill varchar(50) not null,
    primary key (company_name, job_title, country, city, district, skill),
    constraint skill_fk1 foreign key (job_title, country, city, district, company_name) references job_posting(job_title, country, city, district, company_name) on update cascade
);

create table if not exists apply(
	email varchar(50),
	company_name varchar(500),
    job_title varchar(100), 
    country varchar(50),
    city varchar(25) ,
    district varchar(25),
    app_date date not null,
    cover_letter varchar(5000), -- assuming size
    question varchar(1000), -- includes all questions
    answer varchar(6000), -- includes all applicant answers
    primary key(email, job_title, country, city, district),
    constraint apply_fk1 foreign key (email) references user(email),
	constraint apply_fk2 foreign key (job_title, country, city, district,company_name) references job_posting(job_title, country, city, district, company_name) on update cascade
);


-- here is the loading

-- company table
-- I used insertion statements instead
   
-- company_sector table   
-- This worked fine
LOAD DATA INFILE 'company_sector.csv'
IGNORE INTO TABLE company_sector
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- job_posting table was done by inserting statements

-- job_posting_type, category, and skills were done by inserting statements

-- user table
LOAD DATA INFILE 'user.csv'
INTO TABLE user
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(email, username, password, country, city, district, experience, no_experience, GPA, phone_num, @BOD, gender, first_name, middle_name, last_name)
SET BOD = STR_TO_DATE(@BOD, '%Y-%m-%d');

LOAD DATA INFILE 'more_users.csv'
IGNORE INTO TABLE user
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(email, username, password, country, city, district, experience, no_experience, GPA, phone_num, @BOD, gender, first_name, middle_name, last_name)
SET BOD = STR_TO_DATE(@BOD, '%Y-%m-%d');  

LOAD DATA INFILE 'more_more_users.csv'
IGNORE INTO TABLE user
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(email, username, password, country, city, district, experience, no_experience, GPA, phone_num, @BOD, gender, first_name, middle_name, last_name)
SET BOD = STR_TO_DATE(@BOD, '%Y-%m-%d');  


INSERT INTO apply(email, company_name, job_title, country, city, district, app_date, cover_letter, question, answer)
VALUES('alan51@example.org', '(MSA) October University', 'Oracle Developer',  'Egypt', 'Giza', '6th of October', '2023-10-30',NULL, NULL, NULL);

INSERT INTO apply(email, company_name, job_title, country, city, district, app_date, cover_letter, question, answer)
VALUES('alan51@example.org', '2oolAmeme', 'Unity Game Developer',  'Egypt', 'Cairo', '', '2023-09-01',NULL, NULL, NULL);

INSERT INTO apply(email, company_name, job_title, country, city, district, app_date, cover_letter, question, answer)
VALUES('brandon97@example.org', 'Air Products (Middle East) FZE', 'Operational Excellence Mechanical Integrity Engineer', 'Saudi Arabia', 'Khobar', '', '2022-12-12','I am really interested in this job position, and I will put A effort', 'Have you worked in mechanical integrity before?', 'Yes, this is not my first time working on a project related to this field');

INSERT INTO apply(email, company_name, job_title, country, city, district, app_date, cover_letter, question, answer)
VALUES('stephen40@example.org', 'Air Products (Middle East) FZE', 'Operational Excellence Mechanical Integrity Engineer', 'Saudi Arabia', 'Khobar', '', '2022-12-12',NULL, NULL, NULL);

-- delete from job_posting_skill where job_title ='';
-- delete from job_posting_category where job_title ='';
-- delete from job_posting_type where job_title ='';
-- delete from job_posting where company_name = '';
