# django_04_homework





### 1.  models.py를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 두 개의 핵심 명령어를 작성하시오.

> 1. 구조화(설계도 작성) 2. 실제 DB에 반영

``` shell
python manage.py makemigrations
python manage.py migrate
```





### 2. 다음 중 새로운 Post를 저장하기 위하여 작성한 코드 중 옳지 않은 것을고르시오.

``` python
'''
3번 - db의 맨 첫번째 인자로는 id(pk)가 들어가는데 인자명을 지정하지 않고 생성할 경우 id 값에 제목이 들어가게 될 것 입니다.
'''
```





### 3.  Post가 10개 저장되어 있고 id의 값이 1부터 10까지라고 가정할 때 가장 첫 번째 Post를 가져오려고 한다. 다음 중 옳지 않은 코드를 고르시오.

``` python
'''
2번
post2 = Post.objects.all()[-10] 장고는 음수 인덱스를 지원하지 않습니다.
AssertionError: Negative indexing is not supported.
'''
```





### 4.  my_post 변수에 Post 객체 하나가 저장되어 있다. title을 “안녕하세요” content를 “반갑습니다” 로 수정하기 위한 코드를작성하시오.

``` python
my_post.title = '안녕하세요'
my_post.content = '반갑습니다'
my_post.save()
```





### 5.  만들어진 모든 Post 객체를 QuerySet형태로 반환 해주기 위해 빈칸에 들어갈 코드를 작성하시오.

``` python
posts = Post.objects.all()
```

