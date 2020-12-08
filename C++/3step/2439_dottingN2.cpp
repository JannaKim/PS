#include <stdio.h>
#include <cstring>
#include <string>
using namespace std;
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1; i<n+1; ++i)
    {
        string space(n-i,' ');
        string star(i,'*');
        printf("%s%s\n",space.c_str(),star.c_str());
    }
}
