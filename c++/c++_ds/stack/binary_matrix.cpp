void fillleft(vector<int> &left, vector<int> &hist)
{
    stack<int> s;
    int extreme = -1;
    for (int i = 0; i < hist.size(); i++)
    {
        if (s.empty())
        {
            left.push_back(extreme);
        }
        else if (hist[s.top()] < hist[i])
        {
            left.push_back(s.top());
        }
        else
        {
            while (!s.empty() && hist[s.top()] >= hist[i])
            {
                s.pop();
            }
            if (s.empty())
            {
                left.push_back(extreme);
            }
            else
            {
                left.push_back(s.top());
            }
        }
        s.push(i);
    }
}

void fillright(vector<int> &right, vector<int> &hist)
{

    stack<int> s1;
    int extreme = hist.size();
    for (int i = hist.size() - 1; i >= 0; i--)
    {
        if (s1.empty())
        {
            right.push_back(extreme);
        }
        else if (hist[s1.top()] < hist[i])
        {
            right.push_back(s1.top());
        }
        else
        {
            while (!s1.empty() && hist[s1.top()] >= hist[i])
            {
                s1.pop();
            }
            if (s1.empty())
            {
                right.push_back(extreme);
            }
            else
            {
                right.push_back(s1.top());
            }
        }
        s1.push(i);
    }
    reverse(right.begin(), right.end());
}

int largestarea(vector<int> &hist)
{
    vector<int> left;
    vector<int> right;
    vector<int> area;
    fillleft(left, hist);
    fillright(right, hist);

    for (int i = 0; i < hist.size(); i++)
    {
        int width = right[i] - left[i] - 1;
        int answer = hist[i] * width;
        area.push_back(answer);
    }
    int max1 = *max_element(area.begin(), area.end());
    return max1;
}

int maxArea(int M[MAX][MAX], int n, int m)
{
    // Your code here
    // make a matrix of
    vector<vector<int>> matrix(n, vector<int>(m));
    // vector<vector<int>>matrix(n, vector<int>(m));
    vector<int> arr(m);
    for (int i = 0; i < m; i++)
    {
        arr.push_back(M[0][i]);
    }

    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[0].size(); j++)
        {
            matrix[i][j] = M[i][j];
        }
    }
    for (int i = 1; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[0].size(); j++)
        {
            if (M[i][j] == 1)
            {
                matrix[i][j] = 1 + matrix[i - 1][j];
            }
            else
            {
                matrix[i][j] = 0;
            }
        }
    }

    int answer = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        answer = max(answer, largestarea(matrix[i]));
    }
    return answer;
}