import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    time.sleep(3)
    ser.reset_input_buffer()
try:
    while True:
        while ser.in_waiting<=0:
           time.sleep(0.01);
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
except KeyboardInterrupt:
    ser.close()
    print("done")
