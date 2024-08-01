function mergesort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  let mid = Math.floor(arr.length / 2);
  let left = arr.slice(0, mid);
  let right = arr.slice(mid);
  console.log(left)
  console.log(right)
  return merge(mergesort(left), mergesort(right));
}

function merge(left, right) {
    let res = []
    let li = 0
    let ri = 0

    while (li<left.length && ri<right.length){
        if (left[li] < right[ri]){
            res.push(left[li])
            li+=1
        } else{
            res.push(right[ri])
            ri+=1
        }

    }

    return res.concat(left.slice(li)).concat(right.slice(ri));
}

console.log(mergesort([4, 2, 3, 8, 6, 5, 7, 1]));
