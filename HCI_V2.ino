#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3); // RX, TX

const int trigPin = 9;    // Ultrasonic sensor trigger pin
const int echoPin = 10;   // Ultrasonic sensor echo pin

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  // Measure the distance using the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;
  Serial.println(distance);
  delay(500);  // Wait 0.5 seconds before taking another measurement
}
