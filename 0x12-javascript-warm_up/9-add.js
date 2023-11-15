#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const firstNum = parseInt(arg1);
const secondNum = parseInt(arg2);
if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log('Arguments are not integers.');
} else {
  const result = add(firstNum, secondNum);
  console.log(result);
}
