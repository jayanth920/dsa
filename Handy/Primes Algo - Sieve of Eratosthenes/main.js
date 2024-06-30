function sieve(n) {
    let arr = Array(n).fill(1); // Initialize array with 1 (true) for potential primes
    arr[0] = 0; // 0 and 1 are not prime numbers
    arr[1] = 0;
    //[0,0,1,1]
    let len = Math.floor(Math.sqrt(n));
    for (let i = 2; i <= len; i++) { // Loop through potential primes up to sqrt(n)
      if (arr[i] === 1) { // If i is a prime number
        for (let m = i * i; m < n; m += i) { // Mark multiples of i as not prime
          arr[m] = 0;
        }
      }
    }
  
    return arr.filter(j => j == 1).length; // Return the array of prime indicators
  }
  
  console.log(sieve(10)); // Test the sieve function with n = 7