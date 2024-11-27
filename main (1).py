#Yeung Pok 20965361 3.10.4
import csv

class Transaction:
    def __init__(self, transaction_id, date, product_id, product_name, quantity, amount, employee_id, store_id):
        self.transaction_id = transaction_id
        self.date = date
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.amount = amount
        self.employee_id = employee_id
        self.store_id = store_id

class Product:
    def __init__(self, product_id, product_name, product_description, product_cost):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_cost = product_cost

class Store:
    def __init__(self, store_id, store_name, store_location):
        self.store_id = store_id
        self.store_name = store_name
        self.store_location = store_location

class Employee:
    def __init__(self, employee_id, employee_name, employee_email, employee_phone):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_email = employee_email
        self.employee_phone = employee_phone

def validate_date(date_string):
    # Your date validation code here
    return date_string

def validate_product_name(product_name):
    # Your product name validation code here
    return product_name

def validate_quantity(quantity):
    # Your quantity validation code here
    return quantity

def validate_amount(amount):
    # Your amount validation code here
    return amount

def validate_employee_id(employee_id):
    # Your employee ID validation code here
    return employee_id

def validate_store_id(store_id):
    # Your store ID validation code here
    return store_id

def add_transaction():
    # Prompt the user for transaction details
    transaction_id = input("Enter transaction ID: ")
    date = validate_date(input("Enter transaction date (mm/dd/yyyy): "))
    product_id = input("Enter product ID: ")
    product_name = validate_product_name(input("Enter product name: "))
    quantity = validate_quantity(input("Enter quantity: "))
    amount = validate_amount(input("Enter amount: "))
    employee_id = validate_employee_id(input("Enter employee ID: "))
    store_id = validate_store_id(input("Enter store ID: "))

    # Create a new transaction object and write it to the transactions.csv file
    transaction = Transaction(transaction_id, date, product_id, product_name, quantity, amount, employee_id, store_id)
    with open('transactions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction.transaction_id, transaction.date, transaction.product_id, transaction.product_name, transaction.quantity, transaction.amount, transaction.employee_id, transaction.store_id])
    print(f"transaction_id: {transaction.transaction_id}, date: {transaction.date}, product_id: {product_id}, product_name: {product_name}, quantity: {quantity}, amount: {amount}, employee_id: {employee_id}, store_id: {store_id}")
    print("Transaction added successfully!")

def display_latest_transactions():
    # Read the transactions.csv file and extract the 5 latest transactions
    transactions = []
    with open('transactions.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            transaction = Transaction(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            transactions.append(transaction)
    latest_transactions = sorted(transactions, key=lambda x: (x.date, x.transaction_id), reverse=True)[:5]

    # Display the latest transactions on the screen
    print("Displaying the 5 Latest Transactions:")
    for transaction in latest_transactions:
        print(f"transaction_id: {transaction.transaction_id}, date: {transaction.date}, product_id: {transaction.product_id}, product_name: {transaction.product_name}, quantity: {transaction.quantity}, amount: {transaction.amount}, employee_id: {transaction.employee_id}, store_id: {transaction.store_id}")


def calculate_profit():
    # Read the products.csv, stores.csv, and employees.csv files
    products = {}
    with open('products.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            product = Product(row[0], row[1], row[2], float(row[3]))
            products[product.product_id] = product

    stores = {}
    with open('stores.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            store = Store(row[0], row[1], row[2])
            stores[store.store_id] = store

    employees = {}
    with open('employees.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            employee = Employee(row[0], row[1], row[2], row[3])
            employees[employee.employee_id] = employee

    # Read the transactions.csv file
    transactions = []
    with open('transactions.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            transaction = Transaction(row[0], row[1], row[2], row[3], int(row[4]), float(row[5]), row[6], row[7])
            if transaction.product_id not in products:
                print(f"Error: product with ID {transaction.product_id} not found in products.csv")
            else:
                transactions.append(transaction)

    # Calculate the total profit and profit by store name, product name, and employee name
    total_profit = 0
    profit_by_store = {}
    profit_by_product = {}
    profit_by_employee = {}
    for transaction in transactions:
        product = products[transaction.product_id]
        store = stores[transaction.store_id]
        employee = employees[transaction.employee_id]
        profit = transaction.quantity * (transaction.amount - product.product_cost)
        total_profit += profit
        profit_by_store[store.store_name] = profit_by_store.get(store.store_name, 0) + profit
        profit_by_product[product.product_name] = profit_by_product.get(product.product_name, 0) + profit
        profit_by_employee[employee.employee_name] = profit_by_employee.get(employee.employee_name, 0) + profit

    # Display the sales performance summary on the screen
    print("Summary of Sales Profit:")
    print(f"Total Profit: {format(total_profit, '.2f')}")
    print("Profit by Store:")
    for store_name, profit in profit_by_store.items():
        print(f"{store_name}: {format(profit, '.2f')}")
    print("Profit by Product:")
    for product_name, profit in profit_by_product.items():
        print(f"{product_name}: {format(profit, '.2f')}")
    print("Profit by Employee:")
    for employee_name, profit in profit_by_employee.items():
        print(f"{employee_name}: {format(profit, '.2f')}")

while True:
    print("Capturing Sales Transactions")
    print("1. Add new transaction")
    print("2. Display the 5 Latest Transactions")
    print("3. Calculate Sales Profit")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_transaction()
    elif choice == '2':
        display_latest_transactions()
    elif choice == '3':
        calculate_profit()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
