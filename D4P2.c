#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int parse(int *lineNums, char *line, int starti, int endi)
{
    char subString[endi - starti + 2];
    memcpy( subString, &line[starti], (endi - starti + 1) * sizeof(int) );
    return atoi(subString);
}

int findAllP2(char map[140][141], int i, int j)
{
    int subTotal = 0;
    // top
    if (map[i-1][j-1] == 'M' && map[i-1][j+1] == 'M' 
        && map[i+1][j-1] == 'S' && map[i+1][j+1] == 'S')
    {
        subTotal += 1;
    }
    // left
    if (map[i-1][j-1] == 'M' && map[i-1][j+1] == 'S' 
        && map[i+1][j-1] == 'M' && map[i+1][j+1] == 'S')
    {
        subTotal += 1;
    }
    // bot
    if (map[i-1][j-1] == 'S' && map[i-1][j+1] == 'S' 
        && map[i+1][j-1] == 'M' && map[i+1][j+1] == 'M')
    {
        subTotal += 1;
    }
    // right
    if (map[i-1][j-1] == 'S' && map[i-1][j+1] == 'M' 
        && map[i+1][j-1] == 'S' && map[i+1][j+1] == 'M')
    {
        subTotal += 1;
    }
    // printf("%d - %d %d\n", subTotal, i, j);
    return subTotal;
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

    char map[140][141];
    int i = 0; int j = 0;

    int buf = fgetc(file);
    while (buf != EOF)
    {
        if (buf == '\n' || buf == EOF)
        {
            map[i][j] = '\0';
            j = 0;
            i++;
        }
        else
        {
            map[i][j] = buf;
            j++;
        }
        buf = fgetc(file);
    }
    fclose(file);

    int total = 0;
    for (i = 1; i<139; i++)
    {
        
        for (j = 1; j<139; j++)
        {
            if (map[i][j] == 'A')
            {
                total += findAllP2(map, i, j);
            }
        }
        
    }
    printf("total %d\n", total);

    return 0;
}
