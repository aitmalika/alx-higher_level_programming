#!/usr/bin/node
/**
 * function to count number of occurrence in a list
 * @param {list} list - list ti examine
 * @param {number} search Element - element to search for
 * @returns {number} - this number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};
// alternative to arrow function
// list.forEach(function (item) {
//   if (item === searchElement) {
//     i++;
//   }
// });
