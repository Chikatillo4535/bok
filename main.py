'''class Human:
    height=170

class Student(Human):
    satiety = 0

class Worker(Human):
    satiety = 100

class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(f"height={self.height}")
        print(f"satiety={self.satiety}")
        print(f"age={self.age}")

class Hello_world:
    hello="Hello"
    _hello="_Hello"
    __hello="__Hello"
    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
    hello = Hello_world()
    hello.printer()



nick = Child()


nick = Student()
ann = Worker()
print(nick.satiety)
print(ann.satiety)'''
class Tree:
    durability=100
    age = 100
    beautiful = 100

class chair(Tree):
    beautiful=100

class table(chair):
    megapixel=100

    def __init__(self):
        print(f"megapixel={self.megapixel}")
        print(f"beautiful={self.beautiful}")
        print(f"durability={self.durability}")


