import pymysql
from tkinter import *
import sqlite3
import makepass
import tkinter as tk

import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

mydb = pymysql.connect(host='db4free.net',
                             user="mario_ghaly",
                              password="sql8663333",
                             database="wuzzuff",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
mycursor = mydb.cursor()
global_email = ""
global_username = ""

def entry_page():
    condition = True
    while condition:
        print("This is Wuzzuf for IT/Software jobs and internships. Welcome!\nChoose what you want to do by entering its number:")
        print("1. Login\n2. Register")
        inp = input()
        if inp == '1':
            condition = False
            login()
        elif inp == '2':
            condition = False
            register()
        else:
            print("Please Select a valid option!")


def login():
    global global_email
    global global_username
    condition = True
    while condition:
        email = input("Please enter your email address: ")
        password = input("Please enter your password: ")
        sql = """SELECT * FROM user WHERE email = %s AND password = %s"""
        mycursor.execute(sql, (email, password))
        result = mycursor.fetchall()
        if len(result):  
            global_email = email
            global_username = result[0]['username']
            # print(global_username)
            condition = False
            main_page()
        else:
            print("ERROR: Incorrect email address or password\n You have 3 options:\n1. Try logging in again\n2. Register\n3. Exit")
            inp = input()
            if inp == '2':
                condition = False
                register()
            elif inp == '3':
                condition = False
                exit()


def register():
    global global_email
    global global_username
    condition = True
    while condition:
        try:
            email = input("Please enter your email address: ")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            country = input("Please enter your country or N/A if you don't want to: ")
            city = input("Please enter your city or N/A if you don't want to: ")
            district = input("Please enter your district or N/A if you don't want to: ")
            experience = input("Please enter years of experience number or N/A if you don't want to: ")
            GPA = input("Please enter your GPA or N/A if it doesn't exist: ")
            phone_num = input("Please enter your phone number or N/A if you don't want to: ")
            BOD = input("Please enter your date of birth in this format yyyy-mm-dd or N/A if you don't want to: ")
            gender = input("Please enter your gender as M or F or N/A if you don't want to: ")
            first_name = input("Please enter your first name: ")
            middle_name = input("Please enter your middle name or N/A if you don't want to: ")
            last_name = input("Please enter your last name: ")
            no_experience = '1' if experience in ('0','N/A')  else '0'

            sql = """INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            # values = ('yy@gmail.com','xy', '1234', 'France', 'Paris', 'Eiffel', '0', '1', 'N/A', '01288888777', '2019-01-01', 'F', 'Ethel', 'Basma', 'Prevost' )
            values = (email, username, password, country, city, district, experience, no_experience, GPA, phone_num, BOD, gender, first_name, middle_name, last_name)
            values = tuple(None if v == 'N/A' else v for v in values)
            mycursor.execute(sql, values)
            mydb.commit()
            print("Your account has been created successfully!")
            global_username = username
            global_email = email
            condition = False
            main_page()
        except pymysql.DataError:
            print("Error: Incorrect Data Type\n")
        except pymysql.err.IntegrityError:
            print("Error: Email address exists or your input doesn't match the requested data\n") 
        print("You have 3 options:\n1. Try registering again\n2. Login\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            login()
        elif(inp == '3'):
            condition = False
            exit()


def main_page():
    global global_email
    global global_username
    print("\nHello "+ global_username+", Welcome on Wuzzuf!")
    condition = True
    while condition:
        print("Please choose which query you want to do by entering its number: ")
        inp = input("1. Apply for a job posting\n"+
              "2. View all job postings for a given sector\n"+
              "3. View all job postings for a given set of skills\n"+
              "4. View the top 5 sectors by number of job posts, and the average salary range for each\n"+
              "5. View the top 5 skills that are in the highest demand\n"+
              "6. View the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date\n"+
              "7. View the top 5 most paying companies in the field in Egypt\n"+
              "8. View all the postings for a given company / organization\n"+
              "9. View the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings\n"+
              "10. Log out\n"+
              "11. Exit\n"
              )
        if(inp == '1'):
            condition= False
            one()
        elif(inp == '2'):
            condition= False
            two()
        elif(inp == '3'):
            condition= False
            three()
        elif(inp == '4'):
            condition= False
            four()
        elif(inp == '5'):
            condition= False
            five()
        elif(inp == '6'):
            condition = False
            six()
        elif(inp == '7'):
            condition= False
            seven()
        elif(inp == '8'):
            condition= False
            eight()
        elif(inp == '9'):
            condition= False
            nine()
        elif(inp == '10'):
            condition= False
            entry_page()
        elif(inp == '11'):
            condition = False #exit()
            exit()
        else:
            print("Please select a valid option")


def one():
    condition = True
    while condition:
        try:
            inp = input("\nPlease choose your preferred option by entering its number:\n" +
                        "1. Apply for a job post by entering its: (company name, job title, job country, job city, job district if exists)\n" +
                        "2. View all job posts first, then apply for your desired one\n")

            if inp == '1':
                print("Please enter the details of the job post you want to apply for: ")
                company_name = input("company name: ")
                job_title = input("job title: ")
                country = input("job country: ")
                city = input("job city: ")
                district = input("job district(enter N/A if not specified): ")
                
                if district == 'N/A':
                    district = ""

                app_date = datetime.now().strftime('%Y-%m-%d')

                sql = """INSERT INTO apply (company_name, job_title, country, city, district, email, app_date) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                values = (company_name, job_title, country, city, district, global_email, app_date)

                mycursor.execute(sql, values)
                mydb.commit()
                print("Your application has been received successfully!")

            elif inp == '2':
                sql = """SELECT * FROM job_posting;"""
                mycursor.execute(sql)
                result = mycursor.fetchall()
                cnt = 0

                for r in result:
                    print("job#" + str(cnt) + ">> " + str(r))
                    cnt += 1

                cnt = int(input("Now, select the job number that you desire to apply for: "))
                app_date = datetime.now().strftime('%Y-%m-%d')

                values = (
                    result[cnt]['company_name'],
                    result[cnt]['job_title'],
                    result[cnt]['country'],
                    result[cnt]['city'],
                    result[cnt]['district'],
                    global_email,
                    app_date
                )
                print(values)

                sql = """INSERT INTO apply (company_name, job_title, country, city, district, email, app_date) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                mycursor.execute(sql, values)
                mydb.commit()
                print("Your application has been received successfully!")

            else:
                print("Please enter a valid option: ")
        
        except pymysql.DataError:
            print("Error: Incorrect Data Type\n")
        except pymysql.err.IntegrityError:
            print("Error: You have applied for this job post before, or it doesn't exist\n") 

        print("You have 3 options:\n1. Try applying again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False
            exit()


def two():
    condition = True
    while condition:
        try:
            sector = input("\nPlease enter the sector you like to view all job posts under it: ")
            sql = """SELECT * FROM job_posting jp INNER JOIN company_sector cs ON jp.company_name = cs.company_name WHERE cs.sector = %s;"""
            mycursor.execute(sql, sector)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error in your input!")
        print("\nYou have 3 options:\n1. Do the same query again with different input\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()


#3. View all job postings for a given set of skills
def three():
    condition = True
    while condition:
        try:
            print("\nPlease enter the skills you like to view all job posts under it separated by a new line\nWhen you finish, press an extra Enter:")
            skills = []
            cnt = 1
            while True:
                skill = input()
                if not skill:
                    break
                skills.append(skill)
            sql = """SELECT jp.* FROM job_posting jp"""
            cnt = 1
            while cnt <= len(skills):
                sql += f""" INNER JOIN job_posting_skill js{cnt} ON jp.company_name = js{cnt}.company_name AND jp.job_title = js{cnt}.job_title AND jp.country = js{cnt}.country AND jp.city = js{cnt}.city AND jp.district = js{cnt}.district"""
                cnt += 1
            cnt = 1
            sql += """ WHERE"""
            while cnt <= len(skills):
                sql += f""" js{cnt}.skill = '{skills[cnt-1]}' AND"""
                cnt += 1
            sql = sql[:-4]
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error in your input!")
        print("\nYou have 3 options:\n1. Do the same query again with different input\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()


def four():
    condition = True
    while condition:
        try:
            inp = input("\nDo you want to view #posts under this sector as well? Enter: YES or NO>> ")
            if inp == 'YES':
                sql = """SELECT cs.sector, COUNT(*) AS job_posts_number, AVG(jp.salary_max - jp.salary_min) AS Average_Salary_Range FROM company_sector cs
                INNER JOIN job_posting jp ON jp.company_name = cs.company_name
                GROUP BY cs.sector
                ORDER BY COUNT(*) DESC
                LIMIT 5;"""
            else:
                sql = """SELECT cs.sector, AVG(jp.salary_max - jp.salary_min) AS Average_Salary_Range FROM company_sector cs
                INNER JOIN job_posting jp ON jp.company_name = cs.company_name
                GROUP BY cs.sector
                ORDER BY COUNT(*) DESC
                LIMIT 5;"""
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error happened while excuting")
        print("\nYou have 3 options:\n1. Do the same query again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()


def five():
    condition = True
    while condition:
        try:
            inp = input("\nDo you want to view #posts demanding each skill as well? Enter: YES or NO>> ")
            if inp == 'YES':
                sql = """SELECT js.skill, COUNT(*) AS Demand FROM job_posting_skill js
                GROUP BY js.skill
                ORDER BY Demand DESC
                LIMIT 5;"""
            else:
                sql = """SELECT js.skill FROM job_posting_skill js
                GROUP BY js.skill
                ORDER BY COUNT(*) DESC
                LIMIT 5;"""
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error happened while excuting")
        print("\nYou have 3 options:\n1. Do the same query again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()


def six():
    condition = True
    while condition:
        try:
            inp = input("\nDo you want to view the startups foundation date along with their amount of vacancies as well? Enter: YES or NO>> ")
            if inp == 'YES':
                sql = """SELECT c.company_name, c.found_date, COUNT(*) AS vacancies FROM company c
                INNER JOIN job_posting jp ON jp.company_name = c.company_name
                WHERE c.country = 'Egypt'
                GROUP BY(c.company_name)
                ORDER BY(COUNT(*)/DATEDIFF(CURDATE(), c.found_date)) DESC
                LIMIT 5;"""
            else:
                sql = """SELECT c.company_name FROM company c
                INNER JOIN job_posting jp ON jp.company_name = c.company_name
                WHERE c.country = 'Egypt'
                GROUP BY(c.company_name)
                ORDER BY(COUNT(*)/DATEDIFF(CURDATE(), c.found_date)) DESC
                LIMIT 5;"""
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error happened while excuting")
        print("\nYou have 3 options:\n1. Do the same query again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()


def seven():
    condition = True
    while condition:
        try:
            inp = input("\nDo you want to view the companies average salary as well? Enter: YES or NO>> ")
            if inp == 'YES':
                sql = """SELECT c.company_name, AVG((jp.salary_max + jp.salary_min)/2) AS Average_Salary FROM company c
            INNER JOIN job_posting jp ON jp.company_name = c.company_name
            WHERE c.country = 'Egypt'
            GROUP by c.company_name
            ORDER BY AVG((jp.salary_max + jp.salary_min)/2) DESC
            LIMIT 5;"""
            else:
                sql = """SELECT c.company_name FROM company c
                INNER JOIN job_posting jp ON jp.company_name = c.company_name
                WHERE c.country = 'Egypt'
                GROUP by c.company_name
                ORDER BY AVG((jp.salary_max + jp.salary_min)/2) DESC
                LIMIT 5;"""
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error happened while excuting")
        print("\nYou have 3 options:\n1. Do the same query again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()


def eight():
    condition = True
    while condition:
        try:
            inp = input("\nPlease enter the desired company / organization: ")
            sql = """SELECT * FROM job_posting WHERE company_name = %s;"""
            mycursor.execute(sql, inp)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error happened while excuting")
        print("\nYou have 3 options:\n1. Do the same query again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit() 
            exit()


def nine():
    condition = True
    while condition:
        try:
            inp = input("\nDo you want to view #postings under these categories as well? Enter: YES or NO>> ")
            if inp == 'YES':
                sql = """SELECT job_category, COUNT(*) AS "#postings" FROM job_posting_category
                WHERE job_category != 'IT/Software Development'
                GROUP BY job_category
                ORDER BY COUNT(*) DESC
                LIMIT 5;"""
            else:
                sql = """SELECT job_category FROM job_posting_category
                WHERE job_category != 'IT/Software Development'
                GROUP BY job_category
                ORDER BY COUNT(*) DESC
                LIMIT 5;"""
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for r in result:
                print(r)
            print("#rows = " + str(len(result)))
        except pymysql.err.IntegrityError:
            print("Error happened while excuting")
        print("\nYou have 3 options:\n1. Do the same query again\n2. Return to main page\n3. Exit")
        inp = input()
        if(inp == '2'):
            condition = False
            main_page()
        elif(inp == '3'):
            condition = False  #exit()
            exit()

entry_page()