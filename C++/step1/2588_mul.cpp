#include <iostream>
#include <string>
using namespace std;
int main()
{
    int a, b;
    //문자열? 인덱싱?
    string s;
    int n;
    cin>>s;
    string hi= " Hello, "+ s+ "! ";
    string fst(hi.size()+2,'*');
    string space(hi.size(),' ');
    string scnd='*'+space+'*';
    n = scnd.size()/2;
    int m= (n-1)>>1;
    for(int i=0;i<n;i++)
    {
        if(i==0 || i==n-1)
        {
            cout<<fst<<endl;
        }
        else if(i==m)
        {
            cout<<"*"+hi+"*"<<endl;
        }
        else
        {
            cout<<scnd<<endl;
        }
    }



}