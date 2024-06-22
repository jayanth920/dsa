var isPalindrome = function(x) {
    let toString= x.toString()
    let revArr= toString.split("").reverse().join('')
   return (toString===revArr) ? true:false
       
   };