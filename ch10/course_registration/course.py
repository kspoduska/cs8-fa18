class Course:

    def __init__(self, number, name, instructor, date_and_time, credits):
        self.__number = number
        self.__name = name
        self.__instructor = instructor
        self.__date_and_time = date_and_time
        self.__prereqs = []
        self.__credits = credits
        self.__students = []    
    
    def __str__(self):
        return '{} {} taught by {} @ {} has {} students'.format(
            self.__number, self.__name, self.__instructor, self.__date_and_time,
            len(self.__students)
        )
        
    def enroll_student(self, student):
        self.__students.append(student)
        
    def drop_student(self, student):
        found_at = -1
        for i in range(len(self.__students)):
            if s == student:
                found_at = i
                break
        if found_at >= 0:
            del self.__students[i]
     
