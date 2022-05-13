#Jack Krejci
#Python Practice
#Classes
#"The Store" program


'''
Program that uses classes to create a profile for a store that is either a
customer or someone that works for the company which will allow different
rights for said user.
'''


#PARENT/MAIN CLASS 
#User class (Main Class)
class user:
    def __init__(self, username, email, firstName, lastName, age, gender, status):
        self.username = username
        self.email = email
        self.fname = firstName
        self.lname = lastName
        self.age = age
        self.gender = gender
        self.status = status

    #Method to send the user status to the user given the input O, W, or C
    def showStatus(self):
        if self.status == "O":
            return "owner"
        if self.status == "W":
            return "worker"
        if self.status == "C":
            return "customer"
        #Return none if there was a glitch in giving the status
        return None


#CHILD/SUB CLASSES
#Owner class (Extends User Class)
class owner(user):
    def __init__(self, username, email, firstName, lastName, age, gender, status):
        super().__init__(username, email, firstName, lastName, age, gender, status)

    #Method to ask the user for what choice they want to currently make 
    def askChoice(self):
        choice = input("\nWould you like to shop (owner discount 50% off), edit your products or quit?\n(s = shop, e = edit products, q = quit program): ").lower().strip()
        return choice

#Worker class (Extends User Class)
class worker(user):
    def __init__(self, username, email, firstName, lastName, age, gender, status):
        super().__init__(username, email, firstName, lastName, age, gender, status)
        
    #Method to ask the user for what choice they want to currently make 
    def askChoice(self):
        choice = input("\nWould you like to shop (employee discount 20% off), or quit?\n(s = shop, q = quit program): ").lower().strip()
        return choice
    
#Customer class (Extends User Class)
class customer(user):
    def __init__(self, username, email, firstName, lastName, age, gender, status):
        super().__init__(username, email, firstName, lastName, age, gender, status)

    #Method to ask the user for what choice they want to currently make 
    def askChoice(self):
        choice = input("\nWould you like to shop, edit your products or quit?\n(s = shop, q = quit program): ").lower().strip()
        return choice

#Functions for the main code

#Function for the programs store title 
def storeTitle():
    print("*" * 60)
    print(" " * 25, "The Store")
    print("*" * 60)

#Function for the programs greeting message
def greetingMsg():
    print("Welcome to The Store! Feel free to look around and what we have,\nor create an account and add whatever you want to your cart to buy.\nOr if you are a worker you can do a little more ;).")

#Function for showing the items at the store
def showItems():
    #Show the items in a cleaner format
    print("-" * 25, "Items List", "-" * 25)
    for item in products: #Print all the items in the store
        priceString = str(products[item])
        print("|", " " * 12, end = ' ')
        print("%-20s %10s %15s" % (item, priceString, "|"))
    print("-" * 62)

    
#Main Code

#Print the store title
storeTitle()

#Welcome the user to the store's website
greetingMsg()

#Initialize current user to there be no user (false)
currentUser = False

#Products that are at the store
products = {
    "apple": 1.99,
    "carrot": 0.99,
    "shirt": 12.99,
    "hat": 5.99
    }

#Ask the current person using the program if they'd like to make an account or look at our products
choice = input("\nWould you like to create an account or look at our products?\n(a = account, p = look at products, q = quit program): ").lower().strip()

#If the user didn't want to quit then we'll have other options to make
while choice != "q":
    
    #Now we can decide where to go from here whether they wanted to see the products or make an account
    if choice == "p":
        #Call the functions to show all the store items
        print() #Print some white space
        showItems()
    elif choice == "a":
        print("CREATE ACCOUNT\n")
        #Have a new user be created getting input from the user
        userUsername = input("Enter username: ").strip()
        userEmail = input("Enter your email: ").strip()
        userFirstName = input("Enter your first name: ").strip()
        userLastName = input("Enter your last name: ").strip()
        userAge = int(input("Enter your age: ").strip())
        #Catch error for an invalid age
        while userAge < 1 or userAge > 120:
            print("Invalid Age!")
            userAge = int(input("Enter your age: ").strip())

        userGender = input("Enter your gender (M/F): ").upper().strip()
        #Catch error if wrong value typed in for gender
        while userGender != "M" and userGender != "F":
            print("Invalid value for gender!")
            userGender = input("Enter your gender (M/F): ").upper().strip()
    
        userStatus = input("Are you the ownder, worker, or customer? (O, W, C): ").upper().strip()
        #Catch error for invalid status
        while userStatus != "O" and userStatus != "W" and userStatus != "C":
            print("Invalid Status!")
            userStatus = input("Are you the owner, worker, or customer? (O, W, C): ").upper().strip()

        #Create the user according to their status
        if userStatus == "O":
            currentUser = owner(userUsername, userEmail, userFirstName, userLastName, userAge, userGender, userStatus)
        elif userStatus == "W":
            currentUser = worker(userUsername, userEmail, userFirstName, userLastName, userAge, userGender, userStatus)
        elif userStatus == "C":
            currentUser = customer(userUsername, userEmail, userFirstName, userLastName, userAge, userGender, userStatus)


        #Greet the user to the program and show them their status
        print("\nGreetings %s %s, your status for the site is a %s." % (currentUser.fname, currentUser.lname, currentUser.showStatus()))
    else:
        print("Invalid Input!")

    #At the end of what they are doing if they are signed in ask if they want to shop or quit
    #If they are not signed in ask if they want to sign in or see products or quit
    if currentUser != False:
        #Get user choice according to their status
        choice = currentUser.askChoice()
        #choice = input("\nWould you like to shop or quit?(s = shop, q = quit program): ").lower().strip()
    else:
        choice = input("\nWould you like to create an account or look at our products?\n(a = account, p = look at products, q = quit program): ").lower().strip()

#Say goodbye to whoever used the program, say goodbye to the current user if one if logged in
if currentUser != False:
    print("\nGoodbye %s!" % currentUser.fname)
else:
    print("\nGoodbye whoever you are!")


        
