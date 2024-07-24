function solve(mapping, nums) {
    const mapper = (num) => {
      const newnum = num.toString();
      let tmpnum = "";
      for (let i = 0; i < newnum.length; ++i) {
        tmp = mapping[newnum[i]];
        tmpnum += String(tmp);
      }
      return Number(tmpnum)
    };
  
    const mappedNums = nums.map(num => [mapper(num),num])
    mappedNums.sort((a,b) => a[0]-b[0])
    const res = mappedNums.map(item => item[1]);
    console.log(res)
  }
  
  solve([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]);