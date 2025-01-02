#parent class and child

# class parentclass():
#     def mathod_in_class(self) :
#         print('This is method of parent class.')

# class derivedclass(parentclass):
#     def mehtod_in_class(self):
#         print('this is method of child or derived class')


class Person() :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'Name is {self.name}, Age:{self.age}')

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def get_info(self):
        super().get_info()
        print(f'Grade is {self.grade}')

s1= Student(name="BKASH",age=27,grade=18)
s1.get_info()