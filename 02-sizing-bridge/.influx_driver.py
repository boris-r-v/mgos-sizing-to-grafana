#!/usr/bin/env python

#import sys
from influxdb import InfluxDBClient

def main ():
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'std')
#    client.switch_database('std')
    result = client.query('delete from sizing')
    print("Result: {0}".format(result))

    for i in result:
        print (i)



if __name__ == '__main__':
    main()


