def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        student_info = {'id': student_id, 'name': student_name, 'dob': dob}
        students.append(student_info)
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_info = {'id': course_id, 'name': course_name, 'marks': {}}
        courses.append(course_info)
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    for course in courses:
        if course['id'] == course_id:
            for student in students:
                marks = float(input(f"Enter marks for {student['name']} in {course['name']}: "))
                if 'marks' not in course:
                    course['marks'] = {}
                if student['id'] not in course['marks']:
                    course['marks'][student['id']] = []
                course['marks'][student['id']].append(marks)
            break
    else:
        print("Course not found!")

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Birthday: {student['dob']}")

def show_student_marks(students, courses):
    course_id = input("Enter course ID to show student marks: ")
    course = next((c for c in courses if c['id'] == course_id), None) 
    
    if course:
        print(f"\nStudent Marks for {course['name']} in {course_id}:")
        for student_id, marks_list in course['marks'].items():
            student = next((s for s in students if s['id'] == student_id), None)
            if student:
                print(f"Student ID: {student_id}, \tName: {student['name']}, \tMarks: {marks_list}")
            else:
                print(f"Student ID: {student_id}, Marks: {marks_list} (Student not found)")
    else:
        print("Course not found!")


def main():
    students = []
    courses = []

    while True:
        print("\nMenu:")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Courses")
        print("5. List Students")
        print("6. Show Student Marks for a Course")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            students.extend(input_students())
        elif choice == '2':
            courses.extend(input_courses())
        elif choice == '3':
            input_marks(students, courses)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            show_student_marks(students, courses)
        elif choice == '7':
            print("Exitted program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__": 
    main()
