# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.nr = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.nr = 1
    student2.name = "Olivia"
    student2.age = 21
    student2.nr  = 2
    student3.name = "Alex"
    student3.age = 20
    student3.nr = 3

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.nr} {student1.name}, {student1.age} years old')
    print(f'{student2.nr} {student2.name}, {student2.age} years old')
    print(f'{student3.nr} {student3.name}, {student3.age} years old')

if __name__ == "__main__":
    main()