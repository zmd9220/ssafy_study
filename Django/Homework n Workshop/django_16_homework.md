# django_16_homework





### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

``` 
URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.
- T - uri는 자원, 행위는 http method로 구분해서 표현합니다. 추가로 마지막은 representation(표현) 인데, json을 통한 데이터 응답을 함을 의미합니다.
HTTP Method는 GET과 POST 두 종류가 있다.
- F - GET, POST 외에도 PUT, DELETE 등 다양한 method가 존재합니다.
일반적으로 URI 마지막에 슬래시( / )는 포함하지 않는다.
- F - URI는 /를 기준으로 구분하기 때문에 반드시 /를 포함 해야합니다.
‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.
- T - 명시된 주소를 토대로 판단해볼 때 worldcup 관련 정보에서 월드컵 팀, 팀들 중에서 43822에 해당하는 팀 중에 선수나 스태프를 추가하는 기능이지 않을까 생각됩니다.
```



___



### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

``` 
- 200 - ok, 요청이 성공적으로 완료되었다는 의미
- 400 - bad request, 이 응답은 잘못된 문법으로 인하여 서버가 요청을 이해할 수 없음을 의미
- 401 - unauthorized, 이 응답은 "비인증(unauthenticated)"을 의미 - 사용자가 누구인지 알 수 없다.
- 403 - forbidden, 사용자가 여기에 접근할 권한이 없다는 의미
- 404 - not found, 사용자가 요청한 자원을 찾을 수 없다는 의미 - 주로 잘못된 url 접근으로 인한 에러
- 500 - internal server error, 서버가 처리 방법을 모르는 상황이 발생했다는 의미, 해당 문제에 대해 처리할 함수나 기능을 아직 서버가 구현해 놓지 않았을 때
```



___



### 3. 아래의 모델을 바탕으로 Serializer를 정의하려 한다. serializers.py 파일에 StudentSerializer를 작성하시오.

``` python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
```



___



### 4. Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

> https://www.django-rest-framework.org/

``` 
Serializers 는 django 모델에서 모델의 필드에 해당하는 부분을 자동으로 딕셔너리 화 하여, json 파일 형태로 변환해줍니다. 또 외부에서 들어온 데이터는 Serializers를 통해 내부의 언어 (장고는 python)에 맞는 key:value 자료구조 (python은 딕셔너리) 형태로 변환시켜줍니다.
```

