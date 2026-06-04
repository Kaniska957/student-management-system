import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_management"
)

cursor = conn.cursor()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        department = input("Enter department: ")
        year = int(input("Enter year: "))

        query = """
        INSERT INTO students (name, department, year)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, department, year))
        conn.commit()

        print("Student added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print("\n--- Student Records ---")
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Department: {student[2]} | "
                f"Year: {student[3]}"
            )

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        department = input("Enter new department: ")
        year = int(input("Enter new year: "))

        query = """
        UPDATE students
        SET department=%s, year=%s
        WHERE id=%s
        """
        cursor.execute(query, (department, year, student_id))
        conn.commit()

        print("Student updated successfully!")

    elif choice == "4":
        student_id = int(input("Enter Student ID to delete: "))

        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (student_id,)
        )
        conn.commit()

        print("Student deleted successfully!")
    elif choice == "5":
        student_name = input("Enter student name to search: ")

        query = "SELECT * FROM students WHERE name = %s"

        cursor.execute(query, (student_name,))

        students = cursor.fetchall()

        if students:
            print("\n--- Search Results ---")
            for student in students:
                print(
                    f"ID: {student[0]} | "
                    f"Name: {student[1]} | "
                    f"Department: {student[2]} | "
                    f"Year: {student[3]}"
                )
        else:
            print("No student found!")
    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

conn.close()