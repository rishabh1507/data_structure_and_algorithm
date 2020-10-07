TreeNode *Helper(vector<int> &in, vector<int> &post, int inS, int inE, int posS, int posE)
{
    if (inS > inE)
    {
        return NULL;
    }
    int rootData = post[posE];
    int rootIndex = -1;

    for (int i = inS; i <= inE; i++)
    {
        if (in[i] == rootData)
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
    int lposS = posS;
    int lposE = posS + rootIndex - inS - 1;
    int rposS = posS + rootIndex - inS;
    int rposE = posE - 1;
    root->left = Helper(in, post, linS, linE, lposS, lposE);
    root->right = Helper(in, post, rinS, rinE, rposS, rposE);
    return root;
}
TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder)
{
    return Helper(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1);
}