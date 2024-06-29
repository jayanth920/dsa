//O(n^2)
 //https://www.youtube.com/watch?v=BJkpnxf5cfY - Watch the link to refresh over this
//Bad Algo for larger datasets
//Better Approach below:

const bubbleSort = (arr) => {
    const n = arr.length;
  
    for (let i = 0; i < n - 1; i++) {
      for (let j = 0; j < n - 1 - i; j++) {
        if (arr[j] > arr[j + 1]) {
          temp = arr[j + 1];
          arr[j + 1] = arr[j];
          arr[j] = temp;
        }
      }
    }
    console.log(arr);
  };
  
  bubbleSort([3, 1, 9, 6, 2, 99]);



  //This is an approach as well 
  function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                // Swap elements
                let temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
            }
        }
        n--; // Optimization: reduce the range of the next iteration
    } while (swapped);
    return arr;
}
