#!/usr/bin/node
module.exports = {
  callMeMoby: function callMeMoby (a, b) {
    for (i = 0; i < parseInt(a); i++) {
      b();
    }  
  }
};  
