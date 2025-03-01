# GROUP ASSIGNMENT G10 PYTHON [ FINALISED VERSION ] (V5.2.5)
# HERE ARE THE RULES YOU NEED TO KNOW.

# <1.> ANYTHING REGARDED TO PLAGIRISM WILL NOT BE ACCEPTED. (SUCH AS AI USES, DO NOT CLAIM AI WORKS AS YOUR PART.)
# <2.> REGARDING TO USING CODE FROM ONLINE SOURCES. PLEASE AND ABSOULATELY CITATE, PLAGIRISM IS UNACCPETABLE.
# <3.> LEAVE COMMENTS BESIDE YOUR WORK FOR BETTER DOCUMENTATION AND COMMUNICATION.
# <4.> SHARING CODE OUTSIDE OF THIS GROUP IS NOT ACCEPTABLE.

# ALL THE DATA ACROSS EVERY OTHER TXT FILES ARE FAKE DATA, HENCE WE CALL IT DATATEST TO MAKE TESTING EASIER, THE FINAL PRODUCT WILL STAY THAT WAY.
# WE WILL GIVE ACTUAL NAMES WHEN COMES TO PRESENTATION. OTHER THAN THAT BACK ENDS WILL ONLY BE ABLE TO SEE DATATEST

# =GROUP MEMBERS=
# DYLAN DENNY           TP074879 (LEADER)
# AIZIK NATHANIEL LIM   TP073371 (Cool member)
# CHOO YAT HAY          TP074534 (Cool member)
# CHONG VINCENT         TP073972 (Cool member)

# psst. Lecturer won't check our comments right? right..? ( scared_emoji :( )

# // UPDATE ON CODE (V5.2.5)_____________________________________________________________________________
# Debug.
# -
# -
# -

# HEY BUDDY! FEELING LOST? HAVE NO FEAR! WHEN YOU WANT TO LOOK FOR CERTAIN JUST DO CTRL + F WITH THE FOLLOWING KEYWORDS YOU CAN DO!
# EXAMPLE!! "# //" AND ENTER YOUR WAY BUDDY! OR YOU CAN COPY THE PRE MADE HEADERS I GAVE UNDER HERE. :)
# // ID GENERATION
# // LIBRARY AND FUNCTIONS
# // AIZIK : REVENUE
# // DYLAN : CHECK FUCNTIONS
# // VINCENT : CHECK FUCNTIONS
# // DYLAN : LIST SHOWCASE
# // VINCENT : LIST SHOWCASE
# // IAN : LIST SHOWCASE
# // AIZIK : LIST SHOWCASE
# // PANEL : SHARED
# // DYLAN : CAR DETAIL OVERWRITES
# // VINCENT : CUSTOMER SERVICE OVERWRITES
# // IAN : CUSTOMER SERVICE OVERWRITES
# // AIZIK : STAFF DETAIL OVERWRITES
# // DYLAN : CAR REGISTERATION
# // VINCENT : TRANSACTION REGRISTRATION & MODIFY FEATURES
# // IAN : CUSTOMER REGRISTRATION & MODIFY FEATURES
# // AIZIK : STAFF REGRISTRATION
# // UPDATE OWN PROFILE : SHARED
# // LOGINS : SHARED

# // FUNCTION PLACE_______________________________________________________________________________________________________
# // ID GENERATION
# Customer ID generation
def get_customer_id():
    with open('CustomerDB.txt', 'r') as f:
        f.readline()
        max_id = max(int(line.strip().split('|')[0][1:]) for line in f)# This Reads through the .txt file and checks
        # if the there are any existing  Customer ID's

    return max_id if max_id >= 100000 else 99999
# Staff ID generation -  I know they are the same but I'm not the one who are responsible for this part, i know is not optimised - Dylan.
def make_staff_id():
    with open("StaffDB.txt", "r") as f:
        f.readline()
        max_id = max(int(line.strip().split('|')[0][1:]) for line in f)# This Reads through the .txt file and checks
        # if the there are any existing  Staff ID's

    return max_id if max_id >= 1000 else 9999

# // LIBRARY AND IMPORTS
import datetime
import time # Ian's functions - For the Extra funsies, literally, I am serious. He really said that. - Dylan.

# // AIZIK : REVENUE
def revenue(filename = "BillDB.txt", total_revenue = 0):
    with open(filename, 'r') as file:
        header = file.readline().strip().split("|")
        
        tran_Date = header.index("Transaction_Date")
        Total_rental_charge = header.index("Total_Rental")
        
        while True:
            try:
                bill_year = int(input("Please type the year you want to check.\nInput: "))#Input the year they want to check 
                if len(str(bill_year)) == 4: #makes sure that the year is only 4 numbers long 
                    break 
                else:
                    print("Please input a valid year for example 2024")
            except:# This is for any input that might not be a number such as a letter or symbols.
                print("Please input a valid year for example 2024 with the format being (YYYY)")
        while True: 
            try:
                bill_month = int(input("Plese input the month in number from 1 to 12. \nInput:"))
                # the .zfile is to add a 0 at the start of the string  until it reaches the set limit in this case it is "2"
                if str(bill_month).zfill(2) in [str(i).zfill(2) for i in range(1,13)]:
                    print ("ok")
                    break
                else: 
                    print("That wasnt a valid month please try again")
            except:
                print("That wasnt a valid month please try again with the format being (MM)") 
                
        for line in file:
            data = line.strip().split('|')
            date = data[tran_Date]
            breakdown = date.strip().split('/')
                
            if str(breakdown[2]) == str(bill_year) and str(breakdown[1]) == str(bill_month).zfill(2):
               total_revenue += float(data[Total_rental_charge])      
    print(f"The total Revenue for {bill_month}/{bill_year} is: \n--------------------\nRM{total_revenue}\n--------------------")
    Homepage_Panel_manager()
    return total_revenue

# // DYLAN : CHECK FUCNTIONS
def Check_Duplicate_Name(user_input, FileSelected = "StaffDB.txt"):
    with open(FileSelected, "r") as StaffInfo_DB: # Opening files
        header = StaffInfo_DB.readline().strip().split("|") # Splits unecessary informations in txtfiles
        
        Staff_NameCheck = header.index("Staff_Name") # Assigning Variables while giving setting indexs for Username

    with open(FileSelected, "r") as StaffInfo_DB:
        next(StaffInfo_DB)  # Skips the line
        for List in StaffInfo_DB: # For every line in the Staff Database Table, it go through line by line
            Duplication = List.strip().split("|")
            if Duplication[Staff_NameCheck] == user_input: # Verification for duplicated datas.
                print("__________________________________________________________"
                      "\n[!] Error: Username with \""+user_input.upper()+"\" already exist!")
                return True
            elif Duplication[Staff_NameCheck] != user_input: # If the current line isn't matching base on the criteria, it head to next line
                    continue
    return False # Because this checks if it's duplicated. Returning False means there is not such data registered yet. While Returning True means data exist

def Check_Valid_Dates(user_input):
    try: # Return True if no Error occurs
        datetime.datetime.strptime(user_input, '%d/%m/%Y')
        return True
    except ValueError: # Return False if Error occurs
        print("__________________________________________________________"
              "\n[!] Error: Invalid date time format!")
        return False
# Check_Valid_Date well, checks dates, self explanatory. It compares the date format, and if it's true it prompt you to other functions. This function if often called when registering or updating dates

def Check_Duplicate_Registration_Car(user_input, FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, "r") as CarRegistered_DB: # Opening files
        header = CarRegistered_DB.readline().strip().split("|") # Splits unecessary informations in txtfiles
        
        Car_Registered_No = header.index("Car_Registered_No") # Assigning Variables while giving setting indexs for Username

    with open(FileSelected, "r") as CarRegistered_DB:
        next(CarRegistered_DB)  # Skips the line
        for List in CarRegistered_DB:
            Duplication = List.strip().split("|")
            if Duplication[Car_Registered_No].upper() == user_input.upper(): # Verification for duplicated datas.
                print("__________________________________________________________"
                      "\n[!] Error: Car with registration number \""+user_input.upper()+"\" already registered!")
                return True
            elif Duplication[Car_Registered_No].upper() != user_input.upper():
                continue
    return False

# // VINCENT : CHECK FUCNTIONS
def Matching_Registration_Car(user_input, FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, "r") as CarRegistered_DB: # Opening files
        header = CarRegistered_DB.readline().strip().split("|") # Splits unecessary informations in txtfiles
        
        Car_Registered_No = header.index("Car_Registered_No") # Assigning Variables while giving setting indexs for Username
        Rental_Availability = header.index("Rental_Availability")

    with open(FileSelected, "r") as CarRegistered_DB:
        next(CarRegistered_DB)  # Skips the line
        for List in CarRegistered_DB:
            Matching = List.strip().split("|")
            if Matching[Car_Registered_No].upper() == user_input.upper() and Matching[Rental_Availability].upper() == "AVAILABLE": # Verification for duplicated datas.
                return True
            elif Matching[Car_Registered_No].upper() != user_input.upper():
                continue
    print("__________________________________________________________"
          "\n[!] Error: Car with registration number \""+user_input.upper()+"\" is not registered or not avaialble!")
    return False

def Matching_Customer_ID(user_input, FileSelected = "CustomerDB.txt"):
    with open(FileSelected, "r") as Customer_DB: # Opening files
        header = Customer_DB.readline().strip().split("|") # Splits unecessary informations in txtfiles
        
        Customer_ID = header.index("Customer_ID") # Assigning Variables while giving setting indexs for Username

    with open(FileSelected, "r") as Customer_DB:
        next(Customer_DB)  # Skips the line
        for List in Customer_DB:
            Duplication = List.strip().split("|")
            if Duplication[Customer_ID].upper() == user_input.upper(): # Verification for duplicated datas.
                return True
            elif Duplication[Customer_ID].upper() != user_input.upper():
                continue
    print("__________________________________________________________"
          "\n[!] Error: Customer with \""+user_input.upper()+"\" is not registered!")
    return False

# // DYLAN : LIST SHOWCASE
# List for Car that are Registered
def List_Regis_Car(FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, 'r') as CarRegistered_DB: # Open File, Obviously
        
        header = CarRegistered_DB.readline().strip().split('|') # Splits unecessary informations in txtfiles
        Empty = False
        
        print("__________________________________________________________")
        for index, line in enumerate(CarRegistered_DB, start = 1): # Print the amount of data base on how many lines there is, start from line 1 due to header being 0
            print(f'\nCar Number {index}#') # Since it base on how much amount there is, there will be a counter example #1 #2 etc.
            values = line.strip().split('|')
            Empty = True
            for header_line, value in zip(header, values):
                print(f'{header_line.replace("_", " ").title()}: {value}') # Print the well, datas
            print("__________________________________________________________"
                  "\n[!] Successfully load all Data.")
        if not Empty:
            print("\n[!] Error: No Data found.")

# List for Car that are Available
def List_Avail_Car(FileSelected="CarRegisteredDB.txt"):
    with open(FileSelected, 'r') as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split('|')
        
        Rental_Avail = header.index('Rental_Availability')
        Empty = False
        
        print("__________________________________________________________")
        for index, line in enumerate(CarRegistered_DB, start = 1):
            Row_Value = line.strip().split('|')            
            if Row_Value[Rental_Avail].upper() == 'AVAILABLE':
                print(f'\nCar Number {index}#')
                Empty = True
                for header_item, value in zip(header, Row_Value):
                    print(f'{header_item.replace("_", " ").title()}: {value}')
                print("__________________________________________________________"
                      "\n[!] Successfully load all Data.")
        if not Empty:
            print("\n[!] Error: No Data found.")

# List for Car that are Rented
def List_Rented_Car(FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, 'r') as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split('|')
    
        Rental_Avail = header.index('Rental_Availability')
        Empty = False
        
        print("__________________________________________________________")
        for index, line in enumerate(CarRegistered_DB, start = 1):
            Row_Value = line.strip().split('|')
            if Row_Value[Rental_Avail].upper() == 'RENTED':
                print(f'\nCar Number {index}#')
                Empty = True
                values = line.strip().split('|')  
                for header, value in zip(header, values):
                    print(f'{header.replace("_", " ").title()}: {value}')
                print("__________________________________________________________"
                      "\n[!] Successfully load all Data.")
        if not Empty:
            print("\n[!] Error: No Data found.")

# // VINCENT : LIST SHOWCASE
def List_Rental_Car(SeatsNum, FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, 'r') as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split('|')
    
        Rental_Avail = header.index('Rental_Availability')
        Seating_Caps = header.index('Seating_Capacity')
        Empty = False
        
        print("__________________________________________________________")
        for index, line in enumerate(CarRegistered_DB, start=1):
            Row_Value = line.strip().split('|')
            if Row_Value[Rental_Avail].upper() == 'AVAILABLE' and Row_Value[Seating_Caps] == str(SeatsNum):
                print(f'\nCar Number {index}#')
                Empty = True
                values = line.strip().split('|')  
                for header, value in zip(header, values):
                    print(f'{header.replace("_", " ").title()}: {value}')
                print("__________________________________________________________"
                      "\n[!] Successfully load all Data.")
    
        if not Empty:
            print("\n[!] Error: No Data found.")

def List_Transaction_Input():
    user_input = input("__________________________________________________________"
                       "\n<!> Transaction Date:"
                       "\n(Type \"exit\" to leave)"
                       "\n\nInput: ")
    if user_input.upper() == "EXIT":
        print("__________________________________________________________"
              "\n[!] Returning...")
        Customer_Service_Panel_Transaction()
    if not user_input.strip():
        print("__________________________________________________________"
              "\n[!] Error: Value cannot be blank. Please enter again.")
        List_Transaction_Input()
    else:
        if Check_Valid_Dates(user_input) == True:
            List_Transaction_Dt(user_input)
        else:
            List_Transaction_Input()

def List_Transaction_Dt(user_input, FileSelected = "BillDB.txt"):
    user_input = datetime.datetime.strptime(user_input, "%d/%m/%Y")
    with open(FileSelected, 'r') as BillDB:
        header = BillDB.readline().strip().split('|')
    
        Transaction_Date = header.index('Transaction_Date')
        
        print("__________________________________________________________")
        for index, line in enumerate(BillDB, start=1):
            Row_Value = line.strip().split('|')
            transaction_date = datetime.datetime.strptime(Row_Value[Transaction_Date], "%d/%m/%Y")
            if transaction_date == user_input:
                print(f'\nBill {index}#')
                for header, value in zip(header, Row_Value):
                    print(f'{header.replace("_", " ").title()}: {value}')
                print("__________________________________________________________"
                      "\n[!] Successfully load all Data.")

# // IAN : LIST SHOWCASE
def List_view_cus():
    Selected_File = "CustomerDB.txt"
    with open(Selected_File, 'r') as Cust_prof:

        header = Cust_prof.readline().strip().split('|')

        print("__________________________________________________________")
        for index, line in enumerate(Cust_prof, start=1):
            print(f'\nCustomer Profile {index}#') # this Numerates each read profile and categorizes them into ascending numbers
            values = line.strip().split('|')
            for header_line, value in zip(header, values):
                print(f'{header_line.replace("_", " ").title()}: {value}')
            print("__________________________________________________________"
                  "\n[!] Successfully loaded all Data.")
            
# // AIZIK : LIST SHOWCASE

# // PANEL : SHARED
# Car Information Panel
def CI_Panel():
    Menu_Option = [1,2,3,4]
    while True: # If Verification is successful, panel is given
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                     "\n=[!!]= Car Information =[!!]="
                                     "\n"
                                     "\n<!> Please type the options (numbers) listed down below"
                                     "\n1. List of Registered Cars."
                                     "\n2. List of Available car to rent." 
                                     "\n3. List of Rented and Returning Date."
                                     "\n4. Return to Car Service Staff Menu."
                                     "\n\nInput: "))
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
        if Selection_Opt in Menu_Option:
            if 1 <= Selection_Opt <= 3:
                if Selection_Opt == 1:
                    List_Regis_Car()
                if Selection_Opt == 2:
                    List_Avail_Car()
                if Selection_Opt == 3:
                    List_Rented_Car()
            else: # Option for leaving 
                print("__________________________________________________________"
                      "\n[!] Returning to Car Service Staff Menu...") #Heading Back to Main Menu Yup Yup.
                Car_Service_Panel() # break the loop and return to Menu by telling the login user want to leave.
        else:
            print("__________________________________________________________"
                  "\n[!] Error: Invalid option, try again... (Options is only ranged from 1 to 6.)"
                  "\n")

# Car Detail Overwrite Panels
def Car_D_O_Panel():
    Menu_Option = [1,2,3,4,5,6]
    while True: # If Verification is successful, panel is given
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                     "\n=[!!]= Car Detail Overwrite =[!!]="
                                     "\n"
                                     "\n<!> Please type the options (numbers) listed down below"
                                     "\n1. Overwrite Insurance Policy Number."
                                     "\n2. Overwrite Insurance Expiry Date." 
                                     "\n3. Overwrite Road Tax Expiry Date"
                                     "\n4. Overwrite Car Renting Rate Per Day."
                                     "\n5. Overwrite Rental Availablity."
                                     "\n6. Return to Car Service Staff Menu."
                                     "\n\nInput: "))
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
        if Selection_Opt in Menu_Option:
            if 1 <= Selection_Opt <= 5:
                if Selection_Opt == 1:
                    Overwrite_IPN()
                if Selection_Opt == 2:
                    Overwrite_IXD()
                if Selection_Opt == 3:
                    Overwrite_RTXD()
                if Selection_Opt == 4:
                    Overwrite_CRRD()
                if Selection_Opt == 5:
                    Overwrite_RentalAV()
            else: # Option for leaving 
                print("__________________________________________________________"
                      "\n[!] Returning to Car Service Staff Menu...") #Heading Back to Main Menu Yup Yup.
                Car_Service_Panel() # break the loop and return to Menu by telling the login user want to leave.
        else:
            print("__________________________________________________________"
                  "\n[!] Error: Invalid option, try again... (Options is only ranged from 1 to 6.)"
                  "\n")

def Car_Service_Panel():
    Menu_Option = [1,2,3,4,5] # Option user can use 
    while True: # If Verification is successful, panel is given
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                     "\n=[!!]= Car Service Staff =[!!]="
                                     "\n"
                                     "\n<!> Please type the options (numbers) listed down below"
                                     "\n1. Register New Car."
                                     "\n2. Update Car Detail." 
                                     "\n3. Car Information."
                                     "\n4. Update own Profile."
                                     "\n5. Return to Menu."
                                     "\n\nInput: "))
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
        
        if Selection_Opt in Menu_Option:
            if 1 <= Selection_Opt <= 4:
                if Selection_Opt == 1:
                    Car_Service_Registration()
                if Selection_Opt == 2:
                    Car_Detail_Overwrite() #NOT FINISHED
                if Selection_Opt == 3:
                    CI_Panel()
                if Selection_Opt == 4:
                    Update_User_Panel()
            else: # Option for leaving 
                print("__________________________________________________________"
                      "\n[!] Returning to Homepage...") #Heading Back to Main Menu Yup Yup.
                Homepage_Panel()
        else:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options is only ranged from 1 to 5.)"
                  "\n")

def Update_User_Panel():
    Menu_Option = [1,2,3] # Option user can use 
    while True: # If Verification is successful, panel is given
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                     "\n=[!!]= Car Service Staff =[!!]="
                                     "\n"
                                     "\n<!> Please type the options (numbers) listed down below"
                                     "\n1. Update Password."
                                     "\n2. Update Username." 
                                     "\n3. Return to Menu."
                                     "\n\nInput: "))
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
        
        if Selection_Opt in Menu_Option:
            if 1 <= Selection_Opt <= 2:
                if Selection_Opt == 1:
                    Update_User_P_Info()
                if Selection_Opt == 2:
                    Update_User_N_Info()
            else: # Option for leaving 
                print("__________________________________________________________"
                      "\n[!] Returning to Car Service Staff Menu...") #Heading Back to Main Menu Yup Yup.
                break
        else:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options is only ranged from 1 to 3.)"
                  "\n")

def Homepage_Panel():
    Menu_Option = [1,2,3,4]
    while True:
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                      "\n=[!!]= Hello and welcome to Car Rental System V1.0.0! =[!!]="
                                      "\nWhat can we do for you today?"
                                      "\n"
                                      "\n<!> Please type the number corespond to options listed down below:"
                                      "\n1. Manager Profile"
                                      "\n2. Customer Service Staff" 
                                      "\n3. Car Service Staff"
                                      "\n4. Quit."
                                      "\n\nInput: "))
        except ValueError: #Checks the DataType and see if they are acceptable
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
    
        if Selection_Opt in Menu_Option: #Options between the 3 options with each of them have separated work
                if 1 <= Selection_Opt <= 3:
                    if Selection_Opt == 1: #Manager Function: Aizik Part.
                        if SecurityCheck_Staff_Role.upper() == "MANAGER":
                            Homepage_Panel_manager()
                        else:
                            print("[!] You do not have permission to access this!")
                    if Selection_Opt == 2: #Customer Service Staff: Ian, Vincent Part.
                        if SecurityCheck_Staff_Role.upper() == "CUSTOMER_STAFF" or SecurityCheck_Staff_Role.upper() == "MANAGER":
                            Customer_Service_Panel_Menu()
                        else:
                            print("[!] You do not have permission to access this!")
                    if Selection_Opt == 3: #Car Service Staff: Dylan Part.
                        if SecurityCheck_Staff_Role.upper() == "CAR_STAFF" or SecurityCheck_Staff_Role.upper() == "MANAGER":
                            Car_Service_Panel() #Function Called
                        else:
                            print("[!] You do not have permission to access this!")
                else:
                    print("__________________________________________________________"
                          "\n[!] Logging Out...")
                    User_Login()
        else:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options is only ranged from 1 to 4.)"
                  "\n")

def Customer_Service_Panel_Transaction():
    Menu_Option = [1,2,3,4,5,6] # Option user can use 
    while True: # If Verification is successful, panel is given
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                     "\n=[!!]= Customer Service Transactions =[!!]="
                                     "\n"
                                     "\n<!> Please type the options (numbers) listed down below"
                                     "\n1. List of available cars w/ specific seat capacity."
                                     "\n2. Register new transactions." 
                                     "\n3. Update rental availability."
                                     "\n4. List of rental transactions"
                                     "\n5. Delete rental transactions"
                                     "\n6. Return to Menu"
                                     "\n\nInput: "))
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
        
        if Selection_Opt in Menu_Option:
            if 1 <= Selection_Opt <= 5:
                if Selection_Opt == 1:
                    Registered_Car_SeatsCap()
                if Selection_Opt == 2:
                    Transaction_Creation() #NOT FINISHED
                if Selection_Opt == 3:
                    Car_Detail_Customer_Overwrite()
                if Selection_Opt == 4:
                    List_Transaction_Input()
                if Selection_Opt == 5:
                    Delete_Transaction()
            else: # Option for leaving 
                print("__________________________________________________________"
                      "\n[!] Returning to Customer Service Menu...") #Heading Back to Main Menu Yup Yup.
                Customer_Service_Panel_Menu()
        else:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options is only ranged from 1 to 6.)"
                  "\n")

def Cus_D_O_Panel():
    Menu_Option = [1,2,3,4,5,6,7] # allocates the possible inputs
    while True:
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                      "\n=[!]= Customer Detail Overwrite =[!]="
                                      "\n"
                                      "\n<!> Please type the options (numbers) listed down below"
                                      "\n1. Overwrite Customer's Name."
                                      "\n2. Overwrite Customer's Type."
                                      "\n3. Overwrite Customer's License."
                                      "\n4. Overwrite Customer's Phone Number."
                                      "\n5. Overwrite Customer's Address."
                                      "\n6. Overwrite Customer's Email."
                                      "\n7. Return to Customer Service Staff Menu."
                                      "\n\nInput: "))
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
        if Selection_Opt in Menu_Option:
            if 1 <= Selection_Opt <= 6:
                if Selection_Opt == 1:
                    Overwrite_C_N()
                if Selection_Opt == 2:
                    Overwrite_C_Type()
                if Selection_Opt == 3:
                    Overwrite_C_LCE()
                if Selection_Opt == 4:
                    Overwrite_C_PN()
                if Selection_Opt == 5:
                    Overwrite_C_ADD()
                if Selection_Opt == 6:
                    Overwrite_Email()

            else:  # gives users the option to return to the main page
                print("__________________________________________________________"
                      "\n[!] Returning to Customer Service Staff Menu...")
                Customer_Service_Panel_Menu()  # break the loop and return to Menu by telling the login user want to leave.
        else:
            print("__________________________________________________________"
                  "\n[!] Error: Invalid option, try again... (Options is only ranged from 1 to 6.)"
                  "\n")

def Customer_Service_Panel_Menu():
    while True:
        try:
            menu_num = int(input('__________________________________________________________'
                                 '\n=[!!]= Customer Service Staff =[!!]='
                                 '\n'
                                 '\n<!> Please use the numbers below to reach your designated location'
                                 '\n1. Register Customers'
                                 '\n2. View Customer profiles'
                                 '\n3. Update Customer profiles'
                                 '\n4. Update own profile'
                                 '\n5. Delete Customer Profiles'
                                 '\n6. Transaction Creation and many more'
                                 '\n7. Return to the main menu'
                                 '\n\nInput:'))
            
        except ValueError:  # This checks if the input is the correct format requested
            print('Invalid format type, Please enter an Integer (e.g. 1/2/3/4/5/6/7)')
            time.sleep(2)
            return Customer_Service_Panel_Menu()

        if menu_num >= 1 or menu_num <= 6:
            if menu_num == 1:
                Customer_Registration()

            if menu_num == 2:
                List_view_cus()

            if menu_num == 3:
                Cust_Detail_Overwrite()

            if menu_num == 4:
                Update_User_Panel()

            if menu_num == 5:
                Cust_Prof_Del()

            if menu_num == 6:
                Customer_Service_Panel_Transaction()
                
            if menu_num == 7:
                Homepage_Panel()


        else:
            print('Please use Numbers as stated above')
            "\n"
            '\n'
            time.sleep(2)
            return Customer_Service_Panel_Menu()

#__________________________________________#HOME PAGE FOR MANANGER#__________________________________________#

def Homepage_Panel_manager():
    Menu_Option = [1,2,3,4,5,6]
    while True:
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                      "\n=[!!]= Staff Management =[!!]="
                                      "\nWhat can we do for you today?"
                                      "\n"
                                      "\n<!> Please type the number corespond to options listed down below:"
                                      "\n1. Register new Staff" 
                                      "\n2. Edit Staff details "
                                      "\n3. Update car renting rate per day"
                                      "\n4. Update Own Profile"
                                      "\n5. View monthly revenue report"
                                      "\n6. Exit."
                                      "\n\nInput: "))
        except ValueError: #Checks the DataType and see if they are acceptable
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
    
        if Selection_Opt in Menu_Option: #Options between the 3 options with each of them have separated work
                if 1 <= Selection_Opt <= 6:
                    if Selection_Opt == 1: #will call the Staff registration function.
                        Staff_Registration()
                        
                    elif Selection_Opt == 2:# calls staff edfi function 
                        find_staff()
                 
                    elif Selection_Opt == 3:
                        Manager_Car_Detail_Overwrite()
            
                    elif Selection_Opt == 4:
                        Update_User_Panel()
                        
                    elif Selection_Opt == 5:
                        revenue()
                        
                    elif Selection_Opt == 6:
                        Homepage_Panel()
                        
# // DYLAN : CAR DETAIL OVERWRITES
def Car_Detail_Overwrite(FileSelected = "CarRegisteredDB.txt"):
    user_input = input("__________________________________________________________"
                       "\n<!> Car Registered No:"
                       "\n(Type \"exit\" to leave)"
                       "\n\nInput: ")
    if user_input.upper() == "EXIT":
        print("__________________________________________________________"
              "\n[!] Returning to Menu...")
        return False
    else:
        with open(FileSelected, "r") as CarRegistered_DB:
            header = CarRegistered_DB.readline().strip().split("|")
            Registered_Car_No = header.index("Car_Registered_No")
            
        with open(FileSelected, "r") as CarRegistered_DB:
            next(CarRegistered_DB)  # Skips the line
            for List in CarRegistered_DB:
                Duplication = List.strip().split("|")
                if Duplication[Registered_Car_No].upper() == user_input.upper(): # Verification for duplicated datas.
                    global Current_CDO_Data
                    Current_CDO_Data = user_input
                    Car_D_O_Panel()
                elif Duplication[Registered_Car_No].upper() != user_input.upper():
                    continue
        print("__________________________________________________________"
              "\n[!] Error: \""+user_input.upper()+"\" is not registered!")
        Car_Detail_Overwrite()
        

def Overwrite_RTXD(FileSelected = "CarRegisteredDB.txt"):        
    with open(FileSelected, "r") as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split("|")
        
        Car_Registered_No = header.index("Car_Registered_No")
        RoadTax_Expire_Dt = header.index("Road_Tax_Expiry_Date")
    
    with open(FileSelected, "r") as CarRegistered_DB: # Read the entire txt file and store its contents
        Rows = CarRegistered_DB.readlines()
        
    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Car_Registered_No].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the new road tax expiry date: "
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if not user_input.strip():
                print("__________________________________________________________"
                      "\n[!] Error: Value cannot be blank. Please enter again.")
                continue
            else:
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    return False
                if Check_Valid_Dates(user_input) == True:
                    Updated_Value = user_input
                    Index[RoadTax_Expire_Dt] = Updated_Value
                    Rows[i] = "|".join(Index)+"\n"
                    print("__________________________________________________________"
                          "\n[!] Road Tax Expiry Date successfully updated.")
                    break
                else:
                    Overwrite_RTXD()
                    
    with open(FileSelected, "w") as CarRegistered_DB:
        CarRegistered_DB.writelines(Rows)
    
def Overwrite_IXD(FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, "r") as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split("|")
        
        Car_Registered_No = header.index("Car_Registered_No")
        Insurance_Exp_Dt = header.index("Insurance_Expiry_Date")
    
    with open(FileSelected, "r") as CarRegistered_DB: # Read the entire txt file and store its contents
        Rows = CarRegistered_DB.readlines()
        
    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Car_Registered_No].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the new insurance expiry date: "
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if not user_input.strip():
                print("__________________________________________________________"
                      "\n[!] Error: Value cannot be blank. Please enter again.")
                continue
            else:
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    return False
                if Check_Valid_Dates(user_input) == True:
                    Updated_Value = user_input
                    Index[Insurance_Exp_Dt] = Updated_Value
                    Rows[i] = "|".join(Index)+"\n"
                    print("__________________________________________________________"
                          "\n[!] Insurance Expiry Date sucessfully updated.")
                    break
                else:
                    Overwrite_IXD()
                    
    with open(FileSelected, "w") as CarRegistered_DB:
        CarRegistered_DB.writelines(Rows)
        
def Overwrite_IPN(FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, "r") as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split("|")
        
        Car_Registered_No = header.index("Car_Registered_No")
        Insurance_Policy_No = header.index("Insurance_Policy_No")
    
    with open(FileSelected, "r") as CarRegistered_DB: # Read the entire txt file and store its contents
        Rows = CarRegistered_DB.readlines()
        
    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Car_Registered_No].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the new insurance policy number:"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                break
            Updated_Value = user_input
            Index[Insurance_Policy_No] = Updated_Value
            Rows[i] = "|".join(Index)+"\n"
            print("__________________________________________________________"
                  "\n[!] Insurance Policy Number sucessfully updated.")
            break
    
    with open(FileSelected, "w") as CarRegistered_DB:
        CarRegistered_DB.writelines(Rows)
        
def Overwrite_CRRD(FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, "r") as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split("|")
        
        Car_Registered_No = header.index("Car_Registered_No")
        Rent_Rate_Pday = header.index("Renting_Rate_Per_Day")
        
    with open(FileSelected, "r") as CarRegistered_DB: # Read the entire txt file and store its contents
        Rows = CarRegistered_DB.readlines()
        
    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Car_Registered_No].upper() == Current_CDO_Data.upper():
            try:
                user_input = input("__________________________________________________________"
                                   "\n<!> Enter the new Renting Rate: (RM)"
                                   "\n(Type \"exit\" to leave)"
                                   "\n\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    break
                user_input = float(user_input)
                if type(user_input) == float:
                    Updated_Value = str(user_input)
                    Index[Rent_Rate_Pday] = Updated_Value
                    Rows[i] = "|".join(Index)+"\n"
                    print("__________________________________________________________"
                          "\n[!] Car Renting Rate updated.")
                    break
            except ValueError:
                print("__________________________________________________________"
                      "\n[!] Invalid input, try again... (Value only accept numeric.)")
                Overwrite_CRRD()

    with open(FileSelected, "w") as CarRegistered_DB:
        CarRegistered_DB.writelines(Rows)

def Overwrite_RentalAV(FileSelected = "CarRegisteredDB.txt"):
    Option = [1, 2, 3, 4, 5]
    
    with open(FileSelected, "r") as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split("|")

        Car_Registered_No = header.index("Car_Registered_No")
        Rental_Avail = header.index("Rental_Availability")
        Last_Service_Dt = header.index("Last_Service_Date")
        Car_Rental_Date = header.index("Car_Rental_Date")
        Returning_Date = header.index("Return_Date")

    with open(FileSelected, "r") as CarRegistered_DB:
        Rows = CarRegistered_DB.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Car_Registered_No].upper() == Current_CDO_Data.upper():
            try:
                user_input = input("__________________________________________________________"
                                   "\n<!> List any of the option below to update the availability"
                                   "\n(Type \"exit\" to leave)"
                                   "\n1. Available"
                                   "\n2. Reserved"
                                   "\n3. Rented"
                                   "\n4. Under service"
                                   "\n5. Disposed"
                                   "\n\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    break
                if int(user_input) in Option:  # Check if the input is in the option list
                    user_input = int(user_input)
                    if user_input == 1:
                        Updated_Value = "AVAILABLE"
                        Index[Returning_Date] = "NIL"
                        Index[Car_Rental_Date] = "NIL"
                    elif user_input == 2 or user_input == 3:
                        Updated_Value = "RESERVED" if user_input == 2 else "RENTED"
                        while True:
                            user_input = input("__________________________________________________________"
                                               "\n<!> Rental Date"
                                               "\n\nInput: ")
                            if Check_Valid_Dates(user_input):
                                Index[Car_Rental_Date] = user_input
                                break
                            else:
                                continue
                        while True:
                            user_input = input("__________________________________________________________"
                                               "\n<!> Returning Date"
                                               "\n\nInput: ")
                            if Check_Valid_Dates(user_input):
                                Index[Returning_Date] = user_input
                                break
                            else:
                                continue
                    elif user_input == 4:
                        Updated_Value = "UNDER SERVICE"
                        Index[Returning_Date] = "NIL"
                        Index[Car_Rental_Date] = "NIL"
                        Index[Last_Service_Dt] = datetime.date.today().strftime('%d/%m/%Y')
                    elif user_input == 5:
                        while True:
                            user_input = input("__________________________________________________________"
                                               "\n<!> Disposing will result into Car Deletion. YES/NO?"
                                               "\n[!] Warning: ACTION cannot be REVERTED"
                                               "\n\nInput: ")
                            if user_input.upper() == "YES":
                                del Rows[i]
                                print("__________________________________________________________"
                                      "\n[!] Car Deleted.")
                                break
                            elif user_input.upper() == "NO":
                                print("__________________________________________________________"
                                      "\n[!] Returning...")
                                return False
                            else:
                                print("__________________________________________________________"
                                      "\n[!] Error: Input can only accept yes or no.")
                        break  # Exit the loop since the row has been deleted
                    Index[Rental_Avail] = Updated_Value
                    Rows[i] = "|".join(Index) + "\n"
                    print("__________________________________________________________"
                          "\n[!] Car Availability updated.")
                    break
                else:
                    print("__________________________________________________________"
                          "\n[!] Invalid option, try again... (Options are only ranged from 1 to 5.)")
                    Overwrite_RentalAV()  # Return the result of the recursive call
            except ValueError:
                print("__________________________________________________________"
                      "\n[!] Error: Invalid input, try again... (Value only accepts numeric.)")
                Overwrite_RentalAV()  # Return the result of the recursive call

    with open(FileSelected, "w") as CarRegistered_DB:
        CarRegistered_DB.writelines(Rows)

# // VINCENT : CUSTOMER SERVICE OVERWRITES
def Car_Detail_Customer_Overwrite(FileSelected = "CarRegisteredDB.txt"):
    user_input = input("__________________________________________________________"
                       "\n<!> Car Registered No:"
                       "\n(Type \"exit\" to leave)"
                       "\n\nInput: ")
    if user_input.upper() == "EXIT":
        print("__________________________________________________________"
              "\n[!] Returning to Menu...")
        return False
    else:
        with open(FileSelected, "r") as CarRegistered_DB:
            header = CarRegistered_DB.readline().strip().split("|")
            Registered_Car_No = header.index("Car_Registered_No")
            
        with open(FileSelected, "r") as CarRegistered_DB:
            next(CarRegistered_DB)  # Skips the line
            for List in CarRegistered_DB:
                Duplication = List.strip().split("|")
                if Duplication[Registered_Car_No].upper() == user_input.upper(): # Verification for duplicated datas.
                    global Current_CDO_Data
                    Current_CDO_Data = user_input
                    print(Current_CDO_Data)
                    Overwrite_RentalAV_Customer()
                elif Duplication[Registered_Car_No].upper() != user_input.upper():
                        continue
        print("__________________________________________________________"
              "\n[!] Error: \""+user_input.upper()+"\" is not registered!")
        Car_Detail_Customer_Overwrite()

def Overwrite_RentalAV_Customer(FileSelected = "CarRegisteredDB.txt"):
    Option = [1, 2, 3]
    
    with open(FileSelected, "r") as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split("|")

        Car_Registered_No = header.index("Car_Registered_No")
        Rental_Avail = header.index("Rental_Availability")
        Car_Rental_Date = header.index("Car_Rental_Date")
        Returning_Date = header.index("Return_Date")

    with open(FileSelected, "r") as CarRegistered_DB:
        Rows = CarRegistered_DB.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Car_Registered_No].upper() == Current_CDO_Data.upper():
            try:
                user_input = input("__________________________________________________________"
                                   "\n<!> List any of the option below to update the availability"
                                   "\n(Type \"exit\" to leave)"
                                   "\n1. Available"
                                   "\n2. Reserved"
                                   "\n3. Rented"
                                   "\n\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    return False
                if int(user_input) in Option:  # Check if the input is in the option list
                    user_input = int(user_input)
                    if user_input == 1:
                        Updated_Value = "AVAILABLE"
                        Index[Returning_Date] = "NIL"
                        Index[Car_Rental_Date] = "NIL"
                    elif user_input == 2 or user_input == 3:
                        Updated_Value = "RESERVED" if user_input == 2 else "RENTED"
                        while True:
                            user_input = input("__________________________________________________________"
                                               "\n<!> Rental Date"
                                               "\n\nInput: ")
                            if Check_Valid_Dates(user_input):
                                Index[Car_Rental_Date] = user_input
                                break
                            else:
                                continue
                        while True:
                            user_input = input("__________________________________________________________"
                                               "\n<!> Returning Date"
                                               "\n\nInput: ")
                            if Check_Valid_Dates(user_input):
                                Index[Returning_Date] = user_input
                                break
                            else:
                                continue
                    Index[Rental_Avail] = Updated_Value
                    Rows[i] = "|".join(Index) + "\n"
                    print("__________________________________________________________"
                          "\n[!] Car Availability updated.")
                    break
                else:
                    print("__________________________________________________________"
                          "\n[!] Invalid option, try again... (Options are only ranged from 1 to 3.)")
                    return Overwrite_RentalAV_Customer(FileSelected)  # Return the result of the recursive call
            except ValueError:
                print("__________________________________________________________"
                      "\n[!] Error: Invalid input, try again... (Value only accepts numeric.)")
                return Overwrite_RentalAV_Customer(FileSelected)  # Return the result of the recursive call

    with open(FileSelected, "w") as CarRegistered_DB:
        CarRegistered_DB.writelines(Rows)
    Customer_Service_Panel_Transaction()

# // IAN : CUSTOMER SERVICE OVERWRITES
def Overwrite_C_Type():
    Selected_file = "CustomerDB.txt" # Makes it easier to retrieve the same txt file with hopefully shorter text
    with open(Selected_file, "r") as Customer_prof:
        header = Customer_prof.readline().strip().split("|") # reads and splits by the "|" symbol to retrieve data

        Customer_ID = header.index("Customer_ID")
        Customer_Origins = header.index("Customer_Origins")
        Customer_Num_Identification = header.index("Customer_Num_Identification")

    with open(Selected_file, "r") as Customer_prof:  # Reads the requested .txt file and stores data
        Rows = Customer_prof.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            Option = [1, 2, 3, 4, 5]
            try:
                user_input = input("__________________________________________________________"
                                   f"\n<!> Pick The Numbers below to Change Customer's Type:"
                                   "\n(Type \"exit\" to leave)"
                                   "\n1. Local"
                                   "\n2. Foreign"
                                   "\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    return False
                user_input = int(user_input)
                if user_input in Option:
                    if user_input == 1:
                        for i, line in enumerate(Rows):
                            Index = line.strip().split("|")
                            if Index[Customer_ID].upper() == Current_CDO_Data.upper():
                                user_input = input("__________________________________________________________"
                                                   "\n<!> Enter the New Customer's NRIC:"
                                                   "\n(Type \"exit\" to leave)"
                                                   "\n\nInput: ")
                                if user_input.upper() == "EXIT":
                                    print("__________________________________________________________"
                                          "\n[!] Returning...")
                                    return False
                                Updated_Value = user_input
                                Index[Customer_Origins] = "Local"
                                Index[Customer_Num_Identification] = Updated_Value
                                Rows[i] = "|".join(Index) + "\n"
                                print("__________________________________________________________"
                                      "\n[!] Customer's NRIC sucessfully updated.")
                                break

                    elif user_input == 2:
                        for i, line in enumerate(Rows):
                            Index = line.strip().split("|")
                            if Index[Customer_ID].upper() == Current_CDO_Data.upper():
                                user_input = input("__________________________________________________________"
                                                   "\n<!> Enter the New Customer's Passport Number:"
                                                   "\n(Type \"exit\" to leave)"
                                                   "\n\nInput: ")
                                if user_input.upper() == "EXIT":
                                    print("__________________________________________________________"
                                          "\n[!] Returning...")
                                    return False
                                Updated_Value = user_input
                                Index[Customer_Origins] = "Foreign"
                                Index[Customer_Num_Identification] = Updated_Value
                                Rows[i] = "|".join(Index) + "\n"
                                print("__________________________________________________________"
                                      "\n[!] Customer's Passport sucessfully updated.")
                                break
            except ValueError:
                print("__________________________________________________________"
                      "\n[!] Error: Invalid input, try again... (Value only accept numeric.)")
                Overwrite_C_Type()

    with open(Selected_file, "w") as Customer_prof:
        Customer_prof.writelines(Rows)


def Overwrite_Email():
    Selected_file = "CustomerDB.txt"
    with open(Selected_file, "r") as Customer_prof:
        header = Customer_prof.readline().strip().split("|")

        Customer_ID = header.index("Customer_ID")
        Customer_Email = header.index("Customer_Email")

    with open(Selected_file, "r") as Customer_prof:
        Rows = Customer_prof.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the New Customer's Email:"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                return False
            Updated_Value = user_input
            Index[Customer_Email] = Updated_Value
            Rows[i] = "|".join(Index) + "\n"
            print("__________________________________________________________"
                  "\n[!] Customer's Email sucessfully updated.")
            break

    with open(Selected_file, "w") as Customer_prof:
        Customer_prof.writelines(Rows)


def Overwrite_C_PN():
    Selected_file = "CustomerDB.txt"
    with open(Selected_file, "r") as Customer_prof:
        header = Customer_prof.readline().strip().split("|")

        Customer_ID = header.index("Customer_ID")
        Customer_Phone_num = header.index("Customer_Phone_num")

    with open(Selected_file, "r") as Customer_prof:
        Rows = Customer_prof.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the new Customer's Phone Number:"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                return False
            Updated_Value = user_input
            Index[Customer_Phone_num] = Updated_Value
            Rows[i] = "|".join(Index) + "\n"
            print("__________________________________________________________"
                  "\n[!] Customer's Phone Number sucessfully updated.")
            break

    with open(Selected_file, "w") as Customer_prof:
        Customer_prof.writelines(Rows)


def Overwrite_C_ADD():
    Selected_file = "CustomerDB.txt"
    with open(Selected_file, "r") as Customer_prof:
        header = Customer_prof.readline().strip().split("|")

        Customer_ID = header.index("Customer_ID")
        Customer_Address = header.index("Customer_Address")

    with open(Selected_file, "r") as Customer_prof:
        Rows = Customer_prof.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the new Customer's Address:"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                return False
            Updated_Value = user_input
            Index[Customer_Address] = Updated_Value
            Rows[i] = "|".join(Index) + "\n"
            print("__________________________________________________________"
                  "\n[!] Customer's Address sucessfully updated.")
            break

    with open(Selected_file, "w") as Customer_prof:
        Customer_prof.writelines(Rows)


def Overwrite_C_N():
    Selected_file = "CustomerDB.txt"
    with open(Selected_file, "r") as Customer_prof:
        header = Customer_prof.readline().strip().split("|")

        Customer_ID = header.index("Customer_ID")
        Customer_Name = header.index("Customer_Name")

    with open(Selected_file, "r") as Customer_prof:
        Rows = Customer_prof.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the New Customer's Name:"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                return False
            Updated_Value = user_input
            Index[Customer_Name] = Updated_Value
            Rows[i] = "|".join(Index) + "\n"
            print("__________________________________________________________"
                  "\n[!] Customer's Name sucessfully updated.")
            break

    with open(Selected_file, "w") as Customer_prof:
        Customer_prof.writelines(Rows)


def Overwrite_C_LCE():
    Selected_file = "CustomerDB.txt"
    with open(Selected_file, "r") as Customer_prof:
        header = Customer_prof.readline().strip().split("|")

        Customer_ID = header.index("Customer_ID")
        Customer_Licence = header.index("Customer_Licence")

    with open(Selected_file, "r") as Customer_prof:
        Rows = Customer_prof.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            user_input = input("__________________________________________________________"
                               "\n<!> Enter the New Customer's Licence No:"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                return False
            Updated_Value = user_input
            Index[Customer_Licence] = Updated_Value
            Rows[i] = "|".join(Index) + "\n"
            print("__________________________________________________________"
                  "\n[!] Customer's Licence No sucessfully updated.")
            break

    with open(Selected_file, "w") as Customer_prof:
        Customer_prof.writelines(Rows)

def Cust_Detail_Overwrite(FileSelected=f'CustomerDB.txt'):
    user_input = input("__________________________________________________________"
                       "\n<!> Customer ID:"
                       "\n(Type \"exit\" to leave)"
                       "\n\nInput: ")
    if user_input.upper() == "EXIT":
        print("__________________________________________________________"
              "\n[!] Returning to Menu...")
        return Customer_Service_Panel_Menu()
    else:
        with open(FileSelected, "r") as Upd_Cust:
            header = Upd_Cust.readline().strip().split("|")
            Customer_ID = header.index("Customer_ID")

        with open(FileSelected, "r") as Upd_Cust:
            next(Upd_Cust)  # Skips the line
            for List in Upd_Cust:
                Duplication = List.strip().split("|")
                if Duplication[
                    Customer_ID].upper() == user_input.upper():  # Verification for duplicated datas.
                    global Current_CDO_Data
                    Current_CDO_Data = user_input
                    Cus_D_O_Panel()
                elif Duplication[Customer_ID].upper() != user_input.upper():
                    continue
        print("__________________________________________________________"
              "\n[!] Error: \"" + user_input.upper() + "\" is not registered!")
        Cust_Detail_Overwrite()

# // AIZIK : STAFF DETAIL OVERWRITES
def Manager_Car_Detail_Overwrite(FileSelected = "CarRegisteredDB.txt"):
    user_input = input(""
                       "\nPlease input the Car Registered No:"
                       "\n(Type \"exit\" to leave)"
                       "\n\nInput: ")
    if user_input.upper() == "EXIT":
        print(""
              "\n Returning to Menu...")
        return False
    else:
        with open(FileSelected, "r") as CarRegistered_DB:
            header = CarRegistered_DB.readline().strip().split("|")
            Registered_Car_No = header.index("Car_Registered_No")
            
        with open(FileSelected, "r") as CarRegistered_DB:
            next(CarRegistered_DB)  # Skips the line
            for List in CarRegistered_DB:
                Duplication = List.strip().split("|")
                if Duplication[Registered_Car_No].upper() == user_input.upper(): # Verification for duplicated datas.
                    global Current_CDO_Data
                    Current_CDO_Data = user_input
                    Overwrite_CRRD()
                elif Duplication[Registered_Car_No].upper() != user_input.upper():
                        continue
        print(""
              "\n[!] Error: \""+user_input.upper()+"\" is not registered!")
        Manager_Car_Detail_Overwrite()

#____________________________________# Edit Staff information#____________________________________#
def edit_staff(filename, skipped_line): #Defines edit_staff and sets the range

    with open(filename, "r") as file: #open the file in read mood 
        file_header = file.readline().strip().split("|") #reads the lines and removes any empty space and adds a \ to split the information
        staff_role = file_header.index("Staff_Role") #sets staff_role to the posistion that it is found in the in the heard of the list that is 3
        password = file_header.index("Password") #sets the password to the posistion that it is found in the heard of the list that is 2
        username = file_header.index("Staff_Name") #sets the staff_name to the posistion that it is found in the header of list that is 0

    while True: # loops the program. 
        # Ask the user to choose what they will like to edit
        choice = input("Please choose what you would like to edit.\n1. Edit Staff role\n2. Edit Password\n3. Edit username \n4. Delete user \n5. exit \n\nInput: ") 
        if choice == "1": #If user enters 1
            while True:
                choice = input("Please choose the role \n1. Manager \n2. Car staff \n3. Customer Staff \n\nInput: ")
                if int(choice) == 1:
                    index = "Manager"
                    break
                if int(choice) == 2:
                    index = "Car_Staff"
                    break
                if int(choice) == 3:
                    index = "Customer_Staff"
                else:
                    print ("that wasnt an opsition")
                
                index = staff_role #sets index to staff_role
                break
        elif choice == "2":
            index = password #sets index to password
            break
        elif choice == "3":
            index = username #sets index to username
            break
        elif choice == "4":
            new_list = []
            with open(filename, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i != skipped_line:
                        new_list.append(line)
            
            with open(filename, "w") as w_file:
                w_file.writelines(new_list)
            print("User deleted successfully.")
            return
        
        elif choice == "5":
            Homepage_Panel_manager()
        else:
            print("That was not a choice. Please try again.")
            return
        # If manager did not input a correct opsition then it will loop back to the start
    else:
        print("That was not a choice. Please try again.")
# Ask the user to input the new value.  
    new_value = input("What would you like to change it to?\nInput: ")
# replaces the old data with the new one 
    new_list = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == skipped_line:
                parts = line.strip().split("|")
                parts[index] = new_value
                new_line = "|".join(parts)
                new_list.append(new_line + "\n")
            else:
                new_list.append(line)

    with open(filename, "w") as w_file:
        w_file.writelines(new_list)

#_______________________________________#Finds the staff the manager wants to edit#_______________________________________#
def find_staff(filename="StaffDB.txt"):
    staff_id = input("Please type the ID of the staff that you want to edit \n Must include '#' at the start.\nInput: ") #Input the StaffID the manager wants to find 

    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            if line.startswith(f"{staff_id}"): #check if the ID exist 
                print(line.strip()) #Prints out the staff details 
                #ask if this is the profile the manager wants to edit 
                choice = input("Are you sure you want to edit this staff information? Please Input '1' for yes and '2' for no.\nInput: ")

                if choice == "1": #starts the edit staff function 
                    edit_staff(filename, index)
                    break
                elif choice == "2":#ends the function if the manager doesnt want to edit this Staff
                    print("Okay.")
                    break
        else: # if the manager enters the wrong ID or it does not exist
            choice = input("Looks like you entered a staff ID that does not exist. Would you like to try again? (Yes/No)\nInput: ")
            # ask the manager if they want to try again 
            if choice.lower() == "yes":
                find_staff()
            elif choice.lower() == "no":
                Homepage_Panel_manager()
            return

# // DYLAN : CAR REGISTERATION
def Car_Service_Registration(): 
    Rows = []

    with open('CarRegisteredDB.txt', 'r') as CarRegisteredDB:
        header = CarRegisteredDB.readline().strip().split('|')

    for value in header:
        while True:
            if value == "Car_Registered_No":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Car_Service_Panel()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if Check_Duplicate_Registration_Car(user_input) == True:
                            continue
                        else:
                            Rows.append(user_input.upper())
                            break
                except ValueError:
                    pass
            elif value == "Seating_Capacity":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n2/5/7"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Car_Service_Panel()
                    if not user_input:
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if int(user_input) == 2:
                            Rows.append(str(user_input))
                            break
                        if int(user_input) == 5:
                            Rows.append(str(user_input))
                            break
                        if int(user_input) == 7:
                            Rows.append(str(user_input))
                            break
                        else:
                            print("[!] Error: Capacity can only be 2, 5 or 7. Please enter again.")
                            continue
                except ValueError:
                    print("__________________________________________________________"
                          "\n[!] Error: Invalid input, try again... (Value only accept numeric.)")
                    continue
            elif value == "Last_Service_Date" or value == "Insurance_Expiry_Date" or value == "Road_Tax_Expiry_Date":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Car_Service_Panel()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if Check_Valid_Dates(user_input) == True:
                            Rows.append(user_input.upper())
                            break
                        else:
                            continue
                except ValueError:
                    pass
            elif value == "Renting_Rate_Per_Day":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}: (RM)"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Car_Service_Panel()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        user_input = float(user_input)
                        if type(user_input) == float:
                            Rows.append(str(user_input))
                            break
                        else:
                            print("[!] Error: Capacity cannot be 0 or lower. Please enter again.")
                            continue
                except ValueError:
                    print("__________________________________________________________"
                          "\n[!] Invalid input, try again... (Value only accept numeric.)")
                    continue
            elif value == "Rental_Availability":
                user_input = "Available"
                Rows.append(user_input.upper())
                break
            elif value == "Return_Date":
                user_input = "Nil"
                Rows.append(user_input.upper())
                break
            elif value == "Car_Rental_Date":
                user_input = "Nil"
                Rows.append(user_input.upper())
                break
            elif value == "Year_Of_Manufacturer":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Car_Service_Panel()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if user_input.isdigit():
                            if len(str(user_input)) == 4:
                                Rows.append(str(user_input.upper()))
                                break
                            else:
                                print("__________________________________________________________"
                                      "\n[!] Error: Value can only accept 4 value, Please enter again.")
                                continue
                        else:
                            print("__________________________________________________________"
                                  "\n[!] Error: Value can only accept numeric value, Please enter again.")
                except ValueError:
                    print("__________________________________________________________"
                          "\n[!] Error: Value can only accept numeric value, Please enter again.")
            else:
                user_input = input("__________________________________________________________"
                                    f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                    "\n(Type \"exit\" to leave)"
                                    "\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    Car_Service_Panel()
                if not user_input.strip():
                    print("__________________________________________________________"
                          "\n[!] Error: Value cannot be blank. Please enter again.")
                    continue
                else:
                    Rows.append(user_input.upper())
                    break
    
    while True:
        try:
            print("__________________________________________________________")
            print(Rows)
            user_input = input("\n<!> Is this your final decision? YES/NO"
                               "\n(Some value are set to default when registering Cars.)"
                               "\n\nInput: ")
            if user_input.upper() == "YES":
                with open("CarRegisteredDB.txt", "a") as file:
                    file.write("|".join(Rows) + "\n")
                    print("__________________________________________________________"
                          "\n[!] Car successfully registered."
                          "\n[!] Car Detail can be further overwrite in \"Update Car Detail\" Option!")
                break
            elif user_input.upper() == "NO":
                Car_Service_Registration()
            else:
                print("__________________________________________________________"
                      "[!] Error: Input can only accept yes or no.")
        except ValueError:
            pass

# // VINCENT : TRANSACTION REGRISTRATION & MODIFY FEATURES
def Delete_Transaction(FileSelected = "BillDB.txt"):
    with open(FileSelected, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip().split('|')

    print("__________________________________________________________")
    for index, line in enumerate(lines[1:], start=1):
        print(f'\nBill {index}#')
        values = line.strip().split('|')
        for header_line, value in zip(header, values):
            print(f'{header_line.replace("_", " ").title()}: {value}')
        print("__________________________________________________________"
              "\n[!] Successfully load all Data.")

    while True:
        try:
            user_input = input("\n<!> Enter the number of the bill you want to delete"
                               "\n(Type \"exit\" to leave)"
                               "\n\nInput: ")
            if user_input.lower() == "exit":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                Customer_Service_Panel_Transaction()

            bill_number = int(user_input)
            if bill_number < 1 or bill_number > index:
                print("__________________________________________________________"
                      "\n[!] Error: Invalid bill number.")
                continue

            # Confirm deletion
            confirm_input = input(f"Are you sure you want to delete Bill {bill_number}#? (YES/NO): ")
            if confirm_input.upper() == "YES":
                del lines[bill_number]
                with open(FileSelected, "w") as file:
                    file.writelines(lines)
                print(f"__________________________________________________________"
                      f"\n[!] Bill {bill_number}# deleted successfully.")
                break
            elif confirm_input.upper() == "NO":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                Customer_Service_Panel_Transaction()
            else:
                print("__________________________________________________________"
                      "\n[!] Invalid input. Please enter YES or NO.")
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Error: Invalid input. Please enter a valid bill number.")
            continue


def Print_Receipt(header, Rows):
    print("__________________________________________________________")
    print("[!] Receipt:")
    print("----------------------------------------------------------")
    for i, value in enumerate(Rows):
        print(f"{header[i].replace('_', ' ').title()}: {value}")
    print("----------------------------------------------------------")


def Total_Rental(TotalDays, Current_CarNo, FileSelected = "CarRegisteredDB.txt"):
    with open(FileSelected, 'r') as CarRegistered_DB:
        header = CarRegistered_DB.readline().strip().split('|')
    
        Rental_Price = header.index('Renting_Rate_Per_Day')
        Car_Registered_No = header.index('Car_Registered_No')
    
    with open(FileSelected, "r") as CarRegistered_DB:
        next(CarRegistered_DB)  # Skips the line
        for List in CarRegistered_DB:
            Matching = List.strip().split("|")
            if Matching[Car_Registered_No].upper() == Current_CarNo.upper(): # Verification for duplicated datas.
                rental_price = float(Matching[Rental_Price])  # Convert rental price to float
                return (rental_price * TotalDays)
    
def Period_Of_Days(Rental_dt, Return_dt):
 
    #Change the string into a readable date format
    Rental_dt = datetime.datetime.strptime(Rental_dt, "%d/%m/%Y")
    Return_dt = datetime.datetime.strptime(Return_dt, "%d/%m/%Y")

    #Return number of days between the two dates
    return (Return_dt - Rental_dt).days                

def Registered_Car_SeatsCap():
    Option = [1,2,3,4]
    while True:
        try:
            Selection_Opt = int(input("__________________________________________________________"
                                      "\n<!> List any of the option below for customer\'s desire car seat"
                                      "\n"
                                      "\n<!> Please type the number corespond to options listed down below:"
                                      "\n1. 2 seats"
                                      "\n2. 5 seats" 
                                      "\n3. 7 seats"
                                      "\n4. Return the Customer Service Menu."
                                      "\n\nInput: "))
        except ValueError: #Checks the DataType and see if they are acceptable
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options only accept numbers example; '1')"
                  "\n")
            continue
    
        if Selection_Opt in Option: #Options between the 3 options with each of them have separated work
                if 1 <= Selection_Opt <= 3:
                    if Selection_Opt == 1: #Manager Function: Aizik Part.
                        SeatsNum = 2
                        print("__________________________________________________________"
                              "\nList of Available Cars.")
                        List_Rental_Car(SeatsNum)
                    if Selection_Opt == 2: #Customer Service Staff: Ian, Vincent Part.
                        SeatsNum = 5
                        print("__________________________________________________________"
                              "\nList of Available Cars.")
                        List_Rental_Car(SeatsNum)
                    if Selection_Opt == 3: #Car Service Staff: Dylan Part.
                        SeatsNum = 7
                        print("__________________________________________________________"
                              "\nList of Available Cars.")
                        List_Rental_Car(SeatsNum)
                else:
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    Customer_Service_Panel_Transaction()
        else:
            print("__________________________________________________________"
                  "\n[!] Invalid option, try again... (Options is only ranged from 1 to 4.)"
                  "\n")

def Transaction_Creation(): 
    Rows = []

    with open('BillDB.txt', 'r') as BillDB:
        header = BillDB.readline().strip().split('|')

    for value in header:
        while True:
            if value == "Car_Registered_No":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Customer_Service_Panel_Transaction()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if Matching_Registration_Car(user_input) == True:
                            Current_CarNo = user_input
                            Rows.append(user_input.upper())
                            break
                        else:
                            continue
                except ValueError:
                    pass
            elif value == "Customer_ID":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Customer_Service_Panel_Transaction()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if Matching_Customer_ID(user_input) == True:
                            Rows.append(user_input.upper())
                            break
                        else:
                            continue
                except ValueError:
                    pass
            elif value == "Car_Rental_Date" or value == "Return_Date":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Customer_Service_Panel_Transaction()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if Check_Valid_Dates(user_input) == True:
                            if value == "Car_Rental_Date":
                                Rental_dt = user_input
                            if value == "Return_Date":
                                Return_dt = user_input
                            Rows.append(user_input)
                            break
                        else:
                            continue
                except ValueError:
                    pass
            elif value == "Rental_Periods":
                TotalDays = Period_Of_Days(Rental_dt, Return_dt)
                Rows.append(str(TotalDays))
                break
            elif value == "Total_Rental":
                TotalPrice = Total_Rental(TotalDays, Current_CarNo)
                Rows.append(str(TotalPrice))
                break
            elif value == "Transaction_Date":
                user_input = datetime.date.today().strftime('%d/%m/%Y')
                Rows.append(user_input)
                break
            else:
                user_input = input("__________________________________________________________"
                                    f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                    "\n(Type \"exit\" to leave)"
                                    "\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    Customer_Service_Panel_Transaction()
                if not user_input.strip():
                    print("__________________________________________________________"
                          "\n[!] Error: Value cannot be blank. Please enter again.")
                    continue
                else:
                    Rows.append(user_input)
                    break
    
    while True:
        try:
            print("__________________________________________________________")
            print(Rows)
            user_input = input("\n<!> Is this your final decision? YES/NO"
                               "\n\nInput: ")
            if user_input.upper() == "YES":
                with open("BillDB.txt", "a") as file:
                    file.write("|".join(Rows) + "\n")
                    print("__________________________________________________________"
                          "\n[!] Transaction successfully registered."
                          "\n[!] Car Detail can be further overwrite in \"Update Car Detail\" Option!")
                    Print_Receipt(header, Rows)
                break
            elif user_input.upper() == "NO":
                Transaction_Creation()
            else:
                print("__________________________________________________________"
                      "[!] Error: Input can only accept yes or no.")
        except ValueError:
            pass

# // IAN : CUSTOMER REGRISTRATION & MODIFY FEATURES
def Customer_Registration():
    Rows = []

    max_id = get_customer_id()

    with open('CustomerDB.txt', 'r') as f:
        header = f.readline().strip().split('|')

    for value in header:
        while True:
            if value == "Customer_ID":
                if value == 'Customer_ID':
                    new_id = f'C{max_id + 1}' # increments if the function above is proven true
                    Rows.append(new_id)

                break
            elif value == "Customer_Origins":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\n1. Local"
                                        "\n2. Foreign"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Customer_Service_Panel_Menu()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if int(user_input) == 1:
                            user_input = "Local"
                            Rows.append(user_input)
                            break
                        elif int(user_input) == 2:
                            user_input = "Foreign"
                            Rows.append(user_input)
                            break
                except ValueError:
                    print("__________________________________________________________"
                          "\n[!] Error: Invalid input, try again... (Value only accept numeric.)")
                    continue
            elif value == "Customer_Num_Identification":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Customer_Service_Panel_Menu()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        Rows.append(user_input)
                        break
                except ValueError:
                    print("__________________________________________________________"
                          "\n[!] Error: Invalid input, try again... (Value only accept numeric.)")
                    continue
            elif value == "Date_Of_Registration":
                user_input = datetime.date.today().strftime('%d/%m/%Y')
                Rows.append(user_input)
                break
            elif value == "Customer_Phone_num":
                try:
                    user_input = input("__________________________________________________________"
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        Customer_Service_Panel_Menu()
                    if not user_input.strip():
                        print("__________________________________________________________"
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        user_input = int(user_input)
                        if type(user_input) == int:
                            Rows.append(str(user_input))
                            break
                        else:
                            print("[!] Error: Capacity cannot be 0 or lower. Please enter again.")
                            continue
                except ValueError:
                    print("__________________________________________________________"
                          "\n[!] Invalid input, try again... (Value only accept numeric.)")
                    continue

            else:
                user_input = input("__________________________________________________________"
                                    f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                    "\n(Type \"exit\" to leave)"
                                    "\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    Customer_Service_Panel_Menu()
                if not user_input.strip():
                    print("__________________________________________________________"
                          "\n[!] Error: Value cannot be blank. Please enter again.")
                    continue
                else:
                    Rows.append(user_input)
                    break

    while True:
        try:
            print("__________________________________________________________")
            print(Rows)
            user_input = input("\n<!> Is this your final decision? YES/NO"
                               "\n\nInput: ")
            if user_input.upper() == "YES":
                with open("CustomerDB.txt", "a") as file:
                    file.write("|".join(Rows) + "\n")
                    print("__________________________________________________________"
                          "\n[!] Customer successfully registered."
                          "\n[!] Customer Details can be further updated in \"Update Customer Profiles\" Option!"
                          "\n__________________________________________________________")

                break

            elif user_input.upper() == "NO":
                Customer_Registration()
            else:
                print("__________________________________________________________"
                      "[!] Error: Input can only accept yes or no.")
        except ValueError:
            pass

def Cust_Prof_Del():
    FileSelected = f'CustomerDB.txt'
    user_input = input("__________________________________________________________"
                       "\n<!> Customer ID:"
                       "\n(Type \"exit\" to leave)"
                       "\n\nInput: ")
    if user_input.upper() == "EXIT":
        print("__________________________________________________________"
              "\n[!] Returning to Menu...")
        return Customer_Service_Panel_Menu()
    else:
        with open(FileSelected, "r") as Upd_Cust:
            header = Upd_Cust.readline().strip().split("|")
            Customer_ID = header.index("Customer_ID")

        with open(FileSelected, "r") as Upd_Cust:
            next(Upd_Cust)  # Skips the line
            for List in Upd_Cust:
                Duplication = List.strip().split("|")
                if Duplication[Customer_ID].upper() == user_input.upper():  # Verification for duplicated datas.
                    global Current_CDO_Data
                    Current_CDO_Data = user_input
                    Del_cust_panel()
                    return Customer_Service_Panel_Menu()
                elif Duplication[Customer_ID].upper() != user_input.upper():
                    continue
        print("__________________________________________________________"
              "\n[!] Error: \"" + user_input.upper() + "\" is not registered!")
        Cust_Prof_Del()


def Del_cust_panel():
    FileSelected = 'CustomerDB.txt'
    with open(FileSelected, "r") as Cust_DB:
        header = Cust_DB.readline().strip().split("|")

        Customer_ID = header.index("Customer_ID")
    with open(FileSelected, "r") as Cust_DB:
        Rows = Cust_DB.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Customer_ID].upper() == Current_CDO_Data.upper():
            while True:
                user_input = input("__________________________________________________________"
                                   "\n<!> Delete the Customer Profile"
                                   "\n**ONLY IF ZERO RENTAL TRANSACTIONS ARE RECORDED**. YES/NO?"
                                   "\n[!] Warning: This action CANNOT be REVERTED"
                                   "\n\nInput: ")
                if user_input.upper() == "YES":
                    del Rows[i]
                    print("__________________________________________________________"
                          "\n[!] Customer Profile Deleted.")
                    break
                elif user_input.upper() == "NO":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    Cust_Prof_Del()
                else:
                    print("__________________________________________________________"
                          "\n[!] Error: Input can only accept yes or no.")
            break  # Breaks the loop after deleting the profile

    with open(FileSelected, "w") as Cust_DB:
        Cust_DB.writelines(Rows)

# // AIZIK : STAFF REGRISTRATION
#___________________________________________#TO REGISTER NEW STUFF#___________________________________________#

def Staff_Registration(): 
    Rows = []

    with open('StaffDB.txt', 'r') as f:
        header = f.readline().strip().split('|')

    for value in header:
        # To Input todays Date 
        if value == "Registered_Date":
            user_input = datetime.date.today().strftime('%d/%m/%Y')
            Rows.append(user_input)
            
        elif value == "Staff_Role": # lets the user input the data 
            while True:
                try:
                    user_input = input(""
                                        f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                        "\n1. Manager"
                                        "\n2. Car_Staff"
                                        "\n3. Customer_staff"
                                        "\n(Type \"exit\" to leave)"
                                        "\nInput: ")
                    if user_input.upper() == "EXIT":
                        print(""
                              "\n[!] Returning...")
                        Homepage_Panel_manager()
                    if not user_input:
                        print(""
                              "\n[!] Error: Value cannot be blank. Please enter again.")
                        continue
                    else:
                        if int(user_input) == 1:
                            user_input = "Manager"
                            Rows.append(user_input)
                            break
                        if int(user_input) == 2:
                            user_input = "Car_Staff"
                            Rows.append(str(user_input))
                            break
                        if int(user_input) == 3:
                            user_input = "Customer_Staff"
                            Rows.append(str(user_input))
                            break
                        else:
                            print("[!] Error: Capacity can only be 1, 2, or 3. Please enter again.")
                            continue
                except ValueError:
                    print("[!] Error: Value only accept nemuric, try again...")
        elif value == "Staff_ID":
                #Staff ID
                user_input =  make_staff_id()
                new_id = f'#{user_input + 1}' # increments if the function above is proven true
                Rows.append(new_id)
                continue
            
        else:
            #Staff ID
            user_input =  input("__________________________________________________________"
                                f"\n<!> {value.strip().replace('_', ' ').title()}:"
                                "\n(Type \"exit\" to leave)"
                                "\nInput: ")
            if user_input.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                Homepage_Panel_manager()
            if not user_input.strip():
                print("__________________________________________________________"
                      "\n[!] Error: Value cannot be blank. Please enter again.")
                break
            else:
                Rows.append(str(user_input))

    while True:# if the value = staff name or staffID it will aks user to input the name and password 
        try:
            print("__________________________________________________________")
            print("Staff_ID|Staff_Name|Password|Staff_Role|Registered_Date")
            print(Rows)
            user_input = input("\n<!> Is this your final decision? YES/NO"
                               "\n(Some value are set to default when registering Cars.)"
                               "\n\nInput: ")
            if user_input.upper() == "YES":
                with open("StaffDB.txt", "a") as file:
                    file.write("|".join(Rows) + "\n")
                    print("__________________________________________________________"
                          "\n[!] Stuff successfully registered >W<."
                          "\n[!] Stuff Detail can be further Changed in \"Edit Stuff Detail\" Option!")
                break
            elif user_input.upper() == "NO":
                Staff_Registration()
            else:
                print("__________________________________________________________"
                      "[!] Error: Input can only accept yes or no.")
        except ValueError:
            pass


# // UPDATE OWN PROFILE : SHARED
def Update_User_P_Info(FileSelected="StaffDB.txt"):
    with open(FileSelected, "r") as StaffInfo_DB:
        header = StaffInfo_DB.readline().strip().split("|")
        
        Staff_NameCheck = header.index("Staff_Name")
        Staff_Password_Check = header.index("Password")

    with open(FileSelected, "r") as StaffInfo_DB:
        Rows = StaffInfo_DB.readlines()

    for i, line in enumerate(Rows):
        Index = line.strip().split("|")
        if Index[Staff_NameCheck].upper() == Username_Profile.upper():
            while True:
                user_input = input("__________________________________________________________"
                                   "\n<!> Enter old password:"
                                   "\n(Type \"exit\" to leave)"
                                   "\n\nInput: ")
                if user_input.upper() == "EXIT":
                    print("__________________________________________________________"
                          "\n[!] Returning...")
                    return False
                if user_input == Index[Staff_Password_Check]:
                    new_password = input("__________________________________________________________"
                                         "\n<!> Enter new password:"
                                         "\n(Type \"exit\" to leave)"
                                         "\n\nInput: ")
                    if new_password.upper() == "EXIT":
                        print("__________________________________________________________"
                              "\n[!] Returning...")
                        return False
                    new_password_check = input("__________________________________________________________"
                                               "\n<!> Enter new password again:"
                                               "\n\nInput: ")
                    if new_password == new_password_check:
                        Index[Staff_Password_Check] = new_password
                        Rows[i] = "|".join(Index) + "\n"
                        print("__________________________________________________________"
                              "\n[!] Password Updated.")
                        with open(FileSelected, "w") as StaffInfo_DB:
                            StaffInfo_DB.writelines(Rows)
                        return True
                    else:
                        print("__________________________________________________________"
                              "\n[!] Error: Passwords do not match. Restarting...")
                else:
                    print("__________________________________________________________"
                          "\n[!] Error: Incorrect old password. Please try again.")


def Update_User_N_Info(FileSelected="StaffDB.txt"):
    with open(FileSelected, "r") as StaffInfo_DB:
        header = StaffInfo_DB.readline().strip().split("|")
        
        Staff_NameCheck = header.index("Staff_Name")
        Staff_Password_Check = header.index("Password")

    with open(FileSelected, "r") as StaffInfo_DB:
        Rows = StaffInfo_DB.readlines()

    while True:
        try:
            old_password = input("__________________________________________________________"
                                 "\n<!> Enter old password:"
                                 "\n(Type \"exit\" to leave)"
                                 "\n\nInput: ")
            if old_password.upper() == "EXIT":
                print("__________________________________________________________"
                      "\n[!] Returning...")
                return False
            for line in Rows:
                Index = line.strip().split("|")
                if Index[Staff_NameCheck].upper() == Username_Profile.upper() and old_password == Index[Staff_Password_Check]:
                    while True:
                        new_username = input("__________________________________________________________"
                                             "\n<!> Enter new username:"
                                             "\n(Type \"exit\" to leave)"
                                             "\n\nInput: ")
                        if new_username.upper() == "EXIT":
                            print("__________________________________________________________"
                                  "\n[!] Returning...")
                            return False
                        # Check if the new username already exists
                        if Check_Duplicate_Name(new_username):
                            pass
                        else:
                            Index[Staff_NameCheck] = new_username
                            Rows[Rows.index(line)] = "|".join(Index) + "\n"
                            print("__________________________________________________________"
                                  "\n[!] Username Updated.")
                            with open(FileSelected, "w") as StaffInfo_DB:
                                StaffInfo_DB.writelines(Rows)
                            return True
            else:
                print("__________________________________________________________"
                      "\n[!] Password do not match...")
        except ValueError:
            print("__________________________________________________________"
                  "\n[!] Invalid input. Please try again.")

# // LOGINS : SHARED
def User_Login(): 
    for i in range(1,4):
        print("__________________________________________________________"
              "\n<!> Logging user in..")
        Username_Check = str(input("Username: ")) # User input Username
        Password_Check = str(input("Password: ")) # User input Password
        if Username_Login_Verification(Username_Check, Password_Check) : # Login Verification fucntion called <SECOND FUNCTION LOOP>
            print("__________________________________________________________"
                  "\n<!> Name:",Username_Check,
                  "\n<!> Role:",SecurityCheck_Staff_Role)
            Homepage_Panel() # Car Service Panel function called when verification is successful <THIRD FUNCTION LOOP>
            
        else:
            print ("__________________________________________________________"
                  "\n[!] Counter!"
                  "\n[!] "+str(i)+" out of 3 tries remaining"
                  "\n") # Displaying the counter, very cool and scary.
    else: # When Counter reach 3, kicks user from the panel and prevent user to login.
        print("__________________________________________________________"
              "\n[!] You failed logging in." # I was planning to make it said "You failed logging in. Now the four demons of old will ravage this land and take the life out of millions" but I can't decide if I should be funny or not.
              "\n[!] You are kicked from the system!")

def Username_Login_Verification(Username_Check, Password_Check, FileSelected = "StaffDB.txt"): # Argument and function creations
    with open(FileSelected, "r") as StaffInfo_DB: # Opening files
        header = StaffInfo_DB.readline().strip().split("|") # Splits unecessary informations in txtfiles
        
        DBStaff_Name = header.index("Staff_Name") # Assigning Variables while giving setting indexs for Username
        DBStaff_Password = header.index("Password") # Same Functionality as Above but different variable & indexs
        DBStaff_Role = header.index("Staff_Role") # Same Functionality as Above but different variable & indexs

    with open(FileSelected, "r") as StaffInfo_DB:
        next(StaffInfo_DB)  # Skips the line
        for List in StaffInfo_DB:
            Verification = List.strip().split("|")
            if Verification[DBStaff_Name] == Username_Check: # Verification for username
                try:
                    if Verification[DBStaff_Password] == Password_Check: # Verification for password when username exist in list
                        global SecurityCheck_Staff_Role # Assigning Role3 as a Global Variable
                        SecurityCheck_Staff_Role = Verification[DBStaff_Role] # #Assign role for displaying logged in user's
                        global Username_Profile
                        global Password_Profile
                        Username_Profile = Verification[DBStaff_Name]
                        Password_Profile = Verification[DBStaff_Password]
                        return True # Break loops and head back to FIRST FUNCTION LOOP to achieve THIRD FUNCTION LOOP
                    else:
                        print("Password is incorrect.") # When Password does not match
                        return False # Break loops and head back to FIRST FUNCTION LOOP while setting Counter up by 1
                except IndexError:
                    # Handle cases where username is last line and next(CarService_DB) throws error
                    pass  # Does nothing continue to next line

            elif Verification[DBStaff_Name] != Username_Check: # When Password does not match
                continue  # Skip to the next roll in CarServiceStaff Database

    print("Username does not exist under the List.") 
    return False # Break loops and head back to FIRST FUNCTION LOOP while setting Counter up by 1

User_Login()