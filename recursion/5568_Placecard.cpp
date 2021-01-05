// 5568 카드 놓기
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iostream>
#include <set>
#include <string>
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
    selection(0,0,0, "");
    cout<<ans.size();

}
// floor: 몇번째 인풋인지
// sel: 지금까지 몇개 골랐는지
// 비트마스크: 뭘 골랐는지
// string s: 지금까지 고른 애들 이어붙인거

void selection(int floor,int sel,int bit,string s)
{
    if(floor== n+1) // 초과: 재귀 끝냄
        return;
    if(sel==k){ // k개 골랐으니 재귀 끝냄
        ans.insert(s);
        return;
    }
    for(int i=0;i<n;++i){ //nPk용 포문
        if( (1<<i) & bit ) continue;
        int newbit= (1<<i)| bit;
        selection(floor+1, sel+1, newbit,s+ls[i]);
    }

}