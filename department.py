from db import connect_db

def add_department():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- Add New Department ---")
    name = input("Department Name: ")
    location = input("Location: ")

    cur.execute("""
        INSERT INTO Department (Dept_Name, Location)
        VALUES (?, ?)
    """, (name, location))

    conn.commit()
    conn.close()
    print("Department added successfully!\n")

def view_departments():
    conn = connect_db()
    cur = conn.cursor()

    print("\n--- All Departments ---")
    cur.execute("SELECT * FROM Department")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Add Department")
        print("2. View Departments")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_department()
        elif choice == '2':
            view_departments()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
