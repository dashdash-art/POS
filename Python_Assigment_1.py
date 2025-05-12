# Simple POS System in Python using classes (Inheritance)

class POS:
    def __init__(self):
        self.inventory = {'Lego Star Wars': 25, 'Cookie': 5}
        self.reports = []

    def display_menu(self):
        print("\nWelcome to Target! Choose an option:")
        print("1) Make a Purchase")
        print("2) Make a Return")
        print("3) Manage Inventory")
        print("4) View Report")

    def make_transaction(self, transaction_type):
        total = 0
        items_selected = []

        while True:
            print("\nAvailable Items:")
            for item, price in self.inventory.items():
                print(f"{item}: ${price}")

            item_name = input(f"Which item would you like to {transaction_type}? ")
            if item_name in self.inventory:
                items_selected.append(self.inventory[item_name])
            else:
                print("Item not found!")
                continue

            more = input("Anything else? (Y/N) ").upper()
            if more == 'N':
                break

        total = sum(items_selected)

        if transaction_type == "purchase":
            self.reports.append(total)
            print(f"Your total is ${total}. Thank you for shopping at Target!")
        else:
            print(f"Your refund total is ${total}. Thank you for shopping at Target!")

    def manage_inventory(self):
        while True:
            print("\nManage Inventory")
            for item, price in self.inventory.items():
                print(f"{item}: ${price}")

            print("1) Add New Item")
            print("2) Remove Item")
            print("3) Main Menu")

            choice = input("Select option: ")
            if choice == '1':
                name = input("Item Name: ")
                price = float(input("Item Price: "))
                self.inventory[name] = price
                print("Item added successfully!")
            elif choice == '2':
                name = input("Item Name to remove: ")
                if name in self.inventory:
                    del self.inventory[name]
                    print("Item removed successfully!")
                else:
                    print("Item not found!")
            elif choice == '3':
                break

    def view_report(self):
        total_customers = len(self.reports)
        total_profit = sum(self.reports)
        print("\nReports:")
        print(f"Total Customers: {total_customers}")
        print(f"Total Profit: ${total_profit}")
        input("Press any key to return to main menu.")


# Main Execution
pos_system = POS()

while True:
    pos_system.display_menu()
    option = input("Select option: ")

    if option == '1':
        pos_system.make_transaction("purchase")
    elif option == '2':
        pos_system.make_transaction("return")
    elif option == '3':
        pos_system.manage_inventory()
    elif option == '4':
        pos_system.view_report()
    else:
        print("Invalid selection. Try again!")

