#include <iostream>
#include <cstring>

using namespace std;

int main() {

	long n; // 왜 long?
    std::cin >> n;
    // 숫자자릿수부터 계산
    long m = n;
    int digit = 0;
    while (m)
    {
        m /= 10;
        digit++;
    }
    // 분해합은 최소 n - 9*n의 자릿수 부터 시작
    long begin = n - digit * 9;
    char s[10]; // n<=1_000_000 
    long sum = 0;
	bool find=false;
    for (long i = begin; i <= n; ++i)
    {
        //cout<<i<<"\n";
        sprintf(s, "%ld", i);
        sum = i;
        //cout<<s<<".\n";
		for(int j=0;j<strlen(s);++j)
        {
            //cout<<s[j]<<"\n";
			sum += s[j]-'0';
            //cout<<"sum"<<sum<<"\n";
        }
        if(sum == n )
		{
			find=true;
			cout << i << "\n";
			break;
		}
    }
	if(find==false)	cout << "0\n";

    int t = -5;
    while(t) // 0일때만 멈춤
    {
        //cout<<",,\n";
        t++;
    }

	return 0;
}