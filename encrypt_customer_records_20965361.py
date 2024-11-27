# Yeung Pok 20965361

import csv
import os

# Encryption and decryption tables
encryption_table = {
    '0': '5', '1': '3', '2': '0', '3': '2', '4': '1',
    '5': '9', '6': '8', '7': '4', '8': '7', '9': '6'
}

decryption_table = {v: k for k, v in encryption_table.items()}

def encrypt_id(customer_id):
    return ''.join(encryption_table[digit] for digit in customer_id)

def decrypt_id(encrypted_id):
    return ''.join(decryption_table[digit] for digit in encrypted_id)

def encrypt_name(name):
    return ''.join(chr(ord(char) + 3) for char in name)  # Simple Caesar cipher for names

def decrypt_name(encrypted_name):
    return ''.join(chr(ord(char) - 3) for char in encrypted_name)  # Reverse Caesar cipher

def encrypt_gender(gender):
    return chr(ord(gender) + 3)  # Simple Caesar cipher for gender

def decrypt_gender(encrypted_gender):
    return chr(ord(encrypted_gender) - 3)  # Reverse Caesar cipher

def add_customer_record():
    name = input("Enter customer name (upper/lowercase letters and spaces only): ")
    while not all(c.isalpha() or c.isspace() for c in name):
        print("Invalid name. Please enter letters and spaces only.")
        name = input("Enter customer name: ")

    customer_id = input("Enter customer ID (6 digits, unique): ")
    while not (customer_id.isdigit() and len(customer_id) == 6):
        print("Invalid ID. Please enter a 6-digit number.")
        customer_id = input("Enter customer ID: ")

    gender = input("Enter gender (M, m, F, f): ")
    while gender not in ['M', 'm', 'F', 'f']:
        print("Invalid gender. Please enter M, m, F, or f.")
        gender = input("Enter gender: ")

    encrypted_id = encrypt_id(customer_id)
    encrypted_name = encrypt_name(name)
    encrypted_gender = encrypt_gender(gender)

    with open('encrypted_customer_records.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([encrypted_name, encrypted_id, encrypted_gender])

def print_customer_records():
    if not os.path.exists('encrypted_customer_records.csv'):
        print("No Records Exist!")
        return

    with open('encrypted_customer_records.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = decrypt_name(row[0])
            customer_id = decrypt_id(row[1])
            gender = decrypt_gender(row[2])
            print(f"Name: {name}, ID: {customer_id}, Gender: {gender}")

def main():
    while True:
        print("\nMenu:")
        print("1. Enter customer record")
        print("2. Print customer record")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            add_customer_record()
        elif choice == '2':
            print_customer_records()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
