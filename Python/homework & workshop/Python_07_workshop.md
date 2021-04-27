# Python_07_workshop





### 1. pip

> 아래 명령어는 (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성 하시오.

``` bash
$ pip install faker
```

(1) pip 파이썬 패키지 관리자를 통해 faker라는 라이브러리(패키지)를 설치하라는 명령어 입니다.

(2) 프로그램 코드 상이 아닌, 터미널을 통해 설치합니다.



### 2. Basic Usages
> Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다.
> 임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.

```python
from faker import Faker		#1 faker패키지에서 Faker모듈을 사용 하기 위한 코드이다.
fake = Faker()           	#2 Faker는 클래스, fake는 인스턴스이다.
fake.name()					#3 name()은 fake의 인스턴스 메소드이다.
```





### 3.  Localization

> 직접 해당하는 기능을 구현한다고 하였을 때, 빈칸 (a), (b), (c)에 들어갈 코드로 적절한
> 것을 작성하시오. (힌트: 생성자 메서드와 함수의 개념)

```python
class Faker():
    def __init__(self, locale='en_US'):
        pass
```





### 4. Seeding the Generator

>아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고, seed()는
>어떤 종류의 메서드인지 작성하시오.

```python
fake = Faker('ko_KR')
Faker.seed(4321)
print(fake.name()) 	# 1
fake2 = Faker('ko_KR')
print(fake2.name()) # 2
```

- 결과값 - 이도윤 이지후
- 일단 실행시 Faker라는 클래스 자체에 접근하며, 4321이라는 인자를 넣는 것을 보아 class 메소드 임을 알 수 있습니다. 또 시드 지정 후 4321번 시드 결과 값인 이도윤이 고정 되고, 그 다음 시드인 이지후가 나오는 것을 보아, 시드 값을 통해 처음에 나올 이름명을 고르고 다음 이름 또한 순서대로 생성하게 할 수 있습니다.


> 아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고,
> seed_instance()는 어떤 종류의 메서드인지 작성하시오.

```python
fake = Faker('ko_KR')
fake.seed_instance(4321)
print(fake.name()) 	# 1
fake2 = Faker('ko_KR')
print(fake2.name()) # 2
```

- 결과값 - 이도윤 김광수
- 실행시 fake에 접근하여 실행하는 것을 보아 인스턴스 메소드임을 알 수 있습니다. fake변수에는 시드를 4321로 잡아 결과값이 이도윤으로 시행되고, fake2는 다른 인스턴스이기 때문에 fake의 시드 영향이 없이 기본 시드로 김광수라는 이름을 호출했습니다.

> seed()와 seed_instance()는 각각 어떠한 용도로 쓰일 수 있는지 작성하시오.

- seed는 해당 클래스의 시드 값을 변경하기 때문에 모든 인스턴스의 시드에 영향을 줍니다. 그러므로 인스턴스와 상관 없이 해당 시드로  부터 생성되는 난수 이름을 사용할 때 유용할 것 같습니다.
- seed_instance는 시행된 해당 인스턴스의 시드만 바꾸므로 해당하는 인스턴스를 가지고 원하는 시드부터 순서대로 난수 이름을 추출할때 유용할 것 같습니다.

