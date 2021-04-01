# django_01_workshop



![Cap 2021-03-08 17-56-17-644](django_0.assets/Cap 2021-03-08 17-56-17-644-1615193912356.png)

### 1. intro/urls.py

``` python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    # view를 import하고 해당하는 함수이름 넣기
    path('lotto/', views.lotto),
    
    path('admin/', admin.site.urls),
]
```





### 2. pages/views.py

``` python
from django.shortcuts import render
import random
# Create your views here.

def lotto(request):
    # random함수로 6개 랜덤추출
    arr = random.sample(range(1, 46), 6)
    # html페이지에 인자로 넘겨줄 딕셔너리 생성
    context = {
        'arr' : arr
    }
    # 요청받은곳에 lotto.html페이지를 넘겨주며, context인자를 같이 넘겨줌
    return render(request, 'lotto.html', context)
```





### 3. templates/lotto.html

``` python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>제 000회 로또 번호 추천</h1>
  <p> 안병진님께서 선택하신 로또 번호는 {{ arr }} 입니다.</p>
</body>
</html>
```


