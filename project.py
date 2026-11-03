# my projects in python

# project 1 game

print(r'''
         XXXXXXXXX
     XXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXX
   XXXXXX   XXX   XXXXXX
   XXXXXX   XXX   XXXXXX
   XXXXXX   XXX   XXXXXX
    XXXXXXXXXXXXXXXXXXX
     XXXXXX  X  XXXXXX
      XXXXXXXXXXXXXXXX
       XX  XX  XX  XX
''')
print ("welcome to my Island 🏝️")
door=input("choose a door 🚪(red or blue): ").strip().lower()
if door=="red":
    print ("great,now you got 3 boxes")
    box=input ("black 🎁 - white 🎁 - green 🎁\nwhich box do you want to open? ").strip().lower()
    if box =="black":
        print("oops! this box is full of spiders 🕷️ , game over.")
    elif box =="white":
        print ("oops! this box is full of snakes 🐍 , game over.")
    elif box =="green":
        print ("congratulations! you win the treasure 🎊 ")
    else:
        print ("please follow the options")
elif door=="blue":
    print ("this door is full of crocodiles 🐊! game over.")
else:
    print ("invalid choice.")
    
# project 2 account

app=input ("Do you have an account?! ")
if app=='yes':
    print ("great, you can keep going")
    age=int(input("How old are you? "))
    if age>=18:
        print ("you can sign in")
    else:
        print ("sorry you can't sing in til you become 18 year old")
else:
    print ("you should sign first")

# project 3 ID

print("this is for Canada's id")
canada=input("are you Canadian? ")
if canada=='yes':
    print ("great, you'll get the next step")
    is_18=int(input("how old are you? "))
    if is_18>=18:
        print ("you allowed to have an id")
    else:
        print ("sorry buddy you can get it when you're 18")
else:
    print("sorry it's only for Canadians people ")

# project 4 if tantawi

tanta=input("now you're in the station, which ride do you want to choose? (bus or taxi or uber): ").strip().lower()
if tanta=="bus":
    print("sorry, the bus is unavailable.")
elif tanta=="uber":
    print("sorry, the uber is unavailable.")    
elif tanta=="taxi":
    print("great, you can go to your destination.")
    taxi=input("now in front of you 3 taxis,\nwhich one do you want to choose? (red or white or green): ").strip().lower()
    if taxi=="red":
        print("sorry, the red taxi is unavailable in tanta.")
    elif taxi=="green":
        print("sorry, the green taxi is unavailable in tanta.")
    elif taxi=="white":
        pay=input("great, now do you want to pay by cash or visa? ").strip().lower()
        if pay=="cash":
            print("great, you can pay by cash.")
        elif pay=="visa":
            print("sorry, the visa is unavailable in tanta.")
        else:
            print("invalid choice.")
    else:
        print("invalid choice.")
else:
    print("invalid choice.")

# project 5 random PIN Code
 
import random
pin_code=(random.randint(1000,2000))
user_input=int(input("enter 4 digits pin code: "))
if len(str(user_input))!=4:
    print("sorry, your pin code should be 4 digits")
elif user_input==pin_code:
    print(f"great your pin code {user_input} matched the computer pin code {pin_code}")
else:
    print(f"sorry your pin code {user_input} doesn't match the computer pin code {pin_code}")

# project 6 OTP

password= int(input("enter your password here: "))
import random 
is_random= random.randint (100000,900000)
if password == 1555000:
    print (f"your OTP is {is_random}")
    sure=int(input("enter your OTP: "))
    if sure== is_random:
        print ("the payment is done")
    else :
         print ("wrong OTP")
else :
     print ("wrong password")

# project 7 coin guessing game

import random
print("welcome to the coin guessing game")
print("choose one method to play the game (1 for random / 2 for ranint)")
method = int(input("enter your choice: "))
if method==1:
   if random.random()>=0.5:
      result="heads"
   else:
      result="tails"
elif method==2:
   if random.randint(0,1)==0:
      result="heads"
   else:
      result="tails"
else:
   print("wrong choice.")
   exit() # ينهي تشغيل البرنامج هنا فوراً إذا كان الإدخال خطأ

user_choice=input("choose heads or tails: ").lower().strip()
if user_choice==result:
   print("you won! the result was",result)
elif user_choice not in ["heads","tails"]: # uesd instead of != because this is more general and cust mistakes
    print("invalid input, you must choose heads or tails.")
else:
   print("you lost! the result was",result)

# project 8 kick game

import random
# choose a method
print("welcome to the penalty kick game")
user_choice=int(input("choose a method to play (1 for random shot/ 2 for precise shot): "))
if user_choice==1:
    if random.random()>=0.5:
        result1="left"
    else:
        result1="right"
elif user_choice==2:
    x=random.randint(0,2)
    if x==0:
        result2="left"
    elif x==1: 
        result2="middle"
    else:
        result2="right"
else:
    print("wrong choice.")
    exit()
# check the result
if user_choice==1:
    kick=input("great, now choose (left/right): ").lower().strip()
    if kick not in ["left","right"]:
        print("only choose left/right.")
    elif result1==kick:
        print("you won! it was indeed",result1)
    else:
        print("sorry, you lost it was",result1)
elif user_choice==2:
    kick=input("great, now choose (left/middle/right): ").lower().strip()
    if kick not in ["left","middle","right"]:
        print("only choose left/middle/right.")
    elif kick==result2:
        print("great, you won! it was indeed",result2)  
    else:
        print("sorry, you lost it was",result2)

# project 9 second OTP

import random
random_number= random.randint(100000,900000)
card=int(input("please enter you card number here: "))
if card == 12338404934453:
    sure=int(input(f"your OTP is [{random_number}]\nenter your OTP here to confirm: "))
    if sure==random_number:
        print("the pyment has been confirmed")
    else:
        print("the OTP is wrong.")
else:
    print("your card number is wrong.")

# project 10 the library

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

# project 11 whose wallet
import random
# split() make it as a list
names=input("welcome to (whose wallet) enter names separated: ").split()
# count the length of the list
length=len(names)
# generate a random number between 0 and length-1 (from start to end of the list)
random0=random.randint(0,length-1)
# use the name of the list with [] and put the random number inside to get a name.
print(f"the one who should pay the dinner is: {names[random0]}")
# another way to do it is using random.choice() function
import random
names=input("Enter names separated by comma: ").split(", ")
nn=random.choice(names)
print(f"The selected name is: ({nn}) to pay the bill !")

# list inside a list
basket=[["aplle","banana"],["orange","grape"]]
print(basket[0][0],basket[1][0])
b=basket.append(["kiwi","mango"])
print(basket)
books=["book2","book3","book5"]
books.insert(0,"book1")
books.insert(3,"book4")
print(books)

# Project 12 minablate (nested list)..
basket= [['Apples','Bananas'],['Milk','water']]
user=input(f"{basket}\nPress enter to change the content.....")
# we choose the number of a list and element we want to add to it.
basket[0].insert(0,"Oranges") 
basket[0].append('Kiwis')
basket[1].insert(0,"Coffee")
basket[1][2]="Tea" # for replacing an element..
basket.append([1,2,3]) # for adding a new list..
print(f"You list after changing\n{basket}")

# Project 13 place the rabbit and find the carrot
print ("welcome to place the rabbit 🐰")
rabbit=[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
for sublist in rabbit:
  print (*sublist)
user=input("where should the rabbit move? 🐇\n\nto place the rabbit enter the row number then culmen: ")
row=int(user[0]) -1
cul=int(user[1]) -1
if 0 <=row < 3 and 0 <=cul < 3:
  rabbit[row][cul]="🐇"
  print ("\nyou're succeed...\n")
  for sublist in rabbit:
   print (*sublist)
else:
  print ("\nYou should follow up with options list.")
  exit()
rabbit[row][cul]="🌿" # return it again to start over.
print ("\nnow find the carrot 🥕\n")
choose=input ("enter the row number and culmen that you think might be in it: ")
row=int(choose[0])-1
cul=int(choose[1])-1
import random 
us=random.randint(0,2) 
us1=random.randint(0,2)

if 0<=row<3 and 0<=cul<3 :
  if row==us and cul==us1:
    rabbit[us][us1]="🐰"
    print ("\ncongratulations,you found it..💃🏻\n")
    for sublist in rabbit:
     print (*sublist)
  else:
    rabbit[us][us1]="🥕"
    rabbit[row][cul]="🐇"
    print ("\noops! you didn't find it and that was the position..👾\n")
    for sublist in rabbit:
     print (*sublist)
else:
  print ("you should follow up the options.")

# project 14 rock, paper, scissors game
import random

# Save Ascii in variables
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_ascii = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# start with rules
print("welcome the rock, paper, scissors game\n")
user=input("press enter to start the game or type 'help' to get the rules: ").lower()
if user=="help":
    print("""
    ******Rules of the game******
          1) you choose and the computer chooses
          2) rock shmashes scissors -> rock wins 
          3) scissors cut paper -> scissors wins 
          4) paper covers rock -> paper wins
    """)

user_choice=input("enter your choice (rock, paper, scissors): ").lower().strip()
 
optins=['rock', 'paper', 'scissors']

if user_choice not in optins:
    print("vaild choice!")
    exit()
else:
    if user_choice=="rock":
        print(f"\nyou chose:\n{rock_ascii}")
    elif user_choice=="paper":
        print(f"\nyou chose:\n{paper_ascii}")
    else:
        print(f"\nyou chose:\n{scissors_ascii}")
# display computer choice
combuter_choice=random.choice(optins)

if combuter_choice=="rock":
     print(f"\ncomputer chose:\n{rock_ascii}")
elif combuter_choice=="paper":
    print(f"\ncomputer chose:\n{paper_ascii}")
else:
    print(f"\ncomputer chose:\n{scissors_ascii}")

if combuter_choice==user_choice:
    print("\nit's a tie!")
elif(
    (user_choice=="rock" and combuter_choice=="scissors")
    or
    (user_choice=="scissors" and combuter_choice=="paper")
    or
    (user_choice=="paper" and combuter_choice=="rock")
):
    print (f"\nyou won! {user_choice} beets {combuter_choice}")
else:
    print(f"\nyou lost {combuter_choice} beets {user_choice}")

# project 15 for loop with condation.
numbers=[1,2,3,4,5,6]
for t  in numbers:
    if t %2==0:
        print(t)

# in this case i didn't type (else) so it will print only the numbers these mach the condation.
print("the Loop has finshed.")


# project 16 homework for class
# project 1
class Profile:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.language=language

profile_1=Profile("nour ali","nourblack@gmail.com","english language")
profile_2=Profile("malik ahmed","malikso@gmail.com","french language")
profile_3=Profile("sara ali","saratota212@gmail.com","german language")
print(profile_1.name, profile_1.email, profile_1.language)

# project 2
class Telegram:
    def __init__(self,sender_name,futur_name,content_massage,sent_date):
        self.sender_name=sender_name
        self.futur_name=futur_name
        self.content_massage=content_massage
        self.sent_date=sent_date

message1=Telegram("ali moomen","nour younis","hey nour how are you","2026/9/17")
message2=Telegram("khalid ashraf","yousif ashraf","come home soon","2026/9/18")
message3=Telegram("omnia yehya","amira moustafa","where is my hat?","2026/9/17")
print(message1.sent_date)
print(message3.content_massage)

# project 3
class Amazon:
    def __init__(self,name_product,price,descript,evaluation):
        self.name_product=name_product
        self.price=price
        self.descript=descript
        self.evaluation=evaluation
product_1=Amazon("Dress",700,"black drees with yellow flowers","7/10")
profile_2=Amazon("Hat",300,"greet hat for beach","6/10")
profile_3=Amazon("T-Shirt",400,"blue T-Shirt for sport","9/10")
print(profile_3.name_product,profile_3.price)

# project 17 homework for class
print("_________Movies list_________\n")
class Movies:
    def __init__(self,title,director,release_year,genre):
        self.title=title
        self.director=director
        self.release_year=release_year
        self.genre=genre
    def display(self):
        print(f"title: {self.title}\ndirector: {self.director}")
        print(f"release year: {self.release_year}\ngenre: {self.genre}\n")

mavie1=Movies("inception","christpher nolan","2010","sci-fi")
mavie2=Movies("the godfather","francis ford","1972","crime")
mavie3=Movies("parasite","bong joon-ho","2019","thriller")
# now show them
mavie1.display()
mavie2.display()
mavie3.display()
print("\n\nchanging movie directors ...\n\n")
mavie1.director="Nourhan Younis"
mavie2.director="Malik Ahmed"
mavie3.director="Moustaf Yousif"
mavie1.display()
mavie2.display()
mavie3.display()


# project 17 (register an order)

class Product:
    def __init__(self,name_product,price,quantity,category="general"):
        self.name_product=name_product
        self.price=price
        self.quantity=quantity
        self.category=category

def creat_product():
    print("to register an order you need to follow these steps...")
    name_product=input("enter your chosen product: ")
    price=float(input("enter the price of th product: "))
    quantity=int(input("enter the quantity: "))
    return Product(name_product,price,quantity)

item1= creat_product()

print(f"""
your order has been submitted...
details of the order:
name product: {item1.name_product}
category: {item1.category}
total: ${item1.price * item1.quantity}
""")

#project 18 (Library Book System)
class Library:
    def __init__(self,title,author,pages,is_borrowed=False):
        self.title=title
        self.author=author
        self.pages=pages
        self.is_borrowed=is_borrowed
    def borrow(self):
        self.is_borrowed= True
def add_book():
    print("welcome in alexandria Library")
    title=input("enter the title book you wan to borrow: ")
    author=input("enter the author name: ")
    pages=input("enter pages number: ")
    return Library(title,author,pages)

book1=add_book() # use funcation add_book to variable to make an opject from tha class.
book1.borrow() # change it to True
book1.is_borrowed=False # change it back to Fales

import random
id_book=random.randint(100000,900000)
if book1.is_borrowed== False:
    print(f"\ngreat you can borrow this book go to the relevant department with this Id: {id_book}")
else:
    print("\nsorry, this book has been borrowed to someone else check for it later. ")

# project 18
import random
import string
print("\nWelcome to the Password Generator!\n")
user=int(input("Enter the total number of characters in the password: "))
letters=int(input("\nEnter the number of letters in the password: "))
number=int(input("Enter the number of numbers in the password: "))
symbol=int(input("Enter the number of symbols in the password: "))

total= letters + number + symbol
if user != total:
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password length.")
    exit()

random_letters=random.choices(string.ascii_letters,k=letters)
random_number=random.choices(string.digits,k=number)
random_symbol=random.choices(string.punctuation,k=symbol)

gathering_them= random_letters+random_number+random_symbol
random.shuffle(gathering_them)
final_pass="".join(gathering_them)

print(f"\nhere is your strong password: {final_pass}")

# project (19) using for loop and while loop
import random

word = ['good', 'bad', 'ugly']
random_word = random.choice(word)

display = []
for letter in random_word:
    display.append("-")

print(display )
while "-" in display:
    guess = input("guess a letter please: ").lower()

    for m in range(len(display)):
        if guess == random_word[m]:
            display[m] = guess
            
    print(display)

print("***YOU WIN***")

# project (20) using for loop and while loop with 6 tries
import random

word = ['good', 'bad', 'ugly']
random_word = random.choice(word)

display = []
for letter in random_word:
    display.append("-")

print("welcome to hangman game\nyou only have 6 tries...")
print(f"{display}\n")

for g in range(1, 7):
    guess = input(f"this is your {g} try\nguess a letter please: ").lower()

    for m in range(len(display)):
        if guess == random_word[m]:
            display[m] = guess
            
    print(display)

    # 👈 الأسطر دي لازم تكون داخل for g بنفس المحاذاة دي
    get_them = "".join(display)
    if get_them == random_word:
        print("***YOU WIN***")
        exit()  # يوقف البرنامج فوراً بمجرد اكتمال الكلمة

else:
    print(r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |

sorry! you have lost the game
    ''')


# project (20) secret meesage
name="nourhan"
print(name.index("n"))#0
# my project
import string
alphabet=string.ascii_lowercase
secret_meesage=""
user=input("what secret meesage do you wanna deliver? ").lower()
number=int(input("enter the number key: "))
for c in user:
    if c in alphabet:
        orginal=alphabet.index(c)
        new_postion=(orginal+number) %26
        secret_meesage+=alphabet[new_postion]
    else:
        secret_meesage+=c
print(f"your secret meesage is: {secret_meesage}")

# now try to return the meesage to orginal ! (should know the key number.)

key_meesage=input("\ntype here your secret meesage to switch: ").lower()
key_number=int(input("enter the number key: "))
key_user=""
for letters in key_meesage:
    if letters in alphabet:
        postion=alphabet.index(letters)
        key=(postion - key_number)%26
        key_user+=alphabet[key]
    else:
        key_user+=letters

print(f"Great,\nyour meesage is: {key_user}")

# project (21) secret message with all letters.
import string
all_letters=string.ascii_letters
user_message=input("Enter your secret message here: ")
shift_key=int(input("Enter the secret kay: "))

def message(secret_message,secret_key):
    placeholder=""
    for k in secret_message:
        if k in all_letters:
            postion=all_letters.index(k)
            new_postion=(postion + secret_key)%52
            placeholder+=all_letters[new_postion]
        else:
            placeholder+=k
    return placeholder
print(f"Here is your switched message: {message(user_message,shift_key)}")

# project(22) class with many methods for changeing
class Movies:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    def display(self):
        print(f"Title: {self.title}\nDirector: {self.director}\nReleased Year: {self.year}\nGenre: {self.genre}\n"+"_"*30)
    def update_director(self, new_director):
        self.director = new_director
    def update_year_genre(self,new_year,update_genre):
        self.year=new_year
        self.genre=update_genre

movie1 = Movies("Inception", "Christopher Nolan", 2010, "Sci-Fi")
movie2 = Movies("The Godfather", "Francis Ford Coppola", 1972, "Crime")

movie1.display()
movie2.display()
movie1.update_director("Nourhan Younis")
movie1.update_year_genre(2026, "drama")
movie1.display()

# project(23) class with input function to create an object from the class.
class Useer:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status

def create_user():
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    user=Useer(first_name,last_name,email,password)
    return user
user1=create_user()
print(f"\nUser created successfully!\nFirst Name: {user1.first_name}\nLast Name: {user1.last_name}\nEmail: {user1.email}\nStatus: {user1.status}\n"+"_"*30)

# project(24) class with input function (Travel class)
class Travel:
    def __init__(self, destination, duration, cost):
        self.destination = destination
        self.duration = duration
        self.cost = cost

    def display_info(self):
        print(f"\nDestination: {self.destination}")
        print(f"Duration: {self.duration} days")
        print(f"Cost: ${self.cost}\n"+"_"*30)

def ask_user ():
    destination = input("Enter the travel destination: ")
    duration = int(input("Enter the duration of the trip (in days): "))
    cost = float(input("Enter the cost of the trip: "))

    travel = Travel(destination, duration, cost)
    return travel

user1=ask_user()
user1.display_info()

# project(25) class with input function (PC class)
class Pc :
    def __init__(self,type,ram,storage):
        self.type=type
        self.ram=ram
        self.storage=storage
    def display_info(self):
        print(f"_"*30 +"\nPC Order Details:")
        print(f"Type: {self.type}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB\n"+"_"*30)

def order_pc():
    type = input("Enter the type of PC (e.g., Desktop, Laptop): ")
    ram = int(input("Enter the RAM size (in GB): "))
    storage = int(input("Enter the storage size (in GB): "))
    pc=Pc(type,ram,storage)
    return pc

order1=order_pc()
order1.display_info()

# project(26) class with input function (Recipe class)
print("Welcome to Recipe Collection\n")
class Recipe:
    def __init__(self,name,ingredients,time,steps):
        self.name=name
        self.ingredients=ingredients
        self.time=time
        self.steps=steps
    def display_recipe(self):
        print(f"\nRecipe Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Cooking Time: {self.time} minutes")
        print(f"Steps: {self.steps}\n"+"_"*30)

def add_recipe():
    name=input("Enter the recipe name: ")
    ingredients=input("Enter the ingredients (comma-separated): ")
    time=int(input("Enter the cooking time (in minutes): "))
    steps=input("Enter the steps (comma-separated): ")
    recipe=Recipe(name,ingredients,time,steps)
    return recipe

recipe1=add_recipe()
recipe1.display_recipe()

# project(27) class with input function (User class)
print("Welcome to car management system\n")
class Car:
    def __init__(self,model,brand,year,price,status="available"):
        self.model=model
        self.brand=brand
        self.year=year
        self.price=price
        self.status=status

ask= int(input("Choose an action:\n1. Add a new car\n2. Display all cars\n3. Exit\nEnter your choice: "))
car_list = []

while ask != 3:
    if ask==1:
        model=input("Enter the car model: ")
        brand=input("Enter the car brand: ")
        year=int(input("Enter the car year: "))
        price=float(input("Enter the car price: "))
        
        car=Car(model,brand,year,price)
        car_list.append(car)
        print("Car added successfully!\n")
    elif ask==2:
        print("\nDisplaying all cars...\n")
        if not car_list:
            print("No cars found yet!\n")
        else:
            for car in car_list:
                print(f"Model: {car.model}\nBrand: {car.brand}\nYear: {car.year}\nPrice: ${car.price}\nStatus: {car.status}\n" + "-"*30)
    else:
        print("Invalid choice! Please try again.\n")
    ask= int(input("Choose an action:\n1. Add a new car\n2. Display all cars\n3. Exit\nEnter your choice: "))

print("Thank you for using the car management system. Goodbye!")
exit()

# project(28) class with input function (drinks class)
print ("Welcome to management system")
class Drinks:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

drinks_list = []
ask = int(input("Choose an action:\n1. Add a new drink\n2. Display all drinks\n3. Exit\nEnter your choice: "))

while ask !=3:
    if ask==1:
        name=input("\nenter the drink name: ")
        price=float(input("enter the drink price: "))
        quantity=int(input("enter the drink quantity: "))
        drink=Drinks(name,price,quantity)
        drinks_list.append(drink)
        print("\nDrink added successfully!\n")
    elif ask==2:
        print("\nDisplaying all drinks...\n")
        if not drinks_list:
            print("No drinks found yet!\n")
        else:
            for d in drinks_list:
                print("_"*25 +f"\ndrink name: {d.name}\nprice: ${d.price}\nquantity: {d.quantity}\ntotal: ${d.price * d.quantity:.2f}\n" + "_"*25)
    else:
        print("Invalid choice, please try again.\n")
    ask = int(input("Choose an action:\n1. Add a new drink\n2. Display all drinks\n3. Exit\nEnter your choice: "))

print("Exiting program. Goodbye!")

# Project (29) Class in Advanced way
import os
import time
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Car:
    def __init__(self,name,model,year,color,status="Available"):
        self.name=name
        self.model=model
        self.year=year
        self.color=color
        self.status=status
    def display_cars(self):
        print(f"\nCar Name: {self.name}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        print(f"Car Color: {self.color}")
        print(f"Car Status: {self.status}")
        print("-"*30)

def create_car():
    name=input("Enter the Car Name: ")
    model=input("Enter the Car Model: ")
    year=int(input("Enter the Car Year: "))
    color=input("Enter the Car Color: ")
    return Car(name,model,year,color)

cars_list=[]
while True:
    print("*** Car Management System ***")
    print("1. Create Car")
    print("2. Display Cars")
    print("3. Exit\n")
    choice=input("Enter your choice: ")
    if choice =="1":
        cars_list.append(create_car())
        print("\nCar created successfully!\n")
        time.sleep(2)
    elif choice=="2":
        clear_screen()
        if cars_list:
            print("\nDisplaying all Cars.....\n")
            time.sleep(1)
            for car in cars_list:
                car.display_cars()
            time.sleep(1)
        else:
            print("Sorry, no cars found to display.\n")
            time.sleep(1)
    elif choice=="3":
        print("Exiting....")
        time.sleep(3)
        break
    else:
        print("Invalid choice. Please try again.\n")
        time.sleep(1)

## Project (29) Class in Advanced way
import os
import time

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Member:
    def __init__(self,first_name,last_name,id,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.status=status
    def display(self):
        print(f"""
First Name: {self.first_name}
Last Name: {self.last_name}
Membership ID: {self.id}
Membership Status: {self.status}
        """)
        print("_"*30)

def create_member():
    clear_screen()
    first_name=input("Enter the first name: ")
    last_name=input("Enter the last name: ")
    id=input("Enter the ID: ")
    status=input("Enter membership status or click Enter: ")
    if not status:
        status="inactive"
    return Member(first_name,last_name,id,status)

members_list=[]

# making a funcation to search for a member.....
def search_member(members_list):
    print("\nSearch by: ")
    print("""
1. Membership ID
2. First Name
3. Membership Status
    """)
    search_choice=int(input("Enter your choice: "))
    found_member=[]

    if search_choice==1:
        search_id=input("Enter the membership ID to search: ")
        for x in members_list:
            if x.id == search_id:
                found_member.append(x)
                break
    elif search_choice==2:
        first_name=input("Enter the first name to srarch: ").lower()
        for v in members_list:
            if v.first_name.lower() in first_name:
                found_member.append(v)
    elif search_choice==3:
        status=input("Enter membership status to search (Active - Inactive): ").lower()
        for c in members_list:
            if c.status.lower() == status:
                found_member.append(c)
    else:
        print("Invalid choice Please try again.\n")

    if found_member:
        clear_screen()
        for x in found_member:
            x.display()
    else:
        print("There is no member yet!")

while True:
    print("""
*** Welcome to GYM membership management ***

Choose an action: 
1. Add a new member
2. Display all members
3. Search for a member
4. Exit
    """)
    choice=int(input("Enter here your choice: "))
    if choice==1:
        members_list.append(create_member())
        print("\nMembner added successfully!\n")
        time.sleep(1)
    elif choice==2:
        clear_screen()
        print("\nDisplaying all Members.....\n")
        time.sleep(2)
        if members_list:
            for member in members_list:
                member.display()
                
        else:
            print("Sorry, no members found to display.\n")
            time.sleep(1)
    elif choice==3:
        if members_list:
            search_member(members_list)
            time.sleep(2)
        else:
            print("There is no members to search!")
            time.sleep(1)

    elif choice==4:
        print("Exiting...")
        time.sleep(2)
        break
    else:
        print("Invalid choice. Please try again.\n")
        time.sleep(1)
# my project on it...
import os
import time
import random

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Drinks:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.id=random.randint(1000,9000)
    def display_info(self):
        print(f"""
Drink Name: {self.name}
Quantity: {self.quantity}
Price: ${self.price}
total: ${self.price*self.quantity}
The TD: {self.id}
"""+"_"*30)

drinks_list=[]
def add_drink():
    name=input("Enter the name of the drink: ")
    price=float(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    drink=Drinks(name,price,quantity)
    drinks_list.append(drink)
    return drink

def search(drinks_list):
    found_list=[]
    choice=int(input("Search By...\n1. Id\n2. Name Drink\nEnter your choice: "))
    if choice==1:
        ask=int(input("Enter the ID number to search: "))
        for x in drinks_list:
            if x.id == ask:
                found_list.append(x)
                break
    elif choice==2:
        ask=input("Enter the name of the drink to search: ").lower()
        for x in drinks_list:
            if x.name.lower() == ask:
                found_list.append(x)
    else:
        print("Invalid choice, please try again.\n")

    if found_list:
        clear_screen()
        for g in found_list:
            g.display_info()
    else:
        print("There are no drinks to be found!")

while True:
    print("""
*** Welcome to Drinks management ***
choose an action:
1. Add Drink
2. Display Drinks
3. Search for an invoice
4.Exit
    """)
    user=int(input("Enter your choice: "))
    if user==1:
        clear_screen()
        add_drink()
        print("\nThe drink added successfully!\n")
        time.sleep(2)
    elif user==2:
        clear_screen()
        print("\nDisplaying all drinks.....\n")
        time.sleep(2)
        if drinks_list:
            for z in drinks_list:
                z.display_info()
        else:
            print("There are no drinks yet!")
            time.sleep(1)
    elif user==3:
        clear_screen()
        if drinks_list:
            search(drinks_list)
            time.sleep(2)
        else:
            print("You haven't added anything to search.")
            time.sleep(1)
    elif user==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.\n")
        time.sleep(1)

# project (30) draw different shapes
from turtle import Turtle, Screen
window=Screen()
window.setup(width=1000,height=1000)
window.bgcolor("black")
tom=Turtle()
tom.shape("turtle")
tom.color("gold")
tom.pensize(4)
tom.speed("fast")

def draw_circles():
    tom.penup()
    tom.goto(-300,-300)
    tom.pendown()
    for _ in range(10):
        tom.circle(50)
        tom.left(360/10)

def draw_squares():
    tom.penup()
    tom.goto(0,0)
    tom.pendown()
    for _ in range(10):
        for _ in range(4):
            tom.forward(80)
            tom.left(90)
            tom.left(360/10)

def draw_triangles():
    tom.penup()
    tom.goto(300,300)
    tom.pendown()
    for _ in range(10):
        for _ in range(3):
            tom.forward(100)
            tom.left(120)
            tom.left(360/10)

draw_circles()
draw_squares()
draw_triangles()

window.exitonclick()

# project (31) name on  the window
from turtle import Turtle, Screen
window=Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
tom=Turtle()
tom.shapesize(0.2)
tom.color("white")
tom.pensize(7)
tom.speed("fast")
tom.hideturtle()
user=window.textinput(title="Shape with SOM",prompt="Type the name")
tom.write(f"Hello, {user} in our first try.",font=("arial",20,"normal"),align="center")
window.exitonclick()