 symbols = {
     "I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000
 };

var romanToInt = (s) => {
    let value = 0;
    for(let i = 0; i < s.length; i++) {
        if (symbols[s[i]] < symbols[s[i+1]]) {
            value -= symbols[s[i]];
        }
        else {
            value += symbols[s[i]];
        }
    }
    return value;
};
// const romanToInt=s=>[...s].reduce((a,c,i)=>a+(y[c]<y[s[++i]]?-y[c]:y[c]),0);y={I:1,V:5,X:10,L:50,C:100,D:500,M:1e3}