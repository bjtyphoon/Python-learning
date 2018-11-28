from Animal import Animal

class Dog(Animal):
    def talk(self):
        print('%s is  talking:666233' % self.name)
    def walk(self):
        print('%s is  walking' % self.name)
dog=Dog('jingba')
dog.talk()
dog.walk()

class Cat(Animal):
    def talk(self):
        print('%s is  talking:666233' % self.name)
    def walk(self):
        print('%s is  walking' % self.name)
cat=Cat('xuzhen')
cat.talk()
cat.walk()