"""Getting Started Example for Python 2.7+/3.3+"""
#import boto3
#from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

import random
import time
from paho.mqtt import client as mqtt_client

#def say_to_file(say_str):
#    global polly
#    #Joanna
#    #Matthew
#    #Kendra
#    #Salli
#    #try:
#    #    # Request speech synthesis
#    #    response = polly.synthesize_speech(Text=say_str, Engine="neural",
#    #                                        OutputFormat="mp3",
#    #                                        VoiceId="Salli")
#    #except (BotoCoreError, ClientError) as error:
#    #    # The service returned an error, exit gracefully
#    #    print(error)
#    #    sys.exit(-1)
#
#    # Access the audio stream from the response
#    if "AudioStream" in response:
#        # Note: Closing the stream is important because the service throttles on the
#        # number of parallel connections. Here we are using contextlib.closing to
#        # ensure the close method of the stream object will be called automatically
#        # at the end of the with statement's scope.
#        #print("temp directory is " + gettempdir())
#        print(response)
#        with closing(response["AudioStream"]) as stream:
#            output = "speech2.mp3"
#        #    output = os.path.join(gettempdir(), "speech.mp3")
#            try:
#                # Open a file for writing the output as a binary stream
#                with open(output, "wb") as file:
#                    file.write(stream.read())
#            except IOError as error:
#                # Could not write to file, exit gracefully
#                print(error)
#                sys.exit(-1)
#
#    else:
#        # The response didn't contain audio data, exit gracefully
#        print("Could not stream audio")
#        sys.exit(-1)



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client, topic_):
    def on_message(client, userdata, msg):
        global armed
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.topic == "announce/raspi1/speak":
            test_str2 = msg.payload.decode()
            #if is_detection(test_str2) != -1 and is_complete_motion(test_str2) == -1:
            #    speech = build_speech(test_str2)
            #    print(speech)
            #    #publish_message(client, "announce/raspi1/speak", speech)
            #say_to_file(test_str2)
            str_cmd = 'mycroft-speak ' + '"' + test_str2 + '"'
            print(str_cmd)
            #os.system(str_cmd)
                                
            #if msg.payload.decode() == "ON":
            #    publish_message(client, "house/jerry/alert", "OFF")
            #    publish_message(client, "house/jerry/alertack", "OFF")
        #if msg.topic == "house/jerry/triggered":
        #    if msg.payload.decode() == "ON":
        #        if armed == 1:
        #            publish_message(client, "house/jerry/alert", "ON")
        #        publish_message(client, "house/jerry/triggered", "OFF")
        #if msg.topic == "house/jerry/arm":
        #    if msg.payload.decode() == "ON":
        #        armed = 1
        #    else:
        #        armed = 0
        #        publish_message(client, "house/jerry/alert", "OFF")
    client.subscribe(topic_)
    client.on_message = on_message


broker = 'mysmartcasa.duckdns.org'
port = 1883
topic = "wyze/mom/event3"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'trekker'
password = 'DKjkvALDThAcTG3k'
armed = 0

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
#session = Session(profile_name="default")
#polly = session.client("polly")
#polly = boto3.client("polly")


# Play the audio using the platform's default player
#if sys.platform == "win32":
#    os.startfile(output)
#else:
#    # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
#    opener = "open" if sys.platform == "darwin" else "xdg-open"
#    subprocess.call([opener, output])

#say_to_file("test")
#os.system("mpg123 " + "speech2.mp3")

client = connect_mqtt()
client.loop_start()
#publish(client)
#publish_message(client, "house/jerry/alert", "OFF")
subscribe(client, "announce/raspi1/speak")
#    subscribe(client, "house/jerry/triggered")
#    subscribe(client, "house/jerry/alertack")
while True:
    time.sleep(1)
