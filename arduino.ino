#define ledPin 13
#include <SoftwareSerial.h>
SoftwareSerial BTSerial(10, 11); // CONNECT BT RX PIN TO ARDUINO 11 PIN | CONNECT BT TX PIN TO ARDUINO 10 PIN
int state = 1;
//int state1 = 2;
 float sicaklikC;        //sıcaklık değişkeni tanımlandı
 int lm35Pin = 0;    // LM35 sensörünün ortasındaki sinyal ucu Analog 0 bağlandı.
 int val=123;
void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  analogReference(INTERNAL1V1);
  
  Serial.begin(38400);
  BTSerial.begin(38400);  // HC-05 default speed in AT command more
}
void loop() {
  
      float sicaklikVolt = analogRead(lm35Pin);       
      sicaklikC = sicaklikVolt / 9.31; 
      
  //if(BTSerial.available()){ // Checks whether data is comming from the serial port
    //state = BTSerial.read(); // Reads the data from the serial port
//    state1=Serial.read();

     BTSerial.print(sicaklikC);   //sensor1 data
     BTSerial.print('\t');
     BTSerial.print(sicaklikC*3); //sensor2 data 
     BTSerial.print('\n');
     Serial.print(sicaklikC);     //check sensor1 data on serialport screen 
     Serial.print('\t');
     Serial.print(sicaklikC*3);   //check sensor2 data on serialport screen
     Serial.print('\n');
     delay(2000);
// }
//if (state == '0') {
  
//  digitalWrite(ledPin, LOW); // Turn LED OFF
//  Serial.println("LED: OFF"); // Send back, to the phone, the String "LED: ON"
//  state = 0;
// }
// else if (state == '1') {
  
 // digitalWrite(ledPin, HIGH);
 // Serial.println("LED: ON");;
 // state = 0;
 //} 
}
