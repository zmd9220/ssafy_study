# Dictionary 선언

my_home = {
    'location' : 'daejeon',
    'class' : '02',  
    # trailing comma - 위에서 아래로 내려갈 때만 사용함
    # 비었는데도 , 찍는 이유 보통 내용 추가할 때 바로 enter 치고 하기 때문에 미리 넣어두고
    # 'name' : '홍길동'  
}

# 원소 접근 => dict['key']
print(my_home['location'])
print(my_home['class'])

# 원소 접근 => dict.get('key')
print(my_home.get('location'))
print(my_home.get('class'))


# 원소 변경
my_home['location'] = 'Daejeon'
print(my_home['location'])

# 미니 실습 1
# 1-1 자신의 이름, 나이, 인사말로 구성된 my_info dictionary를 만드시오.
# (name, age, msg)

my_info = {
    'name': '안병진',
    'age': '29',
    'msg': {
        'one': '안녕하세요. 잘 부탁드립니다.',
        'two': 'ssafy 5기 화이팅',
    },
    'hobbies': [
        'game',
        'movie',
    ],

}

# 1-2 my_info에서 나이 값을 출력하시오.

print(my_info['age'])

print(my_info['msg']['one'])

print(my_info['hobbies'][1])