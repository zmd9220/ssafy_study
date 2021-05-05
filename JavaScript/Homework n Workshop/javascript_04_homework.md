# javascript_04_homework





### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

> - Event Loop는 Call Stack이 비워지면 Task Queue의 함수들을 Call Stack으로 할당하는 역할을 한다.
> - XMLHttpRequest(XHR)은 AJAX 요청을 생성하는 JavaScript API이다. XHR의 메서드로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다.
> - axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.

``` 
1. T - web api에서 처리가 끝난 후 task queue에 대기중인 함수들을 대상으로 call stack의 상황을 보고 비어있을 경우 채워줍니다.
2. F - XHR은 web API입니다.
3. F - axios는 XHR이 아닌 promise를 보내고 응답 결과를 promise로 받습니다.
```



___



### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

``` 
처음에 call stack에 hello ssafy가 들어가고, 출력이 됩니다. 다음에 call stack에 setTimeout 함수가 들어가는데, 시간을 기다려야하는 외부 함수이므로 call stack에서 web api로 넘기고 다음 일인 bye ssafy를 받습니다. 그리고 bye ssafy를 출력하고 call stack은 빈 상태에서, web api에서 응답을 받게 된 함수는 task queue에 들어가는데, event loop가 call stack이 비었음을 확인하고 task queue에 있는 함수를 가져와서 i am from setTimeout을 출력하고 종료합니다.
```



___



### 3. JS는 Event loop를 기반으로 하는 Concurrency model을 가지고 있다고 한다. Concurrency 키워드의 특징을 작성하고, 이와 비슷한 키워드로 비교되는 Parallelism의 개념과 두 개념의 차이점을 서술 하시오.

> call stack, web api, task queue, event loop

``` 
concurrency(병행성) 모델은 자바스크립트가 싱글쓰레드 기반이기 때문에 한번에 여러가지 일을 처리할 수 없어 고안된 모델로 call stack에 데이터를 순차적으로 처리하다가 setTimeout(), event, AJAX 요청과 같은 시간이 걸리는 일에 대해 Web api에 요청 및 응답을 받는 일을 맡기고, 본인이 처리할 수 있는 빠른 일들을 먼저 처리 한 후, event loop가 Web api에서 응답 받은 데이터를 task queue에 존재 하는지 확인 후, call stack으로 올려 시간이 오래 걸리는 일을 나중에 처리하게 하여 마치 여러 가지 일을 한번에 처리하는 것처럼 보여주는 기능을 의미합니다.

parallelism(병렬성) 은 코어가 멀티 코어이므로 실제로 한 번에 여러가지 일을 동시에 처리되고 있다는 뜻입니다.
즉 병행성은 사용자가 보기엔 동시에 처리하는 것처럼 보이지만 실제로는 하나의 코어로 처리하는 중이며, 병렬성은 실제로 다수의 코어로 처리하고 있는 상태를 의미합니다.
```



___


