# django_02_homework





### 1. MTV

> Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의
> 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는
> 역할을 간략히 서술하시오.

``` python
'''
장고의 MTV는 각각 Model, Template, View를 의미합니다. 이는 기존의 소프트웨어 디자인 패턴인 MVC(Model, View, Controller)요소와 각각 매칭 됩니다. 
Model은 db에 저장되고 불러와지는 데이터의 영역을 의미합니다. 각 요소의 처리나 결과에 있어 db에 저장하고 불러오는 역할을 하게됩니다.
Template는 사용자에게 보여지는 부분입니다. 사용자 요청에 따라 처리된 결과물을 html문서를 통해 보여지게 됩니다.
View의 경우 웹의 요청을 받고 처리하는 중간관리자 역할을 합니다. 이부분은 python 함수를 통해 기능함으로써 요청에 맞게 로직을 처리하고 결과물을 반환하도록 하는 메인 처리를 담당합니다.
'''
```





### 2. URL

> __(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을
> 의미한다. __(a)__는 무엇인지 작성하시오.

``` python
# Variable routing
```





### 3. Django template path

> Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에
> 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을
> 작성하시오.

``` python
# templates
```





### 4. Static web and Dynamic web

> Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.

``` python
'''
static web page는 미리 개발자가 설정해놓은 화면을 사용자에게 그대로 보여줍니다. 대표적으로 문서류나 가이드북 등에서 사용됩니다.
dynamic web page는 현재 대부분의 웹페이지에서 사용되며 사용자의 요청에 따라 웹서버가 적절한 처리를 한뒤 화면을 보여주는 웹페이지를 의미합니다. 사용자의 상황, 요청에 따라 서버는 항상 적절한 처리를 통해 화면을 출력하도록 돕습니다.
'''
```

