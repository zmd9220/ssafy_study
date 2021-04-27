# from faker import Faker
# fake = Faker('ko_KR')
# Faker.seed(4321)
# print(fake.name()) 	# 1
# fake2 = Faker('ko_KR')
# print(fake2.name()) # 2



# fake = Faker('ko_KR')
# fake.seed_instance(4321)
# print(fake.name()) 	# 1
# fake2 = Faker('ko_KR')
# print(fake2.name()) # 2

# print(type(int))
# print(type(float))
# print(type(str))
# print(type(dict))
# print(type(bool))
# print(type(list))
# print(type(set))
# print(type(map))

# dic = {}
# dic.pop

# ls = []
# ls.pop


'''
1.
int
bool
dict
list
str
type(set)

2.
__init__ # 인스턴스가 초기화 될 때 실행
__del__ # 인스턴스가 소멸 될 때
__str__ # print => 출력결과
__repr__ # 인스턴스의 반환값을 결정

3.
dict.get 키값에 따라 value 반환 없으면 None, 다른 값도 지정가능

4. 
from fibo import fibo_recursion as recursion


workshop

1. 
로컬 파이썬 환경에 Faker라는 패키지 설치
터미널

2.
from faker import Faker		#1 faker 모듈에서 Faker class를 호출 
Faker가 class인지 아는법? type(Faker), 밑의 줄 생성자, 클래스 생성 규칙인 앞글자 대문자로 파악
fake = Faker()           	#2 Faker는 클래스, fake는 인스턴스이다.
fake.name()					#3 name()은 fake의 인스턴스 메소드이다. 그냥 메소드?
name()은 fake의 method

3. 
class Faker():
    def __init__(self, locale='en_US'):
        pass

4. 
seed 클래스메서드 - 생성하는 모든 인스턴스를 동일한 시드 값을 가지고 생성하고 싶을경우
seed_instance 특정 인스턴스에만 특정 시드값을 적용하고 싶을때

'''


import random

class ClassHelper:
    pass
    # 아래에 코드를 작성하시오.
    def __init__(self, name_list):
        self.name_list = name_list
        
    def pick(self, n):
        return random.sample(self.name_list, n)
    
    # def match_pair(self):
    #     change = []
    #     count = 0
    #     names = []
    #     while True:
    #         name = self.name_list.pop(random.choice(range(len(self.name_list) - 1))
    #         # print(name)
    #         # names.append(name)
    #         count += 1
    #         if len(self.name_list) > 3:
    #             if count == 2:
    #                 count = 0
    #                 change.append(names.pop())
    #         elif len(self.name_list) == 3:
    #             random.choice(self.name_list, 3)

                
                
            