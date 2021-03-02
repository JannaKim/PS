#include <iostream>
int n;
using namespace std;
vector<int> input;
int ans = 0;
void recur(int idx, int count, bool arr[]){

    if(arr[idx]){
        ans = max(ans,count+1); return;
    }
    arr[idx] = true;
    int nextidx = (idx + input[idx]);
    if(nextidx<0 || nextidx>=n){
        ans = max(ans,count); return;
    }
    recur(nextidx,count+1,arr);

}
int main(){
    cin>>n;
    input.resize(n);
    for(int i=0; i<n; i++) cin>>input[i];
    bool arr[101]={};
    recur(0,0,arr);
   
    recur(1,0,arr);
    recur(2,0,arr);
    cout<<ans;
}