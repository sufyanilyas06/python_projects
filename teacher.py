from db import connect_db

def add_teacher():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- Add New Teacher ---")
    name = input("Teacher Name: ")
    contact = input("Contact No: ")
    email = input("Email: ")
    hire_date = input("Hire Date (YYYY-MM-DD): ")
    dept_id = input("Department ID: ")

    cur.execute("""
        INSERT INTO Teacher (Teacher_Name, Contact_no, Email, Hire_Date, Department_ID)
        VALUES (?, ?, ?, ?, ?)
    """, (name, contact, email, hire_date, dept_id))

    conn.commit()
    conn.close()
    print("Teacher added successfully!\n")

def view_teachers():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- All Teachers ---")
    cur.execute("SELECT * FROM Teacher")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Add Teacher")
        print("2. View Teachers")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_teacher()
        elif choice == '2':
            view_teachers()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
