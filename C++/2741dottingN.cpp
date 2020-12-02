#include <iostream>
#include <string>

int main()
{
    int N=0;
    std::cin>>N;
    for(int i=1;i<=N;i++)
    {
        std::string stars(i,'*');
        std::cout<<stars<<'\n';
    }

}