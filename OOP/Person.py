import uuid

class Person(object):
    area='China'
    
    def __init__(self,name,age):
         self.name=name
         self.age=age
         self.__id=str(uuid.uuid1())
         
    def hello(self):
        print('Hi,i am %s,from %s,my name is %s' %(self.name,self.area,self.__id))
        
    def get_and_print_id(self):
        print(self.__id)
        return self.__id
        
    
        
def test():
    mazc=Person('mazc',24)
    xb=Person('xb',27)
    nql=Person('nql',28)

    print(Person.area,mazc.area,xb.area,nql.area)
    xb.area='jiangsu'
    print(Person.area,mazc.area,xb.area,nql.area)
    Person.area='yuzhousu'
    print(Person.area,mazc.area,xb.area,nql.area)   

    
    print(mazc.name,xb.name,nql.name)
    xb.name='xwx'
    print(mazc.name,xb.name,nql.name)


    mazc.hello()
    xb.hello()
    nql.hello()

    mazc_id=mazc.get_and_print_id()
    xb_id=xb.get_and_print_id()
    nql_id=nql.get_and_print_id()
    print(mazc._Person__id,xb._Person__id,nql._Person__id)
        

if __name__=="__main__":
    test()
