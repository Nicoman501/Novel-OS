#include<Servo.h>
Servo steer;
int r, sp, angl;
unsigned long tn, to;
float rpm;
float count;
int old, neww;
#include <Wire.h>
float x = 0;  // initial state estimate
float P = 1;  // initial estimate covariance
float Q = 0.01;  // process noise covariance
float R = 0.1;  // measurement noise covariance

const int MPU_ADDR = 0x68;  // MPU-6050 I2C address
int16_t yaw, yaw2;
void setup() {
  Serial.begin(9600);

  pinMode(2, INPUT);
  to = millis();

  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(6, OUTPUT);////moter

  pinMode(2, INPUT);//encoder

  steer.attach(13);

  Wire.begin();  // start the I2C communication
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);  // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  delay(100);  // wait for the MPU-6050 to wake up

}

void loop() {
  while (Serial.available() > 0) {

    String datain = Serial.readString();
    r = datain.indexOf(' ');
    sp = datain.substring(0, r).toInt();
    angl = datain.substring(r, datain.length()).toInt();
  }
  movee(sp, angl);
  String data = readimu() + " " + countt();
  Serial.println(data);

}
void movee(int sp , int angl) {
  steer.write(angl + 90);
  if (sp < 0) {
    digitalWrite(5, 1);
    digitalWrite(3, 0);
  }
  else {
    digitalWrite(5, 0);
    digitalWrite(3, 1);
  }
  analogWrite(6, abs(sp+(sp-rpm)*2);
}
String readimu() { // read the raw gyro data from the MPU-6050
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x47);  // starting with register 0x47 (GYRO_ZOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_ADDR, 2, true);  // request 2 bytes of data
  int16_t gyro_z = (Wire.read() << 8 | Wire.read()) / 131.0;
  // put your main code here, to run repeatedly:
  float z = gyro_z ;// read the sensor measurement
  // Prediction step
  float xPred = x;  // predicted state estimate
  float PPred = P + Q;  // predicted estimate covariance
  // Update step
  float K = PPred / (PPred + R);  // Kalman gain
  x = xPred + K * (z - xPred); // updated state estimate
  P = (1 - K) * PPred;  // updated estimate covariance
  // e.g. convert it to degrees per second and integrate it to get the angle
  yaw = yaw + gyro_z + 0.79;
  yaw2 = yaw2 + x;
  return String(yaw2 * 0.01);
}
String countt() {
  neww = digitalRead(2);
  if (neww != old) {
    count++;
  }
  old = neww;
  tn = millis();
  if ((tn - to) > 250) {
    rpm = count * 4 * 0.05;
    rpm = rpm / 12;
    count = 0;
    to = tn;
  }
  return String(rpm);
}
