#include <bits/stdc++.h>
using namespace std;

int arr[10001];

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        arr[num] += 1;
    }



    int flag = 0,i;

    for (i = 0; i < 10001; i++)
    {

        if(i != 10000) arr[i+1]+=arr[i]/2;
        
        if (arr[i]%2 == 1) flag++;
    }

    cout << flag << endl;

    return 0;
}
