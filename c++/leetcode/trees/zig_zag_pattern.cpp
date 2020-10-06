vector<vector<int>> zigzagLevelOrder(TreeNode *root)
{
    //         check null
    if (root == nullptr)
    {
        return {};
    }
    //         make a deque vector vector
    vector<vector<int>> result;
    deque<TreeNode *> q;
    q.push_back(root);
    bool reverse = true;
    // iterate queue make a deq and vector in second loop
    while (!q.empty())
    {
        int count = q.size();
        deque<TreeNode *> q2;
        vector<int> res2;
        for (int i = 0; i < count; i++)
        {
            //                 store front of q and pop it
            TreeNode *curr = q.front();
            q.pop_front();
            res2.push_back(curr->val);
            //                 check reverse and 2 if
            if (reverse == true)
            {
                if (curr->left != nullptr)
                {
                    q2.push_front(curr->left);
                }
                if (curr->right != nullptr)
                {
                    q2.push_front(curr->right);
                }
            }
            else
            {
                if (curr->right != nullptr)
                {
                    q2.push_front(curr->right);
                }
                if (curr->left != nullptr)
                {
                    q2.push_front(curr->left);
                }
            }
        }
        //           inser in main q the q2
        q.insert(q.end(), q2.begin(), q2.end());
        result.push_back(res2);
        reverse = !reverse;
    }
    return result;
}
}
;