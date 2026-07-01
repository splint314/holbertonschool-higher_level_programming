#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const n = process.argv[2];
  for (let i = 1; i <= n; i++) {
    console.log('C is fun');
  }
}
