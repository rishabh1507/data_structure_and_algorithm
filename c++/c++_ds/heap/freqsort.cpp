#include <bits/stdc++.h>
using namespace std;

vector<int> kfreq(int *arr, int n)
{
	unordered_map<int, int> mp;
	vector<int> rest;
	int temp;
	int num;
	int freq;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
	for (int i = 0; i < n; i++)
	{
		mp[arr[i]]++;
	}

	for (auto m : mp)
	{
		q.push({m.second, m.first});
	}
	while (q.size() > 0)
	{
		freq = q.top().first;
		num = q.top().second;
		for (int i = 0; i < freq; i++)
		{
			rest.push_back(num);
		}
		q.pop();
	}
	reverse(rest.begin(), rest.end());
	return rest;
}

int main()
{
	int n;
	int arr[10000];
	cin >> n;
	vector<int> result;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	result = kfreq(arr, n);
	for (auto t : result)
	{
		cout << t << " ";
	}

	return 0;
}



// max heap

#include <bits/stdc++.h>
using namespace std;

vector<int> kfreq(int *arr, int n)
{
	unordered_map<int, int> mp;
	vector<int> rest;
	int temp;
	int num;
	int freq;
	priority_queue<pair<int, int>> q;
	for (int i = 0; i < n; i++)
	{
		mp[arr[i]]++;
	}

	for (auto m : mp)
	{
		q.push({m.second, m.first});
	}
	while (q.size() > 0)
	{
		freq = q.top().first;
		num = q.top().second;
		for (int i = 0; i < freq; i++)
		{
			rest.push_back(num);
		}
		q.pop();
	}
	// reverse(rest.begin(),rest.end());
	return rest;
}

int main()
{
	int n;
	int arr[10000];
	cin >> n;
	vector<int> result;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	result = kfreq(arr, n);
	for (auto t : result)
	{
		cout << t << " ";
	}

	return 0;
}