# Python Projects for AI

# Project 1 ride or not

def ride (age,height,has_ticket,is_vip,heart_condition): # Python automatically treats the variable as True
    if age>=12 and height>=140 and not heart_condition and (has_ticket or is_vip):
        print("great, you can ride")
    else:
        print("sorry, you can't ride")
# first conditoin
ride(16,150,False,True,False) # True
# second condition 
ride(25,175,False,True,True) # False
# third condition
ride(14,145,False,True,False) # True

# Project 2 is student?

is_student= True
graduate= not is_student
print(graduate) # False

# project 3 Finding and replacing

for_ai="""I love AI, AI very important and we made 
the AI more powerfull with the RAG to make AI rely on our information.\n"""
print(for_ai)

# replace
print(for_ai.replace("AI","LLMS"))
llms=for_ai.replace("AI","LLMS")
print(llms)

# Find position
print(for_ai.count("AI")) # 4
print(for_ai.find("AI")) # 7

# Check if something exists  (True - False)
print("AI" in for_ai) # True
print(for_ai.startswith("I")) # True
print(for_ai.endswith("\n")) # True

# project 4 how you can manipulating items in list ?

jop=["nour",24,"AI Engineer"]
# how you add a new item ?
jop.append("from Egypt")
print(jop) # ['nour', 24, 'AI Engineer', 'from Egypt']
# how insert an item ?
jop.insert(1,"ashraf")
print(jop) # ['nour', 'ashraf', 24, 'AI Engineer', 'from Egypt']
# how you change an item ?
jop[1]="malik"
print(jop) # ['nour', 'malik', 24, 'AI Engineer', 'from Egypt']
# how you remove an item ?
jop.remove("nour")
print(jop) # ['malik', 24, 'AI Engineer', 'from Egypt']

# project 5 from  list getting back the whole element..

# loops get back the rest of the element.
myway=['eyeshadow code 2449','tent code 2218','lipstick code 7695']
# old way
for c in myway:
    if "2449" in c:
        print(c)
# new way
get_back=[item for item in myway if "7695" in item ]
print(get_back)
print(get_back[0]) # get it back without []

# if two or more elements have same value just get back the first elemrnt.
back=next(x for x in myway if '2218' in x)
print(back)

# project 6 manipulating items in list advanced way

ask=input("enter the name of a book you own: ")
boox=[ask]
ask1=input("enter the name of another book you want or (press enter to skip): ")
if ask1: # if not empty
    boox.append(ask1)
    print(f"now on your Library: {boox}")
else:
    print(f"ok, as you want your Library: {boox}")
asking=input("enter the name of a book you wish to have in the future: ")
wishlist=[asking]
asking1=input("enter the name of another book you wish to have in the future or (press enter to skip): ")
if asking1: # if not empty
    wishlist.append(asking1)
    print(f"great, your wishlist: {wishlist}")
else:
    print(f"ok, as you want your wishlist: {wishlist}")
if_get=input("enter the name of a book that you've got from your wishlist or (press enter to skip): ")
if if_get:
    if if_get in wishlist:
        wishlist.remove(if_get)
        boox.append(if_get)
        print(f"Update Library: {boox}\nUpdate wishlist {wishlist}")
else:
    print("wish you have the book soon")
donate=input("enter the name of a book from your Library you want donate or (press enter to skip): ")
if donate:
    if donate in boox:
        boox.remove(donate)
        print(f"final Library after donations: {boox}")
else:
    print("ok.")

# project 7 how to campaign together lists

class1=["Yara Ahmed","Omnya Yehya","Sara Ali"]
class2=["Ahmed Mohamed","Malik Yousif","Zyne Adil"]
class1_2=[]
class1_2.extend(class1 + class2)
print (f"for the course here's our names of the students...\n{class1_2}\nmake sure you send the course to each one of them.")
# better way to do it ...
all_students= class1 + class2
print (all_students)

# project 8 def weather.

def check_weather(deg):
    temp=deg
    if temp >24:
        print("it's hot!")
    else:
        print("it's nice weather!")
check_weather(20)
check_weather(29)

# project 9 total price for taxi

def total(price,tax_rate,discount):
    tax= price * tax_rate
    final_price= price + tax - discount
    print(f"total price is ${final_price}")
total (100,0.08,10) # $98

# project 10 return as a result

def calculate_area(width,height):
    return width * height
room_area=calculate_area(10,12)
print(f"room size: {room_area} sq ft")

# project 11 def with return

def double(number):
    return number * 2 # now any number will * 2
# store in variable
result= double(5) # 5*2=10
# use in expresstions...
total= double(5) + double(3) # now it's 10 + 6 =16
# pass to other functions
print(double(10)) # 20
# use in conditions
if double(7) > 10: # 7*2= 14 so it's a big number
    print("it's a big number!")
# another way!.

def simple():
    numbers=[2,3,7,8,9]
    first= numbers[0]
    last= numbers[-1]
    return first,last # when use more then one it automatically uses Tuple that can't be able to edit .
f,l=simple() # evry variable takes a number in order.
# now can print variables.
print(f)
print(l)

# project 12 the library with functions

ask=input("enter the name of a book you own: ")
boox=[ask]
ask1=input("enter the name of another book you own or (press enter to skip): ")
if ask1: # if not empty
    boox.append(ask1)
    print(f"now on your Library: {boox}")
else:
    print(f"ok, as you want your Library: {boox}")
asking=input("enter the name of a book you wish to have in the future: ")
wishlist=[asking]
asking1=input("enter the name of another book you wish to have in the future or (press enter to skip): ")
if asking1: # if not empty
    wishlist.append(asking1)
    print(f"great, your wishlist: {wishlist}")
else:
    print(f"ok, as you want your wishlist: {wishlist}")
if_get=input("enter the name of a book that you've got from yout wishlist or (press enter to skip): ")
if if_get:
    if if_get in wishlist:
        wishlist.remove(if_get)
        boox.append(if_get)
        print(f"Update Library: {boox}\nUpdate wishlist {wishlist}")
else:
    print("wish you have the book soon")
donate=input("enter the name of a book from your Library you want donate or (press enter to skip): ")
if donate:
    if donate in boox:
        boox.remove(donate)
        print(f"final Library after donations: {boox}")
else:
    print("ok.")

# project 13 def with parameters (APIs).

import requests 
def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response=requests.get(url)
    data=response.json()
    return data["current"]["temperature_2m"]
cairo_temp=get_weather(30.04, 31.23)
london_temp=get_weather(51.51,-0.13)
paris_temp=get_weather(48.85,2.35)
print(f"now in cairo: {cairo_temp}°C")
print(f"now in london: {london_temp}°C")
print(f"now in paris: {paris_temp}°C")
# another way to do it in alexandria

import requests
def alex(latitude, longitude):
    url= f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    answer=requests.get(url)
    data=answer.json()
    return data["current"]["temperature_2m"],data["current"]["wind_speed_10m"]
alex_temp=alex(31.20,29.91)
print(f"now in alexandria: {alex_temp[0]}°C, Wind Speed: {alex_temp[1]} km/h")
# better way to do it with unpacking the tuple
temp,wind_speed=alex(31.20,29.91)
print(f"now in alexandria: {temp}°C, Wind Speed: {wind_speed} km/h")

# project 14 how to check if a file exists or not
import os 
print("current working directory:",os.getcwd())
data_path="data/sales.csv"
if os.path.exists(data_path):
    print("file exists",data_path)
else:
    print("file does not exist",data_path)

# project 14 read data and save it as different format.
import pandas as pd
import os
import json
# read and update data
mine=pd.read_csv("data/store.csv")
print("CSV Data:\n", mine)
print(f"\nshape: {mine.shape[0]} rows, {mine.shape[1]} columns")
mine["total_cost"]= mine["unit_cost"] * mine["stock_quantity"]
mine["total_revenue"]= mine["selling_price"] * mine["stock_quantity"]
mine["expected_profit"]= mine["total_cost"] * mine["total_revenue"]
print(f"\nupdate data store:\n{mine}")
print(f"shape:\n{mine.shape[0]} rows, {mine.shape[1]} columns")
# Create inventory_reports directory,(folder)
os.makedirs("inventory_reports",exist_ok=True)
# Save as different formats
mine.to_json("inventory_reports/inventory_analysis.json",orient="records",indent=2)
mine.to_excel("inventory_reports/inventory_analysis.xlsx",index=False)
mine.to_csv("inventory_reports/inventory_with_profits.csv",index=False)
print("\nfiles saved:")
print("- inventory_reports/inventory_analysis.json")
print("- inventory_reports/inventory_analysis.xlsx")
print("- inventory_reports/inventory_with_profits.csv")