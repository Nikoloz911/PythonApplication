from Models.Product import Product
from Models.Order import Order
import os
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')  

def show_menu():
    print("1. Laptop - $1000")
    print("2. Smartphone - $500")
    print("3. Headphones - $150")
    print("4. View Order")
    print("5. Checkout")
    print("6. Exit")

def main():
    product1 = Product(1, "Laptop", 1000)
    product2 = Product(2, "Smartphone", 500)
    product3 = Product(3, "Headphones", 150)

    order = Order(101)

    while True:
        clear_screen()
        show_menu()
        choice = input("")

        if choice == '1':
            order.add_product(product1)
            print("Laptop added to your order!")
        elif choice == '2':
            order.add_product(product2)
            print("Smartphone added to your order!")
        elif choice == '3':
            order.add_product(product3)
            print("Headphones added to your order!")
        elif choice == '4':
            clear_screen()
            order.display_order()
            input("Press Enter to continue...")
        elif choice == '5':
            clear_screen()
            order.display_order()
            print("Thank you for your order!")
            break
        elif choice == '6':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice, please choose a valid option.")
        
        time.sleep(2)  

if __name__ == "__main__":
    main()
