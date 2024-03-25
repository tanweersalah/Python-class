# Inheritance

class Person:
    Planet = 'earth'

    def __init__(self, name, age,password):
        self.name = name
        self.__age = age
        self.username = name
        self.__password = password


    # Getter
    @property
    def age(self):
        return self.__age
    
    #Setter
    @age.setter
    def age(self, value):
        if self.age > 18 :
            self.__age = value
        else :
            print('You cannot modify your age!!!')

    @property
    def password(self):
        return self.__password
    
    def introduce_yourself(self):
        print(f'Hi, This is {self.name}')
    
    def print_age(self):
        print(f'I am {self.age} years old')


class Student(Person):
    
    def __init__(self, name,roll_number, student_class , age):
         
         super().__init__(name, age)
         
         self.roll_number = roll_number
         
         self.student_class = student_class
    
    def print_roll_number(self):
        print('Running')
        print(f'Roll Number : {self.roll_number}')

    def print_class(self):
        print(f'Class : {self.student_class}')

class Boy_student(Student):
    gender = 'male'

    def __init__(self):
        pass
        