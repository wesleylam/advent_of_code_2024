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

    char line[100];
    int tempPrev;
    int totalSafeCount = 0;
    while (fgets(line, sizeof(line), file) != NULL) {

        int lineCount = 0;
        int lineNum[10];
        int starti = 0; 
        int endi;
        int unsafeOnce = 0;
        int tempNum0;
        int tempNum1;
        int tempNum2;
        int tempNum3;
        int noSide = 1;
        int sideSaved = 0;

        for (int i=0; i<100; i++) // per char
        {
            // space, next number
            if (line[i] == ' ' || line[i] == '\n')
            {
                endi = i - 1;
                int newParsed = parse(lineNum, line, starti, endi);
                lineNum[lineCount] = newParsed;
                
                if (lineCount == 0)
                {
                    tempNum0 = newParsed;
                }
                else if (lineCount == 1)
                {
                    tempNum1 = newParsed;
                }
                else if (lineCount == 2)
                {
                    tempNum2 = newParsed;
                }
                else if (lineCount >= 3)
                {
                    int possible = 0;
                    tempNum3 = newParsed;
                    int safe1 = safe(tempNum0, tempNum1);
                    int safe2 = safe(tempNum1, tempNum2);
                    int safe3 = safe(tempNum2, tempNum3);
                    int side1 = side(tempNum0, tempNum1);
                    int side2 = side(tempNum1, tempNum2);
                    int side3 = side(tempNum2, tempNum3);

                    if (safe1 && safe2 && safe3 && side1 == side2 && side2 == side3)
                    {
                        if (noSide)
                        {
                            noSide = 0;
                            sideSaved = side3;
                        }
                        if (sideSaved == side3)
                        {
                            tempNum0 = tempNum1;
                            tempNum1 = tempNum2;
                            tempNum2 = tempNum3;
                            possible = 1;
                        }
                    }

                    // give up num 0
                    if (!possible && !unsafeOnce && safe2 && safe3 && side2 == side3)
                    {
                        if (noSide)
                        {
                            noSide = 0;
                            sideSaved = side3;
                        }
                        if (sideSaved == side3)
                        {
                            tempNum0 = tempNum1;
                            tempNum1 = tempNum2;
                            tempNum2 = tempNum3;
                            possible = 1;
                            unsafeOnce = 1;
                        }
                    }
                    
                    // give up num 1
                    if (!possible && !unsafeOnce && safe(tempNum0, tempNum2) && safe3 && side(tempNum0, tempNum2) == side3)
                    {
                        if (noSide)
                        {
                            noSide = 0;
                            sideSaved = side3;
                        }
                        if (sideSaved == side3)
                        {
                            tempNum0 = tempNum0;
                            tempNum1 = tempNum2;
                            tempNum2 = tempNum3;
                            possible = 1;
                            unsafeOnce = 1;
                        }
                    }
                    
                    // give up num 2
                    if (!possible && !unsafeOnce && safe1 && safe(tempNum1, tempNum3) && side1 == side(tempNum1, tempNum3))
                    {
                        if (noSide)
                        {
                            noSide = 0;
                            sideSaved = side1;
                        }
                        if (sideSaved == side1)
                        {
                            tempNum0 = tempNum0;
                            tempNum1 = tempNum1;
                            tempNum2 = tempNum3;
                            possible = 1;
                            unsafeOnce = 1;
                        }
                    }

                    // give up num 3
                    if (!possible && !unsafeOnce && safe1 && safe2 && side1 == side2)
                    {
                        if (noSide)
                        {
                            noSide = 0;
                            sideSaved = side2;
                        }
                        if (sideSaved == side2)
                        {
                            // No change
                            tempNum0 = tempNum0;
                            tempNum1 = tempNum1;
                            tempNum2 = tempNum2;
                            possible = 1;
                            unsafeOnce = 1;
                        }
                    }
                    if (!possible)
                    {
                        // printf("BROKEN2 %d\n %s", lineCount, line);
                        // printf("%d, %d, %d, %d\n", tempNum0, tempNum1, tempNum2, tempNum3);
                        // printf("%d, %d, %d\n", safe1, safe2, safe3);
                        // printf("%d, %d, %d, %d\n\n", side1, side2, side3, sideSaved);
                        lineCount++;
                        starti = i + 1;
                        break;
                    }
                }
                lineCount++;
                starti = i + 1;
            }
            
            // end of line
            if (line[i] == '\n')
            {
                totalSafeCount++;
                break;
            }
        }
        
    }

    printf("TOTALSAFE: %d\n", totalSafeCount);
    fclose(file);
    return 0;
}

