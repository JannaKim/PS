#include <string>
#include <vector>
#include <tuple>
#include <stdlib.h>
#include <iostream>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int L =10;
    int R =12;
    for(int i:numbers)
    {
        if(i==0)i=11;

        if(i==2|| i==5|| i==8|| i==11)
        {
            auto locL= make_tuple((L-1)/3,(L-1)%3);
            auto locR= make_tuple((R-1)/3,(R-1)%3);
            auto locI= make_tuple((i-1)/3,(i-1)%3);

            int disL= abs(get<0>(locL)-get<0>(locI))+ abs(get<1>(locL)-get<1>(locI));
            int disR= abs(get<0>(locR)-get<0>(locI))+ abs(get<1>(locR)-get<1>(locI));

            if(disL< disR){ L=i; answer+='L';}
            else if(disL> disR){ R=i; answer+='R';}
            else
            {
                if(hand=="right"){ R=i; answer+='R';}
                else { L=i; answer+='L';}
            }
        }
        else
        {
            if((i-1)%3==0) { L=i; answer+='L';}
            else { R=i; answer+='R';}
        }


    }
    return answer;
}

int main(){
    cout<<solution({1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right");
}