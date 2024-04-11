#!/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js file1 file2 dest');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

const data1 = fs.readFile(file1, 'utf8', (err, data1) => {
    if (err) {
        console.error(`Error reading ${file1Path}: ${err}`);
        process.exit(1);
    }
    return data1;
});
const data2 = fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
        console.error(`Error reading ${file2Path}: ${err}`);
        process.exit(1);
    }
    return data2;
});

const data = data1 + data2;

fs.writeFile(dest, data, 'utf8', (err) => {
    if (err) {
        console.error(`Error writing ${dest}: ${err}`);
        process.exit(1);
    }
});