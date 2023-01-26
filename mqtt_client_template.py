import paho.mqtt.client as mqtt

# Connection settings
broker_ip = "192.168.0.123"
port = 1883
keepalive = 60
qos = 0

# Callbacks functions
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata,rc=0):
    client.loop_stop()

def on_message(mqtt_client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqtt_client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mqtt_client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqtt_client, obj, level, string):
    print(string)

# Setting calbacks
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_log = on_log
mqtt_client.on_disconnect = on_disconnect

# Establishing a connection 
mqtt_client.connect(host=broker_ip, port=port, keepalive=keepalive)
mqtt_client.subscribe(topic="$test_topic/#", qos=qos)

# Main loop
mqtt_client.loop_forever()