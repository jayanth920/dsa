function prime(n) {
    let count = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            count++;
            if (n / i !== i) {
                count++;
            }
        }
    }
    
    if (count === 2) {
        return true;
    } else {
        return false;
    }
}

console.log(prime(10)); // Output: true
