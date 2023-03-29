class RoomService:
    def __init__(self):
        self.food_orders = []
        self.cleaning_requested = False

    def order_food(self, item):
        self.food_orders.append(item)
        print(f"Food order for {item} placed.")

    def remove_food_order(self, item):
        if item in self.food_orders:
            self.food_orders.remove(item)
            print(f"Food order for {item} removed.")
        else:
            print(f"No food order for {item} found.")

    def request_cleaning(self):
        self.cleaning_requested = True
        print("Room cleaning requested.")

    def view_orders(self):
        print("Current food orders:")
        for order in self.food_orders:
            print(order)
        if self.cleaning_requested:
            print("Room cleaning has been requested.")

    def clear_orders(self):
        self.food_orders = []
        self.cleaning_requested = False
        print("All orders cleared.")

    def menu(self):
        while True:
            print("\nRoom Service Menu:")
            print("1. Order food")
            print("2. Remove food order")
            print("3. Request room cleaning")
            print("4. View orders")
            print("5. Clear orders")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                item = input("Enter food item to order: ")
                self.order_food(item)
            elif choice == "2":
                item = input("Enter food item to remove: ")
                self.remove_food_order(item)
            elif choice == "3":
                self.request_cleaning()
            elif choice == "4":
                self.view_orders()
            elif choice == "5":
                self.clear_orders()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")