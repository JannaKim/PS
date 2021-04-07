#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>

using namespace std;

unordered_map<string, int> m;

int findShortest(vector<string> words){
    int ret = 0;
//     for(auto word: words){
//         string str = "";
//         for(int i=0; i<word.size(); ++i){
//             str += word[i];
//             m[str] += 1;
//         }
//     }
//     for(auto word: words){
//         string str = "";
//         int localRet = 1;
//         for(int i=0; i<word.size()-1; ++i){
//             str += word[i];
//             if(m[str] > 1){
//                 ++localRet;
//                 continue;
//             }

//             break;
//         }
//         if(localRet >= word.size()){
//             localRet = word.size();
//         }
//         ret += localRet;
//     }

//     return ret;

    for(int i=0; i<words.size(); ++i){
        int localRet = 1;
        if(i == 0){
            for(int j=0; j<words[i].size()-1; ++j){
                char currChar = words[i][j];
                char nextChar = 'A';
                if(words[i+1].size() > j){
                    nextChar = words[i+1][j];
                }
                if(currChar == nextChar){
                    ++localRet;
                } else {
                    break;
                }
            }
        } else if(i == words.size()-1){
            for(int j=0; j<words[i].size()-1; ++j){
                char currChar = words[i][j];
                char prevChar = 'A';
                if(words[i-1].size() > j){
                    prevChar = words[i-1][j];
                }
                if(currChar == prevChar){
                    ++localRet;
                } else {
                    break;
                }
            }
        } else{
            for(int j=0; j<words[i].size()-1; ++j){
                char currChar = words[i][j];
                char prevChar = 'A';
                if(words[i-1].size() > j){
                    prevChar = words[i-1][j];
                }
                char nextChar = 'A';
                if(words[i+1].size() > j){
                    nextChar = words[i+1][j];
                }
                if(currChar == prevChar){
                    ++localRet;
                    continue;
                }
                if(currChar == nextChar){
                    ++localRet;
                    continue;
                }

                break;
            }
        }
        if(localRet > words[i].size()){
            localRet = words[i].size();
        }
        cout << localRet << "\n";
        ret += localRet;
    }

    return ret;
}

int solution(vector<string> words) {
    int answer = 0;
    sort(words.begin(), words.end());
    answer = findShortest(words);
    return answer;
}