# Python_06_homework





### 1. Built-in 함수와 메서드 

> sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

``` python
before_sorted = [5, 7, 8, 4, 3]
before_sort = [5, 7, 8, 4, 3]
after_sorted = sorted(before_sorted)
after_sort = before_sort.sort()
print(f'sorted 전 = {before_sorted} \n sorted 후 = {after_sorted} ')
print(f'sort 전 = {before_sort} \n sort 후 = {after_sort} ')

# 결과값
before_sorted = [5, 7, 8, 4, 3]
safter_sorted = [3, 4, 5, 7, 8]
before_sort = [3, 4, 5, 7, 8]
after_sort = None

sorted의 경우 before_sorted에는 처음 입력 값 그대로 남아 있으며 after_sorted에 정렬된 결과 값이 있는 것에서 보듯, 함수가 실행되면 정렬된 결과본을 새롭게 만들어서 반환해주는 것을 알 수 있습니다.
반면 sort의 경우 before_sort의 값이 정렬되어 있고 after_sort에는 None이 출력되는 것을 통해, 함수가 실행되면 원본의 값을 정렬하고 반환 값이 따로 없어 None을 반환하는 것을 알 수 있습니다.
```





### 2. .extend()와 .append()
> .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
sample = [1, 2, 3, 4, 5]
addon = [6, 7]
app = list(sample)
ext = list(sample)
app.append(addon)
ext.extend(addon)
print(app)
print(ext)

# 결과 값
[1, 2, 3, 4, 5, [6, 7]]
[1, 2, 3, 4, 5, 6, 7]
append의 경우 리스트 안에 [6, 7]이 그대로 들어 오듯, 해당하는 함수에 들어온 인자 그대로 리스트에 집어 넣습니다. 
extend의 경우 현재 받은 인자 기준으로 나눌 수 있는 가장 마지막 iterable 기준으로 값을 집어 넣습니다. 방금과 같은 경우 [6, 7]의 리스트 였으므로 6, 7로 나눠서 값을 집어 넣습니다.

app.append([[8, 9]])
ext.extend([[8, 9]])
print(app)
print(ext)

# 결과 값
[1, 2, 3, 4, 5, [6, 7], [[8, 9]]]
[1, 2, 3, 4, 5, 6, 7, [8, 9]]

마찬가지로 리스트에 리스트를 감싸서 진행해도 append의 경우 [[8, 9]] 그대로 집어넣는 반면, extend의 경우 []안에 있는 [8, 9]를 하나의 단위로 보고 [8, 9]로 집어 넣습니다.
```





### 3. 복사가 잘 된 건가?

> 아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지
> 여부를 판단하고 그 이유를 작성하시오.

```python
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)

# 결과 값
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]

파이썬의 경우 기본적으로 리스트와 같은 자료형은 b = a 와 같이 할당하게 되면 b에 a의 값을 새롭게 복사하는 것이 아니라 a 데이터 공간의 시작 주소를 b에 할당하게 됩니다. 그래서 a와 b가 같은 데이터 공간을 공유하게 됩니다.
따라서 아예 다르게 사용하고싶다면 list()나 slicing을 통하여 아예 새로운 리스트를 생성하게끔 유도해야 합니다.

a = [1, 2, 3, 4, 5]
b = a
c = list(a) # 리스트 방식
d = a[:] # slicing 방식

a[2] = 5
c[2] = 8000
d[2] = 10000

print(a)
print(b)
print(c)
print(d)

# 결과 값
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]
[1, 2, 8000, 4, 5]
[1, 2, 10000, 4, 5]

이와 같이 c와 d는 다른 값을 가지게 됨을 알 수 있습니다. 다만 이와 같은 복사의 경우 내부에 리스트와 같은 mutable 자료가 존재할 경우, 내부의 mutable 자료는 새롭게 복사되어 생성되진 않아, 변수 내부의 mutable 자료 값의 변동은 모든 변수에 영향을 미칩니다. 이를 얕은 복사(shallow copy)라고 합니다.

1차원 배열상에서 이를 해결하려면 깊은 복사(deep copy)를 통해서 내부의 객체까지도 완벽히 복사해서 새로운 객체로 만들어야 합니다.
import copy
a = [1, 2, 3, 4, 5]
b = copy.deepcopy(a)

2차원 배열 이후의 복사는 현재 파이썬 기본 함수로는 어렵고, 반복문을 통해서 만들어야 할 것 같습니다. 
```
