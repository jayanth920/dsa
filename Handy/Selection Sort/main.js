//O(n^2)
function selectionSort(arr) {

  for (let i = 0; i < arr.length - 1; i++) {
    let mi = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[mi]) {
        mi = j;
      }
    }
    if (mi !== i) {
      [arr[i], arr[mi]] = [arr[mi], arr[i]];
    }
  }

  return arr
}

console.log(selectionSort([4,1,7,5,0,2]))