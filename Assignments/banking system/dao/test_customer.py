import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.customer import Customer
from dao.customer_dao import CustomerDAO
from exception.exceptions import InvalidCustomerException
import datetime

def test_insert_customer():
    print("\nTesting Insert Customer...")
    dao = CustomerDAO()

    # Create a customer
    customer = Customer(
        customer_id=None,  # Will be auto-generated
        first_name="John",
        last_name="Doe",
        dob=datetime.date(1985, 7, 20),
        email="john.doe@example.com",
        phone_number="1234567890",
        address="1234 Elm Street"
    )
    
    dao.insert_customer(customer)

def test_get_customer_by_id():
    print("\nTesting Get Customer By ID...")
    dao = CustomerDAO()
    
    # Assuming customer_id 1 exists
    customer = dao.get_customer_by_id(1)
    if customer:
        print(f"Customer fetched: {customer.first_name} {customer.last_name}, {customer.email}")
    else:
        print("Customer not found.")

def test_get_customer_by_email():
    print("\nTesting Get Customer By Email...")
    dao = CustomerDAO()
    
    # Assuming the email john.doe@example.com exists
    customer = dao.get_customer_by_email("john.doe@example.com")
    if customer:
        print(f"Customer fetched: {customer.first_name} {customer.last_name}, {customer.email}")
    else:
        print("Customer not found.")

def test_update_customer():
    print("\nTesting Update Customer...")
    dao = CustomerDAO()
    
    # Assuming customer_id 1 exists
    customer = dao.get_customer_by_id(1)
    if customer:
        customer.first_name = "UpdatedFirstName"
        dao.update_customer(customer)
        print(f"Customer updated: {customer.first_name}")
    else:
        print("Customer not found.")

def test_delete_customer():
    print("\nTesting Delete Customer...")
    dao = CustomerDAO()
    
    # Assuming customer_id 1 exists
    try:
        dao.delete_customer(1)
        print("Customer deleted successfully.")
    except Exception as e:
        print(f"Error deleting customer: {e}")

def test_invalid_customer():
    print("\nTesting Invalid Customer...")
    dao = CustomerDAO()
    
    try:
        # Trying to fetch a non-existent customer with ID 9999
        dao.get_customer_by_id(9999)
    except InvalidCustomerException as e:
        print(f"Handled exception: {e}")

def run_tests():
    test_insert_customer()
    test_get_customer_by_id()
    test_get_customer_by_email()
    test_update_customer()
    test_delete_customer()
    test_invalid_customer()

if __name__ == "__main__":
    run_tests()
