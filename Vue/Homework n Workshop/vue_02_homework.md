# vue_02_homework





### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

> - Vue의 Life Cycle Hook에서 created Hook은 Vue template에 작성한 요소들이 DOM에 다 그려지는 시점에 실행된다.
> - npm은 Node Package Manager의 약자이며, npm을 통해 설치한 package 목록은 package.json 파일에 자동으로 작성된다.
> - Vue CLI를 통해 만든 프로젝트는 브라우저가 아닌 node.js 환경이기 때문에 DOM 조작이나 Web API 호출 등 Vanilla JS에서의 기능을 사용할 수 없다.

``` 
1. F - created hook은 DOM이 그려지기 전에 실행됩니다.
2. T - npm은 node.js 설치시에 같이 설치되며 python의 pip와 유사한 기능을 제공합니다. 더불어 npm은 패키지 설치시 자동으로 package.json에 의존성 항목에 설치된 패키지명을 추가 해줍니다.
3. T - DOM과 Web API는 브라우저의 기능이므로 사용할 수 없습니다.
- F - 브라우저에서도 동작이 된다. (브라우저에서 동작이 된다는 ㄱ)
```



___



### 2. Vue Router에서 설정하는 history mode가 무엇을 뜻하는지 서술하시오.

``` 
vue와 같은 SPA에서는 MPA와 다르게 한 페이지 내에서 url이 움직이지 않기 때문에 사용자 경험이 저하될 수 있습니다. 이를 해결하기 위해 브라우저의 history API를 활용한 history mode를 지원했는데, history mode는 실제 페이지는 SPA에서 작동되므로 한 페이지에서 움직이지 않지만, history API를 통해 브라우저에서 보이는 url 상으로는 기능별로 url을 변경시켜서 마치 MPA 기반으로 구성된 웹 페이지를 보는 듯한 사용자 경험을 만들 수 있습니다.
```



___



### 3. Vue Life Cycle Hook을 참고하여, 다음 Vue application을 실행했을 때 console 창에 출력되는 메시지를 작성하시오.

> https://kr.vuejs.org/v2/guide/instance.html#%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4-%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%ED%9B%85

``` 
created!
mounted!
```



___



