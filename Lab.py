class Personnel:
    def __init__(self, id: int, fullname: str):
        self.__id = id
        self.__fullname = fullname

class Teacher(Personnel):
    def __init__(self, id: str, fullname: str):
        super().__init__(id, fullname)

class Student(Personnel):
    def __init__(self, id: str, fullname: str):
        super().__init__(id, fullname)
        self.__enroll_list = [] 
    
    def enroll(self, subject_add: Subject):
        
        if not isinstance(subject_add, Subject):
            return "Error"
        
        for enrollment in self.__enroll_list:
            if enrollment.get_subject() == subject_add:
                return "Already Enrolled"
        
        new_enrollment = Enroll(subject_add)
        self.__enroll_list.append(new_enrollment)
        return "Done"

    def drop(self, subject_drop: Subject):
        if not isinstance(subject_drop, Subject):
            return "Error"
            
        for enrollment in self.__enroll_list:
            if enrollment.get_subject() == subject_drop:
                self.__enroll_list.remove(enrollment)
                return "Done"
        return "Not Found"
        
    def get_enrolled_subjects(self):
        subjects = []
        for enrollment in self.__enroll_list:
            subjects.append(enrollment.get_subject())
        return subjects
    
    def assign_grade(self, subject: Subject, grade: str):
        for enrollment in self.__enroll_list:
            if enrollment.get_subject() == subject:
                enrollment.set_grade(grade)
                return "Done"
        return "Not Found"
    
    def get_gps(self):
        total_points = 0
        total_credits = 0
        
        for enrollment in self.__enroll_list:
            grade = enrollment.get_grade()
            if grade is not None:
                credit = enrollment.get_subject().get_credit()
                points = enrollment.get_points()
                
                total_points += (points * credit)
                total_credits += credit
        
        if total_credits == 0:
            return 0.0
            
        return total_points / total_credits
    
class Enroll:
    def __init__(self, subject: Subject, grade: str = None):
        self.__subject = subject
        self.__grade = grade
    
    def get_subject(self):
        return self.__subject
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade: str):
        self.__grade = grade
        
    def get_points(self):
        if self.__grade == "A":
            return 4
        elif self.__grade == "B":
            return 3
        elif self.__grade == "C":
            return 2
        elif self.__grade == "D":
            return 1
        elif self.__grade == "F":
            return 0
        else:
            return 0