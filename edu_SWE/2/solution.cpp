#define MAX_N 1000
#define MAX_M 20
#define swap(type, y, x) do{type t = *y; *y = *x; *x = t;}while(0)
struct Result {
	int y, x;
};
int n, m;
int direction = 0;
int (*map)[MAX_N];
bool vis[4][MAX_N][MAX_N];

void init(int N, int M, int Map[MAX_N][MAX_N])
{
    n = N;
    m = M;
    map = Map;
}

bool visited(int r, int c){
    for(int i = r; i < r + m; ++i){
        for(int j = c; j < c + m; ++j){
            vis[direction][i][j] = true;
        }
    }
}

bool match(int r, int c, int(* stars)[MAX_M], struct Result *res){
    int i, j, si, sj;
    int cnt = 0;
    for(i = r, si = 0; i < r + m; ++i, ++si){
        for(j = c, sj = 0; j < c + m; ++j, ++sj){
            //if(!bound(i, j)){return 0;}
            if(stars[si][sj]) ++cnt;
            if(stars[si][sj] == 9){
                (*res).y = i;
                (*res).x = j;
            }
            if(stars[si][sj] && !map[i][j]){return false;}
            if(!stars[si][sj] && map[i][j]){return false;}
        }
    }
    if(cnt<5) visited(r, c);
    return true;
}

void rotate(int(* map)[MAX_N]){
    for(int i = 0; i < n; ++i){
        for(int j = i + 1; j < n; ++j){
            swap(int, &map[i][j], &map[j][i]);
        }
    }

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n/2; ++j){
            swap(int, &map[i][j], &map[i][n- 1 - j]);
        }
    }
}
void starred(int r, int c){
    int i, j, si, sj;
    for(i = r, si = 0; i < r + m; ++i, ++si){
        for(j = c, sj = 0; j < c + m; ++j, ++sj){
}
void traverse(int(* stars)[MAX_M], struct Result *res){
    for(int dir = 0; dir < 4; ++dir){
        direction = dir;
        for(int i = 0; i <= n - m; ++i){
            for(int j = 0; j <= n -m; ++j){
                if(vis[i][j] == true) continue;
                if(match(i, j, stars, res) == true){
                    starred(i, j);
                    //findMainStar(i, j, stars, res);
                    return;
                }
            }
        }
        rotate(map);
    }
}

void turn(struct Result *res){
    for(int i = 0; i < direction; ++i){
        int tmp = (*res).y ;
        (*res).y = (*res).x;
        (*res).x = (n - 1 - tmp);

    }
}
Result findConstellation(int stars[MAX_M][MAX_M])
{
	Result res;
	res.y = res.x = 0;
    traverse(stars, &res);
    turn(&res);
	return res;
}




