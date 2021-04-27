from flask import Flask, request
from pprint import pprint
import requests
import bs4
app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world!'

# 텔리그램이 여기에 알려줄거임
@app.route('/1592437514:AAFr81qI5QHpHKW0KYT39OIDELMqSGwNPY0', methods=['POST'])
def telegram():
    pprint(request.get_json())

    from_telegram = request.get_json()

    # TODO: id , text 값을 변수에 할당하고, 출력하시오
    chat_id = from_telegram['message']['from']['id']
    text = from_telegram['message']['text']

    tele_token = '1592437514:AAFr81qI5QHpHKW0KYT39OIDELMqSGwNPY0'
    tele_base_url = f'https://api.telegram.org/bot{tele_token}'

    dust_key = 'RVXAjvWKDCBHc%2FEHlbCz6uot6m3ULiYotIfgV%2BKXQe2X56eSEq3LXbUmLffYRilFtvhZlVBTZ3M%2B7C6jvKY5vA%3D%3D'
    
    # 거울처럼 받아온 텍스트를 다시 돌려주기 
    # sendMessage 메서드를 이용해서 아래 chat_id에게 text를 보내시오.
    # print (f'id는 {chat_id}, 메세지는 {text}')
    # api_url = f'{tele_base_url}/sendMessage?chat_id={chat_id}&text={text}'
    # requests.get(api_url)

    # 만약에 text가 '미세먼지'라면, 미세먼지 API를 호출해서 그 값을 보낸다.
    if text == '미세먼지':
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={dust_key}&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%8C%80%EC%A0%84&ver=1.0'
        dust_data = requests.get(dust_url).json()
        sidoName = dust_data['response']['body']['items'][0]['sidoName']
        pm10Value = dust_data['response']['body']['items'][0]['pm10Value']
        text = f'{sidoName}의 미세먼지 농도는 {pm10Value} 입니다.'       
    elif text == '코스피':
        kospi_url = 'https://finance.naver.com/sise/'
        selector = '#KOSPI_now'
        response = requests.get(kospi_url).text
        soup = bs4.BeautifulSoup(response, 'html.parser')
        kospi = soup.select_one(selector).text
        text = f'현재의 코스피 지수는 {kospi}입니다.'

    # 그렇지 않다면, 사용자가 보낸 text를 보낸다.
    
    api_url = f'{tele_base_url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(api_url)

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)