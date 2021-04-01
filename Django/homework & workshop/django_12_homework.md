# django_12_homework





### 1. 1:N True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오.

``` 
1) ForeignKey는 부모 테이블의 데이터를 참조하기 위한 키이다. - T
2) 1:N 관계에서 1은 N의 데이터를 직접 참조 할 수 있다. - F 직접 참조할 방법이 없어서 _set 을 이용합니다.
3) on_delete 속성은 ForeignKey 필드의 필수 인자이다. - T
4) 1:N 관계에서 외래 키는 반드시 부모 테이블의 PrimaryKey여야 한다. - F pk가 아니더라도 고유한 키 이기만 하면 가능합니다.
```



___



### 2. ForeignKey column name

> 다음과 같이 이름이 articles인 app의 models.py에 작성된 코드를 바탕으로 테이블이 만들어 졌을 때, 데이터베이스에 저장되는 ForeignKey 컬럼의 이름과 테이블의 이름이 무엇인지 작성하시오.

``` 
외래키가 저장된 테이블은 Comment 테이블이며, 컬럼은 answer_id 로 저장됩니다.
```



___



### 3.  1:N model manager

> 위 2번 문제 모델 관계를 바탕으로 어느 template 페이지가 다음과 같이 작성되어 있을 때, 질문(Question)에 작성된 모든 댓글(Comment)을 출력하고자 한다. 해당 template에서 Question 객체를 사용할 수 있다면 빈칸 __(a)__에 들어갈 알맞은 코드를 작성하시오.

``` 
question.comment_set.all
```



___



### 4. next prameter

> 다음과 같이 게시글을 삭제하는 delete 함수와 로그인을 위한 login 함수가 작성되어 있다. 만약 비로그인 사용자가 삭제를 시도한다면 django는 해당 사용자를 url에 next 파라미터가 붙은 login 페이지로 redirect 한다.
>
>  /accounts/login/?next=/articles/1/delete/
>
> redirect된 로그인 페이지에서 로그인에 성공했을 때 발생하는 HTTP response status code를 작성하고 발생한 원인과 해결을 위해 코드를 수정하시오.
>
> ▪ 게시글 삭제는 HTTP POST method로만 가능하다.
>
> ▪ 인증되지 않은 사용자는 메인페이지로 redirect 되어야 한다.

``` python
'''
login_required 로 인해 login 페이지를 갔다가 다시 리다이렉트로 돌아오게 될 때 해당 요청은 get으로 돌아옵니다. 그래서 require_POST에 막혀 405 에러가 발생합니다.
현재 조건에서는 POST를 유지해야하므로 login_required를 없애고 로그인 체크인 is_authenticated를 사용해서 적용합니다.
'''
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')

```

