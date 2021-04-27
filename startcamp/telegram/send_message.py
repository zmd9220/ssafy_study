import requests

# text = input()
# print('print', text)


# ctrl d 같은 변수명 이름 바꿀때 사용
# alt 누르고 클릭, 여러 줄 동시 작성 가능

key = 'RVXAjvWKDCBHc%2FEHlbCz6uot6m3ULiYotIfgV%2BKXQe2X56eSEq3LXbUmLffYRilFtvhZlVBTZ3M%2B7C6jvKY5vA%3D%3D'

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=RVXAjvWKDCBHc%2FEHlbCz6uot6m3ULiYotIfgV%2BKXQe2X56eSEq3LXbUmLffYRilFtvhZlVBTZ3M%2B7C6jvKY5vA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%8C%80%EC%A0%84&ver=1.0'

json_data = requests.get(url).json()

# sidoName의 미세먼지 농도는 pm10value - 미세먼지 정보
sidoName = json_data['response']['body']['items'][0]['sidoName']
pm10Value = json_data['response']['body']['items'][0]['pm10Value']
 
# 미세먼지 정보가 담긴 리스트
text = f'{sidoName}의 미세먼지 농도는 {pm10Value}입니다.'

# 메세지를 보내는 부분
token = '1592437514:AAFr81qI5QHpHKW0KYT39OIDELMqSGwNPY0'
chat_id =  '1501527005'
base_url = f'https://api.telegram.org/bot{token}'

api_url = f'{base_url}/sendMessage?chat_id={chat_id}&text={text}'

response = requests.get(api_url).json()

print(response)

