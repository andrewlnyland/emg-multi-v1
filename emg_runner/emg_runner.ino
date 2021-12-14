#include "MsTimer2.h"

#define HUMANREADABLE

#define BAUD 115200
#define SIZE 3
#define BUFFER 100 //Do 128 if there is space

#define SEPARATOR ','
#define ACTUATOR 3

int pins[] = {A0, A1, A2};

unsigned short head = 0;
unsigned short tail = 0;
volatile unsigned int epoch = 0;
//bool printing = false;
bool sampling = false;
bool printing = false;  //TODO: might not be needed

typedef struct {
  unsigned int timestamp;
  unsigned short values[SIZE];
} Sample;

Sample buffer[BUFFER];

void flash() {
  if (sampling) {
    buffer[head].timestamp = epoch;
    for (int i=0; i<SIZE; i++) {
      buffer[head].values[i] = analogRead(pins[i]);
    }
    epoch++;
    head++;
    if (head >= BUFFER) {  // to avoid %
      head -= BUFFER;
    }
  }
}

void setup() {
  pinMode(ACTUATOR, OUTPUT);
  for (int i=0; i<SIZE; i++) {
    pinMode(pins[i], INPUT);
  }
  MsTimer2::set(1, flash);
  Serial.begin(BAUD); // Need 80k for 3 sensors
  // Check for gps fix
  Serial.println('G');
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    if (input[0] == 'R') {
      for (int i=0; i<2; i++) {
        digitalWrite(ACTUATOR, HIGH);
        delay(250);
        digitalWrite(ACTUATOR, LOW);
      }
      sampling = true;
      printing = true;
      MsTimer2::start();
    }
    if (input[0] == 'T') {
      sampling = false;
      MsTimer2::stop();
//      Serial.println(epoch); // TODO: remove \/\/\/
//      Serial.println(buffer[head].timestamp);
//      Serial.println(buffer[tail].timestamp);
//      Serial.println(head);
//      Serial.println(tail);
      for (int i=0; i<3; i++) {
        digitalWrite(ACTUATOR, HIGH);
        delay(250);
        digitalWrite(ACTUATOR, LOW);
      }
      epoch = 0;
    }
  }
  for (int i=tail, k=i; i<(head < tail ? BUFFER+head : head) && sampling /*&& printing*/; i++/*, k++*/) {
    if (i > BUFFER-1) {
      k = i - BUFFER;
    } else {
      k = i;
    }
    Sample tmp = buffer[k];
#ifdef HUMANREADABLE
    Serial.print(tmp.timestamp);
    Serial.print(SEPARATOR);
    for (int j=0; j<SIZE; j++) {
      Serial.print(tmp.values[j]);
      if (j < SIZE-1) Serial.print(SEPARATOR);
    }
    Serial.println();
#else
    Serial.print(tmp.timestamp);
    for (int j=0; j<SIZE; j++) {
      Serial.print(tmp.values[j]);
    }
#endif
    tail = i; //TODO: is this right?
  }
  if (tail > BUFFER-1) {
    tail -= BUFFER;
  }
  if (printing && !sampling) {
    //printing = false;
  }
  //if (!sampling  // TODO: see if data loss is at the end
}
