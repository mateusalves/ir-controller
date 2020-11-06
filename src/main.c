#include <stdio.h>
#include <stdlib.h>
#include "irFunctions.h"

int main(int agrc, char *argv[])
{
    printf("Hello World! - Butter Robot \n");

    const char *commandInBinary;

    commandInBinary = ir_receiver();

    for (int i = 0; i < 10; i++)
    {
        printf("%d seconds have passed\n", i + 1);
    }
    
    printf("commandInBinary: %s\n", commandInBinary);
    ir_transmitter(commandInBinary);


    return 0;
}