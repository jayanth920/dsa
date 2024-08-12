var plusOne = function(digits) {
    let num = BigInt(digits.join(""));
    num++;
    let up = num.toString().split('').map(Number);
    return up;
};
