#include <math.h>

float r= 0, coeff = 29.988, power = -1.173;

void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  float v = analogRead(A0);
  r = coeff*(pow(v, power));
  Serial.println(r);
}


