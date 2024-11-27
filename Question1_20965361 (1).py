#Yeung Pok
#20965361
def total_spend_per_customer(purchases):
    """
    Calculate the total spending for each customer.

    Args:
    purchases (list): A list of purchase dictionaries.

    Returns:
    dict: A dictionary with customer_id as keys and total spending as values.
    """
    spend_dict = {}
    for purchase in purchases:
        customer_id = purchase["customer_id"]
        price = purchase["price"]
        # Update the total spend for each customer
        if customer_id in spend_dict:
            spend_dict[customer_id] += price
        else:
            spend_dict[customer_id] = price
    return spend_dict

def most_popular_product(purchases):
    """
    Determine the most popular product based on purchase frequency.

    Args:
    purchases (list): A list of purchase dictionaries.

    Returns:
    list: A list of products that were purchased the most times.
    """
    product_count = {}
    for purchase in purchases:
        product = purchase["product"]
        # Count the occurrences of each product
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1

    # Find the maximum count
    max_count = max(product_count.values(), default=0)
    # Collect all products with the maximum count
    most_popular = [product for product, count in product_count.items() if count == max_count]

    return most_popular if most_popular else None  # Return None if no products were found

def highest_spending_customer(purchases):
    """
    Identify the customer(s) who have spent the most money.

    Args:
    purchases (list): A list of purchase dictionaries.

    Returns:
    list: A list of customer_ids of the highest spending customers.
    """
    spend_dict = total_spend_per_customer(purchases)
    if spend_dict:  # Check if the spend_dict is not empty
        max_spent = max(spend_dict.values())
        highest_spenders = [customer_id for customer_id, total in spend_dict.items() if total == max_spent]
        return highest_spenders
    return None  # Return None if no customers were found

# Example purchases list
purchases = [
    {"customer_id": 1, "product": "Laptop", "price": 1200.00},
    {"customer_id": 2, "product": "Smartphone", "price": 800.00},
    {"customer_id": 1, "product": "Mouse", "price": 20.00},
    {"customer_id": 3, "product": "Headphones", "price": 150.00},
    {"customer_id": 2, "product": "Laptop", "price": 1300.00},
    {"customer_id": 1, "product": "Keyboard", "price": 100.00},
    {"customer_id": 3, "product": "Smartphone", "price": 900.00},
    {"customer_id": 4, "product": "Monitor", "price": 250.00},
    {"customer_id": 4, "product": "Laptop", "price": 1100.00}
]

# Calculate total spend per customer
total_spend = total_spend_per_customer(purchases)
print("1. total_spend_per_customer(purchases):")
for customer_id, total in total_spend.items():
    print(f"Customer {customer_id} spent a total of ${total:.2f}")

# Find the most popular product
popular_products = most_popular_product(purchases)
print("\n2. most_popular_product(purchases):")
if popular_products:
    if len(popular_products) == 1:
        print(popular_products[0])  # Print the single most popular product
    else:
        print(f"{', '.join(popular_products)}.")  # Print multiple products
else:
    print("No products purchased.")

# Find the highest spending customer
highest_spenders = highest_spending_customer(purchases)
print("\n3. highest_spending_customer(purchases):")
if highest_spenders:
    if len(highest_spenders) == 1:
        print(f"The highest spender is Customer {highest_spenders[0]}.")
    else:
        print(f"The highest spender(s): Customer(s) {', '.join(map(str, highest_spenders))}.")
else:
    print("No customers found.")
