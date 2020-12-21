#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    unordered_map<string, vector<pair<int, int> > > musicMap;
     
    //dic 장르별로 만듦
    for(int i=0;i<plays.size();i++){
        if(musicMap.find(genres[i]) == musicMap.end())
            musicMap[genres[i]] = {};
        musicMap[genres[i]].push_back({-plays[i], i});
    }
    
    vector<pair<string, vector<pair<int, int>>>> musicVector(musicMap.begin(), musicMap.end());
    //백터안에 딕셔너리 넣을 수 있다.
    for(auto [genre, songList]: musicVector){ //얘랑
        cout<<genre<<'\n';
        for(auto it: songList)
            cout<<it.first<<' '<<it.second<<'\n';
    }
    cout<<"      정렬전"<<'\n';
    sort(musicVector.begin(), musicVector.end(), [](auto a, auto b){
        int aSum = 0, bSum = 0;
        for(auto it: a.second){
            aSum += it.first;
        }
        for(auto it: b.second){
            bSum += it.first;
        }
        return aSum < bSum;
    });
    
    for(auto [genre, songList]: musicVector){ //얘 프린트하고싶어요
        cout<<genre<<'\n';
        for(auto it: songList)
            cout<<it.first<<' '<<it.second<<'\n';
    }

    cout<<"    곡 합 많은 순으로 genre 정렬됨"<<'\n';
    
    
    for(auto& [genre, songList]: musicVector){
        sort(songList.begin(), songList.end()); //벡터 자체를 바꿔주는 건 아닌가봄?
        for(auto it: songList)
            cout<<it.first<<' '<<it.second<<'\n';
        if(songList.size() == 1){
            answer.push_back(songList[0].second);
            continue;
        }
        answer.push_back(songList[0].second);
        answer.push_back(songList[1].second);
    }
    cout<<"    ."<<'\n';
    for(auto [genre, songList]: musicVector){ //얘 프린트하고싶어요
        cout<<genre<<'\n';
        for(auto it: songList)
            cout<<it.first<<' '<<it.second<<'\n';
    }
    cout<<"    내부 정렬 됐어야하는데 안돼있음"<<'\n';
    
    return answer;
}

int main()
{
vector<string> g;//= {'classic', 'pop', 'classic', 'classic', 'pop'};
g.push_back("pop");
g.push_back("classic");
g.push_back("pop");
g.push_back("classic");
g.push_back("classic");


vector<int> p;//= {500, 600, 150, 800, 2500};
p.push_back(2500);
p.push_back(500);
p.push_back(600);
p.push_back(150);
p.push_back(800);



for(auto it: solution(g, p))
{
    printf("%d ",it);
}
/*
int ans[4]= solution(g, p); //안됨 이건 백터를c배열로 받는단거라 당연히 안될듯
for(int i=0;i<5;i++)
{
    cout<<ans[i]<<' ';
}

*/

}