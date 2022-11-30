
# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

for X in range(50): 
    if X * X < 1000: 
        print(X * X) 
    else: break 


# HINT for #2::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break
# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

for C in range(100):  
    if C == 2 or C == 3 or C == 5 or C == 7: 
        print(C)
    elif C % 2 == 0 or C % 3 == 0 or C % 5 == 0 or C % 7 == 0 or C == 1: 
        continue 
    else:
        print(C)


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

user_age = input("What is your age?") 

if int(user_age) < 18:
    print("kids") 
elif int(user_age) >= 18 and int(user_age) <= 65: 
    print("adults") 
else: 
    print("seniors")

