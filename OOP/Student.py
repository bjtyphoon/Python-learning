from Person import Person

class Student(Person):
    def __init__(self, name, age, level):
        super(Student, self).__init__(name, age)
        self.level=level
    
    def bj (self):
        print('%s is hhhhhhhhhh' % self.name)
       
S1=Student('xxx',27,1221)

S1.hello()
S1.bj()