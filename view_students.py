import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_management"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\n--- Student Records ---\n")

for student in students:
    print(
        f"ID: {student[0]} | "
        f"Name: {student[1]} | "
        f"Department: {student[2]} | "
        f"Year: {student[3]}"
    )

conn.close()