function numIdenticalPairs(nums: number[]): number {
    let counter = 0;
    if(!nums.length) return 0;
    for(let i=0 ; i<nums.length; i++){
        for(let j=i+1 ; j<nums.length; j++){
        if(nums[i] === nums[j]){
            counter++;
        }
        }
    }
    return counter
};