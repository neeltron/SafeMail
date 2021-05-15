#define echo 2
#define trigger 3

#include<Servo.h>

long t;
int s;
Servo s1;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  s1.attach(5);
  s1.write(90);
  Serial.begin(9600);
}
void loop() {
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  t = pulseIn(echo, HIGH);
  s = t * 0.034 / 2;
  Serial.println(s);
  if (Serial.available()) {
    int servo_signal = Serial.read();
    Serial.println(servo_signal);
    if (servo_signal == 97) {
      s1.write(0);
      delay(5000);
      s1.write(90);
    }
    else if (servo_signal == 98) {
      s1.write(90);
    }
  }
}
