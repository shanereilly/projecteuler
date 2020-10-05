#include <stdio.h>

int main() {
    extern int strlen(char*);
    extern void itostr(int, char*);

    char* teststr = "Hello world!\n";
    int len = strlen(teststr);
    printf("%d\n", len);
    printf("%s\n", "Test1, should be 13");
    
    char buff[100];
    int testint = 16;
    itostr(testint, buff);
    printf("%s\n", buff); 
    printf("%s\n", "Test2, should be 16");
    return 0;
}
