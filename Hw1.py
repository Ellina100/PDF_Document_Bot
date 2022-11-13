'''from abc import ABC

class Area(ABC):
    def area(self):
        pass
class SquareArea(Area):
    def __init__(self,a):
        self.a = a
    def area(self):
        return self.a**2

class RectangleArea(Area):
    def __init__(self,b,a):
        self.b = b
        self.a = a
    def area(self):
        return self.a*self.b'''


class TriangleArea(Area):
    def __init__(self,z):
        self.z = z
        self.n = n
    def area(self):
        return self.z*self.z/2

rectangle = RectangleArea(20,10)
print(rectangle.area())


class Counter:
    def __init__(self,b):
        self.__b = b

    def getCounter(self):
        return self.__b

    def increment(self):
        self.__b+=1

    def decrement(self):
        if self.__b <=0:
            print("Ошибка")
        else:
            self.__b-=1



counter = Counter(50)
for x in range(1,52):
    counter.decrement()
    print(counter.getCounter())

