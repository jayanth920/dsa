// Bad Beginner Way
function countPrimes(n) {
  let primes = [];

  for (i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }
  return primes.length;
}

function isPrime(m) {
  let c = 0;
  for (let i = 1; i < Math.floor(Math.sqrt(m) + 1); i++) {
    if (m % i == 0) {
      c = c + 1;
      if (Math.floor(m / i) !== i) {
        c = c + 1;
      }
    }
  }
  if (c == 2) {
    return true;
  } else return false;
}

console.log(countPrimes(11));

//----------------------
// function countPrimes(n) {
//     if(n <= 2) return 0
//     if(n == 3) return 1
//     if(n == 5) return 2
// return Math.floor(n/Math.log(n))
// }
// console.log(countPrimes(5));
