# This variable holds the minimum percentage of payment balance.
Minimum_Percentage = 40  

students = [] # Empty List to store sudent details 
courses = {} # Empyt Dictionary to store courses 

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

# Student class to handle student details and enrollment
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email  # Added email attribute
        self.enrolled_courses = []
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
    if any(student.student_id == student_id for student in students):
        print("Student ID already exists. Please use a different ID.")
        return

    name = input_name("Enter student name: ")
    email = input("Enter student email: ")  # Now taking email as input
    student = Student(student_id, name, email)
    students.append(student)
    print(f"Student {name} has been registered successfully.\n")

# Function to add a new course
def add_course():
    print("\n--- Add Course ---")
    course_id = input("Enter course ID: ")
    course_id = course_id.upper()  # Fix: make course_id uppercase

    # Check for duplicate course ID
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

# This function to enroll a student in a course
def enroll_in_course():
    print("\n--- Enroll a Student in a Course ---")
    student_id = input_id("Enter student ID: ")
    course_id = input("Enter course ID: ")
    course_id = course_id.upper()  # Make course_id uppercase

    # Find the student
    find_student = (s for s in students if s.student_id == student_id) # A generator to find the student
    student = next(find_student, None) # Get the next student from the generator, or None if not found
    if not student:
        print("Student not found.")
        return

    # Find the course
    course = courses.get(course_id)
    if not course:
        print("Course not found.")
        return

    # Enroll the student in the course
    student.enroll(course)
    print(f"Student {student.name} has been enrolled in {course.name}. Balance: {student.balance:.2f}\n")

# Function to make a payment
def make_payment():
    print("\n--- Make a Payment ---")
    student_id = input_id("Enter student ID: ")

    # Find the student
    find_student = (s for s in students if s.student_id == student_id) 
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

# Function to view all students
def show_registered_students():
    print("\n--- Show Registered Students ---")
    if not students:
        print("No students registered.")
    else:
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Balance: {student.balance:.2f}, Email: {student.email}")
    print()

# Function to view all courses
def show_courses():
    print("\n--- Show Courses ---")
    if not courses:
        print("No courses available.")
    else:
        for course in courses.values():
            print(f"Course ID: {course.course_id}, Name: {course.name}, Fee: {course.fee:.2f}")
    print()

# Function to view details of a student's enrollment
def show_students_in_course():
    print("\n--- View Student Details ---")
    student_id = input_id("Enter student ID: ")

    # Find the student
    find_student = (s for s in students if s.student_id == student_id) 
    student = next(find_student, None) 
    if not student: 
        print("Student not found.") # Check if the student was found
        return
    
    # Display student details
    print(f"ID: {student.student_id}, Name: {student.name}, Balance: {student.balance:.2f}, Email: {student.email}")
    print("Enrolled courses:")
    for course in student.enrolled_courses:
        print(f"Course ID: {course.course_id}, Name: {course.name}, Fee: {course.fee:.2f}")
    print()

# Function to check the student's balance
def check_student_balance():
    student_id = input_id("Enter student ID: ")
    # Find the student
    find_student = (s for s in students if s.student_id == student_id) 
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
