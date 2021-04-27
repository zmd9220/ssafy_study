
# 산술 연산자

# print(3 + 5) # 8
# print(5 - 3) # 2
# print(100 * 5) # 500
# print(100 / 3) # 33.33336
# print(100 // 3) # 33 몫
# print(100 % 3) # 나머지
# print(2 ** 5) # 제곱

# # 비교 연산자 => 참/거짓을 반환
# print(5 == 5) # True
# print(5 == '3') # False
# print(3 != 5) # True
# print(3 >= 3) # True
# print(5 < 4) # False

# 미니 실습
# 아래 리스트의 원소 중에서 홀수만 찾아 그 값을 출력하시오.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    if i % 2 == 1:
        print(f '{i}은(는) 홀수입니다.')