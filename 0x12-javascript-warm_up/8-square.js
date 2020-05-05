#!/usr/bin/node
let text
if (process.argv[2] === undefined || (parseInt(process.argv[2]) !== parseInt(process.argv[2]))) {
  console.log('Missing size');
}; 
if (process.argv[2] !== undefined) {  	
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    text = '';	  
    for (j = 0; j < parseInt(process.argv[2]); j++) {     	  
      text += 'X'
    };
    console.log(text);
  }; 	
};
