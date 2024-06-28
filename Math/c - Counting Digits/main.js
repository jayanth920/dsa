function countDigits(n) {
    // Initialize a counter variable
    // 'cnt' to store the count of digits.
    let cnt = 0;
    // While loop iterates until 'n'
    // becomes 0 (no more digits left).
    while (n > 0) {
        // Increment the counter
        // for each digit encountered.
        cnt = cnt + 1;
        // Divide 'n' by 10 to
        // remove the last digit.
        n = Math.floor(n / 10);
    }
    // Return the
    // count of digits.
    return cnt;
}

console.log(countDigits(489237))