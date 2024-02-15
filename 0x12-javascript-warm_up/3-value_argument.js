#!/usr/bin/node

// This line specifies the path to the interpreter for this script.

if (process.argv[2] === undefined) {
  // Checks if there is no argument provided when running this script.
  console.log('No argument');
  // If there's no argument, outputs the string 'No argument' to this console.
} else {
  console.log(process.argv[2]);
  // If an argument is provided, outputs the value of this argument
  // (at index 2 in the process.argv array) to this console.
}
