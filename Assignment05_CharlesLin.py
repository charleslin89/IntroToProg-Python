# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog: Charles Lin, 2023-02-11
# CLin, 2023-02-11 Created File
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = 'ToDoList.txt' # data storage file
objFile = None   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
lstRow = []  # list of data

# -- Processing -- #
# Step 1 - When the program starts, load any data I have
# in a text file called ToDoList.txt into a python list of dictionaries rows

while(True):
    print("Write or Read file Data. Type 'Exit' of you don't wish to process any data.")
    strChoice = input("Choose to [W]rite or [R]ead data or Exit to the next activity: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break # Exits out of while loop

    elif (strChoice.lower() == 'w'):
        objFile = open(strFile, "w")
        dicRow = {"Task": "Paint", "Priority": "Medium"} # Create a data structure with dictionary and seed data
        objFile.write(str(dicRow["Task"]) + ',' +str(dicRow["Priority"] + '\n'))
        dicRow = {"Task": "Scrub", "Priority": "Low"}
        objFile.write(str(dicRow["Task"]) + ',' + str(dicRow["Priority"] + '\n'))
        print('Data has been written to file')
        objFile.close()

    elif (strChoice.lower() == 'r'):
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()} # Reading a row of data and add to a dictionary
            lstTable.append(dicRow)
        for objRow in lstTable:
            objFile.close()
        print(lstTable)

    else:
        print('Please choose either W or R!')


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable: # lstTable is the table-like collection of data processed in Step 1
            print(objRow["Task"] + '|' + objRow["Priority"]) # Display data by the dictionary keys and format with pipe

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while(True): # While loop to return to Menu of Options
            strTask = input("Task: ")
            strPriority = input("Priority: ")
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while (True):
            strTask = input("Task to Remove: ")
            for row in lstTable:
                if row["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    print("row removed")
                else:
                    print("row not found") # Goes through every row to see if there is a match
            # print(lstTable)
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        while (True):
            objFile = open(strFile, "w")
            for row in lstTable:
                objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
            objFile.close()
            print("Tasks written to file!")
            # strChoice = input("Exit? ('y/n'): ")
            # if strChoice.lower() == 'y':
            break
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program

    else:
        print('Please choose either 1, 2, 3, 4, or 5!')

input('Press Enter to Exit')