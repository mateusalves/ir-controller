#!/usr/bin/python
import ctypes
import os
import requests

dirName = os.path.dirname(os.path.abspath(__file__))
teste = ctypes.CDLL(os.path.join(dirName, 'bin/ir_functions.so'))


def main(args):
    arg = ctypes.c_char_p(args.encode('ascii'))
    result = teste.main(arg)
    print(result)
    return result

def ir_transmitter(binaryCommand):
    command = ctypes.c_char_p(binaryCommand.encode('ascii'))
    result = teste.ir_transmitter(command)
    print(result)
    return result

def ir_receiver():
    teste.ir_receiver.restype = ctypes.c_char_p
    tempResult = teste.ir_receiver()
    if (tempResult is None):
        return tempResult
    else:
        result = tempResult.decode('ascii')
        print(result)
        return result

if __name__ == '__main__':
    print(os.getenv("USER"))
    print(os.getenv("SUDO_USER"))
    command = ir_receiver()
    ir_transmitter(command)
