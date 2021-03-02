#!/usr/bin/python
import ctypes
import os
import json
# import requests

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

def mapingController():
    userInput = ''

    try:
        with open('mappedButtons.json', 'r') as r:
            mappedButtonsJson = json.loads(r.read())
            r.close()
    except:
        mappedButtonsJson = json.loads("{}")

    while (userInput.lower() != 'done'):

        userInput = input("\nEnter the button name or type 'done' to exit: ")
        
        if userInput.lower() == 'done':
            break
        
        print("\nNow, point the controller to the receiver and press the button: ")
        command = ir_receiver()

        mappedButtonsJson[userInput.lower()] = command

        os.system('clear')

        with open('mappedButtons.json', 'w') as f:
            f.write(json.dumps(mappedButtonsJson, indent=4))
            f.close()
        
        print(json.dumps(mappedButtonsJson, indent=4))
        print(f'{userInput} - successfully stored')
        


if __name__ == '__main__':
    # print(os.getenv("USER"))
    # print(os.getenv("SUDO_USER"))
    mapingController()
    
    # with open('mappedButtons.json', 'r') as r:
    #    controllerMap = json.loads(r.read())
    #    r.close()
    # print('power', controllerMap['power'])
    # ir_transmitter(controllerMap['power'])
    # ir_transmitter(controllerMap['netflix'])
    # command = ir_receiver()
    # ir_transmitter(command)