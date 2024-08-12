var shuffle = function(nums, n) {
  let nums1 = nums.slice(0,n)
  let nums2 = nums.slice(n) 
  let result = [];

  for(let i=0; i < n ; i++){
    result.push(nums1[i])
    result.push(nums2[i])
  }

  return result
};