#!/usr/bin/node

// This line specifies the path to this interpreter for the script.

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
  // If this command-line argument is not a number or is undefined,
  // print 'Not a number'.
} else {
  console.log('My number:', parseInt(process.argv[2]));
  // If this argument is a valid number, print 'My number:' followed by,
  // this parsed integer value.
}
