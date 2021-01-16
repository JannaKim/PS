#include<stdio.h>
bool v[15],h[15],u[30],d[30];
int N,R;
void f(int i){
	if(i==N)++R;
	for(int j=0;j<N;++j){
		if(v[j]||h[i]||u[i+j]||d[i-j+N])continue;
		v[j]=h[i]=u[i+j]=d[i-j+N]=1;
        for(int i=0;i<15;++i)printf("%d ",v[i]);
        printf("\n");
        for(int i=0;i<15;++i)printf("%d ",h[i]);
        printf("\n");
        for(int i=0;i<30;++i)printf("%d ",u[i]);
        printf("\n");
        for(int i=0;i<30;++i)printf("%d ",d[i]);
        printf("\n\n");

		f(i+1);
		v[j]=h[i]=u[i+j]=d[i-j+N]=0;
	}
}
int main(){
	scanf("%d",&N);
	f(0);
	printf("%d",R);
}