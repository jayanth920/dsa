// // O(min(n1,n2)) - Brute Force
// function gcdandlcm(n1,n2){
//     let gcd = 1;
//     let lcm = 0
//     let sm;
//     if(n1 < n2){
//         sm = n1
//     } else {
//         sm = n2
//     }
//     for(let i=1; i<=sm; i++){
//         if(n1%i == 0 && n2%i == 0){
//             gcd = i
//         }
//     }

//     lcm = (n1 * n2)/gcd
//     return {
//         gcd,
//         lcm
//     }
// }

// console.log(gcdandlcm(10,5))

//Optimal approach using Eucledian Algorithm
//https://takeuforward.org/data-structure/find-gcd-of-two-numbers/

function gcd(n1, n2) {
  if (n2 === 0) {
    console.log("Returning n1")
    return n1;
  }
  let sm = Math.min(n1, n2);
  let bg = Math.max(n1, n2);
  console.log(`gcd(${sm},${bg%sm})`);
  return gcd(sm, bg % sm);
}

console.log(gcd(20, 15));
