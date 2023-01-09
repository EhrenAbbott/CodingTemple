# We will continue practicing Object Oriented Programming in this assignment to become more fluent in Python. 
# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video 
# of what Brandon usually does to calculate his Rental Property ROI.
# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program 
# that will calculate the Return on Investment(ROI) for a rental property.
# This project will be completed individually, though you can feel free to share ideas with your fellow students.
# Once completed, commit the project to github and submit the link to this assignment.

class ROI(): 
    
    def income(self): 
        while True:
            income_answer = input("What is the monthly income of your property?")
            if income_answer: 
                try:  
                    inc = float(re.sub(",","", income_answer).strip('$'))
                    print(inc)
                    break
                except: 
                    print("Please enter a valid number.")
        while True: 
            expenses_answer = input("What are the total monthly expenses of your property?")
            if expenses_answer: 
                try:
                    exp = float(re.sub(",","", expenses_answer).strip('$'))
                    print(exp)
                    break
                except: 
                    print("Please enter a valid number.")
        while True: 
            investment_answer = input("What was your total initial investment on the property?")
            if investment_answer: 
                try: 
                    inv = float(re.sub(",","", investment_answer).strip('$'))
                    print(inv)
                    break 
                except: 
                    print("Please enter a valid number.")
        cash_flow = inc - exp 
        print(f"Your monthly cash flow is: ${cash_flow}")
        CoCROI = ((cash_flow * 12)/inv)*100
        print(f"Your Cash on Cash ROI is: {CoCROI}%")
    
my_property = ROI()

def runROI():
    my_property.income() 
    while True: 
        continue_q = input("Would you like to continue using the ROI calculator?")
        if continue_q.lower().strip('.') == "no": 
            print("Thank you for using the ROI Calculator!")
            break 
        elif continue_q.lower().strip('.') == "yes":
            my_property.income()
        else: 
            print("Please enter 'yes' or 'no'")
        

runROI()