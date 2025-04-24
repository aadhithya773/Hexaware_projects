import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.customer_dao import CustomerDAO
from dao.product_dao import ProductDAO
from dao.order_dao import OrderDAO
from dao.inventory_dao import InventoryDAO
from dao.order_details import OrderDetailDAO
from entity.customer import Customer
from entity.product import Product
from entity.order import Order
from entity.order_detail import OrderDetail
from entity.inventory import Inventory
from datetime import datetime

def customer_menu():
    dao = CustomerDAO()
    while True:
        print("\nCUSTOMER MENU")
        print("1. Add Customer")
        print("2. View Customers")
        print("0. Back")
        choice = input("Enter choice: ")
        if choice == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            customer = Customer(None, first, last, email, phone, address)
            dao.create_customer(customer)
            print("Customer added.")
        elif choice == '2':
            customers = dao.list_customers()
            for c in customers:
                print(vars(c))
        elif choice == '0':
            break

def product_menu():
    dao = ProductDAO()
    while True:
        print("\nPRODUCT MENU")
        print("1. Add Product")
        print("2. View Products")
        print("0. Back")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Product Name: ")
            desc = input("Description: ")
            price = float(input("Price: "))
            product = Product(None, name, desc, price)
            dao.create_product(product)
            print("Product added.")
        elif choice == '2':
            products = dao.list_products()
            for p in products:
                print(vars(p))
        elif choice == '0':
            break

def order_menu():
    order_dao = OrderDAO()
    customer_dao = CustomerDAO()
    while True:
        print("\nORDER MENU")
        print("1. Add Order")
        print("2. View Orders")
        print("0. Back")
        choice = input("Enter choice: ")
        if choice == '1':
            cid = int(input("Customer ID: "))
            customer = customer_dao.get_customer(cid)
            date = datetime.now()
            amount = float(input("Total Amount: "))
            order = Order(None, customer, date, amount)
            order_dao.create_order(order)
            print("Order added.")
        elif choice == '2':
            orders = order_dao.list_orders()
            for o in orders:
                print(vars(o))
        elif choice == '0':
            break

def inventory_menu():
    inventory_dao = InventoryDAO()
    while True:
        print("\nINVENTORY MENU")
        print("1. View Inventory")
        print("2. Update Inventory")
        print("0. Back")
        choice = input("Enter choice: ")
        if choice == '1':
            items = inventory_dao.list_inventory()
            for item in items:
                print(vars(item))
        elif choice == '2':
            pid = int(input("Product ID: "))
            qty = int(input("New Quantity: "))
            inventory_dao.update_inventory(pid, qty)
            print("Inventory updated.")
        elif choice == '0':
            break

def order_detail_menu():
    dao = OrderDetailDAO()
    while True:
        print("\nORDER DETAIL MENU")
        print("1. Add Order Detail")
        print("2. View by Order ID")
        print("0. Back")
        choice = input("Enter choice: ")
        if choice == '1':
            oid = int(input("Order ID: "))
            pid = int(input("Product ID: "))
            qty = int(input("Quantity: "))
            price = float(input("Unit Price: "))
            od = OrderDetail(oid, pid, qty, price)
            dao.create_order_detail(od)
            print("Order detail added.")
        elif choice == '2':
            oid = int(input("Order ID: "))
            details = dao.get_order_details_by_order_id(oid)
            for d in details:
                print(vars(d))
        elif choice == '0':
            break

def main():
    while True:
        print("\nMAIN MENU")
        print("1. Customers")
        print("2. Products")
        print("3. Orders")
        print("4. Inventory")
        print("5. Order Details")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            customer_menu()
        elif choice == '2':
            product_menu()
        elif choice == '3':
            order_menu()
        elif choice == '4':
            inventory_menu()
        elif choice == '5':
            order_detail_menu()
        elif choice == '0':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
