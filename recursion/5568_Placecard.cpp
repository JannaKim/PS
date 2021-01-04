#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iostream>
#include <set>
using namespace std;

vector<string> ls;
set <string> ans;
int n;
int k;
void selection(int floor,int sel,int bit,string s);

int main()
{

scanf("%d\n", &n);
scanf("%d\n", &k);


for(int i=0;i<n;++i)
{
    string x;
    getline(cin,x);
    ls.push_back(x);
}

selection(0,0,0<<(n-1), NULL);
cout<<ans.size();

}
void selection(int floor,int sel,int bit,string s)
{
    if(floor== n+1) // 초과
        return;
    if(sel==k){
        ans.insert(s);
        return;
    }
    for(int i=0;i<n;++i){
        if( (1<<i) & bit ) continue;
        int newbit= (1<<i)| bit;
            selection(floor+1, sel+1, newbit,s+ls[i]);
    }
}
