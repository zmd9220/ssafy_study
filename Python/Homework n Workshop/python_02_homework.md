# python_02_homework



#### 1. Mutable & Immutable 

- mutable - list, set, dictionary
- immutable - string, tuple, range



#### 2. 홀수만 담기

```python
sample_list = list(range(1, 51))
print(sample_list[::2])
```



#### 3. Dictionary 만들기

```python
students = {
    '홍길동' : 21,
    '김철수' : 22,
    '유재석' : 23, # trailing comma
}
print(students, type(students))
```



#### 4. 반복문으로 네모 출력

```python
n = 5
m = 9
for i in range(m):
    print('*' * n)
```



#### 5. 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```



#### 6. 평균 구하기

```python
score = [80, 89, 99, 83]
avg = 0
for i in score:
    avg += i
print(avg / len(score))
```

