#Yeung Pok 20965361
class AVLNode:
    def __init__(self, key, value):
        self.key = key  # Transaction ID
        self.value = value  # Amount
        self.left = None
        self.right = None
        self.height = 1  # Height of node for balancing

class AVLTree:
    def insert(self, root, key, value):
        if not root:
            return AVLNode(key, value)

        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            raise ValueError("Transaction ID must be unique.")

        # Update height and balance the tree
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def balance(self, node):
        balance_factor = self.get_balance(node)

        # Left heavy
        if balance_factor > 1:
            if self.get_balance(node.left) < 0:  # Left Right Case
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right heavy
        if balance_factor < -1:
            if self.get_balance(node.right) > 0:  # Right Left Case
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def search(self, root, key):
        if not root:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append((node.key, node.value))
            self.in_order_traversal(node.right, result)

def is_valid_transaction_id(transaction_id):
    return isinstance(transaction_id, int) and transaction_id > 0

def is_valid_amount(amount):
    return isinstance(amount, (int, float)) and amount >= 0

def main():
    avl_tree = AVLTree()
    root = None

    while True:
        print("\n1. Insert Transaction")
        print("2. Search Transaction")
        print("3. Print AVL Tree (In-order Traversal)")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                transaction_id = int(input("Enter Transaction ID (unique positive integer): "))
                if not is_valid_transaction_id(transaction_id):
                    raise ValueError("Transaction ID must be a positive integer.")

                amount = float(input("Enter Amount (non-negative number): "))
                if not is_valid_amount(amount):
                    raise ValueError("Amount must be a non-negative number.")

                root = avl_tree.insert(root, transaction_id, amount)
                print("Transaction inserted successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                transaction_id = int(input("Enter Transaction ID to search: "))
                if not is_valid_transaction_id(transaction_id):
                    raise ValueError("Transaction ID must be a positive integer.")

                transaction = avl_tree.search(root, transaction_id)
                if transaction:
                    print(f"Transaction found: ID = {transaction.key}, Amount = {transaction.value}")
                else:
                    print("Transaction not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            result = []
            avl_tree.in_order_traversal(root, result)
            print("AVL Tree (In-order Traversal):")
            for key, value in result:
                print(f"Transaction ID: {key}, Amount: {value}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
