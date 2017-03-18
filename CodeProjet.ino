//DIR & STEP
int dirPin2 = 8;
int stepperPin2 = 7;
int dirPin = 10;
int stepperPin = 9;
//Microstepping
int microStep2 = 4; 
int microStep = 11;
//LED infrarouge
int pinLED=2;


void setup() {
  
  pinMode(dirPin,OUTPUT);
  pinMode(stepperPin,OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepperPin2, OUTPUT);
  pinMode(microStep2, OUTPUT);
  pinMode(microStep, OUTPUT);
  pinMode(pinLED,OUTPUT);
  
  //Microstepping 32eme de pas
  digitalWrite(microStep2, HIGH);
  digitalWrite(microStep, HIGH);
  
  //Communication phototransistor
  Serial.begin(9600);
  pinMode(A5,INPUT);

}

//Méthode step(direction, nb pas, nb du pin step, nb du pin dir)
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
  //Nombre d'angles = 40
  for(int j = 0; j<41; j+=2){
     //translation et réception données tous les 16 pas ==> 100 mesures
     for (int i=0; i<1600; i+=16){
        step(true,16,stepperPin, dirPin);
        digitalWrite(pinLED, HIGH);
        delay(10);
        Serial.println(analogRead(A5));  
        digitalWrite(pinLED, LOW);
      }
      
      //Rotation moteur 2 de 160 pas (360 degrés = 6400 pas avec microstepping)
      step(true, 160, stepperPin2, dirPin2);
      
      for (int i=0; i<1600; i+=16){
         step(false,16,stepperPin, dirPin); //sens inverse
         digitalWrite(pinLED, HIGH);
         delay(10);
         Serial.println(analogRead(A5));  
         digitalWrite(pinLED, LOW);
      }
      
      step(true, 160, stepperPin2, dirPin2);
  }
   Serial.println(-10); //Arrêt de réception
}

