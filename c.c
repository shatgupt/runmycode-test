/*
  This program won't run properly without an input.
  Try with: abc
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    puts("Hello World from C!");
    char *buffer = NULL;
    long unsigned int len;
    getline(&buffer, &len, stdin);
    printf("%s", buffer);
    free(buffer);
    return 0;
}
