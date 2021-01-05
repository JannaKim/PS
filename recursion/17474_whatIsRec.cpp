// 17474 재귀함수가 뭔가요
#include <stdio.h>
#include <string>
using namespace std;
int n;

void recursion(int cnt)
{
    printf("%s\"재귀함수가 뭔가요?\"\n",string(4*cnt,'_').c_str());
    if(cnt==n)
    {
        printf("%s\"재귀함수는 자기 자신을 호출하는 함수라네\"\n",string(4*cnt,'_').c_str());
        printf("%s라고 답변하였지.\n",string(4*cnt,'_').c_str());
        return;
    }
    printf("%s\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n",string(4*cnt,'_').c_str());
    printf("%s마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n",string(4*cnt,'_').c_str());
    printf("%s그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n",string(4*cnt,'_').c_str());
    
    recursion(cnt+1);
    printf("%s라고 답변하였지.\n",string(4*cnt,'_').c_str());
    return;
}
int main()
{
    scanf("%d",&n);
    printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
    recursion(0);

}