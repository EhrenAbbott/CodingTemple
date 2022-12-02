# Your assignment for today is to create a parking garage class to get 
# more familiar with Object Oriented Programming(OOP). 


# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) 
# -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation


# When the project is completed, commit the final changes and submit your GitHub link.
#________________________________________________________________________________________________________



# I tried to add a bit more complexity to the program while (hopefully) still addressing all of the criteria 
# in the assignment description above. 
# I included some notes below the methods to describe what the intention of that section was.

class Garage():
    """ 
    Attributes for the class: 
    -Tickets expected to be a list 
    -Parking Spaces expected to be a list 
    -CurrentTicket expected to be a dictionary with 'paid' as the key
    """ 

    def __init__(self, tickets, parking_spaces, current_ticket): 
        self.tickets = tickets 
        self.parking_spaces = parking_spaces 
        self.current_ticket = current_ticket 
    
    def takeTicket(self): 
        for ticket in self.tickets: 
            if ticket > 0:
                print("Please take your ticket")
                self.tickets = [ticket - 1 for ticket in self.tickets]
                self.parking_spaces = [spaces - 1 for spaces in self.parking_spaces]
            else:
                print("Sorry, the lot is full at the moment :( ") 
    # Attepting to avoid giving a parking space ticket if there are no spots left. 
    # I feel like this could be streamlined with a list comprehension? But I could not get that to work. I tried: 
    # x for x in self.tickets if x > 0:          but to no avail :(

    
    def payForParking(self): 
        parking_rate = 10  
        while True:
            parking_hours = input("How many hours has your car been in the garage?")
            if "." in parking_hours and ".5" not in parking_hours:
                print("Please round up to the nearest half hour or full hour.")  
            elif ".5" in parking_hours: 
                print(f'Please pay ${float(parking_hours) * int(parking_rate)}0')
                break
            else: 
                print(f'Please pay ${int(parking_hours) * parking_rate}.00')
                break
    # The if statement is intended to avoid a calculation invovling a non-standard fraction of an hour, 
    # such as 1.2, as most parking garages only calculate based on the full hour or half hour.
    # Also added an equaiton to customize the amount paid with the number of hours in the garage.
    
    def haveYouPaid(self): 
        while True:
            have_you_paid = input("Have you paid? Press 1 for Yes and 2 for No.")
            if have_you_paid == '1': 
                self.current_ticket['paid'] = True
            elif have_you_paid == '2':
                self.current_ticket['paid'] = False  
            else: 
                print("Please enter a valid input")  
            if self.current_ticket['paid'] == True: 
                self.tickets = [ticket + 1 for ticket in self.tickets]
                self.parking_spaces = [spaces + 1 for spaces in self.parking_spaces] 
                print("Thank you have a nice day! You have 15 minutes to leave the lot.")
                break
            elif self.current_ticket['paid'] == False: 
                print("You must pay.")
    # Want to avoid an error if the user input is anything other than 1 or 2 and continue 
    # running this method until user inputs 1 to confirm they have paid
            
    def checkAvailability(self): 
        for spot in self.parking_spaces:  
            if spot > 1:       
                print("There are currently " + str(spot) + " parking spots available.") 
            elif spot == 1: 
                print("There is currently " + str(spot) + " parking spot available.") 
            elif spot == 0: 
                print("Sorry, there are no spots available right now :(")
    # Trying to account to a both a singular and plural noun phrase to avoid printing a 
    # satement like "There are 1 parking spots avaiable." Also want to avoid either of the first two statements 
    # if tickets = 0. 


my_garage = Garage([1], [1], {'paid': '' })

def runGarage(): 
    while True: 
        customer_selection = input("Please press 1 if you are entering the lot," + 
        " 2 if you are leaving, 3 to check parking availability, and 9 to quit.")
        if customer_selection.lower() == '9': 
            print("Thank you, have a nice day!")
            break
        elif customer_selection.lower() == '1': 
            my_garage.takeTicket() 
        elif customer_selection.lower() == '2': 
            my_garage.payForParking() 
            my_garage.haveYouPaid() 
        elif customer_selection.lower() == '3': 
            my_garage.checkAvailability()
        else: 
            print("Please enter a valid option.") 
            
runGarage()

#I've tried to work through every iteration of menu sequences, 
# and it seems they should all work I think.