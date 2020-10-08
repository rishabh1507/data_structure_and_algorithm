void flatten(TreeNode *root)
{
    if (root == nullptr)
    {
        return;
    }
    stack<TreeNode *> st;
    st.push(root);
    while (!st.empty())
    {
        TreeNode *current = st.top();
        st.pop();
        if (current->right != nullptr)
        {
            st.push(current->right);
        }
        if (current->left != nullptr)
        {
            st.push(current->left);
        }
        if (!st.empty())
        {
            current->right = st.top();
        }
        current->left = nullptr;
    }
}
}
;