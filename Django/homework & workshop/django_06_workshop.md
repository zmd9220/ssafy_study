# django_06_workshop





### 1.  '<input type="file">' 태그를 사용할 경우 반드시 사용해야 하는 enctype 속성 값(a)를 작성하시오.

> http form 에서 파일을 받기 위해선 인코딩을 멀티타입으로 변경해야합니다.

``` django
<form action="" method="POST" enctype="multipart/form-data">
```





### 2. accept 속성은 파일 업로드 제어에서 선택할 수 있는 파일 유형을 정의하는 속성이며 input 태그의 type이 file일 경우에만 유효하다.

### 예를 들어 표준 비디오 형식 뿐만 아니라 PDF 파일도 받을 수 있어야 할 때, 빈칸(b)에 들어갈 알맞은 속성 값을 작성하시오.

> https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input/file
>
> https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input/file#%EA%B3%A0%EC%9C%A0_%ED%8C%8C%EC%9D%BC_%EC%9C%A0%ED%98%95_%EC%A7%80%EC%A0%95%EC%9E%90
>
> 참고.
>
> accept 속성으로 특정 파일만 받을 수 있습니다. *의 경우 해당하는 것의 모두, .확장자는 해당하는 확장자는 파일로 받을 수 있게 해줍니다.

``` django
<input type="file" accept="video/*,.pdf">
```


