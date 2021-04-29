# django_01_homework





### 1. 한국 시간 나타내기

> 1-1. django 서버를 실행하고 첫 페이지에 접속했을 때 터미널에 출력된 서버 시간이 현재
> 한국 시간과 다른 시간으로 출력된다. 이를 한국 시간으로 바꾸려면 settings.py에 어떤 변
> 수 그리고 어떤 값을 할당해야 하는지 작성하시오.
> 1-2. 추가로 settings.py에 "이 변수"가 False인 상태로 1-1번 변수를 설정하는 것은 error라
> 고 한다. "이 변수"는 무엇인가?

``` python
# TIME_ZONE = 'Asia/Seoul'
# USE_TZ = False
```





### 2.  경로 설정하기

> 다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때 실
> 행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해
> 빈칸 __(a)__에 추가되어야 할 코드를 작성하시오.

``` python
from pages import views
path('ssafy/', views.ssafy)
```





### 3.  Django Template Language

> 아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오.
> https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

``` python
# 1. for menu in menus

# 2. forloop.counter0	

# 3. empty 
 
# 4. a- if b- else

# 5. a- length b- title

# 6. Y년 m월 d일 (D) A h:i
```





### 4.  Form tag with Django

> 다음은 form tag 에 관한 문제이다. 올바른 답을 작성하시오.

``` python
# 1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.
'''
action은 제출을 했을 때, 해당하는 페이지로 값을 가지고 넘겨주는 역할을 합니다.
'''
# 2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.
'''
name으로 들어가는 title, content, my-site 3개를 가집니다.
'''
# 3) input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit
# 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.
'''
/create/?title=안녕하세요?&content=반갑습니다&my-site=파이팅
'''
```

