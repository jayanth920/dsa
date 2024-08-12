var reversePrefix = function(word, ch) {
// abcdef , d
  let myword = word.split("");
  if(!myword.indexOf(ch)) return word
  let cutIndex = myword.indexOf(ch);
  let i = cutIndex+1;
  //LEFT
  let left = myword.slice(0, i).reverse().join("");
  
  //RIGHT
  let right = myword.slice(i, myword.length).join("")
  left+=right

  return(left)
};