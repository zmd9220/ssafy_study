# vue_04_homework





### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

> - Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다.
> - mutation은 반드시 state를 수정하기 위해서만 사용되어야 한다.
> - mutation은 store.dispatch로, action은 store.commit으로 호출할 수 있다.
> - state는 data와 동일하고, getters는 computed와 동일한 동작을 한다.

``` 
1 - T - 상태 관리를 state 를 통한 관리 라고 한다면 맞는 말이고 단순히 데이터를 관리하기 위함이면 props와 emit을 사용하여 로컬 컴포넌트 별로 관리 할 수 있으므로 F
F - Vuex는 상태 관리를 도와주는 라이브러리 (없어도 문제는 없다.)
2 - T - mutation은 state를 수정하기 위한 목적으로 사용되는 함수입니다.
3 - F - mutation은 commit, action은 dispatch로 호출합니다.
4 - T - state는 vuex에서 data를 사용하는 명칭이고, getters는 computed와 같이 변환 될 연산에 사용합니다.
```



___



### 2. Vuex에서 action과 mutation의 역할과, 두 함수의 차이를 서술하시오.

``` 
action은 해당 컴포넌트에서 진행될 모든 기능에 대한 모든 코드, 절차를 의미합니다. 
예를 들어 todo 앱을 만든다면 로그인 여부 체크, input에 공백인 상태인지 데이터가 있는 상태인지 여부, 데이터를 저장하기 위해 commit을 요청 하고 다시 input라인을 공백으로 만드는 등 전반적인 진행 프로세스를 담당합니다. 
사용자가 어떤 하고자 하는 행위에 대한 정의 (business logic)
mutation은 action에서 commit을 요청하면 mutation을 통해 실제 데이터를 저장하는 공간에 데이터를 삽입하여 state를 수정합니다. mutation을 이용해서 state에 접근하여 데이터를 수정할 수 있도록 만드는 것을 권장합니다. 
state를 변경(저장)하기 위한 정의
```



___

