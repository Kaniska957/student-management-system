import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_management"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID to delete: "))

query = "DELETE FROM students WHERE id = %s"

cursor.execute(query, (student_id,))
conn.commit()

print("Student deleted successfully!")

conn.close()