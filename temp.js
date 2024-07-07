function bubbleSort(arr){
  let n = arr.length
  for(i=0;i<n-1;++i){
    for(j=0;j<n-i-1;++j){
      if(arr[j] > arr[j+1]){
        [arr[j],arr[j+1]]=[arr[j+1],arr[j]]
      }
    }
  }
  return arr
}

console.log(bubbleSort([8,3,4,6,1,5,12,99,43,13,65]))