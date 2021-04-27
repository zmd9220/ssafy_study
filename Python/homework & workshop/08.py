# workshop 
# 1.

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Rectangle:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#         self.height = abs(self.p1.x - self.p2.x)
#         self.width = abs(self.p1.y - self.p2.y)
    
#     def get_area(self):
#         return self.height * self.width
    
#     def get_perimeter(self):
#         return (self.height + self.width) * 2

#     def is_square(self):
#         if self.width == self.height:
#             return True
#         else:
#             return False

# p1 = Point(1, 3)
# p2 = Point(3, 1)
# r1 = Rectangle(p1, p2)
# print(r1.get_area())
# print(r1.get_perimeter())
# print(r1.is_square())
# p3 = Point(3, 7)
# p4 = Point(6, 4)
# r2 = Rectangle(p3, p4)
# print(r2.get_area())
# print(r2.get_perimeter())
# print(r2.is_square())

# home work
# 1.

# class Circle:
#     pi = 3.14
#     x = 0
#     y = 0
#     r = 0

#     def __init__(self, r, x, y):
#         self.r = r
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.pi * self.r * self.r

#     def circumference(self):
#         return 2 * self.pi * self.r
    
#     def center(self):
#         return (self.x, self.y)

# cir = Circle(3, 2, 4)
# print(cir.area())
# print(cir.circumference())

# 2.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')
    
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        print(f'{self.name}! 달린다!')
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def fly(self):
        print(f'{self.name}! 푸드덕!') 

dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!