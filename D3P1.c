#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int parse(int *lineNums, char *line, int starti, int endi)
{
    char subString[endi - starti + 2];
    memcpy( subString, &line[starti], (endi - starti + 1) * sizeof(int) );
    return atoi(subString);
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

    char mulPrefix[5] = "mul(\0";
    char num1Str[4];
    char num2Str[4];
    int i = 0;
    int j = 0;
    int firstNum = 1;
    long total = 0;
    long totalCount = 0;
    
    int buf = fgetc(file);
    while (buf != EOF)
    {
        if (i == 4) // in bracket
        {
            int validChar = (buf >= 48 && buf <= 57) || buf == ',' || buf == ')';
            if (!validChar)
            {
                // invalid character, reset
                num1Str[0] = '\0';
                num2Str[0] = '\0';
                i = 0;
                j = 0;
                firstNum = 1;
            }
            else if (buf == ',')
            {
                if (j == 0) // first numebr is empty
                {
                    // reset
                    num1Str[0] = '\0';
                    num2Str[0] = '\0';
                    i = 0;
                    j = 0;
                    firstNum = 1;
                }
                else
                {
                    // wrap up first number, start record second number
                    num1Str[j] = '\0';
                    j = 0;
                    firstNum = 0;
                }
            }
            else if (buf == ')') // complete statment, calculate
            {
                if (firstNum == 0 || j == 0) // ignore if no second num
                {
                    num2Str[j] = '\0';
                    int prod = atoi(num1Str) * atoi(num2Str);
                    total += prod;
                    totalCount += 1;
                }

                // reset
                num1Str[0] = '\0';
                num2Str[0] = '\0';
                i = 0;
                j = 0;
                firstNum = 1;
            }
            else
            {
                // record character
                if (firstNum)
                    num1Str[j++] = buf;
                else 
                    num2Str[j++] = buf;
            }
        }
        else if (buf == mulPrefix[i])
        {
            // match prefix
            i++;
        }
        else
        {
            // reset match prefix
            i = 0;
        }
        buf = fgetc(file);
    }
    
    fclose(file);
    printf("\nCLOSE FILE, %d, %d\n", total, totalCount);
    return 0;
}