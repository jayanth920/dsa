//Recursive
function binarySearchRecursive(arr, target, left, right) {
    if (left > right) {
        return -1;  // Target not found
    }

    let mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid + 1, right);
    } else {
        return binarySearchRecursive(arr, target, left, mid - 1);
    }
}

// Example usage
let arr = [1, 2, 3, 4, 5, 6, 7];
let target = 5;
console.log(binarySearchRecursive(arr, target, 0, arr.length - 1));  // Output: 4
