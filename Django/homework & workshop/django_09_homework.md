# django_09_homework





### 1. User Model BooleanField

> django에서 기본적으로 사용하는 User 모델은 AbstractUser 모델을 상속받아 정의된다.
>
> 아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField로 정의 된 컬럼을 모두 작성하시오.
>
> https://github.com/django/django/blob/master/django/contrib/auth/models.py

``` python
# 해당 클래스에서는 is_staff, is_active 를 찾을 수 있었습니다.
   is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
```



---



### 2. username max length

> django에서 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길이를 작성하시오.

``` python
# username 필드의 max_length = 150 이므로 최대 길이는 150 입니다.
username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
```



---



### 3.  login validation

> 단순히 사용자가 ‘로그인 된 사용자인지’만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.

``` python
# 로그인 여부만 판단하는 속성은 is_authenticated 입니다.
```



---



### 4. Login 기능 구현

> 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

``` python
from django.contrib.auth.forms import AuthenticationForm # (a) 
from django.contrib.auth import login as auth_login # (b)
auth_login(request, form.get_user()) # (c)
```



---



### 5. who are you?

> 로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.

``` python
# 로그인 하지 않았을 경우 request.user 에는 AnonymousUser 클래스가 담겨서 리턴됩니다.
```



---



### 6. 암호화 알고리즘

> Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해시 함수를 작성하시오.

``` python
'''
django 에서 패스워드에 기본적으로 사용되는 알고리즘은 pbkdf2_sha256 알고리즘을 사용합니다.
공식 문서에 따르면 장고가 지원하는 해시 함수는 5가지가 있으며 그 중의 첫 번째 것을 선택하여 사용한다고 합니다. 그래서 기본 함수로 pbkdf2_sha256이 사용됩니다.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
'''
```



---



### 7. Logout 기능 구현

> 로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오

``` python
'''
제시된 코드에서는 정의한 함수명 logout 과 django.contrib.auth 에서 가져온 logout 함수가 이름이 같기 때문에 가장 가까이 있는 logout 인 본인이 실행 되게 됩니다. 그러므로 django.contrib.auth 에서 가져온 logout 함수의 이름을 바꿔주어 사용하면 문제없이 실행할 수 있습니다.
추가적으로 적자면 로그아웃을 하자마자 로그인 탭으로 다시 리다이렉트 하는 것은 로직상 별로 좋지 않다고 생각합니다. 그래서 메인 페이지로 돌아가도록 수정하면 더 좋을 것 같습니다.
'''
from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
```

