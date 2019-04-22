import sqlite3
import io
import time
import serial
import os

os.system("sudo rfcomm connect 0  20:15:05:20:24:84") #This number bluetooth MAC adress(20:15....)

ser=serial.Serial('/dev/rfcomm0',38400) #Listen to data,baudrate(38400) has to be same with the arduino code

conn = sqlite3.connect('sensordata.db') #Database connection

if(conn):       #Check database connection
    print('y')

else:
    print('n')

my_list=[]      #Sensor1 data array
my_list2=[]     #Sensor2 data array

while 1:
                        #Receive data every five sec.
    timeout=time.time()+5
    my_list.clear()
    while 1:
        if time.time() > timeout:
            break
        data=ser.readline()         #Read all data on one line,
        my_all=data.split(b'\t')    #Split sensor1 and sensor2 data
        my_list.append(my_all[0])
        my_list2.append(my_all[1])

    selct=conn.cursor()  #for database

    for i,j in zip(my_list, my_list2):
        print(i,j)
        selct.execute('''INSERT INTO sensor1 (temperature,temp3x) VALUES (?,?)''',(i,j,)) #Write in database different column
    conn.commit()                       # -sensor1 table name in database,temperature column1 name and temp3x column2 name

conn.close()
sock.close()
