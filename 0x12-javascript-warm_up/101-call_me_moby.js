#!/usr/bin/node

exports.getMeMoby = function (number, theFunction) {
  for (let i = 0; i < number; i++) {
    theFunction();
  }
};
