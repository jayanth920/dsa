var reverse = function(x) {
    const revInt = Math.abs(x).toString().split('').reverse().join('');
    if (revInt > 2**31) return 0;
    if (revInt < 2**-31) return 0;
}