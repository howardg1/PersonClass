from Textbook import Textbook

book1 = Textbook("Python Programming", "Zed", "Shaw", 41, "12345667", 25,"Addison-Wesley", 2017, 10, 39.99)

# Menu Time
menu_choice = 0

while menu_choice != 4:
    print("What would you like to do? Please select from the menu:")
    print("1. Add to inventory")
    print("2. Deduct from inventory")
    print("3. Modify the price of the book")
    print("4. Quit the program")

    menu_choice = int(input())

    if menu_choice == 1:
        print("Which book, 1 or 2?")
        choice = int(input())
        if choice == 1:
            qty = int(input("How many would you like to add?"))
            book1.add_inventory(qty)
            print("The quantity in inventory is now " + str(book1.quantity_available) + "\n\n")
        elif menu_choice == 2:
            qty = int(input("How many would you like to remove?"))
            result = book1.deduct_inventory(qty)
            if result == 0:
                print("The quantity in inventory is now 1 " + str(book1.quantity_available) + "\n\n")
            else:
                print("You do not have enough in inventory to remove that quantity.")
                print("Current inventory in stock is " + str(book1.quantity_available + "\n\n"))
        elif menu_choice == 3:
            price = float(input("What will the new price of the book be?"))
            book1.price = price
            print("The price of " + book1.title + "has been changed to " + str(book1.price) + "\n\n")
        elif menu_choice == 4:
            print("Thank you for using the system!")
        else:
            print("Error, please choose from the menu above!")
