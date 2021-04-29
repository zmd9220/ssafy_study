# Web_03_homework





### 1. Buttons

> Block buttons

``` html
<div class="d-grid gap-2">
    <button type="submit" class="btn btn-success btn-block">Sign in</button>         
</div>   
```





### 2. Navbar

``` html
<nav class="navbar navbar-expand-lg navbar-light bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">SSAFY</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link dropdown-toggle active text-white-50" aria-current="page" href="#" id="navbarDropdown1" role="button" data-bs-toggle="dropdown" aria-expanded="false">프로젝트</a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link dropdown-toggle text-white-50" href="#" id="navbarDropdown2" role="button" data-bs-toggle="dropdown" aria-expanded="false">그룹들</a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown2">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item ">
            <a class="nav-link text-white-50" href="#">활동</a>
          </li>
          <li class="nav-item ">
            <a class="nav-link text-white-50" href="#">마일스톤</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white-50" href="#">스니펫</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
```





### 3. Pagination

``` html
  <nav aria-label="...">
    <ul class="pagination ">
      <li class="page-item disabled">
        <a class="page-link text-" href="#" tabindex="-1" aria-disabled="true">Previous</a>
      </li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item active" aria-current="page">
        <a class="page-link " href="#">2</a>
      </li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item">
        <a class="page-link" href="#">Next</a>
      </li>
    </ul>
  </nav>
```





### 4. Button + login-form

``` html
  <div class="login-form container">
    <div class="alert alert-danger" role="alert">
      Invaild Login or password.
    </div>
    <h2 class="text-center">SSAFY 전용 GitLab 시스템</h2>
    <hr>
    <form action="#" method="post">
        <h2 class="text-center">Sign in</h2>
        <hr>  
        <p>Username or email</p> 
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Username" required="required">
        </div>
        <p>Password</p> 
        <div class="form-group">
            <input type="password" class="form-control" placeholder="Password" required="required">
        </div>  
        <div class="clearfix d-flex justify-content-between">
            <label class="form-check-label"><input type="checkbox"> Remember me</label>
            <a href="#" class="text-start">Forgot your Password?</a>
        </div> 
        <div class="form-group d-grid gap-2">
          <button type="submit" class="btn btn-success btn-block">Sign in</button>
      </div>       
    </form>
</div>
```

