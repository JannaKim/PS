#include <stdio.h>

void try2(int (*arr)[3]){
    printf("%d", arr[0][1]);
}
void try1(int (*arr)[3]){
    try2(arr);
}
int main(){
    int arr[][3] = {{1,2,3}, {4,5,6}};
    try1(arr);
}