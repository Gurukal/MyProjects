# This variable holds the minimum percentage of payment balance.
Minimum_Percentage = 40  

# Course class to handle course details
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

def input_name(check):
    while True:
        name = input(check)
        if name.isdigit():
            print("Invalid input. Please enter a valid name (e.g., John).")
        else:
            return name

def input_id(check):
    while True:
        student_id = input(check)
        if not student_id.isdigit():
            print("Invalid input. Please enter a numeric value (e.g., 1234).")
        else:
            return student_id

courses = {} # Empyt Dictionary to store courses
students = [] # Empty List to store student details

# Student class to handle student details and enrollment
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.enrolled_courses = []
        self.name = name
        self.email = email
        self.balance = 0.0

    def enroll(self, course):
        self.enrolled_courses.append(course)
        self.balance += course.fee

    def make_payment(self, amount):
        if amount < self.balance * Minimum_Percentage / 100:
            print(f"Your payment must be at least {Minimum_Percentage}% of the outstanding balance.")
            return False
        self.balance -= amount
        print(f"Payment of {amount} is accepted. Your remaining balance is: {self.balance:.2f}")
        return True

# Function to register a new student
def register_student():
    print("\n--- Register Student ---")
    student_id = input_id("Enter student ID: ")

    # Check for duplicate student ID
    for student in students:
        if student.student_id == student_id:
            print("Student ID already exists. Please use a different ID.")
            return

    name = input_name("Enter student name: ")
    email = input("Enter student email: ")
    student = Student(student_id, name, email)
    students.append(student)
    print(f"Student {name} has been registered successfully.\n")

# Function to add a new course
def add_course():
    print("\n--- Add Course ---")
    course_id = input("Enter course ID: ")
    course_id = course_id.upper()

    # Checks for duplicate course ID
    if course_id in courses:
        print("Course ID already exists. Please use a different ID.")
        return

    name = input_name("Enter course name: ")
    try:
        fee = float(input("Enter course fee: "))
        if fee <= 0:
            print("Fee must be a positive value.")
            return
    except ValueError:
        print("Invalid fee input. Please enter a valid number.")
        return

    course = Course(course_id, name, fee)
    courses[course_id] = course
    print(f"Course {name} added successfully.\n")


def enroll_in_course(): # This function is used to enroll a student in a course
    print("\n--- Enroll a Student in a Course ---")
    student_id = input_id("Enter student ID: ")
    course_id = input("Enter course ID: ")
    course_id = course_id.upper()


    find_student = (i for i in students if i.student_id == student_id) # Code to find the student
    student = next(find_student, None)
    if not student:
        print("Student not found.")
        return

    course = courses.get(course_id)  # Find the course
    if not course:
        print("Course not found.")
        return

    student.enroll(course)  # Enroll the student in the course
    print(f"Student {student.name} has been enrolled in {course.name}. Balance: {student.balance:.2f}\n")

# Function to make a payment
def make_payment():
    print("\n--- Make a Payment ---")
    student_id = input_id("Enter student ID: ")

    # Find the student
    find_student = (j for j in students if j.student_id == student_id)
    student = next(find_student, None) 
    if not student:
        print("Student not found.")
        return
    print(f"Your minimum payment should be {student.balance * Minimum_Percentage / 100:.2f}")
    
    # Get payment amount
    try:
        payment = float(input(f"Enter payment amount (Outstanding balance: {student.balance:.2f}): "))
        if payment <= 0:
            print("Payment must be a positive value.")
            return
    except ValueError:
        print("Invalid payment amount. Please enter a valid number.")
        return

    # Process payment
    if student.make_payment(payment):
        print(f"Payment of {payment:.2f} processed for {student.name}. Remaining balance: {student.balance:.2f}\n")

# this function is used to view all students
def show_registered_students():
    print("\n--- Show Registered Students ---")
    if not students:
        print("No students registered.")
    else:
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Balance: {student.balance:.2f}, Email: {student.email}")
    print()

# To view all courses i used this function
def show_courses():
    print("\n--- Show Courses ---")
    if not courses:
        print("No courses available.")
    else:
        for course in courses.values():
            print(f"Course ID: {course.course_id}, Name: {course.name}, Fee: {course.fee:.2f}")
    print()

# Function to show all registered students
def show_students_in_course():
    print("\n--- Show All Registered Students ---")
    if not students:
        print("No students registered.")
    else:
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Balance: {student.balance:.2f}, Email: {student.email}")
            if student.enrolled_courses:
                print("Enrolled Courses:")
                for course in student.enrolled_courses:
                    print(f"  Course ID: {course.course_id}, Name: {course.name}, Fee: {course.fee:.2f}")
            else:
                print("No courses enrolled.")
            print()

# Function to check the student's balance
def check_student_balance():
    student_id = input_id("Enter student ID: ")
    # Find the student
    find_student = (l for l in students if l.student_id == student_id)
    student = next(find_student, None) 
    if student:
        print(f"Balance for student {student.name}: {student.balance:.2f}")
    else:
        print("Student not found.")

# Main menu function
def main_menu():
    while True:
        print("\n--- Welcome to the University of the Poor School Enrollment System ---")
        print("1. Register Student")
        print("2. Add Course")
        print("3. Enroll in Course")
        print("4. Make a Payment")
        print("5. Show Registered Students")
        print("6. Show Courses")
        print("7. Show students in course")
        print("8. Check Student Balance")
        print("9. Exit")

        selection = input("Please choose an option (1-9): ")

        match selection:
            case "1":
                register_student()
            case "2":
                add_course()
            case "3":
                enroll_in_course()
            case "4":
                make_payment()
            case "5":
                show_registered_students()
            case "6":
                show_courses()
            case "7":
                show_students_in_course()
            case "8":
                check_student_balance()
            case "9":
                print("Exiting the system.")
                break
            case _:
                print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    main_menu()

# “I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT”.
