from datetime import datetime
import os
print("Welcome to Personal Journal Manager!")
while True:
    print("Please select an option:")
    print("1. Add a New Entry\n2. View All Entries\n3. Search for an Entry\n4. Delete All Entries\n5. Exit")
    try:
        choice = int(input("User Input:"))
        match choice:
            case 1:
                    entry= input("Enter your journal entry:")
                    c_time = datetime.now()
                    date_time = c_time.strftime("%Y-%m-%d %H:%M:%S")
                    with open("journal.txt", "a") as file:
                        file.write("["+date_time+"]\n")
                        file.write(entry+"\n\n")
                    print("Entry added successfully!")
            case 2:
                try:
                    print("View All Entries:")
                    with open("journal.txt","r") as file:
                        data = file.read()
                    if data.strip() == "":
                        print("No journal entries found. Start by adding a new entry!")
                    else:
                        print("Your Journal Entries:")
                        print("--------------------------------------")
                        print(data)
                except FileNotFoundError:
                    print("Error: The journal file does not exist. Please add a new entry first.")
            case 3:
                try:
                    print("Search for an Entry:")
                    key = input("Enter a keyword or date to search:")
                    with open("journal.txt","r") as file:
                        data = file.read()
                    if data.strip()=="":
                         print("No journal entries found.")
                    else:
                        entries = data.strip().split("\n\n")
                        f= False
                        print("Matching Entries:")
                        print("------------------------------")
                        for i in entries:
                            if key.lower() in i.lower():
                                print(i)
                                print()
                                f= True
                        if not f:
                                print("No entries were found for the keyword: ", key)
                except FileNotFoundError:
                    print("Error: The journal file does not exist. Please add a new entry first.")
            case 4:
                try:
                    print("Delete All Entries:")
                    confirm = input("Are you sure you want to delete all entries? (yes/no):")
                    if confirm.lower()=="yes":
                        os.remove("journal.txt")
                        print("All journal entries have been deleted.")
                    else:
                        print("Deletion cancelled.")
                except FileNotFoundError:
                    print("No journal file found. Nothing to delete.")
                except Exception as e:
                    print("Error while deleting entries:", e)
            case 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            case _:
                print("Invalid option. Please select a valid option from the menu.")
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
    except Exception as e:
            print("\nAn unexpected error occurred:", e)
    

