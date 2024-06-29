function insertionSort(arr) {
  const n = arr.length;
  for (let i = 1; i < n - 1; i++) {
    while (i > 0) {
      if (arr[i] < arr[i - 1]) {
        [arr[i], arr[i - 1]] = [arr[i - 1], arr[i]];
      }
    }
  }
  return arr;
}
console.log(insertionSort([9, 4, 3, 7, 5, 1]));
