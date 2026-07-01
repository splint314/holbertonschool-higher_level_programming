#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('NaN');
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  console.log(a + b);
}
