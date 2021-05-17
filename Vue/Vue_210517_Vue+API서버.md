# Vue_210517_Vue+API서버



## 오전



### 지난 시간

- Vue Intro
  - Vuex
    - 상태 관리 패턴 라이브러리
  - Vuex Core Concepts
    - State, Actions, Mutations, Getters



### 서버 & 클라이언트



#### Server

- 클라이언트에게 '정보', '서비스'를 제공하는 컴퓨터 시스템
- 정보 & 서비스
  - Django를 통해 응답한 template
  - DRF를 통해 응답한 JSON



#### Client

- 서버에게 그 서버가 맞는(서버가 제공하는) **서비스를 요청**하고
- 서비스 요청을 위해 필요한 인자를 **서버가 원하는 방식에 맞게 제공**하며
- 서버로부터 반환되는 응답을 **사용자에게 적절한 방식으로 표현**하는 기능을 가진 시스템



#### 정리

- 서버는 정보 제공
  - DB와 통신하며 데이터를 CRUD
  - 요청을 보낸 Client에게 이러한 정보를 응답
- Client는 정보 요청 & 표현
  - 서버에게 정보(데이터) 요청
  - 응답 받은 정보를 잘 가공하여 화면에 보여줌



### CORS



#### Same-origin policy (SOP)

- 동일 출처 정책
- 특정 출처(origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
- 정의
  - 두 URL의 Protocol, Port, Host 가 모두 같아야 동일한 출처



#### Cross-Origin Resource Sharing (CORS)

- 교차 출처 리소스(자원) 공유
- **추가 HTTP header를 사용**하여, 특정 출처에서 실행중인 웹 애플리케이션이 **다른 출처의 자원에 접근 할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제**
- 리소스가 자신의 출처(Domain, Protocol, Port)와 다를 때 교차 출처 HTTP 요청을 실행
- 보안 상의 이유로 브라우저는 교차 출처 HTTP 요청을 제한 (SOP)
  - 예를 들어 XMLHttpRequest는 SOP를 따름
- 다른 출처의 리소스를 불러오려면 그 출처에서 **올바른 CORS header를 포함한 응답을 반환**해야함



#### CORS Policy

- 교차 출처 리소스(자원) 공유 정책
- 다른 출처(origin)에서 온 리소스를 공유하는 것에 대한 정책
- SOP와 반대



#### 교차 출처 접근 허용하기

- CORS를 사용해 교차 출처 접근 허용
- CORS는 HTTP의 일부로, 어떤 호스트에서 자신의 컨텐츠를 불러갈 수 있는지 **서버에 지정할 수 있는 방법**



#### Why CORS?

1. 브라우저 & 웹 어플리케이션 보호
   - 악의적인 사이트의 데이터를 가져오지 않도록 사전 차단
   - 응답으로 받는 자원에 대한 최소한의 검증
   - 서버는 정상적으로 응답하지만 브라우저에서 차단
2. 서버의 자원 관리
   - 누가 해당 리소스에 접근 할 수 있는지 관리 가능



#### How CORS?

- CORS 표준에 의해 추가된 **HTTP Header**를 통해 이를 통제
- CORS HTTP 응답 헤더 예시
  - Access-Control-Allow-Origin - 오늘 사용할 것
  - Access-Control-Allow-Credentials
  - Access-Control-Allow-Headers
  - Access-Control-Allow-Methods



#### Access-Control-Allow-Origin 응답 헤더

- 이 응답이 주어진 출처(origin)으로 부터 요청 코드와 공유 될 수 있는 지를 나타냄
- 예시
  - Access-Control-Allow-Origin: *
  - 브라우저 리소스에 접근하는 임의의 origin으로 부터 요청을 허용한다고 알리는 응답에 포함
  - '*'는 모든 도메인에서 접근할 수 있음을 의미
  - '*'외에 특정 origin 하나를 명시 할 수 있음