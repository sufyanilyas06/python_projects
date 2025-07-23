import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear()
        print("====== Student Management System ======")
        print("1. Student Management")
        print("2. Department Management")
        print("3. Teacher Management")
        print("4. Course Management")
        print("5. Enrollment Management")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            os.system("python student.py")
        elif choice == '2':
            os.system("python department.py")
        elif choice == '3':
            os.system("python teacher.py")
        elif choice == '4':
            os.system("python course.py")
        elif choice == '5':
            os.system("python enrollment.py")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Press Enter to try again.")
            input()

if __name__ == '__main__':
    main_menu()
