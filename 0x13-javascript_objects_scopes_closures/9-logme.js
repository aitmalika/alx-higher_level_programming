#!/usr/bin/node
/**
 * function  that prints this number of argument already printed and this
 * new argument values
 * @param {item} str - argument passed to function
 * @returns void
 */
let narg = 0;
exports.logMe = function (item) {
  console.log(`${narg}: ${item}`);
  narg++;
};
