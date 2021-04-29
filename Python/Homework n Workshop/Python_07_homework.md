# Python_07_homework





### 1. Type Class

> Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는
> 클래스를 최소 5가지 이상 작성하시오.

``` python
print(type(int))
print(type(float))
print(type(str))
print(type(dict))
print(type(bool))
```





### 2. Magic Method
> 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

```python
__init__ # 생성자 - 객체 생성시 실행되어 init에 정의된 대로 실행됩니다.
__del__ # 소멸자 - 객체 소멸시 실행되어 del에 정의된 대로 실행됩니다.
__str__ # 객체가 print로 호출될 때 출력할 내용을 정의합니다.  print 사용시 정의된대로 출력됩니다.
__repr__ # 객체가 기본적으로 호출 될 때 객체가 무엇인지 정의할 내용을 지정합니다. - str은 문자열로 출력하여 객체를 문자화하여 설명한다면, repr은 객체 그 자체에 중점을 두고 설명합니다.
```





### 3. Instance Method

> .sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에
> 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소
> 3가지 이상 그 역할과 함께 작성하시오.

```python
.clear() # 모든 값을 제거하고 초기화 합니다.
.copy() # 얕은 복사를 진행합니다.
.pop() # 해당 인덱스나 key값에 맞춰 데이터를 꺼냅니다.
```





### 4. Module Import

>위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은 형태로
>함수를 실행 할 수 있도록 하는 import 문을 빈칸 (a), (b), (c)를 채워 넣어 완성하시오.

```python
from fibo import fibo_recursion as recursion
```


