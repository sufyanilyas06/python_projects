from db import connect_db

def add_course():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- Add New Course ---")
    name = input("Course Name: ")
    credits = input("Credits: ")
    teacher_id = input("Teacher ID: ")

    cur.execute("""
        INSERT INTO Course (Course_Name, Credits, Teacher_ID)
        VALUES (?, ?, ?)
    """, (name, credits, teacher_id))

    conn.commit()
    conn.close()
    print("Course added successfully!\n")

def view_courses():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- All Courses ---")
    cur.execute("SELECT * FROM Course")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Add Course")
        print("2. View Courses")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_course()
        elif choice == '2':
            view_courses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
