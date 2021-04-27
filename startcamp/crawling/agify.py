import requests

url = 'https://api.agify.io/?name=eric'

# .json() => JSON 문서를 바로 python dict 형태로 변환
response = requests.get(url).json()

print(response)
print(type(response))

name = response['name']
age = response['age']


# print(f'{response['name']}의 나이는 {response['age']}입니다.') 파이썬은 이렇게 쓰면 안됨 
print(f'{name}의 나이는 {age}입니다.')



