#include <bits/stdc++.h>
using namespace std;

// void swap(int* a[5],int i,int pos);

void swap(int a[5], int i, int pos)
{
    int temp;
    temp = a[i];
    a[i] = a[pos];
    a[pos] = temp;
}

void nflag(int a[5], int n)
{
    int low = 0;
    int high = n - 1;
    int mid = 0;
    while (mid <= high)
    {
        if (a[mid] == 0)
        {
            swap(a, mid, low);
            mid++;
            low++;
        }
        else if (a[mid] == 1)
        {
            mid++;
        }
        else
        {
            swap(a, mid, high);
            high--;
        }
    }
}

int main()
{
    int a[5] = {0, 1, 0, 1, 2};
    int n = 5;
    int *result;
    nflag(a, n);

    for (int i = 0; i < n; i++)
    {
        cout << a[i];
    }

    return 0;
}