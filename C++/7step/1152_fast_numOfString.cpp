#include <stdio.h>

using namespace std;

int main() {
	int c = 0;
	char input[1000011];
	scanf("%[^\n]",input);
	for (int i = 0; input[i]; ++i) {
		if (input[i] > 33 && input[i + 1] < 33) c++;
	}

    char a='2';

    while(a)
    {
        printf("%c",'s');
        a='\0';
    }


	printf("%d\n", c);
}



/*
int main(){
    char input[1000000+1];// = {0, };
    //scanf("%[^\n]",input);
    int cnt=0;
    //cout<<token<<"\n";


    
    input[fread(input,1,7,stdin)]=0;
    for(int i=0; input[i]; ++i)
    {
        if (input[i] > 33 && input[i + 1] < 33) cnt++;
    }
    printf("%d", cnt);

    return 0;
}*/