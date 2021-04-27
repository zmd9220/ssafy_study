# Python_06_workshop



### 1. 무엇이 중복일까

> 문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는
> duplicated_letters 함수를 작성하시오.

``` python
def duplicated_letters(word):
    once = [] # 한번 들어온 값
    dupl = [] # 중복 값
    for ch in word: # 문자 하나씩 순회
        if ch in once: # 문자가 한번이라도 나왔을 경우(중복)
            dupl.append(ch)
            once.remove(ch)
        elif not ch in dupl: # 한번도 나오지 않고, 2번 이상 나온적도 없을 때
            once.append(ch)
    print(dupl)
    return dupl 

duplicated_letters('apple') # => ['p']
duplicated_letters('banana') # => ['a', 'n']
```



### 2. 소대소대
> 문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여
> 반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만
> 구성된다.

```python
def low_and_up(word):
    result = '' # 결과담을 문자열
    for idx, ch in enumerate(word):
        if idx % 2 == 0: # 0, 2, 4, 6 ...
            result += ch.lower()
        else: # 1, 3, 5, 7 ...
            result += ch.upper()
    print(result)    
    return result
            
low_and_up('apple') # => aPpLe
low_and_up('banana') # => bAnAnA
```



### 3. 숫자의 의미

> 정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남
> 기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담
> 긴 list의 요소들은 기존의 순서를 유지해야 한다.

```python
def lonely(ls):
    isDupl = 100 # 연속 같은 값인지 확인할 값
    result = [] # 결과 담을 리스트
    for i in ls:
        if i == isDupl: # 앞에 이어서 뒷값이 같으면 다른 값 나올때 까지 진행
            continue
        else: # 앞과 뒷값이 다르면 새롭게 추가하고 확인할 값 갱신
            isDupl = i
            result.append(i)
    print(result)
    return result

lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]
```



