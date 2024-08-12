var inorderTraversal = function(root) {
    const result = []
    function helper(node){
        if(node === null) return
        helper(node.left);
        result.push(node.val);
        helper(node.right);
        }
    helper(root)
    return result;
};