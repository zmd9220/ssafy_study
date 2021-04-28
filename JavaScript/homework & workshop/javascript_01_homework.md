# javascript_01_homework





### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

``` 
1. document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다.
- T - 주어진 태그를 받으면 HTML 요소로 만들어서 반환하는 함수입니다.
2. EventTarget.addEventListener(type, listener) 에서 listener에 작성되는 콜백 함수의 첫번째 매개변수는 발생한 이벤트를 설명하는 Event에 기반한 객체이다.
- T - listener는 해당 이벤트가 발생했을 때 이 함수의 기능을 작동시키라고 하기 때문에 특정 이벤트가 발생했는지 알기위해 Event객체로 지정합니다.
3. event.preventDefault 메서드를 통해 이벤트 동작을 취소할 수 있다.
- T - 특정 이벤트에 대한 동작을 막고 추가적인 처리를 할 수 있습니다. 대표적으로 form의 제출을 막고 데이터를 js상에서 갱신하고 동적으로 보여줄 때 사용됩니다.
4. 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다.
- F - appendChild() 메서드로도 자식 노드로 추가 할 수 있습니다.
```



___



### 2. DOM Event에는 다양한 종류의 Event가 존재한다. 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 다음 MDN 문서를 참고하여 간단하게 작성하시오.

> https://developer.mozilla.org/ko/docs/Web/Events
>
> click, mouseover, mouseout,, keydown, keyup, load, scroll, change, input

``` 
click - 해당 엘레먼트가 클릭 되었을 때 (주로 마우스로 클릭함)
mouseover - 포인팅 장치(주로 마우스)가 리스너에 등록된 엘레먼트나 자식의 엘레먼트의 위로 이동했을 때 
mouseout - 포인팅 장치(주로 마우스)가 리스너에 등록된 엘레먼트나 자식의 엘레먼트의 밖으로 이동했을 때
keydown - 키가 눌렸을 때
keyup - 키 눌렀다가 떼었을 때 
load - 리소스의 로딩이 끝났을 때 (해당 페이지의 HTML 문서가 다 불러와지면)
scroll - 문서 뷰나 엘레먼트가 스크롤 되었을 때
change - 특정 입력 엘레먼트나 선택해야 되는 엘레먼트에서 입력이 끝났거나 선택이 끝났을 때
input - 해당 엘레먼트의 값의 수정이 이루어질 때 (입력되고 있을 때)
```



___



### 3. 다음은 버튼을 클릭했을 때, 콘솔창을 통해 메시지를 확인하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

``` 
이벤트 리스너를 만드는 부분입니다.
a - querySelector
b - addEventListener
c - 'click'
```



___


