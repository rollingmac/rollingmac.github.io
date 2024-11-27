# Yeung Pok 20965361
class Student:
    def __init__(self, name, gender, age, height, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height  # in meters
        self.weight = weight  # in kilograms
        self.bmi = self.calculate_bmi()

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)


def get_valid_input(prompt, valid_type):
    while True:
        try:
            value = valid_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {valid_type.__name__}.")


def get_student_records():
    students = []
    for _ in range(5):
        name = input("Enter student's name: ")
        gender = input("Enter student's gender (M/F): ").strip().upper()
        while gender not in ['M', 'F']:
            print("Invalid gender. Please enter 'M' or 'F'.")
            gender = input("Enter student's gender (M/F): ").strip().upper()

        age = get_valid_input("Enter student's age: ", int)
        height = get_valid_input("Enter student's height in meters (e.g., 1.75): ", float)
        weight = get_valid_input("Enter student's weight in kilograms (e.g., 70): ", float)

        student = Student(name, gender, age, height, weight)
        students.append(student)

    return students


def print_student_records(students):
    print("\nStudent Records:")
    for student in students:
        print(f"Name: {student.name}, Gender: {student.gender}, Age: {student.age}, "
              f"Height: {student.height}, Weight: {student.weight}, BMI: {student.bmi:.2f}")


def main():
    students = get_student_records()
    print_student_records(students)


if __name__ == "__main__":
    main()
