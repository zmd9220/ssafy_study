# django_02_workshop



![2021-0316-57-37-777](image/2021-0316-57-37-777.png)

### 1. intro/urls.py

> 오늘 배운 것을 이용, url를 분산

``` python
# intro/urls.py
from django.contrib import admin
from django.urls import path, include

# include 사용으로 pages앱을 별도로 관리하도록 지정
urlpatterns = [
    path('pages/', include('pages.urls')),
    
    path('admin/', admin.site.urls),
]
# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'
# ~/pages/
urlpatterns = [
    path('dinner/<str:menu>/<int:people>/', views.dinner, name='dinner'),
]
```





### 2. pages/views.py

> 분산해서 처리

``` python
# variable routing은 함수에서 인자로 직접받아옴
# form을 통한 get 방식의 경우 request 내에서 GET or POST 이용
def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'pages/dinner.html', context)

```





### 3. templates/dinner.html

> 앱별로 관리를 위해 templates/pages/dinner.html에서 사용
>
> base.html을 상속받아 사용

``` django
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    {% block container %}
    {% endblock container %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
</body>
</html>

{% comment %} dinner.html 사용시 이부분을 내리거나 제거 {% endcomment %}
{% extends 'base.html' %}
{% block container %}
  <h1>저녁 메뉴</h1>
  <p>저녁 먹을 사람!? {{ people }}명</p>
  <p>어떤 메뉴?! {{ menu }}</p>
{% endblock container %}
```



다만 실행시 

pages/dinner/저녁메뉴/인원

으로 실행됩니다. 수정하려면 가능하지만 일단은 구현 및 앱별로 분산에 초점을 두어 진행했습니다.