#include <stdio.h>

int main()
{
    int ans = 0;
    for(int i = 0; i < 10; ++i)
    {
        for(int j = 0;j < 10;++j)
        {
            for(int k = 0; k < 10;++k)
            ans += 15;
        }
        ans -=10;
    }
    printf("%d %d",ans, 15*1000-100);
}