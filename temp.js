// function bubbleSort(arr){
//   let n = arr.length
//   for(i=0;i<n-1;++i){
//     for(j=0;j<n-i-1;++j){
//       if(arr[j] > arr[j+1]){
//         [arr[j],arr[j+1]]=[arr[j+1],arr[j]]
//       }
//     }
//   }
//   return arr
// }
// console.log(bubbleSort([8,3,4,6,1,5,12,99,43,13,65]))


function runner(nums){
    let inc =  false
    let dec =  false
  
    for(let i=1;i<nums.length;i++){
      if(nums[i] > nums[i-1]){
        inc = true
      }
      if(nums[i] < nums[i-1]){
        dec = true
      }
    }
  
    return !(inc && dec)
  }
  
  console.log(runner([1, 2, 2, 3])); // true (non-decreasing)
  console.log(runner([6, 5, 4, 4])); // true (non-increasing)
  console.log(runner([5,2,7,1,5,3,9,4])) // false