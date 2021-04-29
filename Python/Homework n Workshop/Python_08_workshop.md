# Python_08_workshop





### 1. 도형 만들기

> 아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을
> 표현하시오.

``` python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.height = abs(self.p1.x - self.p2.x) # 가로길이
        self.width = abs(self.p1.y - self.p2.y) # 세로길이
    
    def get_area(self): # 넓이
        return self.height * self.width
    
    def get_perimeter(self): # 둘레
        return (self.height + self.width) * 2

    def is_square(self): # 정사각형 여부
        if self.width == self.height:
            return True
        else:
            return False

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

```


