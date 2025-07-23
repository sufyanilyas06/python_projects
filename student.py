from db import connect_db

def add_student():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- Add New Student ---")
    f_name = input("First Name: ")
    m_name = input("Middle Name: ")
    l_name = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    age = input("Age: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    pin_code = input("Pin Code: ")
    mobile_no = input("Mobile No: ")
    email = input("Email: ")
    dept_id = input("Department ID: ")

    cur.execute("""
        INSERT INTO Student (F_Name, M_Name, L_Name, DOB, Age, Address, City, State, Pin_code, Mobile_no, Email, Department_ID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (f_name, m_name, l_name, dob, age, address, city, state, pin_code, mobile_no, email, dept_id))

    conn.commit()
    conn.close()
    print("Student added successfully!\n")

def view_students():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- All Students ---")
    cur.execute("SELECT * FROM Student")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
