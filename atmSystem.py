import hashlib
import datetime

# database in dictionary
#Initialize the dict....
user_data = {}

user_id_counter = 1 # starting ID

today = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

# menu dictionary key values
menu_dict = {"date": today, 1:"Withdraw", 2:"Deposit", 3:"Complaints", 4:"Other Services"}


def register():
    global user_id_counter

    username = input("Register username: ")

    #check if user is already registered
    if username in user_data:
        return("Username already taken. Please another username")
    
    password = input("Register password: ")

    # hashing password
    hash_password = hashlib.sha256(password.encode()).hexdigest()

    # Assing unique user id
    user_id = user_id_counter
    user_id_counter += 1

    # store the registration details in the database
    user_data[username] = {"user_id":user_id, "hash_password":hash_password}

    return(f"Registration successful for {username} with the ID {user_id} .")

# Calling user registration function to register new users to our database
print(register())

# initialize atm machine variables

currentBalance = 80000


#login details
username = input("Enter username to login: ")

#check login details
if username in user_data:
    store_hash_password = user_data[username]["hash_password"]
    password = input("Enter login password: ")
    print("\n")

    #verify the user login details
    if hashlib.sha256(password.encode()).hexdigest() == store_hash_password:
        print(f"Welcome, {username}")
        print("date: " , today)

        def menu():
            print("Manevia Bank Liberia Limited")
            print("Date:" ,today)
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Complaint")
            print("4. Other services")

        menu()
        selectedOption = int(input("Please select an option: "))

        while selectedOption != 0:
            if(selectedOption == 1):
                print(f"You have selected : {menu_dict[1]}")
                withdrawal_amount = float(input("Enter withdraw amount: "))
                if (withdrawal_amount > currentBalance):
                    print("Insufficient funds. Please try again")
                else:
                    currentBalance -= withdrawal_amount
                    print(f"Transaction successful, take your cash. Balance: {currentBalance} ")
            elif(selectedOption == 2):
                print(f"You have selected : {menu_dict[2]}")
                deposit_amount = float(input("Enter deposit amount: "))
                currentBalance += deposit_amount
                print(f"You have deposited: {deposit_amount}. Balance: {currentBalance}")
            elif(selectedOption == 3 ):
                print(f"You have selected : {menu_dict[3]}")
                print("Please send all complaints to manevia@email.com")
            elif(selectedOption == 4):
                print(f"You have selected : {menu_dict[4]}")
                print("Contact customer service desk for other services.")
            else:
                print(" ")
                print("Enter valid options: 1 - 4 ")
            
            print(" ")
            menu()
            selectedOption = int(input("Please select an option: "))    
        print(" Thanks for your transaction!")
    else:
        print("Incorrect password. Please try again!")
else:
    print("Username not found! Please try again")


