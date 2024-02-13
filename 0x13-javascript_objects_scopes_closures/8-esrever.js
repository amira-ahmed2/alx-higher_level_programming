#!/usr/bin/node
exports.esrever = function (list) {
  reverse_list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverse_list.push(list[i]);
  }
  return reverse_list;
};
