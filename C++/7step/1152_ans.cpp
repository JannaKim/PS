#include <stdio.h>
#include <string.h>
#include <unistd.h>

int is_alpha(char c) {
    if( ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'))
        return 1;
    else
        return 0;
}


char *strip_space(char *str) {
    while(*str == ' ') str++;

    if(*str == 0 )
        return str;
    
    char *end = str + strlen(str) - 1;
    while( (end > str) && ((*end == 0x20) || (*end == 0xa)) ) {
        end--;
    }

    end[1] = 0;
    return str;
}


int main() {
    char buf[1000001] = { 0, };
    char *ptr;
    int cnt = 0;

    read(0, buf, 1000000);

    ptr = strip_space(buf);
    if(is_alpha(ptr[0])) cnt=1;

    for(int i = 0; i < strlen(ptr); i++) {
        if(ptr[i] == ' ') {
            cnt++;
        }
    }
    
    printf("%d\n", cnt);
    return 0;
}