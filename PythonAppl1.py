import os
import time
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'Products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Order(Base):
    __tablename__ = 'Orders'
    
    id = Column(Integer, primary_key=True)
    products = Column(String(1000))
    
    def __init__(self, id, products=""):
        self.id = id
        self.products = products
    
    def add_product(self, product):
        if product.name not in self.products:
            self.products += f"{product.name}, "
    
    def display_order(self):
        print(f"Order ID: {self.id}")
        print(f"Products: {self.products}")

connection_string = (
    "mssql+pyodbc://(localdb)\\mssqllocaldb/Python?"
    "driver=ODBC+Driver+17+for+SQL+Server"
)
engine = create_engine(connection_string)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

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
    product1 = session.query(Product).filter_by(id=1).first()
    if not product1:
        product1 = Product(id=1, name="Laptop", price=1000)
        session.add(product1)

    product2 = session.query(Product).filter_by(id=2).first()
    if not product2:
        product2 = Product(id=2, name="Smartphone", price=500)
        session.add(product2)

    product3 = session.query(Product).filter_by(id=3).first()
    if not product3:
        product3 = Product(id=3, name="Headphones", price=150)
        session.add(product3)
    
    session.commit()

    order = session.query(Order).filter_by(id=101).first()
    if not order:
        order = Order(id=101)

    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option: ")

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
            if not session.query(Order).filter_by(id=order.id).first():
                session.add(order)
                session.commit()
            break
        elif choice == '6':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice, please choose a valid option.")
        
        time.sleep(2)

if __name__ == "__main__":
    main()
