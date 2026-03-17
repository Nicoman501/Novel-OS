#include<Servo.h>
Servo steer;
int r, sp, angl;
void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  steer.attach(3);
}

void loop() {
  while (Serial.available() > 0) {

    String datain = Serial.readString();
    r = datain.indexOf(' ');
    sp = datain.substring(0, r).toInt();
    angl = datain.substring(r, datain.length()).toInt();
  }
  //movee(spr,angl);
  steer.write(angl + 90);
  if (sp > 0) {
    digitalWrite(6, 1);
    digitalWrite(7, 0);
  }
  else {
    digitalWrite(6, 0);
    digitalWrite(7, 1);
  }
  analogWrite(5, abs(sp));
  Serial.println(String(angl + 90) + " " + String (sp));
}
void movee(int spr , int angl) {}
