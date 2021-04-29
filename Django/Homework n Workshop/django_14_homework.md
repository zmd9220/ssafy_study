# django_14_homework





### 1. M:N True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오.

``` 
1) Django에서 1:N 관계는 ForeignKeyField를 사용하고 M:N 관계는 ManyToManyField를 사용한다.
- T
2) ManyToManyField를 설정하고 만들어지는 테이블 이름은 “앱이름_클래스이름_지정한 필드이름”의 형태로 만들어진다.
- T
3) ManyToManyField의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.
- F ManyToManyField에서 참조할 모델인 첫번째 인자는 필수지만, 그 외의 related_name, symmetrical, through 등은 옵션입니다.
```



___



### 2. Like in templates

> 아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

``` 
request.user - (a)
article.like_users.all - (b)
```



___



### 3. Follow in views

> 모델 정보가 다음과 같을 때 빈칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

``` 
user_pk - (a)
followings - (b)
filter - (c)
remove - (d)
add - (e)
```



___



### 4. User AttributeError

> 아래와 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오.

``` python
'''
커스텀 유저 모델을 만들었으나 views의 signup 부분의 UserCreationForm을 커스텀하여 사용하지 않았을 경우 발생하는 에러입니다. 기존 UserCreationForm은 장고 기본 값인 Auth.User와 연결되는 폼이므로 커스텀 유저 모델 생성시 UserCreationForm을 상속받는 커스텀 유저 폼을 생성해 주어야 합니다.
'''
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

```



---



### 5. related_name

> 아래의 경우 related_name을 필수적으로 설정해야 한다. 그 이유를 설명하시오.

``` 
user와 like_users는 모두 user 모델을 참조하기 때문에 user 모델 측에서 역참조를 할 시, related_name을 설정하지 않으면 두 모델을 기본 값인 article_set 으로 참조하게 되기 때문에 중복되어 버립니다. 그래서 둘 중 하나의 역참조 이름을 지정해주어야 합니다.
```

