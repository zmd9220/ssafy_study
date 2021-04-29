# django_17_homework





### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

``` 
JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야 한다.
- T - DRF에서 지원하는 기능을 통해 JSON 형식으로 데이터를 제공합니다.
DRF가 제공하는 기본 Form을 통해서만 여러 HTTP Method를 테스트 해볼 수 있다.
- F - Postman과 같은 외부 http method 전송 프로그램으로도 테스트 가능합니다.
api_view 데코데이터를 사용하지 않아도 HTTP Method에 대한 요청에 응답할 수 있다.
- F - DRF에서는 api 서버로서 응답을 할 때는 함수 작성시 api_view를 명시하도록 되어있으며 동시에 api_view 는 특정 http method 에 대한 요청 만 받을 수 있도록 검사하는 기능도 가지고 있으므로 반드시 적어줘야 합니다.
Serializers는 Queryset 객체를 JSON 포맷으로 변환 할 수 있는 python 데이터 타입으로 만들어준다.
- T - DRF 에서 제공하는 시리얼라이저는 해당 모델의 필드 값들을 적절한 JSON의 형태로 변경시켜줍니다. 동시에 특정 데이터를 받았을 경우에는 해당하는 언어에 맞춘 key:value 형태로 변경시켜줍니다. (장고 - python 이므로 딕셔너리 형태)
```



___



### 2. REST API 디자인 가이드

> EST API 디자인 설계 시 가장 중요한 항목을 2가지로 요약한다면, 정보의 자원을 표현해야 하는 __(a)__와
> 자원의 대한 행위를 표현하는__(b)__라고 할 수 있다. 빈칸 a, b에 들어갈 알맞은 답을 작성하시오.

``` 
a - URI
b - http methods
```



___



### 3. 아래에서 빈칸 a, b, c, d, e 에 들어갈 코드를 작성하시오.

> 해당 view함수는 유효성 검사를 통과 했을 경우 serializer 데이터와 http status code 201를 반환한다.

``` 
a - ['POST']
b - data=request.data
c - raise_exception=True
d - serializer.data
e - status=status.HTTP_201_CREATED
```



___

