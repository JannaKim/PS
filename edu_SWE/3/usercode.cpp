#define MAXR		99
#define MAXC		26
#define ll long long
 data[30][110];
int r, c;

struct calculator{
	int y1, x1, y2, x2;
    int func;
};
void init(int C, int R) {
    r = R;
    c = C;
    for(int i = 0; i < r; ++i){
        for(int j = 0; j < c; ++j){
            data[i][j] = 0;
        }
    }
}
/*
0 ( ) , \0
*/


ll getNum(char* input, const int st, const int ed){
    ll tmp = 0;
    for(int i = st; i <= ed; ++i){
        tmp += (ll)(input[i] - '0');
        if(i != ed) tmp *= 10;
    }
    return tmp;
}

void store(int row, int col, char *input, int n){
    int y1, x1, y2, x2;
    x1 = input[4] - 'A'; 
    for(int i = 6; i < n - 1; ++i){ // 5 첫 숫자 시작
        if(input[i] == ','){
            x2 = input[i + 1] - 'A'; 
            y1 = getNum(input, 5, i - 1);
            y2 = getNum(input, i + 2, n - 1);
        }
    }
    if(input[0] == 'A'){ //add
        data[row][col] = data[y1][x1] + data[y2][x2];
    }
    else if(input[0] == 'S'){ //sub
        data[row][col] = data[y1][x1] - data[y2][x2];
    }
    else if(input[0] == 'M' && input[1] == 'U'){ //mul
        data[row][col] = data[y1][x1] * data[y2][x2];
    }

    else if(input[0] == 'D'){ //div
        data[row][col] = data[y1][x1] / data[y2][x2];
    }
    else{
        ll mn, mx, sm;
        mn = (ll)1e9;
        mx = -(ll)1e9;
        sm = 0;
        if(y1 == y2){// 가로 연산
            for(int i = x1; i <= x2; ++i){
                if(mn > data[y1][i]) mn = data[y1][i];
                if(mx < data[y1][i]) mx = data[y1][i];
                sm += data[y1][i];
            }
        }
        else{ // 세로 연산
            for(int i = y1; i <= y2; ++i){
                if(mn > data[i][x1]) mn = data[i][x1];
                if(mx < data[i][x1]) mx = data[i][x1];
                sm += data[i][x1];
            }
        }

        if(input[1] == 'A') data[row][col] = mx; //max
        else if(input[1] == 'I') data[row][col] = mn; //min
        else data[row][col] = sm; //sum
    }

    
}
void set(int col, int row, char input[]) {
    // 상수 값이나 함수가 설정되어 있지 않은 칸은 값 0이 있는 것으로 생각한다.
    int n = sizeof(input)/sizeof(char);
    if(n == 0) data[row][col] = 0;
    else if(input[n - 1] == ')'){ // store
        store(row, col, input, n);
    }
    else{ // num
        ll num = 1;
        if(input[0] == '-') {
            num *= -1;
            num *= getNum(input, 1, n - 1);
            }
        else{
            num *= getNum(input, 0, n - 1);
        }

    }
	
}

void update(int value[MAXR][MAXC]) {
    for(int i = 0; i < r; ++i){
        for(int j = 0; j < c; ++j){
            value[i][j] = data[i][j];
        }
    }
}