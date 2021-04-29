# django_15_homework





### 1. MTV

> Django는 MTV로 이루어진 Web Framework다. MTV가 무엇의 약자이며 Django에서 각각 어떤 역할을 하고 있는지 작성하시오.

``` 
장고는 기존의 MVC 패턴을 따르는 웹 프레임워크입니다. 다만 장고 스스로가 정의하기에 좀 더 적합하다고 느끼는 이름을 명명한 것이 MTV 입니다. MTV는 Model, Template, View의 약자이며 장고를 구성하는 가장 중요한 3가지 입니다.
Model 은 주로 장고가 db로 연동하여 처리하는 부분을 담당합니다. database에 반영할 데이터 테이블 모델(ERD) 생성과 실제 데이터 영역을 담당합니다. - 실제 데이터
Template 는 사용자에게 실제로 보여주는 화면을 담당합니다. 사용자에 맞게 적절히 처리된 결과물에 맞추어 html 문서를 통해 결과물을 출력해줍니다. - 화면
View 는 사용자와 서버 사이에서 실제 요청에 따라 적절히 데이터를 가공, 처리 한 후 template를 통해 결과를 보여줄 수 있도록 지시하는 중간관리자의 역할을 담당합니다. - 로직
```



___



### 2. 404 Page not found

> 기본적으로 ‘/ ’ 페이지에 접속하게 되면 아래 사진처럼 Page not found 에러가 발생한다. ‘/ ’ 페이지에 접속했을 때 index.html를 렌더링 하고자 한다. 아래 빈칸에 알맞은 코드를 작성하시오. (프로젝트의 이름은 crud 이며 app 이름은 articles이다. index.html 파일을 렌더링 하는 view 함수의 이름은 index라고 가정한다.)

``` python
from . import views # (a), (b)
path('', views.index, name='index'), #(c)
```



___



### 3. templates and static

> Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static 파일을 앱 폴더 내부의 templates와 static 이름의 폴더에서 찾는다. 
>
> 만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 __(a)__ 파일의 __(b)__ 와 __(c)__ 라는 변수에 담긴 리스트의 요소를 정의하면 된다. 
>
> 빈칸 (a), (b), (c)에 들어갈 내용을 작성하시오.

``` 
a - settings
b - TEMPLATES = [
	'DIRS': [],
]
c - STATICFILES_DIRS
```



___



### 4. migration

> 아래는 그림과 같이 Django에서 선언한 Model을 Database에 반영하는 과정에서 사용하는 명령어에 대한 설명이다. 각 설명에 해당하는 명령어를 작성하시오. (app 이름은 articles이다.)
>
> 1) 마이그레이션 생성
>
> 2) 마이그레이션 DB 반영 여부 확인
>
> 3) 마이그레이션에 대응되는 SQL문 출력
>
> 4) 마이그레이션 파일의 내용을 DB에 최종 반영

``` bash
$ python manage.py makemigrations
$ python manage.py showmigrations (articles)
$ python manage.py sqlmigrate articles (0001, 0002...)
$ python manage.py migrate
```



---



### 5. ModelForm True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.
>
> 1) POST와 GET 방식은 의미론상의 차이이며 실제 동작 방식은 동일하다.
>
> 2) ModelForm과 Form Class의 핵심 차이는 Model의 정보를 알고 있는지의 여부이다.
>
> 3) AuthenticationForm은 User 모델과 관련된 정보를 이미 알고 있는 ModelForm으로 구성되어 있다.
>
> 4) ModelForm을 사용할 때 Meta 클래스에 fields 관련 옵션은 반드시 작성해야 한다.

``` 
1 - T - 실제로 요청을 하는 역할이 주 이지만 POST는 의미적으로 어떤 데이터를 넘겨주고 처리하겠다 라는 의미가 강한 반면, GET은 단순히 데이터를 조회하겠다는 의미의 요청입니다.
2 - T - 모델폼은 실제 생성한 모델과 연결하기 때문에 바로 객체로 생성하여 저장이 가능하지만, 일반 폼클래스는 아무리 필드에 맞게 짜더라도 직접적인 연결은 없기 때문에 객체를 생성하고, 필드별로 값을 일일히 넣어 연결해주어야 합니다.
3 - T - AuthenticationForm 은 from django.contrib.auth.forms 에서 import 하며, 별도의 처리 없이 User와 연결되는 것으로 보아 ModelForm이라고 볼 수 있습니다.
4 - T - UserCreationForm 과 같이 장고 자체 내장 지원 폼을 상속받아 사용할 때는 별도로 필드를 처리 안해줘도 작동하지만, 일반 모델 폼의 경우 exclude나 fields 옵션 둘 중에 하나를 반드시 사용해야 합니다. 
발생 에러 - django.core.exceptions.ImproperlyConfigured: Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited; form ArticleForm needs updating.
```



___





### 6. media 파일 경로

> 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더(crud) 내부의 /uploaded_files 폴더로 지정하고자 한다. 이 때, settings.py에 작성해야 하는 설정 2가지를 작성하시오.

``` python
# Media files

# 사용자가 미디어 파일로 접근하기 위한 경로
MEDIA_URL = '/media/'

# 미디어 파일이 업로드 되는 폴더의 위치
MEDIA_ROOT = BASE_DIR / 'uploaded_files'
```



___





### 7. DB True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.
>
> 1) RDBMS를 조작하기 위해서 SQL문을 사용한다.
>
> 2) SQL에서 명령어는 반드시 대문자로 작성해야 동작한다.
>
> 3) 일반적인 SQL문에서는 세미콜론( ; )까지를 하나의 명령어로 간주한다.
>
> 4) SQLite에서 .tables, .headers on과 같은 dot( . )로 시작하는 명령어는 SQL문이 아니다.
>
> 5) 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다.

``` 
1 - T - sql문을 사용하는 이유는 RDBMS에서 적절히 처리하기 위함입니다.
2 - F - 소문자로도 처리는 가능하지만 sql 문법상 대문자는 명령어, 소문자는 테이블이나 속성을 가르키도록 권장하고 있습니다.
3 - T - sql 표준에서 sql문은 ;전 까지를 하나의 문장으로 판단하여 처리합니다. 물론 ; 없이도 문장을 잘 구분해주는 dbms가 많지만 표준은 ; 사용하는 것을 권장합니다.
4 - T - .으로 시작하는 명령어는 sqlite에서 사용자 편의를 위해 제공하는 기능들 입니다.
5 - F - 하나의 데이터베이스 안에는 여러 개의 테이블이 존재할 수 있습니다.
```



___





### 8. on_delete

> 게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 즉, ProtectedError를 발생시켜 참조 된 객체의 삭제를 방지하는 __(a)__를 작성하시오.

``` python
article = models.ForeignKey(Article, on_delete=models.PROTECT)
```



___





### 9. Like in models

> Article 모델과 User 모델을 M:N 관계로 설정하여 ‘좋아요’ 기능을 구현하려고 한다. __(a)__와 __(b)__에 들어갈 내용을 작성하시오. 추가적으로 아래의 상황에서 __(b)__를 반드시 작성해야 하는 이유를 함께 작성하시오.

``` python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

'''
related_name 을 작성하지 않았을 경우 User 모델에서 역참조시에 article 모델에 있는 user와 like_users 가 모두 user_set 으로 역참조 됩니다. (디폴트 값) 그래서 해당 결과 값이 user를 가져올 지 like_users를 가져올지 모르기 때문에 문제가 발생하므로 장고에서 에러로 처리합니다. 그러므로 둘 중 하나의 역참조 이름을 바꿔주어야 하므로 related_name 이 필요합니다.
'''
```



___





### 10. Follow in models

> follow 기능을 구현하기 위해 accounts app의 models.py에 아래와 같은 모델을 작성하였다. Migration 작업 이후에 Database에 만들어지는 중개 테이블의 이름을 작성하고 이 테이블의 id를 제외한 컬럼 이름을 각각 작성하시오.

``` 
테이블 명 - accounts_user_followings - 앱 이름_클래스 이름_필드 이름
해당 MtoM필드가 자기 자신을 모델로 하는 재귀 모델일 경우, 서로의 관계를 from, to로 나눕니다.
컬럼 1 - from_user_id
컬럼 2 - to_user_id
```



___

