# Python_03_homework



### 1. Built-in 함수

> Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

``` python
abs() # 절대값, 
print() # 출력 함수
range() # 범위 설정
min() # 최소값 
max() # 최대값
```



### 2. 정중앙 문자
> 문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를
> 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

```python
def get_middle_char(st):
    result = ''
    mid = len(st) // 2
    if not len(st) % 2:
        result += st[mid-1]
    result += st[mid]
    return result
print(get_middle_char('ssafy')) # => a
print(get_middle_char('coding')) # => di
```



### 3. 위치 인자와 키워드 인자

> 다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는
> 코드를 고르시오.

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('허준')
ssafy(location='대전', name='철수')
ssafy('영희', location='광주')
ssafy(name='길동', '구미') 

# 4
File "test.py", line 53
    ssafy(name='길동', '구미') # 위치 인자는 키워드 인자 앞에 있어야 함.
                         ^
SyntaxError: positional argument follows keyword argument
```



### 4. 나의 반환값은

>다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
print(result) 
# None 왜냐면 return에 아무런 값을 지정하지 않았기 때문에 default인 None이 반환된다. 
```



### 5. 가변 인자 리스트

>가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정
>수들의 평균 값을 반환하는 my_avg 함수를 작성하시오

```python
def my_avg(*ls):
    result = 0
    for i in ls:
        result += i
    print(result / len(ls))
my_avg(77, 83, 95, 80, 70) # => 81.0
```

