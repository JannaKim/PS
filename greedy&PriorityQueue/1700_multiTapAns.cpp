#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <iterator>
#include <string.h>
using namespace std;

int main()
{
    vector<int> app;
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < k; ++i)
    {
        int x;
        scanf("%d", &x);
        app.push_back(x);
    }
    vector<int> on;

    int cnt = 0;
    for (int i = 0; i < k; ++i)
    {
        int chk = false;
        for (auto it : on)
        {
            if (it == app[i])
                chk = true;
        }
        if(chk) continue;
        if(on.size() < n){
            on.push_back(app[i]);
            continue;
        }

        int last_to_be_used = 0, check_cnt = 0;
        bool check[102];
        memset(check, false, 102); //loc var should be initialized
        for (int j = i + 1; j < k; ++j)// check all left app: plugged, or not?
        {
            for (auto it : on) 
            {
                if (app[j] == it) //plugged
                {
                    if (check[it] == false) // newly plugged
                    {
                        check_cnt++;
                    }
                    check[it] = true;
                    last_to_be_used = it; //?
                    break;
                }
            }
            if(check_cnt == n)//?
                break;
        }
        for (auto& it : on)
        {
            if ((check[it] == false && check_cnt < n) || (it == last_to_be_used && check_cnt == n))
            {
                // plug out anything no more used
                it = app[i];
                cnt++;
                break;
            }
        }
    }
    printf("%d\n", cnt);
}