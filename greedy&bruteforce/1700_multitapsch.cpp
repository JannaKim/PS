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
    bool valids[102]; 
    memset(valids,false,102);//loc var should be initialized
    int initPlug=0;
    int i;
    for(i=0;i<k;++i)
    {
        if(valids[app[i]]==false){
            valids[app[i]]=true;
            on.push_back(app[i]);
            initPlug++;
        }
        if(initPlug==n) break;
    }
    int left=n-initPlug;
    while(left--){
        on.push_back(0);
    }
    int cnt=0;
    for(;i<k;++i)
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
            int last_to_be_used=0;
            for(int j=i+1;j<k;++j)
            {
                for(auto it: on){
                    if(it==app[j]){
                        if(check[app[j]]==false){
                            check[app[j]]=true;
                            checked++;
                        }
                        last_to_be_used=app[j];
                        break;
                    }
                }
                if(checked==n){ //all plugged app is valid: plug out anything= x, unplug lastly used?
                    break;
                }
                
            }

            // plug out last_ or plugged app that is "no more used" exists
                for(auto& it: on){
                    if((check[it]==false && checked!=n) || (it==last_to_be_used&& checked==n)){// plug out anything no more used
                        for(auto it: on) printf("%d ",it);
                        printf("->\n");
                        it=app[i];
                        for(auto it: on) printf("%d ",it);
                        printf("\nㅡㅡ\n");
                        
                        cnt++;
                        break;
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



