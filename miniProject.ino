
#include <Stepper.h>
int pin1 = 8, pin2 = 9, pin3 = 10, pin4 = 11;
//int r = 0;

Stepper myStepper(721, pin1, pin3, pin2, pin4);
//SharpIR sharp(A0, "1080");

void setup() {
  //pinMode(A0, INPUT);
  Serial.begin(9600);
  myStepper.setSpeed(30);
}

void loop() { 
  if(Serial.available()) {
    int steps = Serial.parseInt();
    myStepper.step(steps);
  }
}
