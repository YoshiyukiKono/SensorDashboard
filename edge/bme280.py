#coding: utf-8
 
import bme280_custom
import datetime
import os
 
dir_path = '/home/pi/bme280-data'
 
now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d')
label = now.strftime('%H:%M:%S')
csv = bme280_custom.readData()
 
if not os.path.exists('/home/pi/bme280-data'):
    os.makedirs('/home/pi/bme280-data')
f = open('/home/pi/bme280-data/'+filename+'.csv','a')
f.write('1,'+filename +","+label+","+csv+"\n")
f.close()
