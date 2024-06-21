//1 Hash Table (Single pass) O(n) + Map storage optimisation based on nums - CLEVER, EXCELLENT
//2 Hash Table (Double pass) O(n) - GOOD
//3 Brute force O(n^2) - Dont know hash table ay, BASIC

//CHECK main.py for explanation

//-------------1------------------------
function twoSum(nums, target) {
    const myMap = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
            if (myMap.has(complement)) {
                return [myMap.get(complement), i];
            }
    
            myMap.set(nums[i], i);
        }
    
        return [];
    }
    
//---------------2---------------------
function twoSum(nums, target) {
    const myMap = new Map();
    const n = nums.length;

    // First pass to fill the map
    for (let i = 0; i < n; i++) {
        myMap.set(nums[i], i);
    }

    // Second pass to find the complement
    for (let i = 0; i < n; i++) {
        const complement = target - nums[i];
        if (myMap.has(complement) && myMap.get(complement) !== i) {
            return [i, myMap.get(complement)];
        }
    }

    return [];
}
//--------------------3----------------------
function twoSum(nums, target) {
    const n = nums.length;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }

    return [];
}

//-------------------------------------------

// Test cases
console.log(twoSum([2, 7, 11, 15], 9));  // Output: [0, 1]
console.log(twoSum([3, 2, 4], 6));       // Output: [1, 2]
console.log(twoSum([3, 3], 6));          // Output: [0, 1]