#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int parse(int *lineNums, char *line, int starti, int endi)
{
    char subString[endi - starti + 2];
    memcpy( subString, &line[starti], (endi - starti + 1) * sizeof(int) );
    return atoi(subString);
}

int safe(int a, int b)
{
    return !(a==b || (a-b > 0 ? a - b > 3 : b - a > 3));
}

int side(int a, int b)
{
    return a < b;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("GIVE A FILE");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("CANNOT READ FILE");
        return 1;
    }
    
    int buf = fgetc(file);
    while (buf != EOF)
    {
        printf("%c", buf);
        buf = fgetc(file);
    }
    
    fclose(file);
    return 0;
}

