#1) Build a Shopping Cart
#You can use either lists or dictionaries. The program should have the following capabilities:

#1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list

from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
amazon_shopping_cart = {}

def amazon_cart(item, quantity):
    amazon_shopping_cart[item] = quantity
    
def list():
    while True:
        clear_output()
        question =input("Do you want to : Show, Add, Delete or Quit?")
        if question.lower() =='add':
            item = input('What item would you like to add?' )
            quantity = input('How many do you want?')
            if item not in amazon_shopping_cart:
                amazon_cart(item,quantity)
        elif question.lower() == 'delete':
            witem = input('What do you want to delete?' )
            if witem in amazon_shopping_cart:
                amazon_shopping_cart.pop(witem)
                print(f'You removed:{witem}!')
            else:
                print(f"{witem} not found in cart.")
        elif question.lower() =='show':
            print(amazon_shopping_cart)
        elif question.lower() =='quit':
            print('All DONE!')
            break
        else:
            print("Incorect input!")
    print(amazon_shopping_cart)
    
list()



### 2) Create a Module in VS Code and Import It into jupyter notebook 
#Module should have the following capabilities:
#1) Has a function to calculate the square footage of a house 
#   Reminder of Formula: Length X Width == Area
        
#2) Has a function to calculate the circumference of a circle
#Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

from homework import sqft
import math
from homework import circumference


def house():
    question = input('Would you like some help today?(y/n) ')
    if question.lower() == 'n':
        print("Have a nice day!")
    elif question.lower() == 'y':
        question1 = input("Do you need calculate circumference('c') or house square foot('s')?")
        if question1.lower() == 'c':
            radius = float(input('What is the radius? '))
            x = circumference(radius)
            print(x)
        elif question1.lower()== 's':
                length = input('What is the lenth of your house? ')
                width = input('What is the width of your house? ')
                y = sqft(length, width)
                print(y)
        else:
            print('Invalid Entry')
    else:
        print('Invalid Entry')
house()