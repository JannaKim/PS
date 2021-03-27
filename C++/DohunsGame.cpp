#define _CRT_SECURE_NO_WARNINGS

#define LEFT 75
#define UP 72
#define DOWN 80
#define RIGHT 77
#define ENTER 13

#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <Windows.h>

struct Gameboard
{
   char board[361];
   double pref[361];
   double eval[361];
   double score[3];
};

int cx = 26, cy = 12;
void setcolor(unsigned short text, unsigned short back)
{
   SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), text | (back << 4));
}

void gotoxy(int x, int y)
{
   COORD pos = { x,y };
   SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void move(char key)
{
   switch (key)
   {
   case LEFT: cx--; cx--; break;
   case RIGHT: cx++; cx++; break;
   case UP: cy--; break;
   case DOWN: cy++; break;
   }
   gotoxy(60, 10);
   printf("x : %2d, y : %2d", cx / 2 - 3, cy - 2);

   gotoxy(cx, cy);
}

void DisplayPref(struct Gameboard Game)
{
   for (int i = 0; i < 19; i++)
   {
      for (int j = 0; j < 19; j++)
      {
         gotoxy(50 + j*3, 3 + i);
         
         printf("%2.0lf ", Game.pref[19 * i + j]);
      }
   }
}

void DisplayData(struct Gameboard Game)
{
   for (int i = 0; i < 19; i++)
   {
      for (int j = 0; j < 38; j++)
      {
         gotoxy(80 + j, 3 + i);
         printf(" ");
      }
   }
   for (int i = 0; i < 19; i++)
   {
      gotoxy(80, 3 + i);
      for (int j = 0; j < 19; j++)
      {
         gotoxy(80 + (j * 2), 3 + i);

         if (Game.board[j + 19 * i] == 'B')
         {
            printf("0");
         }
         else if (Game.board[j + 19 * i] == 'W')
         {
            printf("1");
         }
         else if (Game.board[j + 19 * i] == 'X')
         {
            setcolor(4, 0);
            printf("X ");
            setcolor(7, 0);
         }
         else if (Game.board[j + 19 * i] != 0)
         { 
            printf("%c", Game.board[j + 19 * i]);
         }
      }
   }
}

void DisplayBoard(struct Gameboard Game)
{
   for (int i = 0; i < 19; i++)
   {
      for (int j = 0; j < 38; j++)
      {
         gotoxy(6 + j, 3 + i);
         printf(" ");
      }
   }

   for (int i = 0; i < 19; i++)
   {
      gotoxy(6, 3 + i);
      printf("%2d", i + 1);
      for (int j = 0; j < 19; j++)
      {
         gotoxy(8 + (j * 2), 3 + i);

         if (Game.board[j + 19 * i] == 'B')
         {
            printf("○");
         }
         else if (Game.board[j + 19 * i] == 'W')
         {
            printf("●");
         }
         else if (Game.board[j + 19 * i] == 'X')
         {
            setcolor(4, 0);
            printf("◆");
            setcolor(7, 0);
         }

         if (i == 0)
         {
            if (j == 0)
            {
               printf("┌");
            }
            else if (j == 18)
            {
               printf("┐");
            }
            else
            {
               printf("┬");
            }
         }
         else if (i == 18)
         {
            if (j == 0)
            {
               printf("└");
            }
            else if (j == 18)
            {
               printf("┘");
            }
            else
            {
               printf("┴");
            }
         }
         else
         {
            if (j == 0)
            {
               printf("├");
            }
            else if (j == 18)
            {
               printf("┤");
            }
            else
            {
               printf("┼");
            }
         }
      }
   }
}

void array(struct Gameboard* g, char temp[4][9], int index, int us)
{
   char myMark;
   char enemyMark;
   int x = 0, y = 0, ui = 0, r = 0, count = 0;
   int limit[361][8];
   int dxy[8] = { -1, -19, 18, -20, 1, 19, -18, 20 };
   // 0 은 가로 1은 세로 2는 / 3은 \ 공백은 n(대각선은 높은 곳에 서 낮은 곳으로)

   for (int i = 0; i < 4; i++)
   {
      for (int j = 0; j < 9; j++)
      {
         temp[i][j] = 'n';
      }
   }

   if (us == 1)
   {
      myMark = 'B';
      enemyMark = 'W';
   }
   else
   {
      myMark = 'W';
      enemyMark = 'B';
   }

   for (int i = 0; i < 361; i++)
   {
      x = i % 19;
      y = i / 19;
      limit[i][0] = x;
      limit[i][1] = y;
      limit[i][2] = (18 - y > x) ? x : 18 - y;
      limit[i][3] = (y > x) ? x : y;
      limit[i][4] = 18 - x;
      limit[i][5] = 18 - y;
      limit[i][6] = (y > 18 - x) ? 18 - x : y;
      limit[i][7] = (18 - y > 18 - x) ? 18 - x : 18 - y;
   }

   if (index != 361)
   {
      for (ui = 0; ui < 4; ui++)
      {
         count = 0;
         r = index + dxy[ui];

         for (int k = 1; k < limit[index][ui]; ++k)
         {
            if (g->board[r] == enemyMark)
            {
               temp[ui][4 - k] = g->board[r];
               break;
            }
            else if (g->board[r] == myMark)
            {
               temp[ui][4 - k] = g->board[r];
            }
            else
            {
               temp[ui][4 - k] = 'n';
            }

            r += dxy[ui];
            count++;

            if (count == 4)
            {
               break;
            }
         }
      }
      for (ui = 4; ui < 8; ui++)
      {
         count = 0;
         r = index;

         for (int k = 1; k < limit[index][ui]; ++k)
         {
            if (g->board[r] == enemyMark)
            {
               temp[ui - 4][k + 3] = g->board[r];
               break;
            }
            else if (g->board[r] == myMark)
            {
               temp[ui - 4][k + 3] = g->board[r];
            }
            else
            {
               temp[ui - 4][k + 3] = 'n';
            }

            r += dxy[ui];
            count++;

            if (count == 5)
            {
               break;
            }
         }
      }
   }

   /*for (int j = 0; j < 4; j++)
   {
      switch (j)
      {
      case 0:
         printf("가로   |");
         break;
      case 1:
         printf("세로   |");
         break;
      case 2:
         printf("좌하향 |");
         break;
      case 3:
         printf("우하향 |");
         break;
      }
      for (int j1 = 0; j1 < 9; j1++)
      {
         printf("%c", temp[j][j1]);
      }
      printf("\n");
   }*/
}

static int threeRule(struct Gameboard* g, int index, int us)
{
   char myMark, enemyMark;
   char temp = 0;
   double preftemp = 0;
   char Ban[4][9];
   int cnt1 = 0, cnt2 = 0, cnt3 = 0, cnt4 = 0;
   int uT = 0, u1 = 0, u2 = 0, u3 = 0, u4 = 0;
   int x = 0, y = 0;
   char ptrn[30][9];

   if (us == 1)
   {
      myMark = 'B';
      enemyMark = 'W';
   }
   else
   {
      myMark = 'W';
      enemyMark = 'B';
   }

   if (myMark == 'B')
   {
      strcpy(ptrn[0], "nnBBBnnnn");
      strcpy(ptrn[1], "nnnBBBnnn");
      strcpy(ptrn[2], "nnnnBBBnn");
      strcpy(ptrn[3], "nBnBBnnnn");
      strcpy(ptrn[4], "nnBnBBnnn");
      strcpy(ptrn[5], "nnnnBnBBn");
      strcpy(ptrn[6], "nBBnBnnnn");
      strcpy(ptrn[7], "nnnBBnBnn");
      strcpy(ptrn[8], "nnnnBBnBn");
      strcpy(ptrn[9], "WnnBBBnnn");
      strcpy(ptrn[10], "nnnBBBnnW");
      strcpy(ptrn[11], "WnBnBBnnn");

      strcpy(ptrn[12], "nnBBBnnWn");
      strcpy(ptrn[13], "WnnBBBnnW");
      strcpy(ptrn[14], "nWnnBBBnn");
      strcpy(ptrn[15], "nBnBBnWnn");
      strcpy(ptrn[16], "WnBnBBnWn");
      strcpy(ptrn[17], "nnWnBnBBn");
      strcpy(ptrn[18], "nBBnBnWnn");
      strcpy(ptrn[19], "nWnBBnBnW");
      strcpy(ptrn[20], "nnWnBBnBn");
      strcpy(ptrn[21], "nnBnBBnWn");
      strcpy(ptrn[22], "nWnBBnBnn");
      strcpy(ptrn[23], "nnnBBnBnW");
   }

   if (myMark == 'W')
   {
      strcpy(ptrn[0], "nnWWWnnnn");
      strcpy(ptrn[1], "nnnWWWnnn");
      strcpy(ptrn[2], "nnnnWWWnn");
      strcpy(ptrn[3], "nWnWWnnnn");
      strcpy(ptrn[4], "nnWnWWnnn");
      strcpy(ptrn[5], "nnnnWnWWn");
      strcpy(ptrn[6], "nWWnWnnnn");
      strcpy(ptrn[7], "nnnWWnWnn");
      strcpy(ptrn[8], "nnnnWWnWn");
      strcpy(ptrn[9], "BnnWWWnnn");
      strcpy(ptrn[10], "nnnWWWnnB");
      strcpy(ptrn[11], "BnWnWWnnn");

      strcpy(ptrn[12], "nnWWWnnBn");
      strcpy(ptrn[13], "BnnWWWnnB");
      strcpy(ptrn[14], "nBnnWWWnn");
      strcpy(ptrn[15], "nWnWWnBnn");
      strcpy(ptrn[16], "BnWnWWnBn");
      strcpy(ptrn[17], "nnBnWnWWn");
      strcpy(ptrn[18], "nWWnWnBnn");
      strcpy(ptrn[19], "nBnWWnWnB");
      strcpy(ptrn[20], "nnBnWWnWn");
      strcpy(ptrn[21], "nnWnWWnBn");
      strcpy(ptrn[22], "nBnWWnWnn");
      strcpy(ptrn[23], "nnnWWnWnB");
   }

   if (g->board[index] == 0 || g->board[index] == 'X')
   {
      temp = g->board[index];
      preftemp = g->pref[index];
      g->board[index] = myMark;

      x = index % 19;
      y = index / 19;

      for (int iy = y - 2; iy < y + 3; iy++)
      {
         for (int ix = x - 2; ix < x + 3; ix++)
         {
            if (ix < 0 || ix >= 19 || iy < 0 || iy >= 19)
            {
               continue;
            }
            if (g->board[ix + 19 * iy] != myMark && g->board[ix + 19 * iy] != 'X') //문제 있을지도
            {
               continue;
            }

            array(g, Ban, ix + 19 * iy, us);

            for (int ptr = 0; ptr < 24; ptr++)
            {
               for (int num = 0; num < 9; num++)
               {
                  if (ptrn[ptr][num] == Ban[0][num])
                  {
                     cnt1++;
                  }
                  if (ptrn[ptr][num] == Ban[1][num])
                  {
                     cnt2++;
                  }
                  if (ptrn[ptr][num] == Ban[2][num])
                  {
                     cnt3++;
                  }
                  if (ptrn[ptr][num] == Ban[3][num])
                  {
                     cnt4++;
                  }
               }
               if (cnt1 == 9)
               {
                  u1 = 1;
               }
               if (cnt2 == 9)
               {
                  u2 = 1;
               }
               if (cnt3 == 9)
               {
                  u3 = 1;
               }
               if (cnt4 == 9)
               {
                  u4 = 1;
               }
               cnt1 = 0;
               cnt2 = 0;
               cnt3 = 0;
               cnt4 = 0;
            }
            uT = u1 + u2 + u3 + u4;

            if (uT >= 2)
            {
               //printf("%d %d %d %d\n", u1, u2, u3, u4);
               g->board[index] = temp;
               g->pref[index] = preftemp;
               //printf("%d\n", uT);
               return 1;
            }
            u1 = 0;
            u2 = 0;
            u3 = 0;
            u4 = 0;
            uT = 0;
         }
      }
      g->board[index] = temp;
      g->pref[index] = preftemp;
   }
   return 0;
}

int blackpref(struct Gameboard* g, int threerule, int point)
{
   char cpuMark = 'B';
   char enemyMark = 'W';
   double temp = 0;
   double periadv = 0.05;
   double d[4] = { 2, 20, 32, 400 };
   double a[4] = { 2, 18, 30, 600 };
   double ctradv = 0.1;
   int thR = 0;
   int opt[361] = { -1 };
   char virt[4][9];
   char virtuoso[4][9];

   for (int p = 0; p < 19; p++)
   { //가운데로 갈수록 선호도 증가
      for (int px = p; px < 19 - p; px++)
      {
         for (int py = p; py < 19 - p; py++)
         {
            g->pref[px + 19 * py] += ctradv;
         }
      }
   }

   for (int ix5 = 0; ix5 < 19; ix5++)
   {
      for (int iy5 = 0; iy5 < 19; iy5++)
      {
         if (g->board[ix5 + 19 * iy5] == cpuMark)
         {
            for (int ix1 = ix5 - 2; ix1 <= ix5 + 2; ix1++)
            {
               for (int iy1 = iy5 - 2; iy1 <= iy5 + 2; iy1++)
               {
                  if (ix1 >= 0 && ix1 < 19 && iy1 >= 0 && iy1 < 19)
                  {
                     g->pref[ix1 + 19 * iy1] += periadv; // 주위 돌의 선호도
                  }
               }
            }
         }
      }
   }
   int vx1 = 0, vx2 = 0, vy1 = 0, vy2 = 0;
   int cnt1 = 0, cnt2 = 0, cnt3 = 0, cnt4 = 0, cnt5 = 0, cnt6 = 0, cnt7 = 0, cnt8 = 0;

   char atkptrn[60][9]; //패턴 작성
   strcpy(atkptrn[0], "nnnBBBnnn");

   strcpy(atkptrn[1], "nnnWBBBnn");
   strcpy(atkptrn[2], "nnBBBWnnn");

   strcpy(atkptrn[3], "nnBBnnnnn");
   strcpy(atkptrn[4], "nnnnnBBnn");

   strcpy(atkptrn[5], "nnBnBBnnn");
   strcpy(atkptrn[6], "nnnBBnBnn"); //패턴 추가하기

   strcpy(atkptrn[7], "nnBBBBWnn");
   strcpy(atkptrn[8], "nnWBBBBnn");

   strcpy(atkptrn[9], "nnBBBnBnn");
   strcpy(atkptrn[10], "nWBBBnBnn");
   strcpy(atkptrn[11], "nnBBBnBWn");
   strcpy(atkptrn[12], "nWBBBnBWn");

   strcpy(atkptrn[13], "nnBnBBBnn");
   strcpy(atkptrn[14], "nWBnBBBnn");
   strcpy(atkptrn[15], "nnBnBBBWn");
   strcpy(atkptrn[16], "nWBnBBBWn");

   strcpy(atkptrn[17], "nnBBnBBnn");
   strcpy(atkptrn[18], "nWBBnBBnn");
   strcpy(atkptrn[19], "nnBBnBBWn");
   strcpy(atkptrn[20], "nWBBnBBWn");

   strcpy(atkptrn[21], "nnBBBBnnn");
   strcpy(atkptrn[22], "nnBBBBnWn");
   strcpy(atkptrn[23], "nWnBBBBnn");

   strcpy(atkptrn[24], "nnBnBBWnn");
   strcpy(atkptrn[25], "nnBnBBnWn");
   strcpy(atkptrn[26], "nWnBnBBnn");

   strcpy(atkptrn[27], "nnBBnBWnn");
   strcpy(atkptrn[28], "nnBBnBnWn");
   strcpy(atkptrn[29], "nWnBBnBnn");

   strcpy(atkptrn[30], "nnWBnBBnn");
   strcpy(atkptrn[31], "nnWBBnBnn");

   double atkprefptrn[60][9] = {
      {0, a[1], a[1], 0, 0, 0, a[1], a[1], 0},

      {0, 0, 0, 0, 0, 0, 0, a[0], a[0]},
      {a[0], a[0], 0, 0, 0, 0, 0, 0, 0},

      {a[0], a[0], 0, 0, a[0], a[0], a[0], 0, 0},
      {0, 0, a[0], a[0], a[0], 0, 0, a[0], a[0]},

      {0, a[1], 0, a[3], 0, 0, a[1], 0, 0}, //5
      {0, 0, a[1], 0, 0, a[3], 0, a[1], 0},

      {0, 3 * a[3], 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 3 * a[3], 0},

      {0, 0, 0, 0, 0, a[3], 0, 0, 0},
      {0, 0, 0, 0, 0, a[3], 0, 0, 0}, //10
      {0, 0, 0, 0, 0, a[3], 0, 0, 0},
      {0, 0, 0, 0, 0, a[3], 0, 0, 0},

      {0, 0, 0, a[3], 0, 0, 0, 0, 0},
      {0, 0, 0, a[3], 0, 0, 0, 0, 0},
      {0, 0, 0, a[3], 0, 0, 0, 0, 0}, //15
      {0, 0, 0, a[3], 0, 0, 0, 0, 0},

      {0, 0, 0, 0, a[3], 0, 0, 0, 0},
      {0, 0, 0, 0, a[3], 0, 0, 0, 0},
      {0, 0, 0, 0, a[3], 0, 0, 0, 0},
      {0, 0, 0, 0, a[3], 0, 0, 0, 0}, //20

      {0, 6 * a[3], 0, 0, 0, 0, 6 * a[3], 0, 0},
      {0, a[3], 0, 0, 0, 0, a[3], 0, 0},
      {0, 0, a[3], 0, 0, 0, 0, a[3], 0},

      {0, a[2], 0, a[2], 0, 0, 0, 0, 0},
      {0, a[0], 0, a[3], 0, 0, a[0], 0, 0}, //25
      {0, 0, a[0], 0, a[3], 0, 0, a[0], 0},

      {0, a[2], 0, 0, a[2], 0, 0, 0, 0},
      {0, a[0], 0, 0, a[3], 0, a[0], 0, 0},
      {0, 0, a[0], 0, 0, a[3], 0, a[0], 0},

      {0, 0, 0, 0, a[1], 0, 0, a[1], 0}, //30
      {0, 0, 0, 0, 0, a[1], 0, a[1], 0},
   };

   char defptrn[60][9]; //패턴 작성
   strcpy(defptrn[0], "nnnWWWnnn");

   strcpy(defptrn[1], "nnnBWWWnn");
   strcpy(defptrn[2], "nnWWWBnnn");

   strcpy(defptrn[3], "nWWnWnnnn");
   strcpy(defptrn[4], "nnnWWWWnn");

   strcpy(defptrn[5], "nnWnWWnnn");
   strcpy(defptrn[6], "nnnWWnWnn"); //패턴 추가하기

   strcpy(defptrn[7], "nnWWWWBnn");
   strcpy(defptrn[8], "nnBWWWWnn");

   strcpy(defptrn[9], "nnWnWWWnn");
   strcpy(defptrn[10], "nBWnWWWnn");
   strcpy(defptrn[11], "nnWnWWWBn");
   strcpy(defptrn[12], "nBWnWWWBn");

   strcpy(defptrn[13], "nnWWWnWnn");
   strcpy(defptrn[14], "nBWWWnWnn");
   strcpy(defptrn[15], "nnWWWnWBn");
   strcpy(defptrn[16], "nBWWWnWBn");

   strcpy(defptrn[17], "nnWWnWWnn");
   strcpy(defptrn[18], "nBWWnWWnn");
   strcpy(defptrn[19], "nnWWnWWBn");
   strcpy(defptrn[20], "nBWWnWWBn");

   strcpy(defptrn[21], "nnWnWWBnn");
   strcpy(defptrn[22], "nnWWnWBnn");
   strcpy(defptrn[23], "nnWWWnBnn");
   strcpy(defptrn[24], "nnBWnWWnn");
   strcpy(defptrn[25], "nnBWWnWnn");
   strcpy(defptrn[26], "nnBnWWWnn");

   strcpy(defptrn[27], "nBnWWWWBn");
   strcpy(defptrn[28], "nBWWWWnBn");

   strcpy(defptrn[29], "nnWnnWWnn");
   strcpy(defptrn[30], "nBWnnWWnn");
   strcpy(defptrn[31], "nnWnnWWBn");
   strcpy(defptrn[32], "nBWnnWWBn");

   strcpy(defptrn[33], "nnWWnnWnn");
   strcpy(defptrn[34], "nBWWnnWnn");
   strcpy(defptrn[35], "nnWWnnWBn");
   strcpy(defptrn[36], "nBWWnnWBn");

   strcpy(defptrn[37], "nnWnWnWnn");
   strcpy(defptrn[38], "nBWnWnWnn");
   strcpy(defptrn[39], "nnWnWnWBn");
   strcpy(defptrn[40], "nBWnWnWBn");

   strcpy(defptrn[41], "nnBnWnWWn");
   strcpy(defptrn[42], "nnBnWWnWn");
   strcpy(defptrn[43], "nWnWWnBnn");
   strcpy(defptrn[44], "nWWnWnBnn");

   double defprefptrn[60][9] = {
      {0, 0, 2 * d[2], 0, 0, 0, 2 * d[2], 0, 0},

      {0, 0, 0, 0, 0, 0, 0, d[0], 0},
      {0, d[0], 0, 0, 0, 0, 0, 0, 0},

      {0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0},

      {0, 0, 0, d[3], 0, 0, 0, 0, 0}, //5
      {0, 0, 0, 0, 0, d[3], 0, 0, 0},

      {0, d[2], 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, d[2], 0},

      {0, 0, 0, d[3], 0, 0, 0, 0, 0},
      {0, 0, 0, d[3], 0, 0, 0, 0, 0}, //10
      {0, 0, 0, d[3], 0, 0, 0, 0, 0},
      {0, 0, 0, d[3], 0, 0, 0, 0, 0},

      {0, 0, 0, 0, 0, d[3], 0, 0, 0},
      {0, 0, 0, 0, 0, d[3], 0, 0, 0},
      {0, 0, 0, 0, 0, d[3], 0, 0, 0}, //15
      {0, 0, 0, 0, 0, d[3], 0, 0, 0},

      {0, 0, 0, 0, d[3], 0, 0, 0, 0},
      {0, 0, 0, 0, d[3], 0, 0, 0, 0},
      {0, 0, 0, 0, d[3], 0, 0, 0, 0},
      {0, 0, 0, 0, d[3], 0, 0, 0, 0}, //20

      {0, d[1], 0, d[1], 0, 0, 0, 0, 0},
      {0, d[1], 0, 0, d[1], 0, 0, 0, 0},
      {0, d[1], 0, 0, 0, d[1], 0, 0, 0},
      {0, 0, 0, 0, d[1], 0, 0, d[1], 0},
      {0, 0, 0, 0, 0, d[1], 0, d[1], 0}, //25
      {0, 0, 0, d[1], 0, 0, 0, d[1], 0},

      {0, 0, d[3], 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, d[3], 0, 0},

      {0, d[1], 0, d[1], d[1], 0, 0, d[1], 0},
      {0, 0, 0, d[0], d[0], 0, 0, d[0], 0}, //30
      {0, d[0], 0, d[0], d[0], 0, 0, 0, 0},
      {0, 0, 0, d[0], d[0], 0, 0, 0, 0},

      {0, d[1], 0, 0, d[1], d[1], 0, d[1], 0},
      {0, 0, 0, 0, d[0], d[0], 0, d[0], 0},
      {0, d[0], 0, 0, d[0], d[0], 0, 0, 0}, //35
      {0, 0, 0, 0, d[0], d[0], 0, 0, 0},

      {0, d[1], 0, d[1], 0, d[1], 0, d[1], 0},
      {0, 0, 0, d[0], 0, d[0], 0, d[0], 0},
      {0, d[0], 0, d[0], 0, d[0], 0, 0, 0},
      {0, 0, 0, d[0], 0, d[0], 0, 0, 0}, //40

      {0, 0, 0, d[0], 0, d[3], 0, 0, d[0]},
      {0, 0, 0, d[0], 0, 0, d[3], 0, d[0]},
      {d[0], 0, d[3], 0, 0, d[0], 0, 0, 0},
      {d[0], 0, 0, d[3], 0, d[0], 0, 0, 0},
   };

   for (int xx = 0; xx < 19; xx++)
   { //같은 패턴을 찾기
      for (int yy = 0; yy < 19; yy++)
      {
         int index = xx + 19 * yy;
         array(g, virt, index, 1);    //공격
         array(g, virtuoso, index, 2); //방어

         for (int ptr = 0; ptr < 60; ptr++)
         {
            for (int num = 1; num < 8; num++)
            {
               if (atkptrn[ptr][num] == virt[0][num])
               {
                  cnt1++;
               }
               if (atkptrn[ptr][num] == virt[1][num])
               {
                  cnt2++;
               }
               if (atkptrn[ptr][num] == virt[2][num])
               {
                  cnt3++;
               }
               if (atkptrn[ptr][num] == virt[3][num])
               {
                  cnt4++;
               }
               if (defptrn[ptr][num] == virtuoso[0][num])
               {
                  cnt5++;
               }
               if (defptrn[ptr][num] == virtuoso[1][num])
               {
                  cnt6++;
               }
               if (defptrn[ptr][num] == virtuoso[2][num])
               {
                  cnt7++;
               }
               if (defptrn[ptr][num] == virtuoso[3][num])
               {
                  cnt8++;
               }
            }
            if (cnt1 == 7)
            {
               for (int vx = 0; xx + vx < 23, vx < 9; vx++)
               {
                  if (xx + vx >= 4)
                  {
                     g->pref[xx + vx - 4 + 19 * yy] += atkprefptrn[ptr][vx];
                     g->eval[xx + vx - 4 + 19 * yy] += atkprefptrn[ptr][vx];
                  }
               }
            }
            if (cnt2 == 7)
            {
               for (int vy = 0; yy + vy < 23, vy < 9; vy++)
               {
                  if (yy + vy >= 4)
                  {
                     g->pref[xx + 19 * (yy + vy - 4)] += atkprefptrn[ptr][vy];
                     g->eval[xx + 19 * (yy + vy - 4)] += atkprefptrn[ptr][vy];
                  }
               }
            }

            if (cnt3 == 7)
            {
               for (vx1 = 0, vy1 = 0; xx + vx1 < 23, vx1 < 9; vx1++, vy1--)
               {
                  if (yy + vy1 >= -4 && xx + vx1 >= 4 && yy + vy1 < 15)
                  {
                     g->pref[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] += atkprefptrn[ptr][vx1];
                     g->eval[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] += atkprefptrn[ptr][vx1];
                  }
               }
            }
            if (cnt4 == 7)
            {
               for (vx2 = 0, vy2 = 0; yy + vy2 < 23, vy2 < 9; vx2++, vy2++)
               {
                  if (xx + vx2 < 23 && yy + vy2 >= 4 && xx + vx2 >= 4)
                  {
                     g->pref[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] += atkprefptrn[ptr][vy2];
                     g->eval[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] += atkprefptrn[ptr][vy2];
                  }
               }
            }

            if (cnt5 == 7)
            {
               for (int vx = 0; xx + vx < 23, vx < 9; vx++)
               {
                  if (xx + vx >= 4)
                  {
                     g->pref[xx + vx - 4 + 19 * yy] += defprefptrn[ptr][vx];
                     g->eval[xx + vx - 4 + 19 * yy] -= defprefptrn[ptr][vx];
                  }
               }
            }
            if (cnt6 == 7)
            {
               for (int vy = 0; yy + vy < 23, vy < 9; vy++)
               {
                  if (yy + vy >= 4)
                  {
                     g->pref[xx + 19 * (yy + vy - 4)] += defprefptrn[ptr][vy];
                     g->eval[xx + 19 * (yy + vy - 4)] -= defprefptrn[ptr][vy];
                  }
               }
            }
            if (cnt7 == 7)
            {
               for (vx1 = 0, vy1 = 0; xx + vx1 < 23, vx1 < 9; vx1++, vy1--)
               {
                  if (yy + vy1 >= -4 && xx + vx1 >= 4 && yy + vy1 < 15)
                  {
                     g->pref[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] += defprefptrn[ptr][vx1];
                     g->eval[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] -= defprefptrn[ptr][vx1];
                  }
               }
            }
            if (cnt8 == 7)
            {
               for (vx2 = 0, vy2 = 0; yy + vy2 < 23, vy2 < 9; vx2++, vy2++)
               {
                  if (xx + vx2 < 23 && yy + vy2 >= 4 && xx + vx2 >= 4)
                  {
                     g->pref[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] += defprefptrn[ptr][vy2];
                     g->eval[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] -= defprefptrn[ptr][vy2];
                  }
               }
            }
            cnt1 = 0;
            cnt2 = 0;
            cnt3 = 0;
            cnt4 = 0;
            cnt5 = 0;
            cnt6 = 0;
            cnt7 = 0;
            cnt8 = 0;
         }
      }
   }

   int x = 0, y = 0;
   int limit[361][8];
   int dxy[8] = { -19, -18, 1, 20, 19, 18, -1, -20 };

   for (int i = 0; i < 361; i++)
   {
      x = i % 19;
      y = i / 19;
      limit[i][0] = y;
      limit[i][1] = (y > 18 - x) ? 18 - x : y;
      limit[i][2] = 18 - x;
      limit[i][3] = (18 - y > 18 - x) ? 18 - x : 18 - y;
      limit[i][4] = 18 - y;
      limit[i][5] = (18 - y > x) ? x : 18 - y;
      limit[i][6] = x;
      limit[i][7] = (y > x) ? x : y;
   }

   int index = 0, r = 0, mycount = 0, encount = 0;

   for (index = 0; index < 361; index++)
   {
      for (int ui = 0; ui < 8; ui++)
      {
         r = index;

         for (int k = 1; k < limit[index][ui]; ++k)
         {
            if (g->board[r] == cpuMark)
            {
               mycount++;
            }
            if (mycount > 0 && g->board[r] != cpuMark)
            {
               break;
            }
            if (g->board[r] == enemyMark)
            {
               encount++;
            }
            if (encount > 0 && g->board[r] != enemyMark)
            {
               break;
            }
            if (mycount == 5)
            {
               g->score[1] = 999999;
            }
            if (encount == 5)
            {
               g->score[2] = -999999;
            }
            r += dxy[ui];
         }
         mycount = 0;
         encount = 0;
      }
   }

   for (int i = 0; i < 361; i++) //삼삼 막기
   {
      thR = threeRule(g, i, 1);
      if (thR == 1 && g->board[i] == 0)
      {
         g->pref[i] += d[1];
      }
   }

   for (int n = 0; n < 361; n++)
   { //중복 방지용 겸 33 방지용
      if (threerule == 1)
      {
         thR = threeRule(g, n, 1);
         if (thR == 1 && g->board[n] == 0)
         {
            g->board[n] = 'X';
            g->pref[n] = -989999;
         }
         if (thR == 0 && g->board[n] == 'X')
         {
            g->board[n] = 0;
         }
      }
      if (g->board[n] == enemyMark)
      {
         g->pref[n] = -999999;
      }
      if (g->board[n] == cpuMark)
      {
         g->pref[n] = -999999;
      }
   }

   int temps = 0;
   double data[361] = { -1 };

   for (int j = 0; j < 361; j++)
   {
      data[j] = g->pref[j];
      if (g->board[j] >= 0)
      {
         opt[j] = j;
      }
   }

   for (int iu = 0; iu < 360; iu++)
   {
      for (int ju = iu + 1; ju < 361; ju++)
      {
         if (data[iu] < data[ju])
         {
            temp = data[iu];
            data[iu] = data[ju];
            data[ju] = temp;

            temps = opt[iu];
            opt[iu] = opt[ju];
            opt[ju] = temps;
         }
      }
   }
   //printf("Position = %d %d\n", opt[0] % 19 + 1, opt[0] / 19 + 1);
   return opt[point];
}

int whitepref(struct Gameboard* g, int threerule, int point)
{
   char cpuMark = 'W';
   char enemyMark = 'B';
   double temp = 0;
   double periadv = 0.05;
   double d[4] = { 2, 20, 32, 400 };
   double a[4] = { 2, 18, 30, 600 };
   double ctradv = 0.1;
   int thR = 0;
   int opt[361] = { -1 };
   char virt[4][9];
   char virtuoso[4][9];

   for (int p = 0; p < 19; p++)
   { //가운데로 갈수록 선호도 증가
      for (int px = p; px < 19 - p; px++)
      {
         for (int py = p; py < 19 - p; py++)
         {
            g->pref[px + 19 * py] += ctradv;
         }
      }
   }

   for (int ix5 = 0; ix5 < 19; ix5++)
   {
      for (int iy5 = 0; iy5 < 19; iy5++)
      {
         if (g->board[ix5 + 19 * iy5] == cpuMark)
         {
            for (int ix1 = ix5 - 2; ix1 <= ix5 + 2; ix1++)
            {
               for (int iy1 = iy5 - 2; iy1 <= iy5 + 2; iy1++)
               {
                  if (ix1 >= 0 && ix1 < 19 && iy1 >= 0 && iy1 < 19)
                  {
                     g->pref[ix1 + 19 * iy1] += periadv; // 주위 돌의 선호도
                  }
               }
            }
         }
      }
   }
   int vx1 = 0, vx2 = 0, vy1 = 0, vy2 = 0;
   int cnt1 = 0, cnt2 = 0, cnt3 = 0, cnt4 = 0, cnt5 = 0, cnt6 = 0, cnt7 = 0, cnt8 = 0;

   char defptrn[60][9]; //패턴 작성
   strcpy(defptrn[0], "nnnBBBnnn");

   strcpy(defptrn[1], "nnnWBBBnn");
   strcpy(defptrn[2], "nnBBBWnnn");

   strcpy(defptrn[3], "nnBBBBnnn"); //보류
   strcpy(defptrn[4], "nnnnBBnnn");

   strcpy(defptrn[5], "nnBnBBnnn");
   strcpy(defptrn[6], "nnnBBnBnn"); //패턴 추가하기

   strcpy(defptrn[7], "nnBBBBWnn");
   strcpy(defptrn[8], "nnWBBBBnn");

   strcpy(defptrn[9], "nnBBBnBnn");
   strcpy(defptrn[10], "nWBBBnBnn");
   strcpy(defptrn[11], "nnBBBnBWn");
   strcpy(defptrn[12], "nWBBBnBWn");

   strcpy(defptrn[13], "nnBnBBBnn");
   strcpy(defptrn[14], "nWBnBBBnn");
   strcpy(defptrn[15], "nnBnBBBWn");
   strcpy(defptrn[16], "nWBnBBBWn");

   strcpy(defptrn[17], "nnBBnBBnn");
   strcpy(defptrn[18], "nWBBnBBnn");
   strcpy(defptrn[19], "nnBBnBBWn");
   strcpy(defptrn[20], "nWBBnBBWn");

   strcpy(defptrn[21], "nnBnBBWnn");
   strcpy(defptrn[22], "nnBBnBWnn");
   strcpy(defptrn[23], "nnBBBnWnn");
   strcpy(defptrn[24], "nnWBnBBnn");
   strcpy(defptrn[25], "nnWBBnBnn");
   strcpy(defptrn[26], "nnWnBBBnn");

   strcpy(defptrn[27], "nWnBBBBWn");
   strcpy(defptrn[28], "nWBBBBnWn");

   strcpy(defptrn[29], "nnBnnBBnn");
   strcpy(defptrn[30], "nWBnnBBnn");
   strcpy(defptrn[31], "nnBnnBBWn");
   strcpy(defptrn[32], "nWBnnBBWn");

   strcpy(defptrn[33], "nnBBnnBnn");
   strcpy(defptrn[34], "nWBBnnBnn");
   strcpy(defptrn[35], "nnBBnnBWn");
   strcpy(defptrn[36], "nWBBnnBWn");

   strcpy(defptrn[37], "nnBnBnBnn");
   strcpy(defptrn[38], "nWBnBnBnn");
   strcpy(defptrn[39], "nnBnBnBWn");
   strcpy(defptrn[40], "nWBnBnBWn");

   strcpy(defptrn[41], "nnWnBnBBn");
   strcpy(defptrn[42], "nnWnBBnBn");
   strcpy(defptrn[43], "nBnBBnWnn");
   strcpy(defptrn[44], "nBBnBnWnn");

   double defprefptrn[60][9] = {
      {0, 0, 2 * d[2], 0, 0, 0, 2 * d[2], 0, 0},

      {0, 0, 0, 0, 0, 0, 0, d[0], d[0]},
      {d[0], d[0], 0, 0, 0, 0, 0, 0, 0},

      {0, d[1], 0, 0, 0, 0, d[1], 0, 0},
      {0, d[0], d[0], d[0], 0, 0, d[0], d[0], d[0]},

      {0, 0, 0, d[3], 0, 0, 0, 0, 0}, //5
      {0, 0, 0, 0, 0, d[3], 0, 0, 0},

      {0, d[3], 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, d[3], 0},

      {0, 0, 0, 0, 0, d[3], 0, 0, 0},
      {0, 0, 0, 0, 0, d[3], 0, 0, 0}, //10
      {0, 0, 0, 0, 0, d[3], 0, 0, 0},
      {0, 0, 0, 0, 0, d[3], 0, 0, 0},

      {0, 0, 0, d[3], 0, 0, 0, 0, 0},
      {0, 0, 0, d[3], 0, 0, 0, 0, 0},
      {0, 0, 0, d[3], 0, 0, 0, 0, 0}, //15
      {0, 0, 0, d[3], 0, 0, 0, 0, 0},

      {0, 0, 0, 0, d[3], 0, 0, 0, 0},
      {0, 0, 0, 0, d[3], 0, 0, 0, 0},
      {0, 0, 0, 0, d[3], 0, 0, 0, 0},
      {0, 0, 0, 0, d[3], 0, 0, 0, 0}, //20

      {0, d[1], 0, d[1], 0, 0, 0, 0, 0},
      {0, d[1], 0, 0, d[1], 0, 0, 0, 0},
      {0, d[1], 0, 0, 0, d[1], 0, 0, 0},
      {0, 0, 0, 0, d[1], 0, 0, d[1], 0},
      {0, 0, 0, 0, 0, d[1], 0, d[1], 0}, //25
      {0, 0, 0, d[1], 0, 0, 0, d[1], 0},

      {0, 0, d[3], 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, d[3], 0, 0},

      {0, d[1], 0, d[1], d[1], 0, 0, d[1], 0},
      {0, 0, 0, d[0], d[0], 0, 0, d[0], 0}, //30
      {0, d[0], 0, d[0], d[0], 0, 0, 0, 0},
      {0, 0, 0, d[0], d[0], 0, 0, 0, 0},

      {0, d[1], 0, 0, d[1], d[1], 0, d[1], 0},
      {0, 0, 0, 0, d[0], d[0], 0, d[0], 0},
      {0, d[0], 0, 0, d[0], d[0], 0, 0, 0}, //35
      {0, 0, 0, 0, d[0], d[0], 0, 0, 0},

      {0, d[1], 0, d[1], 0, d[1], 0, d[1], 0},
      {0, 0, 0, d[0], 0, d[0], 0, d[0], 0},
      {0, d[0], 0, d[0], 0, d[0], 0, 0, 0},
      {0, 0, 0, d[0], 0, d[0], 0, 0, 0}, //40

      {0, 0, 0, d[0], 0, d[3], 0, 0, d[0]},
      {0, 0, 0, d[0], 0, 0, d[3], 0, d[0]},
      {d[0], 0, d[3], 0, 0, d[0], 0, 0, 0},
      {d[0], 0, 0, d[3], 0, d[0], 0, 0, 0},
   };

   char atkptrn[60][9]; //패턴 작성
   strcpy(atkptrn[0], "nnnWWWnnn");

   strcpy(atkptrn[1], "nnnBWWWnn");
   strcpy(atkptrn[2], "nnWWWBnnn");

   strcpy(atkptrn[3], "nnWWnnnnn");
   strcpy(atkptrn[4], "nnnnnWWnn");

   strcpy(atkptrn[5], "nnWnWWnnn");
   strcpy(atkptrn[6], "nnnWWnWnn"); //패턴 추가하기

   strcpy(atkptrn[7], "nnWWWWBnn");
   strcpy(atkptrn[8], "nnBWWWWnn");

   strcpy(atkptrn[9], "nnWWWnWnn");
   strcpy(atkptrn[10], "nBWWWnWnn");
   strcpy(atkptrn[11], "nnWWWnWBn");
   strcpy(atkptrn[12], "nBWWWnWBn");

   strcpy(atkptrn[13], "nnWnWWWnn");
   strcpy(atkptrn[14], "nBWnWWWnn");
   strcpy(atkptrn[15], "nnWnWWWBn");
   strcpy(atkptrn[16], "nBWnWWWBn");

   strcpy(atkptrn[17], "nnWWnWWnn");
   strcpy(atkptrn[18], "nBWWnWWnn");
   strcpy(atkptrn[19], "nnWWnWWBn");
   strcpy(atkptrn[20], "nBWWnWWBn");

   strcpy(atkptrn[21], "nnWWWWnnn");
   strcpy(atkptrn[22], "nnWWWWnBn");
   strcpy(atkptrn[23], "nBnWWWWnn");

   strcpy(atkptrn[24], "nnWnWWBnn");
   strcpy(atkptrn[25], "nnWnWWnBn");
   strcpy(atkptrn[26], "nBnWnWWnn");

   strcpy(atkptrn[27], "nnWWnWBnn");
   strcpy(atkptrn[28], "nnWWnWnBn");
   strcpy(atkptrn[29], "nBnWWnWnn");

   strcpy(atkptrn[30], "nnBWnWWnn");
   strcpy(atkptrn[31], "nnBWWnWnn");

   double atkprefptrn[60][9] = {
      {0, a[1], a[1], 0, 0, 0, a[1], a[1], 0},

      {0, 0, 0, 0, 0, 0, 0, a[0], a[0]},
      {a[0], a[0], 0, 0, 0, 0, 0, 0, 0},

      {a[0], a[0], 0, 0, a[0], a[0], a[0], 0, 0},
      {0, 0, a[0], a[0], a[0], 0, 0, a[0], a[0]},

      {0, a[1], 0, a[3], 0, 0, a[1], 0, 0}, //5
      {0, 0, a[1], 0, 0, a[3], 0, a[1], 0},

      {0, 3 * a[3], 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 3 * a[3], 0},

      {0, 0, 0, 0, 0, a[3], 0, 0, 0},
      {0, 0, 0, 0, 0, a[3], 0, 0, 0}, //10
      {0, 0, 0, 0, 0, a[3], 0, 0, 0},
      {0, 0, 0, 0, 0, a[3], 0, 0, 0},

      {0, 0, 0, a[3], 0, 0, 0, 0, 0},
      {0, 0, 0, a[3], 0, 0, 0, 0, 0},
      {0, 0, 0, a[3], 0, 0, 0, 0, 0}, //15
      {0, 0, 0, a[3], 0, 0, 0, 0, 0},

      {0, 0, 0, 0, a[3], 0, 0, 0, 0},
      {0, 0, 0, 0, a[3], 0, 0, 0, 0},
      {0, 0, 0, 0, a[3], 0, 0, 0, 0},
      {0, 0, 0, 0, a[3], 0, 0, 0, 0}, //20

      {0, 3 * a[3], 0, 0, 0, 0, 3 * a[3], 0, 0},
      {0, a[3], 0, 0, 0, 0, a[3], 0, 0},
      {0, 0, a[3], 0, 0, 0, 0, a[3], 0},

      {0, a[2], 0, a[2], 0, 0, 0, 0, 0},
      {0, a[0], 0, a[3], 0, 0, a[0], 0, 0}, //25
      {0, 0, a[0], 0, a[3], 0, 0, a[0], 0},

      {0, a[2], 0, 0, a[2], 0, 0, 0, 0},
      {0, a[0], 0, 0, a[3], 0, a[0], 0, 0},
      {0, 0, a[0], 0, 0, a[3], 0, a[0], 0},

      {0, 0, 0, 0, a[1], 0, 0, a[1], 0}, //30
      {0, 0, 0, 0, 0, a[1], 0, a[1], 0},
   };

   for (int xx = 0; xx < 19; xx++)
   { //같은 패턴을 찾기
      for (int yy = 0; yy < 19; yy++)
      {
         int index = xx + 19 * yy;
         array(g, virt, index, 2);    //공격
         array(g, virtuoso, index, 1); //방어

         for (int ptr = 0; ptr < 60; ptr++)
         {
            for (int num = 1; num < 8; num++)
            {
               if (atkptrn[ptr][num] == virt[0][num])
               {
                  cnt1++;
               }
               if (atkptrn[ptr][num] == virt[1][num])
               {
                  cnt2++;
               }
               if (atkptrn[ptr][num] == virt[2][num])
               {
                  cnt3++;
               }
               if (atkptrn[ptr][num] == virt[3][num])
               {
                  cnt4++;
               }
               if (defptrn[ptr][num] == virtuoso[0][num])
               {
                  cnt5++;
               }
               if (defptrn[ptr][num] == virtuoso[1][num])
               {
                  cnt6++;
               }
               if (defptrn[ptr][num] == virtuoso[2][num])
               {
                  cnt7++;
               }
               if (defptrn[ptr][num] == virtuoso[3][num])
               {
                  cnt8++;
               }
            }
            if (cnt1 == 7)
            {
               for (int vx = 0; xx + vx < 23, vx < 9; vx++)
               {
                  if (xx + vx >= 4)
                  {
                     g->pref[xx + vx - 4 + 19 * yy] += atkprefptrn[ptr][vx];
                     g->eval[xx + vx - 4 + 19 * yy] += atkprefptrn[ptr][vx];
                  }
               }
            }
            if (cnt2 == 7)
            {
               for (int vy = 0; yy + vy < 23, vy < 9; vy++)
               {
                  if (yy + vy >= 4)
                  {
                     g->pref[xx + 19 * (yy + vy - 4)] += atkprefptrn[ptr][vy];
                     g->eval[xx + 19 * (yy + vy - 4)] += atkprefptrn[ptr][vy];
                  }
               }
            }

            if (cnt3 == 7)
            {
               for (vx1 = 0, vy1 = 0; xx + vx1 < 23, vx1 < 9; vx1++, vy1--)
               {
                  if (yy + vy1 >= -4 && xx + vx1 >= 4 && yy + vy1 < 15)
                  {
                     g->pref[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] += atkprefptrn[ptr][vx1];
                     g->eval[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] += atkprefptrn[ptr][vx1];
                  }
               }
            }
            if (cnt4 == 7)
            {
               for (vx2 = 0, vy2 = 0; yy + vy2 < 23, vy2 < 9; vx2++, vy2++)
               {
                  if (xx + vx2 < 23 && yy + vy2 >= 4 && xx + vx2 >= 4)
                  {
                     g->pref[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] += atkprefptrn[ptr][vy2];
                     g->eval[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] += atkprefptrn[ptr][vy2];
                  }
               }
            }

            if (cnt5 == 7)
            {
               for (int vx = 0; xx + vx < 23, vx < 9; vx++)
               {
                  if (xx + vx >= 4)
                  {
                     g->pref[xx + vx - 4 + 19 * yy] += defprefptrn[ptr][vx];
                     g->eval[xx + vx - 4 + 19 * yy] -= defprefptrn[ptr][vx];
                  }
               }
            }
            if (cnt6 == 7)
            {
               for (int vy = 0; yy + vy < 23, vy < 9; vy++)
               {
                  if (yy + vy >= 4)
                  {
                     g->pref[xx + 19 * (yy + vy - 4)] += defprefptrn[ptr][vy];
                     g->eval[xx + 19 * (yy + vy - 4)] -= defprefptrn[ptr][vy];
                  }
               }
            }
            if (cnt7 == 7)
            {
               for (vx1 = 0, vy1 = 0; xx + vx1 < 23, vx1 < 9; vx1++, vy1--)
               {
                  if (yy + vy1 >= -4 && xx + vx1 >= 4 && yy + vy1 < 15)
                  {
                     g->pref[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] += defprefptrn[ptr][vx1];
                     g->eval[xx + vx1 - 4 + 19 * (yy + vy1 + 4)] -= defprefptrn[ptr][vx1];
                  }
               }
            }
            if (cnt8 == 7)
            {
               for (vx2 = 0, vy2 = 0; yy + vy2 < 23, vy2 < 9; vx2++, vy2++)
               {
                  if (xx + vx2 < 23 && yy + vy2 >= 4 && xx + vx2 >= 4)
                  {
                     g->pref[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] += defprefptrn[ptr][vy2];
                     g->eval[xx + vx2 - 4 + 19 * (yy + vy2 - 4)] -= defprefptrn[ptr][vy2];
                  }
               }
            }
            cnt1 = 0;
            cnt2 = 0;
            cnt3 = 0;
            cnt4 = 0;
            cnt5 = 0;
            cnt6 = 0;
            cnt7 = 0;
            cnt8 = 0;
         }
      }
   }
   int x = 0, y = 0;
   int limit[361][8];
   int dxy[8] = { -19, -18, 1, 20, 19, 18, -1, -20 };

   for (int i = 0; i < 361; i++)
   {
      x = i % 19;
      y = i / 19;
      limit[i][0] = y;
      limit[i][1] = (y > 18 - x) ? 18 - x : y;
      limit[i][2] = 18 - x;
      limit[i][3] = (18 - y > 18 - x) ? 18 - x : 18 - y;
      limit[i][4] = 18 - y;
      limit[i][5] = (18 - y > x) ? x : 18 - y;
      limit[i][6] = x;
      limit[i][7] = (y > x) ? x : y;
   }

   int index = 0, r = 0, mycount = 0, encount = 0;

   for (index = 0; index < 361; index++)
   {
      for (int ui = 0; ui < 8; ui++)
      {
         r = index;

         for (int k = 1; k < limit[index][ui]; ++k)
         {
            if (g->board[r] == cpuMark)
            {
               mycount++;
            }
            if (mycount > 0 && g->board[r] != cpuMark)
            {
               break;
            }
            if (g->board[r] == enemyMark)
            {
               encount++;
            }
            if (encount > 0 && g->board[r] != enemyMark)
            {
               break;
            }
            if (mycount == 5)
            {
               g->score[2] = 999999;
            }
            if (encount == 5)
            {
               g->score[1] = -999999;
            }
            r += dxy[ui];
         }
         mycount = 0;
         encount = 0;
      }
   }

   for (int i = 0; i < 361; i++) //삼삼 막기
   {
      thR = threeRule(g, i, 1);
      if (thR == 1 && g->board[i] == 0)
      {
         g->pref[i] += d[1];
      }
   }

   for (int n = 0; n < 361; n++)
   { //중복 방지용 겸 33 방지용
      if (threerule == 1)
      {
         thR = threeRule(g, n, 2);
         if (thR == 1 && g->board[n] == 0)
         {
            g->board[n] = 'X';
            g->pref[n] = -989999;
         }
         if (thR == 0 && g->board[n] == 'X')
         {
            g->board[n] = 0;
         }
      }
      if (g->board[n] == enemyMark)
      {
         g->pref[n] = -999999;
      }
      if (g->board[n] == cpuMark)
      {
         g->pref[n] = -999999;
      }
   }

   int temps = 0;
   double data[361] = { -1 };

   for (int j = 0; j < 361; j++)
   {
      data[j] = g->pref[j];
      if (g->board[j] >= 0)
      {
         opt[j] = j;
      }
   }

   for (int iu = 0; iu < 360; iu++)
   {
      for (int ju = iu + 1; ju < 361; ju++)
      {
         if (data[iu] < data[ju])
         {
            temp = data[iu];
            data[iu] = data[ju];
            data[ju] = temp;

            temps = opt[iu];
            opt[iu] = opt[ju];
            opt[ju] = temps;
         }
      }
   }
   //printf("Position = %d %d\n", opt[0] % 19 + 1, opt[0] / 19 + 1);
   /*for(int i = 0; i < 361; i++)
   {
      printf("%d %d %0.lf\n",opt[i]%19+1,opt[i]/19+1,data[i]);
   }*/
   return opt[point];
}

int Putboard(struct Gameboard* g, int index, int us, int ai)
{
   int key = 0;
   int count = 0;
   int enemy = (us ^ 3);
   int dxy[8] = { -19, -18, 1, 20, 19, 18, -1, -20 };
   int limit[361][8];
   int x = 0, y = 0, k = 0, r = 0;
   char myMark;
   char enemyMark;
   if (us == 1)
   {
      myMark = 'B';
      enemyMark = 'W';
   }
   else
   {
      myMark = 'W';
      enemyMark = 'B';
   }

   for (int i = 0; i < 361; i++)
   {
      x = i % 19;
      y = i / 19;
      limit[i][0] = y;
      limit[i][1] = (y > 18 - x) ? 18 - x : y;
      limit[i][2] = 18 - x;
      limit[i][3] = (18 - y > 18 - x) ? 18 - x : 18 - y;
      limit[i][4] = 18 - y;
      limit[i][5] = (18 - y > x) ? x : 18 - y;
      limit[i][6] = x;
      limit[i][7] = (y > x) ? x : y;
   }

   if (index < 361 && index >= 0)
   {
      g->board[index] = myMark;

      for (int ui = 0; ui < 8; ui++)
      {
         r = index;

         for (k = 1; k < limit[index][ui]; ++k)
         {
            if (g->board[r] == myMark)
            {
               count++;
            }
            if (g->board[r] != myMark)
            {
               break;
            }
            if (count == 5 && ai == 0)
            {
               DisplayBoard(*g);
               gotoxy(60, 3);
               printf("%c팀의 승리!!\n", myMark);
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               return 1;
            }
            r += dxy[ui];
         }
         count = 0;
      }
   }
   else
   {
      printf("에러");
   }
   return 0;
}

int depth(struct Gameboard g, int us, int tn, int max_depth, int bTH, int wTH)
{
   int minval = -999999999, maxval = 999999999;
   char myMark, enemyMark;
   int caldepth = 0, en = 0;
   int slot[20];
   double score[20];
   int pos[20];
   int p[20];
   double nodescore = 0;
   int nodenum = 0, bFlag = 0, kk = 0;
   struct Gameboard ab[20];
   int limit[64][8] = { 0 };
   double t1 = 0, t2 = 0;
   int x = 0, y = 0, index = 0;
   int depth = 0;
   int estimate = 5;
   t1 = clock();

   if (us == 1)
   {
      en = 2;
      myMark = 'B';
      enemyMark = 'W';
   }
   else
   {
      en = 1;
      myMark = 'W';
      enemyMark = 'B';
   }

   for (int a = 0; a < max_depth; a++)
   {
      for (int b = 0; b < 361; b++)
      {
         if (a == 0)
         {
            ab[a].board[b] = g.board[b];
         }
         else
         {
            ab[a].board[b] = 0;
         }
      }
   }
   ab[0] = g;
   slot[0] = 0;
   p[0] = 0;
   score[0] = (tn == 1) ? minval : maxval;

   while (1)
   {   
      gotoxy(0, 25);
      printf("\r%3.2lf%%", (double)(nodenum * 100 / pow(estimate - 1, max_depth)));
      if (nodenum % 100 == 0)
      {
         for (int h = 0; h < nodenum / 100; h++)
         {
            printf(".");
         }
      }
      while (p[depth] < estimate)
      {
         if (tn == 1)
         {
            slot[depth] = blackpref(&ab[depth], bTH, p[depth]);
         }
         else
         {
            slot[depth] = whitepref(&ab[depth], wTH, p[depth]);
         }
         if (ab[depth].board[slot[depth]] == 0)
         {
            //printf("\nslot[%d] = %d, %d\n", depth, 1 + slot[depth] % 19, 1 + slot[depth] / 19);
            break;
         }

         p[depth]++;
      }

      if (p[depth] < estimate)
      {
         //printf("Turn = %d\n", tn);
         ab[depth + 1] = ab[depth];
         Putboard(&ab[depth + 1], slot[depth], tn, 1);
         depth++;
         tn ^= 3;
         if (caldepth < depth)
         {
            caldepth = depth;
         }

         score[depth] = (tn == 1) ? minval : maxval;
         nodenum++;
         slot[depth] = 0;
         p[depth] = 0;
         if (depth != max_depth)
         {
            //printf("depth transferred\n");
            continue;
         }

         //printf("node %lf\n", nodescore);

         for (int r = 0; r < 361; r++)
         {
            ab[depth].score[tn] += ab[depth].eval[r];
         }

         nodescore = ab[depth].score[1] - ab[depth].score[2];
      }
      else if (depth == 0)
      {
         break;
      }
      else
      {
         nodescore = score[depth];
      }

      bFlag = 0;

      if (tn == 2) // max check
      {
         if (score[depth - 1] >= nodescore)
            bFlag = 1;
      }
      else // min check
      {
         if (score[depth - 1] <= nodescore)
            bFlag = 1;
      }
      depth--;
      tn ^= 3;

      if (bFlag == 0)
      {
         score[depth] = nodescore;
         pos[depth] = slot[depth];
         if (depth > 0)
         {
            if (tn == 2) // max check
            {
               if (score[depth - 1] >= nodescore)
                  bFlag = 1;
            }
            else // min check
            {
               if (score[depth - 1] <= nodescore)
                  bFlag = 1;
            }
            if (bFlag == 1)
            {
               depth--;
               tn ^= 3;
            }
         }
      }

      /*for (int i = 1; i < max_depth; i++)
      {
         printf("%d번째 가상\n", i);
         DisplayBoard(ab[i]);
      }*/
      p[depth]++;
   }

   t2 = clock();
   gotoxy(0, 25);
   printf("\r살핀 노드의 수 : %4d, %d수 앞까지 봄\n", nodenum, caldepth/2);
   printf("걸린 시간 : %2.3lf초\n", (float)(t2 - t1) / CLOCKS_PER_SEC);
   printf("CPU 가로 : %2d ,세로 : %2d 에 착수, DATA : %3d \n", pos[0] % 19 + 1, pos[0] / 19 + 1, pos[0]);

   return pos[0];
}

int main()
{
   int x1 = 0, y1 = 0;
   int key = 0;
   int index = 0;
   int autoindex = 0;
   int turn = 1, tr = 0, mode = 0, btrsw = 0, wtrsw = 0;
   struct Gameboard g;
   char temp[4][9];
   int opt[361] = { 0 };
   int cnt = 0;
   srand(time(NULL));

   for (int i = 0; i < 361; i++)
   {
      g.board[i] = 0;
      g.pref[i] = 0;
      g.eval[i] = 0;
   }

   for (int i = 0; i < 4; i++)
   {
      for (int j = 0; j < 9; j++)
      {
         temp[i][j] = 'n';
      }
   }
   printf("~~ 오목~~\n 1.흑\n 2.백\n 3.커스텀\n 4.기존AI끼리 대전\n 5.AB AI끼리 대전\n 6.서로 다른 AI끼리 대결\n주의사항 : ◇표시 있는 곳에는 놓을 수 없어요!\n");
logo:
   scanf("%d", &mode);
   if (mode >= 7 || mode == 0)
   {
      printf("다시 입력하세요!!!\n");
      goto logo;
   }
   system("cls");
   while (1)
   {
      if (btrsw == 1 || wtrsw == 1)
      {
         for (int i = 0; i < 361; i++)
         {
            if (g.board[i] == 'X')
            {
               g.board[i] = 0;
            }
            tr = threeRule(&g, i, turn);
            if (tr == 1 && g.board[i] == 0)
            {
               g.board[i] = 'X';
            }
            if (tr == 0 && g.board[i] == 'X')
            {
               g.board[i] = 0;
            }
         }
      }

      if (mode == 1)
      {
         if (turn == 1)
         {
            if (cnt == 0)
            {
               Putboard(&g, 180, 1, 0);
               goto Next;
            }
            btrsw = 1;
         Input0:
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("흑팀의 차례");
            gotoxy(cx, cy);
            while (1)
            {
               key = _getch();
               move(key);
               if (key == ENTER)
               {
                  x1 = cx / 2 - 3;
                  y1 = cy - 2;
                  break;
               }
            }
            index = x1 - 1 + 19 * (y1 - 1);
            if (g.board[index] != 0)
            {
               gotoxy(0, 24);
               printf("다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input0;
            }
            if (btrsw == 1 && threeRule(&g, index, 1) == 1)
            {
               gotoxy(0, 24);
               printf("삼삼이에요. 다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input0;
            }
            else
            {
               if (Putboard(&g, index, 1, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 1);
            }
         }
         if (turn == 2)
         {
            if (cnt == 1)
            {
               if (rand() % 2 == 0)
               {
                  Putboard(&g, 161, 2, 0);
               }
               else
               {
                  Putboard(&g, 162, 2, 0);
               }
               goto Next;
            }
            wtrsw = 0;
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("백팀의 차례");
            gotoxy(0, 25);
            autoindex = depth(g, turn, 2, 6, btrsw, wtrsw);
            if (autoindex == 64)
            {
               goto Next;
            }
            if (Putboard(&g, autoindex, 2, 0) == 1)
            {
               return 0;
            }
         }
      }
      if (mode == 2)
      {
         if (turn == 2)
         {
            wtrsw = 0;
         Input2:
            if (cnt == 1)
            {
               printf("처음 착수 시에는 10 9, 11 9만 가능합니다.\n");
            }
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("백팀의 차례");
            gotoxy(cx, cy);
            while (1)
            {
               key = _getch();
               move(key);
               if (key == ENTER)
               {
                  x1 = cx / 2 - 3;
                  y1 = cy - 2;
                  break;
               }
            }
            
            index = x1 - 1 + 19 * (y1 - 1);
            if (cnt == 1 && (index != 161 && index != 162))
            {
               gotoxy(0, 24);
               printf("다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input2;
            }
            if (g.board[index] != 0)
            {
               gotoxy(0, 24);
               printf("다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input2;
            }
            if (wtrsw == 1 && threeRule(&g, index, 2) == 1)
            {
               gotoxy(0, 24);
               printf("삼삼이에요. 다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input2;
            }
            else
            {
               if (Putboard(&g, index, 2, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 1);
            }
         }
         if (turn == 1)
         {
            if (cnt == 0)
            {
               Putboard(&g, 180, 1, 0);
               goto Next;
            }
            btrsw = 0;
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("흑팀의 차례\n");
            autoindex = depth(g, turn, 1, 4, btrsw, wtrsw);
            if (autoindex == 64)
            {
               goto Next;
            }
            if (Putboard(&g, autoindex, 1, 0) == 1)
            {
               return 0;
            }
         }
      }
      if (mode == 3)
      {
         if (turn == 1)
         {
            btrsw = 1;
         Input5:
            DisplayBoard(g);
            DisplayData(g);
            gotoxy(4, 1);
            printf("흑팀의 차례");
            gotoxy(cx, cy);
            while (1)
            {
               key = _getch();
               move(key);
               if (key == ENTER)
               {
                  x1 = cx / 2 - 3;
                  y1 = cy - 2;
                  break;
               }
            }
            index = x1 - 1 + 19 * (y1 - 1);
            if (btrsw == 1 && threeRule(&g, index, 1) == 1)
            {
               gotoxy(0, 24);
               printf("삼삼이에요. 다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input5;
            }
            else
            {
               if (Putboard(&g, index, 1, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 1);
            }
         }

         if (turn == 2)
         {
            wtrsw = 0;
         Input6:
            DisplayBoard(g);
            DisplayData(g);
            gotoxy(4, 1);
            printf("흑팀의 차례");
            gotoxy(cx, cy);
            while (1)
            {
               key = _getch();
               move(key);
               if (key == ENTER)
               {
                  x1 = cx / 2 - 3;
                  y1 = cy - 2;
                  break;
               }
            }
            index = x1 - 1 + 19 * (y1 - 1);
            if (wtrsw == 1 && threeRule(&g, index, 2) == 1)
            {
               gotoxy(0, 24);
               printf("삼삼이에요. 다시 입력하세요.\n");
               while (1)
               {
                  key = _getch();
                  if (key == ENTER) break;
               }
               system("cls");
               goto Input6;
            }
            else
            {
               if (Putboard(&g, index, 2, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 2);
            }
         }
      }
      if (mode == 4)
      {
         if (turn == 1)
         {
            if (cnt == 0)
            {
               Putboard(&g, 180, 1, 0);
               goto Next;
            }
            btrsw = 0;
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("흑팀의 차례\n");
         Input7:
            index = blackpref(&g, 0, 0);
            if (btrsw == 1 && threeRule(&g, index, 1) == 1)
            {
               goto Input7;
            }

            else
            {
               if (Putboard(&g, index, 1, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 1);
            }
         }

         if (turn == 2)
         {
            if (cnt == 1)
            {
               if (rand() % 2 == 0)
               {
                  Putboard(&g, 161, 2, 0);
               }
               else
               {
                  Putboard(&g, 162, 2, 0);
               }
               goto Next;
            }
            wtrsw = 0;
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("백팀의 차례\n");
         Input8:
            index = whitepref(&g, 0, 0);
            if (wtrsw == 1 && threeRule(&g, index, 2) == 1)
            {
               goto Input8;
            }
            else
            {
               if (Putboard(&g, index, 2, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 1);
            }
         }
      }
      if (mode == 5)
      {
         if (turn == 1)
         {
            if (cnt == 0)
            {
               Putboard(&g, 180, 1, 0);
               goto Next;
            }
            btrsw = 0;
            DisplayBoard(g);
            DisplayPref(g);
            gotoxy(4, 1);
            printf("흑팀의 차례\n");
            autoindex = depth(g, turn, 1, 4, btrsw, wtrsw);
            if (autoindex == 64)
            {
               goto Next;
            }
            if (Putboard(&g, autoindex, 1, 0) == 1)
            {
               return 0;
            }
         }

         if (turn == 2)
         {
            if (cnt == 1)
            {
               if (rand() % 2 == 0)
               {
                  Putboard(&g, 161, 2, 0);
               }
               else
               {
                  Putboard(&g, 162, 2, 0);
               }
               goto Next;
            }
            wtrsw = 0;
            DisplayBoard(g);
            DisplayPref(g);
            gotoxy(4, 1);
            printf("백팀의 차례\n");
            autoindex = depth(g, turn, 2, 4, btrsw, wtrsw);
            if (autoindex == 64)
            {
               goto Next;
            }
            if (Putboard(&g, autoindex, 2, 0) == 1)
            {
               return 0;
            }
         }
      }
      if (mode == 6)
      {
         if (turn == 1)
         {
            if (cnt == 0)
            {
               Putboard(&g, 180, 1, 0);
               goto Next;
            }
            btrsw = 0;
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("흑팀의 차례\n");
         Input9:
            index = blackpref(&g, 0, 0);
            if (btrsw == 1 && threeRule(&g, index, 1) == 1)
            {
               goto Input9;
            }

            else
            {
               if (Putboard(&g, index, 1, 0) == 1)
               {
                  return 0;
               }
               //array(&g, temp, index, 1);
            }
         }

         if (turn == 2)
         {
            if (cnt == 1)
            {
               if (rand() % 2 == 0)
               {
                  Putboard(&g, 161, 2, 0);
               }
               else
               {
                  Putboard(&g, 162, 2, 0);
               }
               goto Next;
            }
            wtrsw = 0;
            DisplayBoard(g);
            gotoxy(4, 1);
            printf("백팀의 차례\n");
            autoindex = depth(g, turn, 2, 6, btrsw, wtrsw);
            if (autoindex == 64)
            {
               goto Next;
            }
            if (Putboard(&g, autoindex, 2, 0) == 1)
            {
               return 0;
            }
         }
      }
   Next:
      cnt++;
      turn ^= 3;
      //system("cls");
   }
}