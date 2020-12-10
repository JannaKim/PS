#include <vector>



long long sum(std::vector<int> &a){
    int sum=0;
    for(auto i:a)
    {
        sum+=i;
    }
    return sum;
}