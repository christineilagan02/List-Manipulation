# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

import sys

def intro():
    separator()
    title1()
    title2()
    separator()
    name = input("\n\t    Hello! What is your name? \n\t      >> ")
    print(f"\n\t     Well \33[1m{name.title()}\33[0m enjoy playing \n\t       and let's begin!!\n")
    separator()
    
def title1():
    from time import sleep
    string = ("\t\33[1m            Welcome to \33[0m\n")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()
        
def title2():
    from time import sleep
    string = ("\33[1m\33[33m\t      Manipulating the List\33[0m\n")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()
    
def separator():
    print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
    
def listing():
    print("\n\t\33[3m\33[1m          This is the list: \33[0m")
    list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
    print("\t" + str(list1) + "\n")
    
def menu():
    print("\t\33[1m\33[33m*\33[0m---+---+---+--\33[1m\33[33mMENU\33[0m--+---+---+---\33[1m\33[33m*\33[0m")
    menu_list = ["\n\t \33[3m\33[1m 1 -> Add an element \33[0m", "\t \33[3m\33[1m 2 -> Insert an element \33[0m", "\t \33[3m\33[1m 3 -> Sum of an elements \33[0m", "\t \33[3m\33[1m 4 -> Delete an element \33[0m", "\t \33[3m\33[1m 5 -> Arrange in ascending order \33[0m", "\t \33[3m\33[1m 6 -> Arrange in descending order \33[0m", "\t \33[3m\33[1m 7 -> Exit \33[0m\n"]
    for item in menu_list:
        print(item)

def play():
    while True:
        choice = input("\n\t\33[92m      Enter your choice[1-7]\33[0m \n\t   >> ")
        if choice == '1':
            print("\n\t\33[3m\33[1m          This is the list: \33[0m")
            list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
            print("\t" + str(list1) + "\n")
            userInput = input('\n\t\33[92m   Enter a number you want to add\33[0m \n\t    >> ')
            list1.append(userInput)
            print("\t" + str(list1) + "\n")
            separator()
            
        elif choice == '2':
            print("\n\t\33[3m\33[1m          This is the list: \33[0m")
            list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
            print("\t" + str(list1) + "\n")
            userInput = int(input('\n\t\33[92m   Enter a number you want to insert\33[0m \n\t    >> '))
            list1.insert(userInput)
            print("\t" + str(list1) + "\n")
            separator()
            
        elif choice == '3':
            print("\n\t\33[3m\33[1m          This is the list: \33[0m")
            list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
            print("\t" + str(list1) + "\n")
            print("\t\33[3m\33[1mThis is the Sum of the elements: \33[0m")
            total = sum(list1)
            print("\t" + str(total) + "\n")
            separator()
            
        elif choice == '4':
            print("\n\t\33[3m\33[1m          This is the list: \33[0m")
            list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
            print("\t" + str(list1) + "\n")
            userInput = int(input('\n\t\33[92m   Enter a number you want to delete\33[0m \n\t    >> '))
            list1.remove(userInput)
            print("\n\t" + str(list1) + "\n")
            separator()
            
        elif choice == '5':
            print("\n\t\33[3m\33[1m          This is the list: \33[0m")
            list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
            print("\t" + str(list1) + "\n")
            list1 = sorted([1, 9, 2, 12, 26, 17, 83, 8, 15, 79])
            print("\t\33[3m\33[1mSorted in ascending order: \33[0m")
            print("\t" + str(list1) + "\n")
            separator()
            
        elif choice == '6':
            print("\n\t\33[3m\33[1m          This is the list: \33[0m")
            list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
            print("\t" + str(list1) + "\n")
            list1 = sorted([1, 9, 2, 12, 26, 17, 83, 8, 15, 79], reverse=True)
            print("\t\33[3m\33[1mSorted in descending order: \33[0m")
            print("\t" + str(list1) + "\n")
            separator()
            
        elif choice == '7':
            print("\n")
            separator()
            print ("\t\33[1m\33[93m\33[3m        You can now exit.\33[0m")
            separator()
            sys.exit("\n")
            
        else:
            separator()
            print("\33[31m\33[1m\t       Error! Invalid input.\33[0m")
            print("\33[31m\33[1m\t   Press any key to continue...\33[0m")
            separator()
            
    

def main():
    print("\n")
    intro()
    listing()
    menu()
    separator()
    play()
    
main()