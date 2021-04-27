# 1이 연속적으로 3번 이상 나오는지?
# nums = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1]

# def check(nums):
#     count = 0
#     for i in nums:
#         if i == 1:
#             count += 1
#             if count >= 3:
#                 return True
#         else:
#             count = 0
    
#     return False

# print(check(nums))


# apple =>
# n
# ascii 코드 이동
def foo(word, n):
    result = ''

    step = n % 26 # 30 => 4

    for char in word:
        code = ord(char)

        # 대문자
        if code <= 90:
            code += step
            if code > 90:
                code -= 26 # code %= 65
        # 소문자
        else:
            code += step
            if code > 122:
                code -= 26 # code %= 122

        result += chr(code)
    
    return result

print(foo('asdf', 4))   