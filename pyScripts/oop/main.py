from student import Student

student1 = Student("Jim", "Business", 3.7, False)
student2 = Student("Pam", "Arts", 2.1, True)

if student1.on_honor_roll():
    print('This student has honor')
else:
    print('This student does not have honor')
