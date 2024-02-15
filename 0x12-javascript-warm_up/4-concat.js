#!/usr/bin/node

// This line specifies the path to the interpreter for this script.

console.log(process.argv[2] + ' is ' + process.argv[3]);
// This line accesses command-line arguments using this "process.argv" array.
// It concatenates the value at index 2 with the string  is and this value,
// at index 3, then outputs the resulting string to this console
// This can be used to display a custom message using command-line argument
