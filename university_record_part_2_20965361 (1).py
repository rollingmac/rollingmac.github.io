#Yeung Pok 20965361
import csv

class Person:
    def __init__(self, person_id, name, age, gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = ""

    def display_info(self):
        return f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Role: {self.role}"


class Student(Person):
    def __init__(self, person_id, name, age, gender, role, student_type, major):
        super().__init__(person_id, name, age, gender)
        self.role = role
        self.student_type = student_type
        self.major = major

    def display_info(self):
        return super().display_info() + f", Type: {self.student_type}, Major: {self.major}"


class Staff(Person):
    def __init__(self, person_id, name, age, gender, role, category, position):
        super().__init__(person_id, name, age, gender)
        self.role = role
        self.category = category
        self.position = position

    def display_info(self):
        return super().display_info() + f", Category: {self.category}, Position: {self.position}"


def validate_id(input_id):
    while True:
        try:
            input_id = int(input_id)
            if input_id <= 0:
                raise ValueError
            return input_id
        except ValueError:
            print("Invalid ID. ID should be a positive integer.")
            input_id = input("Enter the ID again: ")


def validate_name(input_name):
    while True:
        if input_name.isalpha():
            return input_name
        else:
            print("Invalid name. Name should contain only alphabets.")
            input_name = input("Enter the name again: ")


def validate_age(input_age):
    while True:
        try:
            input_age = int(input_age)
            if input_age <= 1 or input_age >= 100:
                raise ValueError
            return input_age
        except ValueError:
            print("Invalid age. Age should be an integer between 1 and 100.")
            input_age = input("Enter the age again: ")


def validate_gender(input_gender):
    while True:
        if input_gender in ['M', 'F']:
            return input_gender
        else:
            print("Invalid gender. Gender should be either 'M' or 'F'.")
            input_gender = input("Enter the gender again: ")


def validate_role(input_role):
    while True:
        if input_role in ['student', 'staff']:
            return input_role
        else:
            print("Invalid role. Role should be either 'student' or 'staff'.")
            input_role = input("Enter the role again: ")


def validate_student_type(input_type):
    while True:
        if input_type.isalpha():
            return input_type
        else:
            print("Invalid student type. Student type should contain only alphabets.")
            input_type = input("Enter the student type again: ")


def validate_major(input_major):
    while True:
        if input_major.isalpha():
            return input_major
        else:
            print("Invalid major. Major should contain only alphabets.")
            input_major = input("Enter the major again: ")


def validate_category(input_category):
    while True:
        if input_category.isalpha():
            return input_category
        else:
            print("Invalid category. Category should contain only alphabets.")
            input_category = input("Enter the category again: ")


def validate_position(input_position):
    while True:
        if input_position.isalpha():
            return input_position
        else:
            print("Invalid position. Position should contain only alphabets.")
            input_position = input("Enter the position again: ")


def add_student():
    print("Please enter the following personal details for the student:")
    person_id = validate_id(input("Enter the student ID: "))
    name = validate_name(input("Enter the student name: "))
    age = validate_age(input("Enter the student age: "))
    gender = validate_gender(input("Enter the student gender (M/F): "))
    role = validate_role('student')
    student_type = validate_student_type(input("Enter the student type: "))
    major = validate_major(input("Enter the student major: "))
    if all([person_id, name, age, gender, role, student_type, major]):
        s = Student(person_id, name, age, gender, role, student_type, major)
        print("Student added successfully.")
        return s
    else:
        print("Failed to add student.")
        return None


def add_staff():
    print("Please enter the following personal details for the staff:")
    person_id = validate_id(input("Enter the staff ID: "))
    name = validate_name(input("Enter the staff name: "))
    age = validate_age(input("Enter the staff age: "))
    gender = validate_gender(input("Enter the staff gender (M/F): "))
    role = validate_role('staff')
    category = validate_category(input("Enter the staff category: "))
    position = validate_position(input("Enter the staff position: "))
    if all([person_id, name, age, gender, role, category, position]):
        s = Staff(person_id, name, age, gender, role, category, position)
        print("Staff added successfully.")
        return s
    else:
        print("Failed to add staff.")
        return None


def view_all_students(students):
    if not students:
        print("No student records found.")
    else:
        for s in students:
            print(s.display_info())


def view_all_staff(staffs):
    if not staffs:
        print("No staff records found.")
    else:
        for s in staffs:
            print(s.display_info())


def save_data(data, filename):
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Age', 'Gender', 'Role', 'Type/Major/Category/Position'])
            for d in data:
                if isinstance(d, Student):
                    writer.writerow([d.person_id, d.name, d.age, d.gender, d.role, f"{d.student_type}/{d.major}"])
                elif isinstance(d, Staff):
                    writer.writerow([d.person_id, d.name, d.age, d.gender, d.role, f"{d.category}/{d.position}"])
        print(f"Data saved to {filename} successfully.")
    except FileNotFoundError:
        print(f"Failed to save data to {filename}. File not found.")


def read_data(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            data = []
            for row in reader:
                person_id, name, age, gender, role, details = row
                if role == 'student':
                    student_type, major = details.split('/')
                    s = Student(person_id, name, age, gender, role, student_type, major)
                    data.append(s)
                elif role == 'staff':
                    category, position = details.split('/')
                    s = Staff(person_id, name, age, gender, role, category, position)
                    data.append(s)
        print(f"{len(data)} records read from {filename}.")
        return data
    except FileNotFoundError:
        print(f"Failed to read data from {filename}. File not found.")
        return []


def main():
    students = []
    staffs = []
    while True:
        print("\n--- MENU ---")
        print("1. Add new student")
        print("2. Add new staff")
        print("3. View all students")
        print("4. View all staff")
        print("5. Save data to a file")
        print("6. Exit program")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            s = add_student()
            if s:
                students.append(s)
        elif choice == '2':
            s = add_staff()
            if s:
                staffs.append(s)
        elif choice == '3':
            view_all_students(students)
        elif choice == '4':
            view_all_staff(staffs)
        elif choice == '5':
            filename = input("Enter filename to save data to: ")
            save_data(students + staffs, filename)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()
