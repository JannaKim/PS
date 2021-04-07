#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
    int mx= pow(100,2);
	for(test_case = 1; test_case <= T; ++test_case)
	{

		int n;
        cin>>n;
        int L[100]={0,};
        for(int i=0;i<n;++i){
            cin>> L[i];
        }

        int dp[mx+1]={0,};
        dp[0]=0;
        for(auto a;L)

        

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}