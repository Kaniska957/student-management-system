import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_management"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID to update: "))
new_department = input("Enter new department: ")
new_year = int(input("Enter new year: "))

query = """
UPDATE students
SET department = %s, year = %s
WHERE id = %s
"""

values = (new_department, new_year, student_id)

cursor.execute(query, values)
conn.commit()

print("Student updated successfully!")

conn.close()