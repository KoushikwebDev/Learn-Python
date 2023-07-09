let str = "Koushikm\b Saha";
console.log(str);

console.log("1" + 2);

console.log(Number("H"));

for (let i = 0; i < str.length; i++) {
  //   console.log(str[i]);
}

for (let x in str) {
  //   console.log(x + " " + str[x]);
}

for (let x of str) {
  console.log(x);
}

console.log();

if (5 == 5) {
  console.log("print");
  if (true) {
    console.log("Nested");
  }
}

let x = 12;

switch (x) {
  case 0:
    console.log("Value not matched");
    break;
  case 10:
    console.log("Value matched");
    break;

  case x < 20:
    console.log("X less than 20");
    break;
  default:
    console.log("Default value");
    break;
}

let name = "Koushik";
for (x in name) {
  console.log(x + name[x]);
}

let xx = 0;
do {
  console.log("do while");
  xx = xx - 1;
} while (xx > 10);

let arr = [1];

console.log(arr[2]); // undefined

function myFunction() {}

let arr2 = [1, 2, 3];
console.log(arr2.reverse());
