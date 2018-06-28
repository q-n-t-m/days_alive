#while True: # this is an infinite loop
    #your_name = input("Enter your name:")
    #print("hello,", your_name)



# exercise to get someones birthday and tell them how many days they have been alive

import datetime
import time

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

user_birth_year = input("what year were you born in?")
while len(user_birth_year) == 2:
    user_birth_year = input("sorry I am expecting a 4-digit year. please try again")
user_birth_month = input("what month were you born in?")
# normalizing user input to the canonical before doing look-up
#the canonical version is the lower case first three letter of every month
user_birth_month = user_birth_month.lower()
user_birth_month = user_birth_month[:3]
if user_birth_month in months:
    user_birth_month = months.index(user_birth_month) + 1

user_birth_day = input("what day were you born?")

user_birthdate = datetime.date(int(user_birth_year), int(user_birth_month), int(user_birth_day))
now_date = datetime.date.today()

days_alive = now_date - user_birthdate
print("you have been alive for:", days_alive.days, 'days')