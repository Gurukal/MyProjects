Author: Keron Ellis

Date Created: 30/11/2024

Course: ITT103
 
GitHub Public URL to Code: https://github.com/Gurukal/MyProjects/tree/main


University of the Poor School Course Registration and Payment System

Purpose

This program is designed to manage student registrations, course offerings, and student payments in an educational institution. It allows administrators to register students, add courses, enroll students in courses, process payments, and view various details about students and courses.

How to Run the Program

Ensure you have Python installed on your system.

Save the program code in a file Ellis.Keron-Course_Registration-ITT103-F2024.py

Open a terminal or command prompt.

Navigate to the directory where the file is saved.

Run the program using the command: Ellis.Keron-Course_Registration-ITT103-F2024.py

Follow the prompts in the menu to interact with the system.

Assumptions

Student IDs are unique identifiers for each student.

Course IDs are unique identifiers for each course.

A minimum payment of 40% of the outstanding balance is required to process a payment.

The system assumes valid input formats for names, emails, IDs, and fees.

Limitations

The program uses a simple list and dictionary to store student and course information, which means the data will be lost when the program terminates.

Added Email Attribute: The Student class now includes an email attribute to store the student's email address.

Uppercase Course IDs: Course IDs are converted to uppercase to ensure consistency.

Improved Input Validation: Functions input_name and input_id are used to validate name and ID inputs, ensuring names do not contain digits and IDs are numeric.

Payment Percentage: The minimum payment percentage is defined by the Minimum_Percentage variable, set to 40%.

Duplicate Checks: The program checks for duplicate student and course IDs during registration and addition, respectively.

Enhanced Menu: The menu includes options for registering students, adding courses, enrolling in courses, making payments, showing registered students, showing courses, showing students in a course, and checking student balances.


Example Menu


--- Welcome to the University of the Poor School Enrollment System ---

1. Register Student
2. Add Course
3. Enroll in Course
4. Make a Payment
5. Show Registered Students
6. Show Courses
7. Show Students in Course
8. Check Student Balance
9. Exit


