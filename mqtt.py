from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
# import logging
import time
import json

endpoint = "ENDPOINT"
rootCAPath = "<PATH>/rootCA.pem"
certificatePath = "<PATH>/certificate.pem.crt"
privateKeyPath = "<PATH>/private.pem.key"
clientId = 'irc_0'
topic = 'teste'
mode = 'both'
port = 8883
allowedActions = ['both', 'publish', 'subscribe']

if mode not in allowedActions:
    print("Unknown --mode option %s. Must be one of %s" % (mode, str(allowedActions)))
    exit(2)

if not certificatePath or not privateKeyPath:
    print("Missing credentials for authentication.")
    exit(2)

# Configure logging
# logger = logging.getLogger("AWSIoTPythonSDK.core")
# logger.setLevel(logging.DEBUG)
# streamHandler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# streamHandler.setFormatter(formatter)
# logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(endpoint, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 128, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myAWSIoTMQTTClient.connect()


def subscribe():
    myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)

def publish(self, messageToPublish):
    print(topic)
    print(messageToPublish)
    return myAWSIoTMQTTClient.publish(topic, messageToPublish, 1)

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("--------------\n\n")
    print("Received a new message: ")

    messageJson = json.loads(message.payload)
    print(json.dumps(messageJson, indent=4))

    # print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


def main():
    messageToPublish = 'Teste publish'
    subscribe()
    while True:
        time.sleep(0.1)


if __name__ == '__main__':
    
    main()
