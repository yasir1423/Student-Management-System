import json
import os
class Student:
    def __init__(self,roll,name,marks=None,grade=None):
        #__init__:to initialize a variable that can be used globally.
        self.roll=roll
        self.name=name
        self.marks=marks if marks is not None else{}
        self.grade=grade
    def calculate_grade(self):
        if not self.marks:
            self.grade="N/A"
            return
        avg=sum(self.marks.values())/len(self.marks)
        if avg>=90:
            self.grade="A"
        elif avg>=80:
            self.grade="B"
        elif avg>=70:
            self.grade="C"
        elif avg>=60:
            self.grade="D"
        elif avg>=50:
            self.grade="E"
        else:
            self.grade="F"
    def to_dictionary(self):
        return{"roll":self.roll,
               "name":self.name,
               "marks":self.marks,
               "grade":self.grade}
#Student Management System       
class StudentSystem:
    def __init__(self,filename="students.json"):
        self.filename=filename
        self.students=[]#List use square brackets and dictionary uses curly braces.
        self.load_data()
    #Loads student data from json
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as file:
                data=json.load(file)
                for s in data:
                    student=Student(roll=s["roll"],name=s["name"],marks=s["marks"],grade=s["grade"])
                    self.students.append(student)
    #Save students to json
    def save_students(self):
        with open(self.filename,"w") as f:
            json.dump([s.to_dictionary() for s in self.students],f,indent=4)
    #Add new students 
    def add_students(self,roll,name):
        for s in self.students:
            if s.roll==roll:
                print("Roll number already exist!!!")
                return
        new_student=Student(roll,name)
        self.students.append(new_student)
        self.save_students()
        print("Student added successfully!!!")
    #Remove student
    def remove_student(self,roll):
        for s in self.students:
            if s.roll==roll:
                self.students.remove(s)
                self.save_students()
                print("Student removed successfully!!!")
                return
        print("Student not found!!!")#
    #for search of students
    def search_student(self,keyword):
        for s in self.students:
            if s.roll==keyword or s.name.lower()==keyword.lower():
                print("Student found.")
                print(f"Roll No:{s.roll}")
                print(f"Name:{s.name}")
                print(f"Marks:{s.marks}")
                print(f"Grade:{s.grade}")
                return
        print("No student found!!!!")
    #Add or updates marks
    def add_marks(self,roll,subject,marks):
        for s in self.students:
            if s.roll==roll:
                s.marks[subject]=marks
                s.calculate_grade()
                self.save_students()
                print("Marks updated and Grade calculated successfully!!!!")
                return
        print("No student found!!!!")
    #Update student name
    def update_name(self,roll,new_name):
        for s in self.students:
            if s.roll==roll:
                s.name=new_name
                self.save_students()
                print("Student name updated!")
                return
        print("No student found!!!!")
    #Show all students
    def show_students(self):
        if not self.students:
            print("No students found!!!")
            return
        print("----All Students-----")
        for s in self.students:
            print(f"Roll No:{s.roll},Name:{s.name},Marks:{s.marks},Grade:{s.grade}")
#Main Menu
def main():
    system=StudentSystem()
    while True:
        print("===STUDENT MANAGEMENT SYSTEM===")
        print("1.Add Student.")
        print("2.Remove Student.")
        print("3.Search Student.")
        print("4.Add/Update marks.")
        print("5.Update Student name.")
        print("6.Show All Students.")
        print("7.Exit.")
        choice=input("Enter your choice(1-7):")
        if choice=="1":
            roll=input("Enter roll number:")
            name=input("Enter Name:")
            system.add_students(roll,name)
        elif choice=="2":
            roll=input("Enter roll number to remove:")
            system.remove_student(roll)
        elif choice=="3":
            keyword=input("Enter roll number or name to search:")
            system.search_student(keyword)
        elif choice=="4":
            roll=input("Enter roll number:")
            subject=input("Enter subject:")
            marks=int(input("Enter marks:"))
            system.add_marks(roll,subject,marks)
        elif choice=="5":
            roll=input("Enter roll number:")
            name=input("Enter new name:")
            system.update_name(roll,name)
        elif choice=="6":
            system.show_students()
        elif choice=="7":
            print("Exiting the program......")
            break
        else:
            print("Invalid choice!!!!")
#Run the main program
main()


            






