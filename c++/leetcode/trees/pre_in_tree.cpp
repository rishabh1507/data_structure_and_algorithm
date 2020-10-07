TreeNode *Helper(vector<int> &pre, vector<int> &in, int inS, int inE, int preS, int preE)
{
    if (inS > inE)
    {
        return NULL;
    }
    int rootData = pre[preS];
    int rootIndex = -1;
    for (int i = inS; i <= inE; i++)
    {
        if (rootData == in[i])
        {
            rootIndex = i;
            break;
        }
    }
    TreeNode *root = new TreeNode(rootData);
    int linS = inS;
    int linE = rootIndex - 1;
    int rinS = rootIndex + 1;
    int rinE = inE;
    int lpreS = preS + 1;
    int lpreE = linE - linS + lpreS;
    int rpreS = lpreE + 1;
    int rpreE = preE;
    root->left = Helper(pre, in, linS, linE, lpreS, lpreE);
    root->right = Helper(pre, in, rinS, rinE, rpreS, rpreE);
    return root;
}
TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
{
    return Helper(preorder, inorder, 0, inorder.size() - 1, 0, preorder.size() - 1);
}