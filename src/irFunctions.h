
#ifndef IRRECEIVER_H_INCLUDED
#define IRRECEIVER_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

char *ir_receiver(void);

int ir_transmitter(const char *binaryCommand);

#ifdef __cplusplus
}
#endif

#endif // IRRECEIVER_H_INCLUDED
