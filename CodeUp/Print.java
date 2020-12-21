package CodeUp;


import java.util.*;
public class Print{
    public static void main(String[] arv) throws Exception
    {
        char x;
        Scanner sc= new Scanner(System.in);
        x = sc.next().charAt(0);
        System.out.printf("%c%n",x);
        //System.out.println("\u250C\u252C\u2510");
        //System.out.println("\u251C\u253C\u2524");
        //System.out.println("\u2514\u2534\u2518");
    }
}
/*
#include <stdio.h>
int main(){
    printf("\u250C\u252C\u2510\n");
    printf("\u251C\u253C\u2524\n");
    printf("\u2514\u2534\u2518\n");
}
*/