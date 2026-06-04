import tkinter as tk
from tkinter import ttk
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_management"
)

cursor = conn.cursor()


def view_students():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("""
        SELECT id, name, department, year, email, attendance
        FROM students
    """)

    for student in cursor.fetchall():
        tree.insert("", tk.END, values=student)


def add_student():

    name = name_entry.get()
    department = dept_entry.get()
    year = year_entry.get()
    email = email_entry.get()
    attendance = attendance_entry.get()

    if (
        name == ""
        or department == ""
        or year == ""
        or email == ""
        or attendance == ""
    ):
        status_label.config(text="Please fill all fields")
        return

    cursor.execute(
        """
        INSERT INTO students
        (name, department, year, email, attendance)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            name,
            department,
            year,
            email,
            attendance
        )
    )

    conn.commit()

    status_label.config(text="Student Added Successfully")

    clear_fields()

    view_students()


def search_student():

    search_name = search_entry.get()

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute(
        """
        SELECT id, name, department, year, email, attendance
        FROM students
        WHERE name LIKE %s
        """,
        ("%" + search_name + "%",)
    )

    results = cursor.fetchall()

    for student in results:
        tree.insert("", tk.END, values=student)

    status_label.config(
        text=f"{len(results)} student(s) found"
    )


def delete_student():

    selected = tree.selection()

    if not selected:
        status_label.config(
            text="Select a student first"
        )
        return

    student_id = tree.item(
        selected[0]
    )["values"][0]

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (student_id,)
    )

    conn.commit()

    status_label.config(
        text="Student Deleted Successfully"
    )

    view_students()


def clear_fields():

    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    attendance_entry.delete(0, tk.END)


# GUI Window
root = tk.Tk()

root.title("Student Management System")
root.geometry("1100x700")

title = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 22, "bold")
)

title.pack(pady=15)

# Name
tk.Label(root, text="Name").pack()

name_entry = tk.Entry(root, width=50)
name_entry.pack()

# Department
tk.Label(root, text="Department").pack()

dept_entry = tk.Entry(root, width=50)
dept_entry.pack()

# Year
tk.Label(root, text="Year").pack()

year_entry = tk.Entry(root, width=50)
year_entry.pack()

# Email
tk.Label(root, text="Email").pack()

email_entry = tk.Entry(root, width=50)
email_entry.pack()

# Attendance
tk.Label(root, text="Attendance (%)").pack()

attendance_entry = tk.Entry(root, width=50)
attendance_entry.pack()

# Add Button
add_btn = tk.Button(
    root,
    text="Add Student",
    width=25,
    command=add_student
)

add_btn.pack(pady=10)

# Search
tk.Label(root, text="Search Student").pack()

search_entry = tk.Entry(root, width=50)
search_entry.pack()

search_btn = tk.Button(
    root,
    text="Search",
    width=25,
    command=search_student
)

search_btn.pack(pady=5)

# Delete
delete_btn = tk.Button(
    root,
    text="Delete Selected Student",
    width=25,
    command=delete_student
)

delete_btn.pack(pady=5)

status_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold")
)

status_label.pack(pady=10)

# Table
tree = ttk.Treeview(
    root,
    columns=(
        "ID",
        "Name",
        "Department",
        "Year",
        "Email",
        "Attendance"
    ),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Department", text="Department")
tree.heading("Year", text="Year")
tree.heading("Email", text="Email")
tree.heading("Attendance", text="Attendance")

tree.column("ID", width=50)
tree.column("Name", width=180)
tree.column("Department", width=120)
tree.column("Year", width=80)
tree.column("Email", width=250)
tree.column("Attendance", width=100)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=20
)

view_students()

root.mainloop()