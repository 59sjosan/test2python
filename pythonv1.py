phoneDirectory = {}

print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
while True:
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit.")

    choice = input("Enter your choice: ").upper()
    if choice == "1":
        Name = input("Enter name: ")
        Number = input("Enter your 10-digit phone number: ")
        while len(Number)!=10 and Number.isnumeric():
            print("Enter Valid Number")
            Number = input("Enter your 10-digit phone number: ")
        phoneDirectory[Name] = Number
        print("Record Added")
    
    elif choice == "2":
        Name = input("Enter Name to Search: ")
        if Name in phoneDirectory:
            Number = phoneDirectory[Name]
            print(Name,":",Number)
        else:
            print("No phone number exists with this name")
    elif choice =="3":
        Name = input("Enter name: ")
        Number = input("Enter new 10-digit phone number: ")
        while len(Number)!=10 and Number.isnumeric():
            print("Enter Valid Number")
            Number = input("Enter new 10-digit phone number: ")
        phoneDirectory[Name] = Number
        print("Record Updated")
    elif choice=='4':
        Name = input("Enter name: ")
        if Name in phoneDirectory:
            phoneDirectory.pop(Name)
            print("Record Deleted")
        elif len(phoneDirectory)==0:
            print("Phone Directory is Empty")
    elif choice=='5':
        break
    else:
        print("Wrong Option Entered")
    print("\n")