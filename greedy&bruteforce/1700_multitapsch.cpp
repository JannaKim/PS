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
    scanf("%d %d",&n, &k);
    for(int i=0;i<k;++i)
    {
        int x;
        scanf("%d",&x);
        app.push_back(x);
    }
    vector<int> on;
    for(int i=0;i<n;++i)
    {
        on.push_back(app[i]);
    }


    int cnt=0;
    for(int i=n;i<k;++i)
    {

        bool pass=false;
        for(auto it:on)
        {
            //printf("%d %d\n",it, app[i]);
            if(it==app[i]) pass=true;
        }
        //printf("\n");
        if(pass==false){ //app[i] unplugged: should be switched
            bool check[102]; 
            memset(check,false,102);//loc var should be initialized
            int checked=0;
            for(int j=i+1;j<k;++j)
            {
                if(check[app[j]]==false){
                    check[app[j]]=true;
                    checked++;
                }
                if(checked==n){ //all plugged app is valid: plug out anything
                    int popped= on.back();
                    on.pop_back();
                    on.push_back(app[i]);
                    cnt++;
                    //printf("%d뽑고 %d넣음\n",popped,app[i]);
                    break;
                }
            }

            if(checked!=n){// plugged app that is "no more used" exists
                for(auto& it: on){
                    if(check[it]==false){// plug out anything no more used
                        it=app[i];
                        cnt++;
                        break;
                    }
                }
            }

            
        }
    }
    printf("%d\n",cnt);

}

/*

2 7
2 3 1 2 2 3 2 2 2 

3 7
2 3 4 5 3 2 2
2. 앞에 n개 플러그 꼽음
3. n+1번째부터 for문 돌려서 플러그에 꽂혀있으면 pass
4. 아니면 현재 이후 ~ 마지막까지 포문 돌려서
현재 기구가 플러그에 꽂혀있다면 체크. 

    if 도는 중에 전부다 체크되면 break, 아무거나 뽑음 cnt+=1
    elif 체크안된애가 있다면 그 중 아무거나 뽑음cnt+=1

print cnt
*/


