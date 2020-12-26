package CodeUp;


import java.util.*;
public class Print{
    public static void main(String[] arv) throws Exception
    {
        //int a;
        Scanner sc= new Scanner(System.in);
        String[] input = sc.nextLine().split("\\.");
        int y= Integer.parseInt(input[0]);
        int a= Integer.parseInt(input[1]);
        int b= Integer.parseInt(input[2]);
        //a = Integer.parseInt(input);
        System.out.printf("%04d.%02d.%02d%n",y,a,b);
        //System.out.println("\u250C\u252C\u2510");
        //System.out.println("\u251C\u253C\u2524");
        //System.out.println("\u2514\u2534\u2518");
    }
}
/*
#include <stdio.h>
#include <string.h>
#
int main(){
    char input[15];
    scanf("%s",input);
    char *tok = strtok(input,".");
    printf("%04s",*tok);
    tok = strtok(NULL,".");
    printf("%02s",*tok);

    tok = strtok(NULL," ");
    printf("%02s",*tok);
}
*/