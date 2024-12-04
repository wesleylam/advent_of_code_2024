#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int parse(int *lineNums, char *line, int starti, int endi)
{
    char subString[endi - starti + 2];
    memcpy( subString, &line[starti], (endi - starti + 1) * sizeof(int) );
    return atoi(subString);
}

int findAll(char map[140][141], int i, int j)
{
    int jLim = 140 - 4;
    int iLim = 140 - 4;

    int subTotal = 0;
    // top
    if (i>=3 && map[i-1][j] == 'M' && map[i-2][j] == 'A' && map[i-3][j] == 'S')
    {
        subTotal += 1;
    }
    // top left
    if (i>=3 && j>=3 && map[i-1][j-1] == 'M' && map[i-2][j-2] == 'A' && map[i-3][j-3] == 'S')
    {
        subTotal += 1;
    }
    // top right
    if (i>=3 && j<=jLim && map[i-1][j+1] == 'M' && map[i-2][j+2] == 'A' && map[i-3][j+3] == 'S')
    {
        subTotal += 1;
    }
    // bot
    if (i<=iLim && map[i+1][j] == 'M' && map[i+2][j] == 'A' && map[i+3][j] == 'S')
    {
        subTotal += 1;
    }
    // bot left
    if (i<=iLim && j>=3 && map[i+1][j-1] == 'M' && map[i+2][j-2] == 'A' && map[i+3][j-3] == 'S')
    {
        subTotal += 1;
    }
    // bot right
    if (i<=iLim && j<=jLim && map[i+1][j+1] == 'M' && map[i+2][j+2] == 'A' && map[i+3][j+3] == 'S')
    {
        subTotal += 1;
    }
    // left
    if (j>=3 && map[i][j-1] == 'M' && map[i][j-2] == 'A' && map[i][j-3] == 'S')
    {
        subTotal += 1;
    }
    // right
    if (j<=jLim && map[i][j+1] == 'M' && map[i][j+2] == 'A' && map[i][j+3] == 'S')
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
    for (i = 0; i<140; i++)
    {
        
        for (j = 0; j<140; j++)
        {
            if (map[i][j] == 'X')
            {
                // find in 8 direction
                total += findAll(map, i, j);

            }
        }
        
    }
    printf("total %d\n", total);

    return 0;
}
