import json
import requests


def publish2Iot(event, context):

    certificatePath = "keys/certificate.pem.crt"
    privateKeyPath = "keys/private.pem.key"
    mqtt_url = "ENDPOINT"
    mqtt_publish_msg = event['body']
    publish = requests.request(
        'POST',
        mqtt_url,
        data=mqtt_publish_msg,
        cert=[certificatePath, privateKeyPath]
    )

    print("Response status: ", str(publish.status_code))

    return {"statusCode": 200, "body": json.dumps(mqtt_publish_msg)}
