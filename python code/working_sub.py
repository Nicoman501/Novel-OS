import serial
import time
import math
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    time.sleep(3)
    ser.reset_input_buffer()
    actual= [1,2]
    tau=0.5
    dax=0
    v=0.5
    l=0
    day=0
    angout=0
    spa=0
    ora=0
try:
    while True:
        ser.reset_input_buffer()
        while ser.in_waiting<=0:
           time.sleep(0.01);
        datain = ser.readline().decode('utf-8').rstrip()
        #print(datain)
        actual=datain.split(" ")
        print(len(actual))
        #print(actual)
        spa=float(actual[len(actual)-1])/255
        ora=float(actual[len(actual)-2])/180*math.PI

        dax=dax+spa*math.cos(ora)*tau
        day=day+spa*math.sin(ora)*tau
        if(dax>0.2):
            v=0.5
            l=-0.5
        if(dax>1):
            v=1
            l=0.5
        if(dax>1.3):
            v=0
            l=0
        u=2*(v-spa)
        if(u>2):
            u=0
        spout=spa+tau*u
        if(abs(day)<abs(l)*5):
            angout=l/abs(l)*(l-day/l)
            if (abs(angout)>0.5):
                angout=l/abs(l)
            if abs(angout)<0.1:
                angout=0
        print(day)
        print(dax)
        time.sleep(0.6)
        dataout=str(spout*255)+" "+str(angout*180/math.PI)
        print(dataout)
        ser.write(dataout.encode('utf-8'))      
except KeyboardInterrupt:
    ser.close()
    print("done")