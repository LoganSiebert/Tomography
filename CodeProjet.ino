int dirPin2 = 8;
int stepperPin2 = 7;
int dirPin = 10;
int stepperPin = 9;
int microStep2 = 4;
int microStep = 11;
int pinLED=1;


void setup() {
  pinMode(dirPin,OUTPUT);
  pinMode(stepperPin,OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepperPin2, OUTPUT);
  pinMode(microStep2, OUTPUT);
  pinMode(microStep, OUTPUT);
  pinMode(pinLED,OUTPUT);
  digitalWrite(microStep2, HIGH);
  digitalWrite(microStep, HIGH);

  Serial.begin(9600);
  pinMode(A5,INPUT);

}
void step(boolean dir, int steps, int stepNumber, int dirNumber ) {
  digitalWrite(dirNumber, dir);
  delay(150);
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepNumber, HIGH);
    delayMicroseconds(2000);
    digitalWrite(stepNumber, LOW);
    delayMicroseconds(2000);
  }
}

void loop() {
  Serial.println(analogRead(A5));
  for(int j = 1; j<37; j+=2){
     for (int i=0; i<1600; i+=16){
        step(true,16,stepperPin, dirPin);
        digitalWrite(pinLED, HIGH);
        delay(10);
        Serial.println(analogRead(A5));  
        digitalWrite(pinLED, LOW);
      }
      
      step(true, 177, stepperPin2, dirPin2);
      
      for (int i=0; i<1600; i+=16){
         step(false,16,stepperPin, dirPin);
         digitalWrite(pinLED, HIGH);
         delay(10);
         Serial.println(analogRead(A5));  
         digitalWrite(pinLED, LOW);
      }
      
      step(true, 177, stepperPin2, dirPin2);
  }
   Serial.println(-10);
}

