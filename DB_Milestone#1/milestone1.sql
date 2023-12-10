create database if not exists wuzzuf;
use wuzzuf;
 
create table if not exists user(
	email varchar(50) not null primary key,
    username varchar(50) not null, -- assuming size
    password varchar(50) not null, -- assuming size
    country varchar(25), -- longest country name is Bosnia and Herzegovina
    city varchar(25), -- assuming no city is longer than the longest country
    district varchar(25), -- same assumption as above
    experience double, -- as in case of less than 1 year
    GPA double, 
    phone_num varchar(15), -- assuming size
    foreign key (phone_num) references general_info(phone_num)
);

create table if not exists user_skill(
	skill varchar(50), -- assuming size
    email varchar(50) ,
	foreign key (email) references user(email) on delete set null on update cascade
);

create table if not exists general_info(
	phone_num varchar(15) not null primary key,
    BOD date not null,
    gender char not null,
    nationality varchar(25) not null, -- same as country
    marital_status varchar(11), -- values given on the website do not exceed length of 11
    country varchar(25) not null,
    city varchar(25) not null, 
    area varchar(25),
    relocation bool, -- question about if willing to relocate for job
    postal_code varchar(15), -- assuming size
    first_name varchar(15) not null, -- assuming size
    middle_name varchar(15), -- assuming size
    last_name varchar(15) not null, -- assuming size
    military_status varchar(15), -- values given on the website do not exceed this length
    dependents_num int,
    driving_license bool,
    tag_line varchar(20)
);

create table if not exists general_info_alternative(
	phone_num varchar(15),
    alternative varchar(15),  -- alternative phone numbers
    foreign key (phone_num) references general_info(phone_num) on delete set null on update cascade
);

create table if not exists company(
	email varchar(50) primary key,
    career_level varchar(17),
    job_title varchar(50) not null,
    search_status int not null, -- job search status has 5 options that I am representing as integers. Moreoever, a value is given by default, so no NULL
    find bool not null, -- Let companies find me on WUZZUF by default is true
    public_profile bool not null, -- by default the profile is public
    salary_num int not null, 
    salary_currency varchar(35) not null, -- the maximum possible length according to values given, and there is a default value
    salary_period varchar(5) not null, -- same as above
    salary_hide bool not null, -- choose to hide salary from companies
    foreign key (email) references user(email) on update cascade
);

create table if not exists career_interest_category(
	job_category varchar(50) not null,
    email varchar(50),
    foreign key (email) references user(email) on update cascade,
    primary key(job_category, email)
);

create table if not exists career_interest_type(
	job_type varchar(20), -- it is not a must to enter a value for it
    email varchar(50),
    foreign key (email) references user(email) on update cascade,
    primary key(job_type, email)
);

create table if not exists career_interest_title(
	job_title varchar(50) not null,
    email varchar(50),
    foreign key (email) references user(email) on update cascade,
    primary key(job_title, email)
);

create table if not exists career_interest_location(
	email varchar(50),
	country varchar(25),
    city varchar(25),
    foreign key (email) references user(email) on delete set null on update cascade,
    primary key (email, country, city)
);

create table if not exists company(
	company_name varchar(50) not null primary key,
    business_email varchar(50) not null, -- employer business email
    emp_fname varchar(15) not null,
    emp_lname varchar(15) not null,
    found_date date,
    size_min int,
    size_max int,
    country varchar(25) not null, -- by default it is Egypt
    city varchar(25),
    district varchar(25),
    description varchar(15000), -- assuming size
    URL varchar(1000) -- assuming size
);

create table if not exists company_sector(
	company_name varchar(50),
    sector varchar(100) ,
	foreign key (company_name) references company(company_name) on update cascade,
	primary key(company_name, sector)
);

create table if not exists job_posting(
    job_title varchar(50) not null, -- assuming size
    country varchar(25) not null,
    city varchar(25) not null,
    district varchar(25),
    description varchar(15000) not null, 
    requirements varchar(1000), -- assuming  size, and it can be emoty
    post_type varchar(10) not null, -- job or internship
    post_date date not null,
    viewed int, -- #applicatns viewed for this job posting
	considered int, -- #applicants considered for this job posting
    experience_min int,
    experience_max int,
    salary_min int not null,
    salary_max int not null,
    hidden_salary bool not null,
    vacancies int not null,
    career_level varchar(17) not null,
    education_level varchar(20),
	company_name varchar(50),
    foreign key (company_name) references company(company_name) on update cascade,
	primary key (company_name, job_title, country, city, district)
);

-- ALTER TABLE job_posting
-- ADD INDEX jccd (job_title, country, city, district);

CREATE TABLE IF NOT EXISTS job_posting_type (
	company_name varchar(50),
    job_title varchar(50),
    country varchar(25),
    city varchar(25),
    district varchar(25),
    job_type varchar(20) not null,
    primary key (company_name, job_title, country, city, district, job_type),
    constraint fk1 foreign key (job_title, country, city, district) references job_posting(job_title, country, city, district) on update cascade, 
    constraint fk2 foreign key (company_name) references company(company_name)

);

create table if not exists job_posting_category(
	company_name varchar(50),
    job_title varchar(50), 
    country varchar(25),
    city varchar(25) ,
    district varchar(25),
    job_category varchar(50) not null,
	primary key (company_name, job_title, country, city, district, job_category),
    constraint category_fk1 foreign key (job_title, country, city, district) references job_posting(job_title, country, city, district) on update cascade, 
    constraint category_fk2 foreign key (company_name) references company(company_name)
);

create table if not exists job_posting_keyword(
	company_name varchar(50),
    job_title varchar(50), 
    country varchar(25),
    city varchar(25) ,
    district varchar(25),
    keyword varchar(20) not null,
    primary key (company_name, job_title, country, city, district, keyword),
    constraint keyword_fk1 foreign key (job_title, country, city, district) references job_posting(job_title, country, city, district) on update cascade, 
    constraint keyword_fk2 foreign key (company_name) references company(company_name)
);

create table if not exists job_posting_skill(
	company_name varchar(50),
    job_title varchar(50), 
    country varchar(25),
    city varchar(25) ,
    district varchar(25),
    skill varchar(50) not null,
    primary key (company_name, job_title, country, city, district, skill),
    constraint skill_fk1 foreign key (job_title, country, city, district) references job_posting(job_title, country, city, district) on update cascade, 
    constraint skill_fk2 foreign key (company_name) references company(company_name)
);

create table if not exists apply(
	email varchar(50),
    job_title varchar(50), 
    country varchar(25),
    city varchar(25) ,
    district varchar(25),
    app_date date not null,
    cover_letter varchar(5000), -- assuming size
    question varchar(1000), -- includes all questions
    answer varchar(6000), -- includes all applicant answers
    primary key(email, job_title, country, city, district),
    constraint apply_fk1 foreign key (email) references user(email),
	constraint apply_fk2 foreign key (job_title, country, city, district) references job_posting(job_title, country, city, district) on update cascade
);

create table if not exists saved_jobs(
	email varchar(50),
    job_title varchar(50), 
    country varchar(25),
    city varchar(25) ,
    district varchar(25),
    primary key(email, job_title, country, city, district),
    constraint saved_fk1 foreign key (email) references user(email),
	constraint saved_fk2 foreign key (job_title, country, city, district) references job_posting(job_title, country, city, district) on update cascade
);

show tables;