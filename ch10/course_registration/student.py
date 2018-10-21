import random

class Student:

    def __init__(self, name):
        self.__id = random.randint(10000, 99999)
        self.__name = name
        self.__email = '{}@pitt.edu'.format(name.lower().replace(' ', '.'))
        self.__standing = 'Freshman'
        self.__credits = 0
        self.__gpa = 0.0
        self.__completed_courses = []
        self.__enrolled_courses = []       

    def set_credits(self, credits):
        self.__credits = credits
        if self.__credits < 32:
            self.__standing = 'Freshman'
        elif self.__credits < 64:
            self.__standing = 'Sophomore'
        elif self.__credits < 96:
            self.__standing = 'Junior'
        else:
            self.__standing = 'Senior'
            
    def enroll_in_course(self, course):
        self.__enrolled_courses.append(course)
        
    def __str__(self):
        return ('Id: {}, Name: {}, Email: {}, Standing: {}, '
            'Credits: {}, GPA: {}, Courses Completed: {}, '
            'Courses in Progress: {}').format(self.__id, self.__name,
            self.__email, self.__standing, self.__credits, self.__gpa,
            len(self.__completed_courses), len(self.__enrolled_courses)
        )
