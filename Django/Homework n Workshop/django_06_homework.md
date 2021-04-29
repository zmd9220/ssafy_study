# django_06_homework





### 1. static 파일 기본 설정

> 개발자가 작성한 CSS 파일이나 미리 업로드한 이미지 파일 등이 Django 프로젝트 폴더 (my_pjt) 내부 assets 폴더에 있다. 
>
> 이처럼 기존 static 파일 경로 외에 추가 경로를 정의해야 할 경우 settings.py에 추가해야 하는 설정과 값을 작성하시오.

``` python
'''
기본적으로 장고는 앱에서 만들어진 static 폴더는 인식하지만 메인프로젝트 폴더나 그외에 다른 외부 경로에 대해서는 static 폴더를 개별적으로 지정해줘야 합니다. 그것은 STATICFILE_DIRS 키워드를 통해 지정할 수 있습니다.
'''
STATICFILES_DIRS = [
    BASE_DIR / 'my_pjt' / 'asset',
]
'''
추가적으로 배포시에는 여러 앱과 경로에 있는 static 파일들을 한 곳에 모아둬야 하는데, 그것을 위해 STATIC_ROOT를 지정해주고, collectstatic 명령어를 통해 폴더를 생성하도록 해주어야 합니다.
'''
# 정적 파일 접근 경로
STATIC_URL = '/static/'
# 배포 환경
STATIC_ROOT = BASE_DIR / 'staticfiles'
```





### 2. media 파일 기본 설정

> 사용자가 업로드 파일의 저장처를 Django 프로젝트 폴더(my_pjt) 내부 uploaded_files 폴더로 지정하고자 한다. 이 때, settings.py에 작성해야 하는 설정과 값을 모두 작성하시오.

``` python
'''
사용자가 업로드 한 파일은 미디어 파일이라고 하며, 장고에서는 기본적으로 별도로 폴더를 생성해서 관리해주지 않기 때문에, 개발자가 직접 세팅에 미디어 파일 접근을 위한 경로, 미디어 파일의 저장 위치를 지정해 주고, urls에 연결해 주어야 합니다.
'''
MEDIA_ROOT = BASE_DIR / 'my_pjt' / 'uploaded_files'

'''
추가적으로 미디어 파일 접근을 위한 경로와 urls.py 세팅까지 추가 해봅니다.
'''
# settings.py
MEDIA_URL = /'media'/
# my_pjt/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```





### 3. Serving files uploaded by user during development

> settings.py에 MEDIA_URL 값이 작성되어 프로젝트에 사용자가 업로드한 파일이 업로드 될 수 있게 되었다. 하지만 사용자가 실제 웹 페이지 내에서 이 파일을 조회 할 수 있도록 하기 위해선 업로드 된 파일에 대한 URL을 생성 해주는 설정이 필요하다. 
>
> 빈칸 __(a)__, __(b)__, __(c)__, __(d)__에 들어 갈 코드를 작성하시오.

``` python
'''
2번에 추가적으로 미리 적었지만 다시 한번 적어봅니다.
'''
from django.conf import settings # (a)
from django.conf.urls.static import static # (b), (c)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # (d)
```


