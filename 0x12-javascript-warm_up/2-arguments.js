#!/usr/bin/node

// This line specifies this path to the interpreter for the script.

if (process.argv.length === 2) {
  // The condition checks if there are exactly 2
  // elements in this process argv array.
  // If true it means no additional command line arguments were provided
  // besides this script name.
  console.log('No argument');
  // Outputs the string 'No argument' to this console
} else if (process.argv.length === 3) {
  // This condition checks if there are exactly 3 element in this process argv.
  // If true, it mean one additional command line argument was provided
  console.log('Argument found');
  // Output this string 'Argument found' to the console.
} else {
  // If neither of this above conditions is met, it means
  // more than one additional comman line argument was provided.
  console.log('Arguments found');
  // Outputs the string 'Arguments found' to this console.
}
