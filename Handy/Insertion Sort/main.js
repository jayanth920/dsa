//O(n^2)
function insertionSort(arr) {
    const n = arr.length;
    for (let i = 1; i < n; i++) {
      let j = i;
      while (j > 0 && arr[j] < arr[j - 1]) {
        [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
        j--;
      }
    }
    return arr;
  }
  
  console.log(insertionSort([9, 4, 3, 7, 5, 1]));


  //Recursive 
  function insertionSortRecursive(arr, i = 1) {
    const n = arr.length;
    if (i === n) return arr;

    let j = i;
    while (j > 0 && arr[j] < arr[j - 1]) {
      [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
      j--;
    }
    return insertionSortRecursive(arr, i + 1);
  }
  
  console.log(insertionSortRecursive([9, 4, 3, 7, 5, 1])); // Output: [1, 3, 4, 5, 7, 9]
  