import sqlite3
import bluetooth
import time
import serial
import os

os.system("sudo rfcomm connect 0  20:15:05:20:24:84") #This number bluetooth MAC adress(20:15....)

ser=serial.Serial('/dev/rfcomm0',38400) #Listen to data,baudrate(38400) has to be same with the arduino code

conn = sqlite3.connect('sensordata.db') #Database connection

if(conn):            #Check database connection
    print('y')

else:
    print('n')

my_list=[]      #Sensor data array

while 1:

    timeout=time.time()+5            #Receive data every five sec.
    my_list.clear()
    while 1:
        if time.time() > timeout:
            break
        data=ser.readline()      #Read all data on one line
        my_list.append(data)
    selct=conn.cursor()          #for database
    for i in my_list:
        print(i)
    for i in my_list:
        selct.execute('''INSERT INTO sensor1 VALUES (?)''',(i,))     #Write in database -sensor1 table name in database-
    conn.commit()

conn.close()
sock.close()
