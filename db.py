import sqlite3

def connect_db():
    return sqlite3.connect("student_mgmt.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Dept_Name TEXT NOT NULL,
        Location TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Student (
        Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        F_Name TEXT,
        M_Name TEXT,
        L_Name TEXT,
        DOB TEXT,
        Age INTEGER,
        Address TEXT,
        City TEXT,
        State TEXT,
        Pin_code TEXT,
        Mobile_no TEXT,
        Email TEXT,
        Department_ID INTEGER,
        FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Teacher (
        Teacher_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Teacher_Name TEXT,
        Contact_no TEXT,
        Email TEXT,
        Hire_Date TEXT,
        Department_ID INTEGER,
        FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Course (
        Course_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Course_Name TEXT,
        Credits INTEGER,
        Teacher_ID INTEGER,
        FOREIGN KEY (Teacher_ID) REFERENCES Teacher(Teacher_ID)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Enrollment (
        Enrolment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Student_ID INTEGER,
        Course_ID INTEGER,
        Enrolment_Date TEXT,
        Grade TEXT,
        FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
        FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")
