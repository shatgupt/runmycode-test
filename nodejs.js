/*
  This program won't run properly without an input.
  Try with: abc
*/
console.log('Hello World from Nodejs!')
console.log(require('fs').readFileSync(0).toString())
