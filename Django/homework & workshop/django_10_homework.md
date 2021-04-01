# django_10_homework





### 1. Lookup

> 지문의 코드에서 ‘__gt’ 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용 가능 한 lookup 세가지와 그 의미를 작성하시오.
>
> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups

``` python
'''
exact - 완전히 일치하는 값만 찾습니다.
iexact - 대소문자는 구분하지 않지만, 일치하는 값을 찾는 것은 exact와 같습니다.
contains - 조건값을 포함한 값을 찾습니다. 대소문자를 구분합니다.
'''
```



___



### 2.  1:N 관계 설정

> 지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지를 선택 후 그 의미를 작성하시오.
>
> https://docs.djangoproject.com/en/3.0/ref/models/fields/#arguments

``` python
'''
CASCADE - 해당 참조 되는 행이 삭제가 되면 참조하는 속성(키)에 해당 되는 열까지 같이 삭제 되는 속성입니다.
SET_NULL - null 이 true 일 때만 사용 가능하며 참조 되는 행이 삭제 될 때, 해당 외래키를 null로 만듭니다.
DO_NOTHING - 참조 되는 행이 삭제 되더라도 아무런 행동을 취하지 않습니다. 그러므로 항상 참조 무결성을 깨트릴 수 있음을 염두해 두어야 합니다.
'''
```



___



### 3. comment create view

> 지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드와 의미를 작성하시오.

``` python
comment = form.save(commit=False)
# db에 당장 저장하지 않는다는 의미 입니다. 저장하기 전에 사용자가 원하는 특정 행동이나, 특정 정보를 추가해야 겠다고 판단했을 때, 사용하게 됩니다.
```



___



### 4.  1:N DB API

> 게시물 아래에 댓글을 출력하려고 한다. Article과 Comment 모델이 1:N으로 관계설정이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

``` python
# a - comments
```

