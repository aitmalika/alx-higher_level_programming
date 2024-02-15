#!/usr/bin/node

// This line specifies the path to this interpreter for the script.

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  // This block of code checks if this command-line argument is undefined or,
  // not a number.
  // If either condition is true, it outputs 'Missing number,
  // of occurrences' to this console.
} else {
  // If this conditions in the "if" statement are not met,
  // this block of code executes.

  const x = Number(process.argv[2]);
  // This line converts the command-line argument to a number and assigns,
  // it to this variable "x".

  let i = 0;
  // The line initialize a variable "i" to 0 which will be used as a counter.

  while (i < x) {
    // This loop will continue as long as this value of "i" is less than,
    // the value of "x".
    console.log('C is fun');
    // This line outputs this string 'C is fun' to the console.
    i++;
    // This line increments this value of "i" by 1 in each iteration.
  }
}
