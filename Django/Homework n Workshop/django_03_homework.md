# django_03_homework





### 1. Model 반영하기

> “Django가 Model에 생긴 변화를 DB에 반영하는 방법”을 뜻하는 용어를 작성하시오.

``` python
# migration
```





### 2. Model 변경사항 저장하기

> 위에서 작성한 Model의 변경 사항을 저장하기 위한 명령어를 작성하시오. 이로 인해 생성된 파일에 대응되는 SQL문을 확인하는 명령어와 출력 결과를 작성하시오.

``` python

# 먼저 설계도 생성 python manage.py makemigrations
# 이후 DB에 반영 python manage.py migrate

# sql문을 확인하는 명령어 python manage.py sqlmigrate articles 0001
'''
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100)
NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
COMMIT;
'''

```





### 3. Python Shell

> Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어
> 떠한 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오

``` python
'''
python manage.py shell이 기본 장고에서 제공하는 shell 이지만 편한 사용을 위해
django_extansion 설치하면 python manage.py shell_plus로 사용 가능합니다.
'''
```





### 4. Django Model Field

> Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오.

``` python
'''
CharField, TextField, DateTimeField, TimeField, DateField
'''
```

