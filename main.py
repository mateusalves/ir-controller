from irController import mapingController, ir_transmitter
from time import sleep
import json


def parseCommandFromAWS(msg):
    try:
        with open('mappedButtons.json', 'r') as r:
            mappedButtonsJson = json.loads(r.read())
            r.close()
    except:
        print('Could not open mappedButtons File.')
        mapController = input('Do you want to map a remote controller right now? [Y/N] ')
        if mapController.upper() == 'Y':
            mapingController()
            with open('mappedButtons.json', 'r') as r:
                mappedButtonsJson = json.loads(r.read())
        else:
            return

    for word in msg:
        if word in mappedButtonsJson.keys():
            print(f'\n\nsending signal - {word}\n\n')
            sleep(3)
            ir_transmitter(mappedButtonsJson[word])


if __name__ == '__main__':
    
    msg = 'tell BR to power the TV and then put on netflix'
    parseCommandFromAWS(msg.split(' '))
