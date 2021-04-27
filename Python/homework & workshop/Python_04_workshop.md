# Python_04_workshop

### 1. 숫자의 의미

> 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인
> 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하
> 그리고 97이상 122이하의 정수로만 구성되어 있다.

``` python
# ord : str => ascii code
# chr : 반대 동작

def get_secret_word(ls):
    result = ''
    for i in ls:
        result += chr(i)
    print(result)

get_secret_word([83, 115, 65, 102, 89]) # => SsAfY
```



### 2. 내 이름은 몇일까?
> 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는
> get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

```python
def get_secret_number(ls):
    result = 0
    for i in ls:
        result += ord(i)
    print(result)
get_secret_number('tom') # => 336
```



### 3. 강한 이름

> 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하
> 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```python
def get_strong_word(st1, st2):
    result1, result2 = 0, 0
    for i in st1:
        result1 += ord(i)
    for i in st2:
        result2 += ord(i)
    if result1 > result2:
        print(st1)
    else:
        print(st2)
        
get_strong_word('z', 'a') #=> 'z' 
get_strong_word('tom', 'john') #=> 'john' 
```


