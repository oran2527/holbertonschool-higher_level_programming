#!/usr/bin/node
module.exports = {
  callMeMoby: function (x, theFunction) {
    for (i = 0; i < parseInt(x); i++) {
      theFunction();
    }  
  }
};  
