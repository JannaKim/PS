#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <iostream>
using namespace std;

#define MAXR		99
#define MAXC		26

#define MAXL		100

extern void init(int C, int R);
extern void set(int col, int row, char input[]);
extern void update(int value[MAXR][MAXC]);

#define INIT		100
#define SET			200
#define UPDATE		300

static int R;
static int C;

using namespace std;
#define MAXR		99
#define MAXC		26
#define BIG (int)1e9 + 10000
int db[MAXR][MAXC];
int r, c, n, num;

struct calculator{
	int y1, x1, y2, x2;
    int f;
};

calculator funcs[MAXR][MAXC];

void init(int C, int R) {
    r = R;
    c = C;
    for(int i = 0; i < r; ++i){
        for(int j = 0; j < c; ++j){
            db[i][j] = 0;
        }
    }
}
/*
0 ( ) , \0
*/

void print(int (* arr)[MAXC]){
        for(int i = 0; i < r; ++i){
        for(int j = 0; j < c; ++j){
            cout<<arr[i][j]<<" ";
        }
        cout<<"\n";
    }
}

int getNum(char* input, int st, int ed){
    int tmp = 0;
    for(int i = st; i <= ed; ++i){
        if (input[i] <'0' || input[i] > '9') return 0;
        tmp += (input[i] - '0');
        if(i != ed) tmp *= 10;
    }
    return tmp;
}

void cal(int row, int col, char *input, int n){
    int y1, x1, y2, x2;
    x1 = input[4] - 'A'; 
    bool found = false;
    for(int i = 6; i < n - 1; ++i){ // 5 첫 숫자 시작
        if(input[i] == ','){
            found = true;
            //cout<<input[i + 1]<<" \n";
            x2 = input[i + 1] - 'A'; 
            y1 = getNum(input, 5, i - 1) - 1; // y 좌표 1씩 빼줌
            y2 = getNum(input, i + 2, n - 2) - 1;
            if((y1 == -1) ||( y2 == -1)) { db[row][col] = 0 ; return;}
            break;
        }
        
    }
    if(found == false){ db[row][col] = 0 ; return;}
    funcs[row][col].y1 = y1;
    funcs[row][col].x1 = x1;
    funcs[row][col].y2 = y2;
    funcs[row][col].x2 = x2;

    db[row][col] = BIG;
    //cout<<y1<<" "<<x1<<" "<<y2<<" "<<x2<<'\n';
    if(input[0] == 'A' && input[1] == 'D' && input[2] == 'D'){ //1 add
        funcs[row][col].f = 1;
        //if (db[y1][x1] < BIG && db[y2][x2] && BIG) db[row][col] = db[y1][x1] + db[y2][x2];
        //db[row][col] = db[y1][x1] + db[y2][x2];
    }
    else if(input[0] == 'S' && input[1] == 'U' && input[2] == 'B'){ //2 sub
        funcs[row][col].f = 2;
        //if (db[y1][x1] < BIG && db[y2][x2] && BIG) db[row][col] = db[y1][x1] - db[y2][x2];
        //db[row][col] = db[y1][x1] - db[y2][x2];
    }
    else if(input[0] == 'M' && input[1] == 'U' && input[2] == 'L'){ // 3 mul
        //if (db[y1][x1] < BIG && db[y2][x2] && BIG) db[row][col] = db[y1][x1] * db[y2][x2];
        funcs[row][col].f = 3;
        //db[row][col] = db[y1][x1] * db[y2][x2];
    }

    else if(input[0] == 'D' && input[1] == 'I' && input[2] == 'V'){ // 4 div
        cout << db[y1][x1] / db[y2][x2] <<"\n";
        //if (db[y1][x1] < BIG && db[y2][x2] && BIG) db[row][col] = db[y1][x1] / db[y2][x2];
        funcs[row][col].f = 4;
        //db[row][col] = db[y1][x1] / db[y2][x2];
    }
    else if(input[0] == 'M' && input[1] == 'A' && input[2] == 'X') funcs[row][col].f = 5; 
        //db[row][col] = mx;
    else if(input[0] == 'M' && input[1] == 'I' && input[2] == 'N') funcs[row][col].f = 6; 
        //db[row][col] = mn;
    else if(input[0] == 'S' && input[1] == 'U' && input[2] == 'M') funcs[row][col].f = 7; 
            //db[row][col] = sm; // 7 sum
    
    else db[row][col] = 0; // 이상하게 설정됨

    return;
}
void set(int col, int row, char input[]) {
    col -= 1;
    row -= 1;
    // 상수 값이나 함수가 설정되어 있지 않은 칸은 값 0이 있는 것으로 생각한다.
    n = 0;
    for(int i = 0; input[i] != '\0' ; ++i){
        ++n;
    }
    if(n == 0) db[row][col] = 0;
    else if(input[n - 1] == ')'){ // cal
        cal(row, col, input, n);
    }
    else{ // num
        num = 1;
        if(input[0] == '-') {
            //cout<<"minus"<<'\n';
            num *= -1;
            num *= getNum(input, 1, n - 1);
            //cout<<num<<'\n';
            }
        else if(input[0] <'0' || input[0] > '9') num = 0;
        else{
            num *= getNum(input, 0, n - 1);
        }
        db[row][col] = num;


    }
	
}

struct loc{
    int x, y;
};

struct loc waiting[MAXR * MAXC];
int top = -1;
bool done[MAXR * MAXC];

void calcul(int (* value)[MAXC]){
    int i, j, y1, x1, y2, x2;
    int mn, mx, sm;
    for(int a = 0; a <= top + 1; ++a){
        for(int b = 0; b <= top; ++b){
            if(done[b] == true) continue;

            bool flag = false;
            i = waiting[b].y;
            j = waiting[b].x;

            y1 = funcs[i][j].y1;
            x1 = funcs[i][j].x1;
            y2 = funcs[i][j].y2;
            x2 = funcs[i][j].x2;
            //cout<<y1<<' '<<x1<<' '<<y2<<' '<<x2<<" "<<i<<" "<<j<<" "<<funcs[i][j].f<<"\n\n";
            //cout<<funcs[i][j].f<<"\n\n";
            if(funcs[i][j].f >= 5){
                
                mn = (int)1e9;
                mx = -(int)1e9;
                sm = 0;
                //cout<<input[0]<<" \n";
                if(y1 == y2){// 가로 연산
                    for(int i = x1; i <= x2; ++i){
                        if(db[y1][i] == BIG) {flag = true; break;}
                        if(mn > db[y1][i]) mn = db[y1][i];
                        if(mx < db[y1][i]) mx = db[y1][i];
                        sm += db[y1][i];
                    }
                }
                else{ // 세로 연산
                
                    for(int i = y1; i <= y2; ++i){
                        if(db[i][x1] == BIG) {flag = true; break;}
                        if(mn > db[i][x1]) mn = db[i][x1];
                        if(mx < db[i][x1]) mx = db[i][x1];
                        sm += db[i][x1];
                    }
                }
            
            if(flag || (db[y1][x1] == BIG) || (db[y2][x2] == BIG)) continue;
        }
            cout << funcs[i][j].f <<"dd\n";
            switch(funcs[i][j].f){
                case 1:
                    
                    db[i][j] = db[y1][x1] + db[y2][x2];
                    value[i][j] = db[i][j];
                    break;
                case 2:
                    //printf("?");
                    db[i][j] = db[y1][x1] - db[y2][x2];
                    value[i][j] = db[i][j];
                    break;
                case 3:
                    
                    db[i][j] = db[y1][x1] * db[y2][x2];
                    value[i][j] = db[i][j];
                    break;
                case 4:
                    if(db[y2][x2] == 0){cout<<"!"<<db[y2][x2]<<'\n'; flag = true; break;}
                    db[i][j] = db[y1][x1] / db[y2][x2];
                    cout<<"????"<<db[i][j]<<'\n';
                    value[i][j] = db[i][j];
                    break;
                case 5:
                    
                    db[i][j] = mx;
                    value[i][j] = db[i][j];
                    break;
                case 6:
                    
                    db[i][j] = mn;
                    value[i][j] = db[i][j];
                    break;
                case 7:
                    
                    db[i][j] = sm;
                    value[i][j] = db[i][j];  
                    break;        
                default:
                    db[i][j] = 0;
                    value[i][j] = 0;  
                    
                    }
                //printf("fin\n");
                if(flag == false) done[b] = true;
                
            }
        if( a == top + 1){
            for(int k = 0; k <= top; ++k){
                if(done[k] == false){
                    i = waiting[k].y;
                    j = waiting[k].x;
                    db[i][j] = 0;
                    value[i][j] = 0;  


                }
            }
            break;

        }
    }
    
    return;
}

void update(int value[MAXR][MAXC]) {
    int y1, x1, y2, x2;

    top = -1;
    for(int i = 0; i < r; ++i){
        for(int j = 0; j < c; ++j){
            //cout <<i <<" "<<j<<" "<<db[i][j] <<"?\n";
            if(db[i][j] >= BIG){
                
                waiting[++top].y = i;
                waiting[top].x = j;
            }
            else {value[i][j] = db[i][j];}
        }
    }
    //cout<< "top"<<top<<'\n';
    if(top>=0){
        for(int i = 0; i <= top; ++i){
            done[i] = false;
        }
        calcul(value);
    }

    return;
}

static int gethash(int value[MAXR][MAXC]) {
	int ret = 0;

	for (int r = 0; r < R; ++r)
	for (int c = 0; c < C; ++c)
		ret = (ret * 7 + value[r][c]) & 0x7fffffff;

	return ret;
}

static bool run() {
	int  Q;
	bool okay = true;

	scanf("%d", &Q);

	for (int q = 0; q < Q; ++q) {
		int cmd, row, col;
		int userhash, answerhash;

		char input[MAXL];
		int value[MAXR][MAXC];

		scanf("%d", &cmd);

		switch(cmd) {
		case INIT:
			scanf("%d %d", &C, &R);
			if (okay) {init(C, R); cout<<"\n";
                print(db);
                cout<<"\n";}

			break;
		case SET:
			scanf("%d %d %s", &col, &row, input);
			if (okay) {set(col, row, input); cout<<"\n";
                print(db);
                cout<<"\n";}
            
			break;
		case UPDATE:
			scanf("%d", &answerhash);
			if (okay) {
				update(value);
                cout<<"\n";
                print(db);
                cout<<"\n";
				userhash = gethash(value);
				if (answerhash != userhash)
					okay = false;
			}
			break;
		default:
			break;
		}
	}

	return okay && Q > 0;
}



int main() {
	int TC;

    freopen("inp", "r", stdin);

	setbuf(stdout, NULL);
    scanf("%d", &TC);

	int totalscore = 0;
    for (int testcase = 1; testcase <= TC; ++testcase) {
		int score = run() ? 100 : 0;
		printf("#%d %d\n", testcase, score);
		totalscore += score;
    }
	printf("total score = %d\n", totalscore / TC);
    return 0;
}

