class Student:
    def __init__(self, name, age, grades):
        
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        
        if self.grades:  # Check if grades list is not empty
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0

student1 = Student("Alice", 20, [85, 90, 78, 92])
student2 = Student("Bob", 19, [88, 74, 95, 100])

student1.display_details()
print(f"Average Grade: {student1.calculate_average_grade():.2f}\n")

student2.display_details()
print(f"Average Grade: {student2.calculate_average_grade():.2f}")
