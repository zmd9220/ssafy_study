# workshop
# 1. 무엇이 중복일까

# def duplicated_letters(word):
#     once = [] # 한번 들어온 값
#     dupl = [] # 중복 값
#     for ch in word: # 문자 하나씩 순회
#         if ch in once: # 문자가 한번이라도 나왔을 경우(중복)
#             dupl.append(ch)
#             once.remove(ch)
#         elif not ch in dupl: # 한번도 나오지 않고, 2번 이상 나온적도 없을 때
#             once.append(ch)
#     print(dupl)
#     return dupl 

# def duplicated_letters(word):
#     result = []

#     for char in word:
#         if word.count(char) > 1:
#             if char not in result:
#                 result.append(char)
#     return result

# duplicated_letters('apple') # => ['p']
# duplicated_letters('banana') # => ['a', 'n']

# # 2. 소대소대

# def low_and_up(word):
#     result = '' # 결과담을 문자열
#     for idx, ch in enumerate(word):
#         if idx % 2 == 0: # 0, 2, 4, 6 ...
#             result += ch.lower()
#         else: # 1, 3, 5, 7 ...
#             result += ch.upper()
#     print(result)    
#     return result

def low_and_up(word):
    result = ''

    for idx, char in enumerate(word):
        if idx % 2:
            result += char.upper()
        else:
            result += char.lower()
    return result


# low_and_up('apple') # => aPpLe
# low_and_up('banana') # => bAnAnA

# # 3. 숫자의 의미

# def lonely(ls):
#     isDupl = 100 # 연속 같은 값인지 확인할 값
#     result = [] # 결과 담을 리스트
#     for i in ls:
#         if i == isDupl: # 앞에 이어서 뒷값이 같으면 다른 값 나올때 까지 진행
#             continue
#         else: # 앞과 뒷값이 다르면 새롭게 추가하고 확인할 값 갱신
#             isDupl = i
#             result.append(i)
#     print(result)
#     return result

# lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
# lonely([4, 4, 4, 3, 3]) # => [4, 3]



# homework
# 1. Built-in 함수와 메서드 
# before_sorted = [5, 7, 8, 4, 3]
# before_sort = [5, 7, 8, 4, 3]
# after_sorted = sorted(before_sorted)
# after_sort = before_sort.sort()
# print(f'before_sorted = {before_sorted}\nafter_sorted = {after_sorted} ')
# print(f'before_sort = {before_sort}\nafter_sort = {after_sort} ')

# 2. .extend()와 .append()
sample = [1, 2, 3, 4, 5]
addon = [6, 7]
app = list(sample)
ext = list(sample)
app.append(addon)
ext.extend(addon)
print(app)
print(ext)
app.append([[8, 9]])
ext.extend([[8, 9]])
print(app)
print(ext)

# 3. 복사가 잘 된 건가?
# a = [1, 2, 3, 4, 5]
# b = a
# c = list(a) # 리스트 방식
# d = a[:] # slicing 방식

# a[2] = 5
# c[2] = 8000
# d[2] = 10000

# print(a)
# print(b)
# print(c)
# print(d)

# import copy
# a = [1, 2, 3, 4, 5]
# b = copy.deepcopy(a)