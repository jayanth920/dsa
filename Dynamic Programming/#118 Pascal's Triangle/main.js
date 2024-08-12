var generate = function(numRows) {
  if (numRows === 0) {
    return [];
  }

  const result = [];

  for (let i = 0; i < numRows; i++) {
    const row = generateNextRow(result[i - 1]);
    result.push(row);
  }

  return result;
};

// Helper function to generate the next row
function generateNextRow(prevRow) {
  if (!prevRow) {
    return [1];
  }

  const nextRow = [1];

  for (let i = 0; i < prevRow.length - 1; i++) {
    const sum = prevRow[i] + prevRow[i + 1];
    nextRow.push(sum);
  }

  nextRow.push(1);

  return nextRow;
}