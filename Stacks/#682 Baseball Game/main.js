var calPoints = function (operations) {
    let record = [];
    for (var item of operations) {
      if (item == "+") record.push(record[record.length - 2] + record[record.length - 1])
      else if (item == "D") record.push(2 * record[record.length - 1]);
      else if (item == "C") record.pop();
      else record.push(+item);
    }
    let totalSum = record.reduce((a, c) => {
      return a + c;
    }, 0);
    return totalSum;
  };