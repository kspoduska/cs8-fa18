import course
import student

def build_students():
    name = input('Type a student name: ')
    while name != 'QUIT':
       s = student.Student(name)
       credits = int(input('Enter credits: '))
       s.set_credits(credits)
       print(s)
       name = input('Enter another student: ')


def build_course():       
    number = input('Course Number: ')
    name = input('Course Name: ')
    instructor = input('Instructor: ')
    date_and_time = input('Date/Time: ')
    credits = int(input('Credits: '))
    return course.Course(
        number, name, instructor, date_and_time, credits
    )


def main():
    action = input('Enter courses...')
    courses = []
    while action != 'DONE':
       c = build_course()       
       courses.append(c)
       action = input('Type DONE to exit loop...')
       
    for c in courses:
        print(c)
       
    
    
main()
