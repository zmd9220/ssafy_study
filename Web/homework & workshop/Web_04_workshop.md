# Web_04_workshop





### 1. 기본 그리드 레이아웃

> 각 문항의 지시에 따라 01_grid.html 파일에 정답을 작성하시오.
> 1) 제시된 3개의 컬럼이 container를 가득 채우도록 클래스를 추가 작성하시오.
> 단, 각 컬럼의 너비는 동일하도록 작성하시오.
> 2) 제시된 2개의 컬럼이 container를 가득 채우도록 클래스를 변경하시오.
> 단, 각 컬럼의 너비는 동일하도록 작성하시오.
> 3) 제시된 12개의 컬럼이 3칸, 6칸, 3칸씩 차지하도록 마크업과 클래스를 변경하시오.
> 4) 제시된 3개의 컬럼이 2칸, 7칸, 3칸씩 차지하도록 클래스를 변경하시오.

``` html
  <!-- 1. -->
    <div class="row">
      <div class="item col">
        <p>4개</p>
      </div>
      <div class="item col">
        <p>4개</p>
      </div>
      <div class="item col">
        <p>4개</p>
      </div>
    </div>

    <!-- 2. -->
    <div class="row">
      <div class="item col-6">
        <p>6개</p>
      </div>
      <div class="item col-6">
        <p>6개</p>
      </div>   
    </div>

    <!-- 3. -->
    <div class="row">
      <div class="item col-3">
        <p>1개</p>
      </div>  
      <div class="item col-6">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
      <div class="item col-6">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
      <div class="item col-6">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
      <div class="item col-6">
        <p>1개</p>
      </div>
      <div class="item col-3">
        <p>1개</p>
      </div>
    </div> 
    
    <!-- 4. -->
    <div class="row">
      <div class="item col-2">
        <p>4개</p>
      </div>
      <div class="item col-7">
        <p>4개</p>
      </div>
      <div class="item col-3">
        <p>4개</p>
      </div> 
    </div>
```





### 2. 반응형 그리드

> 각 문항의 지시에 따라 02_grid.html 파일에 정답을 작성하시오.
> 1) Viewport 너비가 576px 미만인 경우, 각 컬럼이 4칸, 4칸, 4칸씩 차지하고
> 576px 이상인 경우, 2칸, 5칸, 5칸씩 차지하도록 클래스를 추가하시오.
> 2) Viewport 너비가 768px 미만인 경우, 각 컬럼이 1칸, 3칸, 4칸, 1칸, 3칸씩 차지하고
> 768px 이상인 경우, 2칸, 3칸, 3칸, 2칸, 2칸씩 차지하도록 클래스를 추가하시오.
> 3) Viewport 너비가 576px 미만인 경우, 각 컬럼이 4칸, 6칸, 2칸씩 차지하고
> 576px 이상인 경우, 3칸, 3칸, 6칸씩 차지하며
> 768px 이상인 경우, 6칸, 6칸, 12칸을 차지하도록 클래스를 추가하시오.
> 4) Viewport 너비가 768px 미만인, 경우 각 컬럼이 12칸, 12칸, 12칸씩 차지하고
> 768px 이상인 경우, 4칸, 4칸. 4칸씩 차지하며
> 1200px 이상인 경우, 2칸, 2칸씩 차지하고 12칸을 차지하는 컬럼이 그 다음에
> 내려오도록 클래스를 추가하시오.

``` html
<!-- 1. -->
    <div class="row">
      <div class="item col-4 col-sm-2">
        <p>576px 미만 4 <br> 576px 이상 2</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-3">
        <p>768px 미만 3 <br> 768px 이상 3</p>
      </div>
      <div class="item col-4 col-md-3">
        <p>768px 미만 4 <br> 768px 이상 3</p>
      </div>
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-2">
        <p>768px 미만 3 <br> 768px 이상 2</p>
      </div>
    </div>


    <!-- 3. -->
    <div class="row">
      <div class="item col-4 col-sm-3 col-md-6">
        <p>576px 미만 4 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-6 col-sm-3 col-md-6">
        <p>576px 미만 6 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-2 col-sm-6 col-md-12">
        <p>576px 미만 2 <br> 768px 미만 6 <br> 768px 이상 12</p>
      </div>
    </div>


    <!-- 4. -->
    <div class="row">
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-12">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 12</p>
      </div>
    </div>
```





### 3. 그리드 심화

> 각 문항의 지시에 따라 03_grid.html 파일에 정답을 작성하되 offset 클래스를 적절한
> 상황에 사용하여 작성하시오.

``` html
<!-- 1. -->
    <div class="row">
      <div class="item col-4">
        <p>item1</p>
      </div>
      <div class="item col-8 col-md-4 ms-md-auto">
        <p>item2</p>
      </div>
    </div>
    
    
    <!-- 2. -->
    <div class="row">
      <div class="item col-4 ms-md-auto col-lg-5 offset-lg-6">
        <p>item1</p>
      </div>
      <div class="item col-4 ms-auto ms-md-0 col-lg-8 mx-lg-auto">
        <p>item2</p>
      </div>
    </div>
    

    <!-- 3. -->
    <div class="row">
      <div class="item col-12 col-md-3">
        item1
      </div>
      <div class="item col-md-9">
        <div class="row">
          <div class="item col-6 col-lg-3">item2</div>
          <div class="item col-6 col-lg-3">item3</div>
          <div class="item col-6 col-lg-3">item4</div>
          <div class="item col-6 col-lg-3">item5</div>
        </div>
      </div>
    </div> 
```


