
// 1. object destructuring

const fruits = {
  apple,
  banana,
}

// 1-1
const apple = fruits.apple
const banana = fruits.banana
// 1-2
const { apple, banana } = fruits

// 2. object destructuring
/*
 * @param { apple, banana } fruits
 */
const handleFruits = function ({ apple, banana }) {
  apple
  banana
}
handleFruits(fruits)

// 3. array destructuring
const fruits = ['apple', 'banana']
// a = apple, b = banana (a만 쓰면 apple만 지정됨)
const [a, b] = fruits
console.log(a, b)


// 이 코드는 좋다
const student = {
  name: '홍길동'
}

// 1.
colsole.log(Object.entries(struent))
Object.entries(student).forEach(items => {
  // console.log(items) // [key, value]
  const [key, value] = items
  console.log(key, value)
})

// 2. 
Object.entries(student).forEach(([key, value]) => {
  console.log(key, value)
})