#include <stdio.h>
#include <pigpio.h>
#include <string.h>
#include <stdlib.h>
#include "ir-slinger/irslinger.h"

char *ir_receiver(void)
{
    uint32_t startTime;
    uint32_t rightNow;
    int inPin = 23;
    int command[67][2];
    int pulseLength;
    int numOnes = 0;
    int previousValue = 0;
    char binaryCommand[33] = "";
    char *returnCommandString = binaryCommand;

    if (gpioInitialise() < 0)
    {
        printf("GPIO Initialization failed\n");
        return NULL;
    }

    gpioSetMode(inPin, PI_INPUT);
    while (1)
    {
        int value = 1;
        while (value)
            value = gpioRead(inPin);

        startTime = gpioTick();

        int loopCounter = 0;
        for (;;)
        {
            if (value != previousValue)
            {
                rightNow = gpioTick();
                pulseLength = rightNow - startTime;
                startTime = rightNow;

                command[loopCounter][0] = previousValue;
                command[loopCounter][1] = pulseLength;
                printf("\t%d %d %d\n", loopCounter, command[loopCounter][0], command[loopCounter][1]);
                loopCounter++;
            }

            if (value)
                numOnes += 1;
            else
                numOnes = 0;

            previousValue = value;
            value = gpioRead(inPin);

            if (numOnes > 50000)
            {
                printf("LoopCounter: %d\n", loopCounter);
                break;
            }
        }
        printf("Binary command: ");
        for (int i = 3; i <= 66; i++)
        {
            if (command[i][0])
                command[i][1] > 1000 ? strcat(binaryCommand, "1") : strcat(binaryCommand, "0");
        }
        printf("\n");
        printf("%s\n", binaryCommand);
        
        if (loopCounter > 66)
        {
            gpioTerminate();
            return returnCommandString;
        }
        strcpy(binaryCommand, "");
    }
}

int ir_transmitter(const char *binaryCommand)
{
    uint32_t outPin = 18;            // The Broadcom pin number the signal will be sent on
    int frequency = 38000;           // The frequency of the IR signal in Hz
    double dutyCycle = 0.5;          // The duty cycle of the IR signal. 0.5 means for every cycle,
                                     // the LED will turn on for half the cycle time, and off the other half
    int leadingPulseDuration = 9000; // The duration of the beginning pulse in microseconds
    int leadingGapDuration = 4500;   // The duration of the gap in microseconds after the leading pulse
    int onePulse = 562;              // The duration of a pulse in microseconds when sending a logical 1
    int zeroPulse = 562;             // The duration of a pulse in microseconds when sending a logical 0
    int oneGap = 1688;               // The duration of the gap in microseconds when sending a logical 1
    int zeroGap = 562;               // The duration of the gap in microseconds when sending a logical 0
    int sendTrailingPulse = 1;       // 1 = Send a trailing pulse with duration equal to "onePulse"
                                     // 0 = Don't send a trailing pulse

    int result = irSling(
                     outPin,
                     frequency,
                     dutyCycle,
                     leadingPulseDuration,
                     leadingGapDuration,
                     onePulse,
                     zeroPulse,
                     oneGap,
                     zeroGap,
                     sendTrailingPulse,
                     binaryCommand);

    return result;
}