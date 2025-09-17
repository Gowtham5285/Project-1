import sqlite3

# ---------------- Database Setup ---------------- #
def create_tables():
    conn = sqlite3.connect("course_management.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
                        course_id INTEGER PRIMARY KEY,
                        course_name TEXT,
                        instructor TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments(
                        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        course_id INTEGER,
                        FOREIGN KEY (student_id) REFERENCES students(student_id),
                        FOREIGN KEY (course_id) REFERENCES courses(course_id))''')

    conn.commit()
    conn.close()

# ---------------- Admin Functions ---------------- #
def add_course(course_id, course_name, instructor):
    conn = sqlite3.connect("course_management.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses VALUES(?,?,?)",
                   (course_id, course_name, instructor))
    conn.commit()
    conn.close()
    print("✅ Course added successfully!")

def view_courses():
    conn = sqlite3.connect("course_management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# ---------------- Student Functions ---------------- #
def register_student(name, email):
    conn = sqlite3.connect("course_management.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name, email) VALUES(?,?)",
                   (name, email))
    conn.commit()
    conn.close()
    print("✅ Student registered successfully!")

def enroll_student(student_id, course_id):
    conn = sqlite3.connect("course_management.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments(student_id, course_id) VALUES(?,?)",
                   (student_id, course_id))
    conn.commit()
    conn.close()
    print("🎓 Student enrolled in course!")

def view_enrollments():
    conn = sqlite3.connect("course_management.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT e.enrollment_id, s.name, c.course_name
                      FROM enrollments e
                      JOIN students s ON e.student_id = s.student_id
                      JOIN courses c ON e.course_id = c.course_id""")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# ---------------- Main Menu ---------------- #
def main():
    create_tables()

    while True:
        print("\n===== Course Management System =====")
        print("1. Add Course (Admin)")
        print("2. View Courses")
        print("3. Register Student")
        print("4. Enroll Student in Course")
        print("5. View Enrollments")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            cid = int(input("Enter Course ID: "))
            cname = input("Enter Course Name: ")
            inst = input("Enter Instructor: ")
            add_course(cid, cname, inst)

        elif choice == 2:
            view_courses()

        elif choice == 3:
            name = input("Enter Student Name: ")
            email = input("Enter Email: ")
            register_student(name, email)

        elif choice == 4:
            sid = int(input("Enter Student ID: "))
            cid = int(input("Enter Course ID: "))
            enroll_student(sid, cid)

        elif choice == 5:
            view_enrollments()

        elif choice == 6:
            print("🚪 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
