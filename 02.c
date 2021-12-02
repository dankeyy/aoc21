#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    FILE *fp = fopen("02.txt", "r");
    if (!fp) exit(EXIT_FAILURE);

    char op[16];
    int x, pos = 0, aim_depth = 0, real_depth = 0;

    do
    {
        fscanf(fp, "%s %d", op, &x);

        if(strcmp(op, "forward") == 0)
        {
            pos += x;
            real_depth += aim_depth * x;
        }

        else if(strcmp(op, "up") == 0)
        {
            aim_depth -= x;
        }

        else if(strcmp(op, "down") == 0)
        {
            aim_depth += x;
        }

    } while (!feof(fp));

    fclose(fp);
    printf("%d\n%d\n", aim_depth * pos, real_depth * pos);
}
