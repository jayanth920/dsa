var flat = function (arr, n) {
    let result = [];

function flattenHelper(arr, depth) {
    arr.forEach((element) => {
        if (Array.isArray(element) && depth < n) {
            flattenHelper(element, depth + 1);
        } else {
            result.push(element);
        }
    });
}

flattenHelper(arr, 0);

return result;
};