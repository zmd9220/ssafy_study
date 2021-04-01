# django_05_workshop





### 1. 모델 폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오.

> forms의 모델폼, 메타데이터를 정의하는 메타클래스

``` python
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        field = '__all__'
```





### 2. 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

> POST 요청으로 들어왔는데, 유효성 검사에서 통과하지 못한 경우 리턴이 없어서 문제가 발생합니다. 이를 방지하기 위해 마지막에 리턴하는 함수를 넣어주는데 이것이 GET의 리턴과 동일하게 변수를 넣어 작동하므로 GET 부분의 context와 리턴을 꺼내서 같이 사용합니다.

``` python
def create(request):
	if request.method == 'POST':
        pass
    else:
        pass
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)
```





### 3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

> 양 쪽다 form을 가져오는 부분인데 a는 POST 요청이므로 수정 반영된 결과, b는 get이므로 수정하기전 원본 데이터를 가져오는 역할을 해야합니다. 둘다 기존 db 데이터를 받아 작동하므로 해당하는 instance를 인자로 넣어서 인식하게 해줘야합니다.

``` python
# a
form = ReservationForm(request.POST, instance=reservation)
# b
form = ReservationForm(instance=reservation)
```





### 4. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

> 대표적으로 p와 ul을 사용합니다 table은 거의 사용 X

``` django
<!-- a -->
{{ form.as_p }}
{{ form.as_ul }}
```

