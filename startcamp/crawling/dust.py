import requests

key = 'RVXAjvWKDCBHc%2FEHlbCz6uot6m3ULiYotIfgV%2BKXQe2X56eSEq3LXbUmLffYRilFtvhZlVBTZ3M%2B7C6jvKY5vA%3D%3D'

# url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?serviceKey={key}&returnType=xml&numOfRows=100&pageNo=1&searchDate=2020-11-14&InformCode=PM10'

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=RVXAjvWKDCBHc%2FEHlbCz6uot6m3ULiYotIfgV%2BKXQe2X56eSEq3LXbUmLffYRilFtvhZlVBTZ3M%2B7C6jvKY5vA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%8C%80%EC%A0%84&ver=1.0'


json_data = requests.get(url).json()

# ctrl d 같은 변수명 이름 바꿀때 사용
# alt 누르고 클릭, 여러 줄 동시 작성 가능

# sidoName의 미세먼지 농도는 pm10value

print(json_data['response']['body']['items'][0]['sidoName'] + '의 미세먼지 농도는 ' + json_data['response']['body']['items'][0]['pm10Value'] + ' 입니다.')
print(json_data['response']['body']['items'][1]['stationName'] + '의 미세먼지 농도는 ' + json_data['response']['body']['items'][0]['pm10Value'] + ' 입니다.')

# pylint제거?
# Ctrl + Shift + P
# lint
# Python: Enable Linting => off
# Python: Select Linter => Disable linting