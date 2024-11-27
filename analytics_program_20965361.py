import csv

def load_transactions(filename):
    transactions = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Convert Amount and Quantity to appropriate types
                    row['Amount'] = float(row['Amount'])
                    row['Quantity'] = int(row['Quantity'])
                    # Convert ProductID to integer and strip any whitespace
                    row['ProductID'] = int(row['ProductID'].strip())
                    transactions.append(row)
                except ValueError as ve:
                    print(f"Value error for transaction {row.get('TransactionID', 'unknown')}: {ve}")
                except KeyError as ke:
                    print(f"Missing key in transaction data: {ke}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return transactions

def find_transactions_by_amount(transactions, min_amount, max_amount):
    results = [transaction for transaction in transactions if min_amount <= transaction['Amount'] <= max_amount]
    return results

def find_transactions_by_product_id(transactions, product_id):
    results = [transaction for transaction in transactions if transaction['ProductID'] == product_id]
    return results

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    filename = 'transactions.csv'
    transactions = load_transactions(filename)

    if not transactions:
        print("No transactions loaded. Please check the CSV file.")
        return

    # Get valid minimum and maximum amounts from the user
    min_amount = get_float_input("Enter minimum amount: ")
    max_amount = get_float_input("Enter maximum amount: ")

    print("Transactions within the given amount range:")
    found_transactions = find_transactions_by_amount(transactions, min_amount, max_amount)
    if found_transactions:
        for transaction in found_transactions:
            print(transaction)
    else:
        print("No transactions found in the specified amount range.")

    # Get valid ProductID from the user
    product_id = get_int_input("Enter ProductID to search for: ")

    print("Transactions for the specified ProductID:")
    found_transactions = find_transactions_by_product_id(transactions, product_id)
    if found_transactions:
        for transaction in found_transactions:
            print(transaction)
    else:
        print(f"No transactions found for the specified ProductID: {product_id}")

if __name__ == "__main__":
    main()
