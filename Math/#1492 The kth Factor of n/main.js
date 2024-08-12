var kthFactor = function (n, k) {
  if (k > n || n > 1000 || k > 1000 || k < 1 || n < 1) return -1;
  let res = [];
  for (i = 1; i <= n; i++) {
    if (n % i === 0) {
      res.push(i);
    }
  }

  if (!res[k - 1]) return -1;
  return res[k - 1];
};
