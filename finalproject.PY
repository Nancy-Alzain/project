class CourseStudent:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_student(self):
        name = input("Enter the name of student : ")
        level = input("Enter the level of student : ").upper()
        value = False
        while not value:
            if level in ['A', 'B', 'C']:
                student = Student(name, level)
                self.students.append(student)
                print("student added successfully ....")
                value = True
            else:
                print("Invalid input ! , Please enter class level again (A / B / c)")
                x = input("Enter the level : ")
                level = x.capitalize()

    def add_course(self):
        name = input("Enter the name of course : ")
        level = input("Enter the level of course : ").upper()
        value = False
        while not value:
            if level in ['A', 'B', 'C']:
                course = Course(name, level)
                self.courses.append(course)
                print("course added successfully ....")
                value = True
            else:
                print("Invalid input ! , Please enter class level again (A / B / c)")
                x = input("Enter the level : ")
                level = x.capitalize()

    def find_id_std(self, id1):
        for student in self.students:
            if student.id_std == id1:
                return student
            else:
                print("Invalid ID_student")

    def remove_student(self):
        id1 = int(input("Enter the id student, Please : "))
        x = self.find_id_std(id1)
        if x:
            self.students.remove(x)
            print(f"student {x.name} deleted successfully")
        else:
            print("user not exist")

    def edit_std(self):
        id1 = int(input("Enter the id student, Please : "))
        std = self.find_id_std(id1)
        if std:
            name = input("Enter the name of student : ")
            level = input("Enter the level of student in list [ A , B , C ] : ").upper()
            value = False
            while not value:
                if level in ['A', 'B', 'C']:
                    print("Student details updated successfully")
                    value = True
                else:
                    print("Invalid input ! , Please enter class level again (A / B / c)")
                    x = input("Enter the level : ")
                    level = x.capitalize()
        else:
            print("***")
        std.name = name
        std.level = level

    def find_id_course(self, id1):
        for course in self.courses:
            if course.id_course == id1:
                return course
        else:
            print("Invalid ID_course")

    def show_students(self):
        space = " "*15
        # max length of name is (15)
        print(f"ID  |   Name{' '*12}|level{' '*25}")
        for student in self.students:
            s1 = 15 - len(student.name)
            s2 = 15 - len(student.level)
            print(f'{student.id_std}   |   {student.name + space[ :s1]} | {student.level + space[ :s2]}')

    def show_courses(self):
        space = " "*15
        # max length of name is (15)
        print(f" ID  | Name {' ' * 12 }| laval")
        print(" "*30)
        for course in self.courses:
            s1 = 15-len(course.name)
            print(f'{course.id_course}    | {course.name +space[:s1]}  | {course.level}')

    def add_course_student(self):
        id_student = int(input("enter the id_student : "))
        values = ['keep', 'enough']
        for value in values:
            while value in values and value != 'enough':
                id_course = int(input("enter the id_course : "))
                student11 = self.find_id_std(id_student)
                course11 = self.find_id_course(id_course)
                if student11 is None or course11 is None:
                    print("student or course not found.")
                elif student11.level == course11.level:
                    student11.student_courses.append(course11)
                    print(f"{course11.name} add to {student11.name} successfuly !")
                else:
                    print("student and  course  level  mismatch")
                value = (input("Input keep if you want to continue add courses to this student "
                               ", if you not Input enough >>> "))

    def show_student_courses(self):
        id_student = int(input("enter the id_student : "))
        student11 = self.find_id_std(id_student)
        space = " " * 15
        print("***** The courses of student >>>")
        print(f" Id courses || name courses {' '*12}  || level courses \t")
        for course in student11.student_courses:
            s1 = 15 - len(course.name)
            print(f"  {course.id_course}         || {course.name +space[:s1]}            || {course.level}")

    def display_student(self):
        id_student = int(input("enter the id_student : "))
        student11 = self.find_id_std(id_student)
        print(f"The id of student is {student11.id_std}\n"
              f"The name of student is {student11.name}\n"
              f"The level of student is {student11.level}")
        self.show_student_courses()


class Student:
    counter_std = 1

    def __init__(self, name, level):
        self.id_std = Student.counter_std
        Student.counter_std += 1
        self.name = name
        self.level = level
        self.student_courses = []


class Course:
    counter_course = 1

    def __init__(self, name, level):
        self.id_course = Course.counter_course
        Course.counter_course += 1
        self.name = name
        self.level = level


cs = CourseStudent()
menu = ("""\n\nSelect Choice Please :-

 1. Add New Student

 2. Remove Student

 3. Edit Student

 4. Display ALL Students

 5. Create New Course

 6. Add course to student
 
 7. show_student_courses
 
 8. display_student
 
 9. show courses

 0. Exit
 \n\n""")
print('  Welcome to the student_course system ! ' .center(100, '*'))
while True:
    print(menu)
    try:
        choice = int(input("Enter the the one of menu choices , please : "))
    except:
        print("value error !please enter numerical value")
    else:
        if choice == 1:
            cs.add_student()
        elif choice == 2:
            cs.remove_student()
        elif choice == 3:
            cs.edit_std()
        elif choice == 4:
            cs.show_students()
        elif choice == 5:
            cs.add_course()
        elif choice == 6:
            cs.add_course_student()
        elif choice == 7:
            cs.show_student_courses()
        elif choice == 8:
            cs.display_student()
        elif choice == 9:
            cs.show_courses()
        else:
            exit()


