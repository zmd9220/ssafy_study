import requests
import bs4

# 내가 원하는 정보가 있는 주소
url = 'https://finance.naver.com/sise/'
selector = '#KOSPI_now'

# requests 모듈을 통해 주소로 요청을 보내고 받아온 문서
response = requests.get(url).text
# print(response)

# 문서를 검색할 수 있게 만들어 주는 작업
soup = bs4.BeautifulSoup(response, 'html.parser')

# Selector를 통해 원하는 값에 접근
kospi = soup.select_one(selector).text

print(f'현재의 코스피 지수는 {kospi}입니다.')

# 환율 코드 짜보기?
# https://finance.naver.com/marketindex/