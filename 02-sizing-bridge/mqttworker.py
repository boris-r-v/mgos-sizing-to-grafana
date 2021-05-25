#!/usr/bin/env python3

"""A MQTT to InfluxDB Bridge

This script receives MQTT data and saves those to InfluxDB.

"""

import json
import re
import sys
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

INFLUXDB_ADDRESS = 'localhost'
INFLUXDB_USER = 'admin'
INFLUXDB_PASSWORD = 'admin'
INFLUXDB_DATABASE = 'std'

MQTT_ADDRESS = "localhost"
MQTT_USER = 'mqttuser'
MQTT_PASSWORD = 'mqttpassword'
MQTT_TOPIC = 'devices/+/+'  # [device_id/[data|diag]
MQTT_REGEX = 'devices/([^/]+)/([^/]+)'
MQTT_CLIENT_ID = 'MQTTInfluxDBBridge'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
#   print("message received ", str(msg.payload.decode("utf-8")))
#   print("message topic=", msg.topic)
#   print("message qos=", msg.qos)
#   print("message retain flag=", msg.retain)
#   return

    device_id, data_type = re.findall(MQTT_REGEX, msg.topic)[0]
    data = json.loads( ( msg.payload.decode('utf-8') ) )

    if ( "diag" == data_type ):
        _send_diag_data_to_influxdb( device_id, data )

    if ( "data" == data_type ):
        _send_sizing_data_to_influxdb( device_id, data )

def _send_diag_data_to_influxdb( device_id, data ):
    json_body =[
        {
            'measurement': "diag",
            'tags': {
                'device_id': device_id
            },
            'fields': {
                'temp': data['temp'],
                'hall': data['hall'],
                'ram_usage': round( (1-data["free_ram"]/data["total_ram"]), 3 )
            }
        }
    ]

    try:
        influxdb_client.write_points(json_body)
    except:
        print ( sys.exc_info() )  
    
def _send_sizing_data_to_influxdb( device_id, data ):
    json_body =[
        {
            'measurement': "sizing",
            'tags': {
                'device_id': device_id
            },
            'fields': {
                'VDC1': float(data['VDC1']),
                'VAC1': float(data['VAC1']),
                'F1cur': data["F1cur"],
                'VDC2': float(data['VDC2']),
                'VAC2': float(data['VAC2']),
                'F2cur': data["F2cur"]
            }
        }
    ]
    try:
        influxdb_client.write_points(json_body)
    except:
        print ( sys.exc_info() )  

def _init_influxdb_database():
    databases = influxdb_client.get_list_database()
    print (databases)
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)


def runner():
    _init_influxdb_database()

    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    #mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS)

    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    runner()
