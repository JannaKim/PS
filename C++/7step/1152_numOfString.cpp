#include <iostream>
#include <cctype> // isspace
#include <vector>
#include <string>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
using namespace std;

/*
vector<string> split(const string&s)
{
    vector<string> ret;
    auto string_size = s.size();
    int i=0;
    while(i!=string_size)
    {
        while(i!=string_size && isspace(s[i])) i++;
        //i: index of first alphabet

        int j = i;
        while(j<string_size && !isspace(s[j])) j++;

        if(i!=j)
            ret.push_back(s.substr(i,j-i));

        i=j;
    }
    return ret;

}

int main()
{
    string s;
    getline(cin, s);
    auto word_size = split(s).size();
    cout<<word_size<<"\n";
}

#include<cstdio>

int main() {
	int c = 0;
	char input[1000011];
	input[fread(input, 1, 1000011, stdin)] = 0;
	for (int i = 0; input[i]; ++i) {
		if (input[i] > 33 && input[i + 1] < 33) c++;
	}
	printf("%d", c);
}

*/

//3M 정도 되는 입력 데이터를 cin으로 처리하면 
//데이터 읽어들이는 데에만 1초 이상 소모하게 되는 경우도 종종 있습니다


#include<cstdio>
int main()
{
    char buf[1000001];
    int cnt = 0;
    read(0, buf, 1000001);
    for(int i=0;buf[i];i++)
        if (buf[i]>=33 && buf[i+1]<=32) cnt++;
        //if (buf[i] > 33 && buf[i + 1] < 33) cnt++;

    printf("%d",cnt);
}



