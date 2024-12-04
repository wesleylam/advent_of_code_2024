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

    char doFunc[] = "do()\0";
    char dontFunc[] = "don't()\0";
    int activated = 1;
    int a = 0;
    int b = 0;
    char mulPrefix[5] = "mul(\0";
    int i = 0;
    char num1Str[4];
    char num2Str[4];
    int j = 0;
    int firstNum = 1;
    long total = 0;
    long totalCount = 0;
    
    int buf = fgetc(file);
    while (buf != EOF)
    {
        int reset = 0;
        if (i == 4) // in bracket
        {
            int validChar = (buf >= 48 && buf <= 57) || buf == ',' || buf == ')';
            if (!validChar)
            {
                // invalid character, reset
                reset = 1;
            }
            else if (buf == ',')
            {
                if (j == 0) // first numebr is empty
                {
                    // reset
                    reset = 1;
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
                reset = 1;
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
        else if (buf == mulPrefix[i] && activated)
        {
            // match prefix
            i++;
        }
        else if (buf == doFunc[a] || buf == dontFunc[b])
        {
            if (buf == doFunc[a] && buf == dontFunc[b])
            {
                a++; b++;
            }
            else if (buf == doFunc[a])
            {
                // match prefix
                a++;
                b = 0;
                if (a == strlen(doFunc))
                {
                    activated = 1;
                    a = 0;
                }
            }
            else if (buf == dontFunc[b])
            {
                // match prefix
                b++;
                a = 0;
                if (b == strlen(dontFunc))
                {
                    activated = 0;
                    b = 0;
                }
            }
        }
        else
        {
            // reset match prefix
            i = 0;
            a = 0;
            b = 0;
        }


        // reset if flagged
        if (reset)
        {
            
            num1Str[0] = '\0';
            num2Str[0] = '\0';
            i = 0;
            j = 0;
            firstNum = 1;
        }
        // get new buffer
        buf = fgetc(file);
    }
    
    fclose(file);
    printf("\nCLOSE FILE, %d, %d\n", total, totalCount);
    return 0;
}