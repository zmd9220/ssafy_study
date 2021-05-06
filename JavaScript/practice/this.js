const name = '유재석'

const home = {
  name: '김재석',
}

function call() {
  console.log(this.name)
}

// 유재석
call()

// 김재석
home.call = call
home.call()