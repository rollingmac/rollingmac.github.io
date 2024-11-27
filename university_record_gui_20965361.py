#Yeung Pok 20965361
import csv
import tkinter as tk
from tkinter import messagebox, filedialog

class Person:
    def __init__(self, person_id, name, age, gender, role):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role

class Student(Person):
    def __init__(self, person_id, name, age, gender, role, student_type, major):
        super().__init__(person_id, name, age, gender, role)
        self.student_type = student_type
        self.major = major

class Staff(Person):
    def __init__(self, person_id, name, age, gender, role, category, position):
        super().__init__(person_id, name, age, gender, role)
        self.category = category
        self.position = position

def add_student_window():
    def add_student():
        person_id = person_id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        student_type = student_type_entry.get()
        major = major_entry.get()

        if not person_id or not name or not age or not gender or not student_type or not major:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        s = Student(person_id, name, age, gender, "student", student_type, major)
        students.append(s)
        messagebox.showinfo("Success", "Student added successfully.")
        add_student_window.destroy()

    add_student_window = tk.Toplevel(root)
    add_student_window.title("Add new student")

    person_id_label = tk.Label(add_student_window, text="Person ID:")
    person_id_label.grid(row=0, column=0, padx=5, pady=5)
    person_id_entry = tk.Entry(add_student_window)
    person_id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = tk.Label(add_student_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(add_student_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    age_label = tk.Label(add_student_window, text="Age:")
    age_label.grid(row=2, column=0, padx=5, pady=5)
    age_entry = tk.Entry(add_student_window)
    age_entry.grid(row=2, column=1, padx=5, pady=5)

    gender_label = tk.Label(add_student_window, text="Gender:")
    gender_label.grid(row=3, column=0, padx=5, pady=5)
    gender_entry = tk.Entry(add_student_window)
    gender_entry.grid(row=3, column=1, padx=5, pady=5)

    student_type_label = tk.Label(add_student_window, text="Student Type:")
    student_type_label.grid(row=4, column=0, padx=5, pady=5)
    student_type_entry = tk.Entry(add_student_window)
    student_type_entry.grid(row=4, column=1, padx=5, pady=5)

    major_label = tk.Label(add_student_window, text="Major:")
    major_label.grid(row=5, column=0, padx=5, pady=5)
    major_entry = tk.Entry(add_student_window)
    major_entry.grid(row=5, column=1, padx=5, pady=5)

    add_button = tk.Button(add_student_window, text="Add", command=add_student)
    add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

def add_staff_window():
    def add_staff():
        person_id = person_id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        category = category_entry.get()
        position = position_entry.get()

        if not person_id or not name or not age or not gender or not category or not position:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        s = Staff(person_id, name, age, gender, "staff", category, position)
        staffs.append(s)
        messagebox.showinfo("Success", "Staff added successfully.")
        add_staff_window.destroy()

    add_staff_window = tk.Toplevel(root)
    add_staff_window.title("Add new staff")

    person_id_label = tk.Label(add_staff_window, text="Person ID:")
    person_id_label.grid(row=0, column=0, padx=5, pady=5)
    person_id_entry = tk.Entry(add_staff_window)
    person_id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = tk.Label(add_staff_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(add_staff_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    age_label = tk.Label(add_staff_window, text="Age:")
    age_label.grid(row=2, column=0, padx=5, pady=5)
    age_entry = tk.Entry(add_staff_window)
    age_entry.grid(row=2, column=1, padx=5, pady=5)

    gender_label = tk.Label(add_staff_window, text="Gender:")
    gender_label.grid(row=3, column=0, padx=5, pady=5)
    gender_entry = tk.Entry(add_staff_window)
    gender_entry.grid(row=3, column=1, padx=5, pady=5)

    category_label = tk.Label(add_staff_window, text="Category:")
    category_label.grid(row=4, column=0, padx=5, pady=5)
    category_entry = tk.Entry(add_staff_window)
    category_entry.grid(row=4, column=1, padx=5, pady=5)

    position_label = tk.Label(add_staff_window, text="Position:")
    position_label.grid(row=5, column=0, padx=5, pady=5)
    position_entry = tk.Entry(add_staff_window)
    position_entry.grid(row=5, column=1, padx=5, pady=5)

    add_button = tk.Button(add_staff_window, text="Add", command=add_staff)
    add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

def view_all_students_window():
    if not students:
        messagebox.showwarning("Warning", "No students found.")
        return

    view_all_students_window = tk.Toplevel(root)
    view_all_students_window.title("View all students")

    table = tk.Frame(view_all_students_window)
    table.pack(padx=10, pady=10)

    headings = ["Person ID", "Name", "Age", "Gender", "Type", "Major"]
    for i, heading in enumerate(headings):
        label = tk.Label(table, text=heading, font="Helvetica 10 bold")
        label.grid(row=0, column=i, padx=5, pady=5)

    for i, student in enumerate(students):
        label = tk.Label(table, text=student.person_id)
        label.grid(row=i+1, column=0, padx=5, pady=5)

        label = tk.Label(table, text=student.name)
        label.grid(row=i+1, column=1, padx=5, pady=5)

        label = tk.Label(table, text=student.age)
        label.grid(row=i+1, column=2, padx=5, pady=5)

        label = tk.Label(table, text=student.gender)
        label.grid(row=i+1, column=3, padx=5, pady=5)

        label = tk.Label(table, text=student.student_type)
        label.grid(row=i+1, column=4, padx=5, pady=5)

        label = tk.Label(table, text=student.major)
        label.grid(row=i+1, column=5, padx=5, pady=5)

def view_all_staffs_window():
    global view_all_staffs_listbox

    view_all_staffs_window = tk.Toplevel(root)
    view_all_staffs_window.title("View all staffs")

    view_all_staffs_listbox = tk.Listbox(view_all_staffs_window)
    view_all_staffs_listbox.pack(padx=10, pady=10)

    for staff in staffs:
        view_all_staffs_listbox.insert(tk.END, f"{staff.name} - {staff.category} - {staff.position}")


root = tk.Tk()
root.title("School Management System")

students = []
staffs = []

add_student_button = tk.Button(root, text="Add new student", command=add_student_window)
add_student_button.pack(padx=10, pady=10)

add_staff_button = tk.Button(root, text="Add new staff", command=add_staff_window)
add_staff_button.pack(padx=10, pady=10)

view_all_students_button = tk.Button(root, text="View all students", command=view_all_students_window)
view_all_students_button.pack(padx=10, pady=10)

view_all_staffs_button = tk.Button(root, text="View all staffs", command=view_all_staffs_window)
view_all_staffs_button.pack(padx=10, pady=10)


root.mainloop()
