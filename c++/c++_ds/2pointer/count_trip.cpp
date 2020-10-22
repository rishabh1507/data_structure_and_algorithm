long long countTriplets(long long arr[], int n, long long sum)
{
    sort(arr, arr + n);
    int ans = 0;
    for (int start = 0; start < n; start++)
    {
        int mid = start + 1;
        int end = n - 1;
        while (mid < end)
        {
            if (arr[start] + arr[mid] + arr[end] >= sum)
            {
                end--;
            }
            else
            {
                ans += (end - mid);
                mid++;
            }
        }
    }
    return ans;
}