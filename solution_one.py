# import json
import json
import matplotlib.pyplot as plt

json_file_path = "student.json"

try:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        
except FileNotFoundError:
    print("Check the file path")

def grading_system(grades):
    if grades >= 90  and  grades <= 100:
        return("A")
    elif grades >= 87 and grades <= 89:
        return("A-")
    elif grades >= 84 and grades <= 86:
        return("B+")
    elif grades >= 80 and grades <= 83:
        return("B")
    elif grades >= 77 and grades <= 79:
        return("B-")
    elif grades >= 74 and grades <= 76:
        return("C+")
    elif grades >= 70 and grades <= 73:
        return("C")
    elif grades >= 67 and grades <= 69:
        return("C-")
    elif grades >= 64 and grades <= 66:
        return("D+")
    elif grades >= 62 and grades <= 63:
        return("D")
    elif grades >= 60 and grades <= 61:
        return("D-")
    else:
        return("F")


def student_data():
    try:
        num_students = int(input("How many students do you want to add: \n"))

        for i in range(num_students):
            while True:
                student_name = input("Enter student name: \n")

                if student_name == "":
                    print("Student name cannot be empty!!!")
                    continue  
                else:
                    try:
                        student_id = float(input("Enter student id: "))
                        if student_id == "":
                            print("Student ID cannot be empty!!!")
                            break
                        else:
                            courses = {}
                            graded_courses = {}
                            for i in range(5):
                                course = input("Enter course code: \n")
                                grade = int(input("Enter course grade: \n"))

                                courses[course] = grade
                                graded_courses[course] = grading_system(grade)
                            
                            data["students"].append({
                                "id": len(data["students"]) + 1,
                                "student_name": student_name,
                                "student_id": student_id,
                                "courses": courses,
                                "graded_courses": graded_courses
                            })

                            with open(json_file_path, 'w') as file: 
                                json.dump(data, file)
                            
                            break
                        
                    except ValueError:
                        print("Student Id must be a number!!!")
                        break
    except ValueError:
        print('Number of students must be an integer')

def report_card():
    student_name = input("Enter student's name: \n")
    found = False
    
    for student in data["students"]:
        if student["student_name"].lower() == student_name.lower():
            print("Student Name:", student["student_name"])
            print("Student ID:", student["student_id"])
            print("Courses:")
            course_labels = []
            grades = []
            for course, grade in student["courses"].items():
                print(f"{course}: {grade} ({student['graded_courses'][course]})")
                course_labels.append(course)
                grades.append(grade)
            found = True
            break
    
    if not found:
        print("Student not found!")
        return
    
    # Plotting the grades using a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(course_labels, grades, color='skyblue')
    plt.xlabel('Courses')
    plt.ylabel('Grades')
    plt.title(f'Grades for {student_name}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def decision_block():
    decision = input("Do you want a Report card (R) or Add Student Data (S)?\n")

    if decision.lower() == 's':
        student_data()
    elif decision.lower() == 'r':
        report_card()
    else:
        print("Your decision must be either (R) for Report Card or (S) for Adding a student")

decision_block()     

