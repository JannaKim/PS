#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;
/*
킹 퀸 나이트 비숍 룩 폰
k q n b r p
0 1 2 3 4 5

세로 파일 가로 랭크

기물 잡을 때 take
*/

struct chess{
    int y, x;
    char chesspiece;
};
chess Q[70] = {};
int top;

int vis[10][10] = {}; // auto?
 // 위 오 아 왼 ~ ~ ~ ~
int dy[] = { -1, 0, 1, 0 , 1, 1, -1, -1};
int dx[] = { 0, 1, 0, -1 ,-1, -1, -1, 1};


void init(){
    fill(&vis[0][0], &vis[9][10], 0);
    for(int i = 0; i < 40; ++i){
        Q[i].x = -1;
        Q[i].y = -1;
        Q[i].chesspiece = '\0';
    }
}

int ascii(char alpha){ // lower
    if( 0 <= alpha - 'a' && 26 >= alpha - 'a') return (alpha - 'a');

    else return (alpha - 'A');
}


int step(int y, int x){
    if(vis[y][x] != 0) return 0;
    vis[y][x] = 1;
    return 1;
}


bool bound(int y, int x){
    if(0 <= y && y < 8 && 0 <= x && x < 8) return true;
    return false;
}

int move(int y, int x, int dir, bool rec){
    y += dy[dir];
    x += dx[dir];
    if(bound(y, x) == false) return 0;
    if(vis[y][x] == -1) return 0; // blocked

    int cnt = 0;
    cnt += step(y, x);
    if(rec == false) return cnt;

    cnt += move(y, x, dir, rec);
    return cnt;
}
int king(int y, int x){
    int cnt = 0;
    for(int i = 0; i < 8; ++i)
        cnt += move(y, x, i, false);
    return cnt;
}


int queen(int y, int x){
    int cnt = 0;
    for(int i = 0; i < 8; ++i)
        cnt += move(y, x, i, true);
    return cnt;
}

int ky[] = {1, 1, 2, 2,  -1, -1, -2, -2};
int kx[] = {2, -2, 1, -1, 2, -2, 1, -1};

int knight(int y, int x){
    int cnt = 0;
    for(int i = 0; i < 8; ++i)
        cnt += step(y + ky[i], x + kx[i]);
    return cnt;
}

int bishop(int y, int x){
    int cnt = 0;
    for(int i = 4; i < 8; ++i)
        cnt += move(y, x, i, true);
    return cnt;
}

int rook(int y, int x){
    int cnt = 0;
    for(int i = 0; i < 4; ++i)
        cnt += move(y, x, i, true);
    return cnt;
}

int pawn(int y, int x, char color){
    int cnt = 0;
    if(color == 'p')// down
        cnt += move(y, x, 2, false);
    else //up
        cnt += move(y, x, 0, false);
    return cnt;
}


int take(char piece, int y, int x){
    int take = piece;
    //printf("%c\n", piece);
    if(piece != 'p' && piece != 'P')
        take = ascii(piece);
    int steps = 0;

    switch(take){
        case 'k' - 'a':
            steps += king(y, x);
            cout << steps<<"?\n";
        case 'q' - 'a':
            steps += queen(y, x);
        case 'n' - 'a':
            steps += knight(y, x);
        case 'b' - 'a':
            steps += bishop(y, x);
        case 'r' - 'a':
            steps += rook(y, x);
        default:
            steps += pawn(y, x, take);
        
        }
        
    return steps;
    
}


int implement(){
    int cnt = 0;
    for(int i = 0; i < 64; ++i){
        if(Q[i].x == -1) break;
        cnt += take(Q[i].chesspiece, Q[i].y, Q[i].x);
    }
    return cnt;
}

void fix(string line, int file){
    char word;
    cout << line<< "\n";
    int rank, i;
    rank = 0;
    for(i = 0; i < line.size();  ++i){
        word = line.at(rank);
        printf("%c\n", word);
        //return;
        if('0' <= word && word <= '9') {
            printf("%c\n", word);
            rank += (word - '0');
            continue;
        }
        vis[file][rank] = -1;
        Q[++top].y = file;
        Q[top].x = rank;
        Q[top].chesspiece = word;
        ++rank;
    }

}
int main(){
    string s;
    int ans;
    int file;
    while ( getline(cin, s)){
        top = -1;
        init();
        ans = 0;
        size_t lo = 0, hi;
        hi = s.find('/');

        file = 0;
        string line;
        while(hi != string::npos){//find 함수는 해당 위치부터 문자열을 찾지 못할 경우 npos를 반환한다.
            line = s.substr(lo, hi - lo);
            //cout << line << " ";
            fix(line, file);
            //break;
            lo = hi + 1;
            hi = s.find('/', lo);
        }
        line = s.substr(lo, hi - lo);
        //cout << line << " ";
        fix(line, file);

        ans += implement();
        cout << ans << "\n";
    }

}

/*
5k1r/2q3p1/p3p2p/1B3p1Q/n4P2/6P1/bbP2N1P/1K1RR3
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
*/

    