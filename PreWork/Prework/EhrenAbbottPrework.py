# Question 1  
# Write a function to print "hello_USERNAME!"  
# USERNAME is the input of the function.  
# The first line of the code has been defined as below. 


def hello_name(user_name): 
    print("Hello_" + user_name + "!")

user_name = input("What is your username?")
hello_name(user_name) 

# Question 2 
# Write a python function, first_odds,  
# that prints the odd numbers from 1-100 and returns nothing  

def first_odds():  
    for value in range (0, 101): 
        if value % 2 == 1: 
            print(value) 

first_odds() 

# Question 3 
# Please write a Python function, max_num_in_list, 
# to return the max number of a given list.  
# The first line of the code has been defined as below.

def max_num_in_a_list(a_list):
    a_list.sort() 
    print(a_list[-1])

number_list = [34, 3, 1000, 45, 23, 80, 11, 1]  
max_num_in_a_list(number_list) 


# Question 4 
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100,  
# unless it is also divisible by 400.
# The return should be boolean Type (true/false). 

def is_leap_year(a_year): 
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(True)  
    elif a_year % 400 == 0:
        print(True)
    else: 
        print(False)

is_leap_year(2000) 

# Question 5 
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. 

new_list = []
def is_consecutive(a_list):   
    for X in a_list:
        Y = X + 1 
        new_list.append(Y)  
    if new_list[0:-1] == List_Of_Numbers[1:]:
        print(True) 
    else: 
        print(False)


List_Of_Numbers = [1, 2, 3, 4, 5, 6, 7, 9]
is_consecutive(List_Of_Numbers)
