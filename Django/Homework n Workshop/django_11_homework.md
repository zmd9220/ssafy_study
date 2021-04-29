# django_11_homework





### 1. SQL 용어 및 개념

> 아래의 보기에서 각 문항의 설명에 맞는 용어를 고르시오.
>
> 기본키 테이블 스키마 레코드 컬럼

``` 
1) 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것 - 스키마
2) 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합 - 테이블
3) 고유한 데이터 형식이 지정되는 열 - 컬럼
4) 단일 구조 데이터 항목을 가리키는 행 - 레코드
5) 각 행의 고유값 - 기본키
```



___



### 2. SQL 문법

> 아래의 보기 (1) ~ (4) 중에서, DML이 아닌 것을 고르시오.

``` 
(1) CREATE
(2) UPDATE
(3) DELETE
(4) SELECT

1번 CREATE는 데이터 정의 언어인 DDL 입니다. DDL은 데이터 베이스의 구조 등을 정의하는데 사용합니다. CREATE는 테이블을 생성하는 명령어 입니다.
```



___



### 3. Relational DBMS

> RDBMS의 개념적 정의와 이를 기반으로 한 DB-Engine의 종류 세가지 이상 작성하시오.

``` 
RDB(Relational DataBase)란 관계형 모델을 기반으로 한 데이터 베이스 형태입니다. 관계형 모델이란 데이터 구성을 하는 방법 중 하나로 데이터를 2차원의 테이블 표를 통하여 표현합니다. 그리고 이러한 RDB를 관리하는 시스템(Management System)을 RDBMS라고 합니다. 대표적인 RDBMS로는 mysql, sqlite, oracle 등이 있습니다.
```



___



### 4. INSERT INTO

> 다음과 같은 스키마를 가지는 테이블이 있을 때, 아래의 보기 (1) ~ (4) 중 틀린 문장을 고르시오.

``` 
(1) INSERT INTO classmates (name, age, address)
VALUES(‘홍길동’, 20, ‘seoul’);
(2) INSERT INTO classmates VALUES(‘홍길동’, 20, ‘seoul’);
(3) insert into classmates
values(address=‘seoul’, age=20, name=‘홍길동’);
(4) insert into classmates (address, age, name)
values(‘seoul’, 20, ‘홍길동’);

3번 - classmates 의 별다른 속성없이 불러오면 기본값으로 생성된 name, age, address 순으로 데이터를 가져오게 됩니다.
```



___



### 5. 와일드카드 문자

> SQL에서 사용가능한 와일드카드 문자인 %와 _을 비교하여 작성하시오.

``` 
% 의 경우 해당하는 위치에 문자가 없거나 크기 상관없이 어떤 문자가 와도 괜찮습니다.
_ 의 경우 어떤 값이라도 단 하나의 문자만 가능합니다.
```


