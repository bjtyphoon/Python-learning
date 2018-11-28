import uuid
class Person(object):
    nationality='China'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._id=str(uuid.uuid1())
        
    # 成员方法/实例方法  
    def sayHello(self):
         print('Hello, i am %s from %s, i am %d years old.' % (self.name, self.nationality, self.age))
    
    # 私有方法
    
    def __sayHello(self):
        print('private method:__sayHello')
        print(self.name, self.age, self.__id, self.nationality)
        
    # 类方法
    @classmethod
    def Hi(cls):
        print(cls.nationality)
        
    # 静态方法
    @staticmethod
    def youga(a,b):
        print(a+b)
        
    # 属性方法
    @property
    def bj(self):
        return '%s:%d'%(self.name,self.age)
p=Person('xwx',27)

p.sayHello()
Person.sayHello(p)

Person.Hi()
p.Hi()

Person.youga(2,5)
p.youga(2,5)

print(Person.bj)
print(p.bj)