from db import connect_db

def enroll_student():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- Enroll Student in Course ---")
    student_id = input("Student ID: ")
    course_id = input("Course ID: ")
    enrollment_date = input("Enrollment Date (YYYY-MM-DD): ")
    grade = input("Grade (optional): ")

    cur.execute("""
        INSERT INTO Enrollment (Student_ID, Course_ID, Enrolment_Date, Grade)
        VALUES (?, ?, ?, ?)
    """, (student_id, course_id, enrollment_date, grade))

    conn.commit()
    conn.close()
    print("Student enrolled successfully!\n")

def view_enrollments():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- All Enrollments ---")
    cur.execute("SELECT * FROM Enrollment")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Enroll Student")
        print("2. View Enrollments")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            enroll_student()
        elif choice == '2':
            view_enrollments()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
