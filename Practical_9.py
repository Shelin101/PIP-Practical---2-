# class student,exam,result
class Student:
    def __init__(self, rollno, name, division):
        self.name = name
        self.rollno = rollno
        self.divison = division

    def getStudent(self):
        print("Name: ", self.name)
        print("Enrollment No: ", self.rollno)
        print("Division: ", self.divison)


class Exam(Student):
    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


class Result(Exam):
    def getTotalMarks(self):
        Total_Marks = sum(self.getMarks())
        return Total_Marks


object = Result(101, "Shelin Vankawala", 2)
print("\nStudent Information: ")
object.getStudent()
object.setMarks([55, 69, 83, 71, 70, 91])
print("Total Marks:", object.getTotalMarks())
