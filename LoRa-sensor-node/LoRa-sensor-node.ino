#include <TH02_dev.h>
#include <ArduinoJson.h>
#include <LoRa.h>
#include <SPI.h>

#define ECHO_PIN 4
#define TRIGGER_PIN 5
#define DEVICE_ID "LORA_NODE_1"

float duration,distance,temperature,humidity;
DynamicJsonDocument data(200);


void setup() 
{
  Serial.begin(9600); 
  
  //Ultrasound config
  pinMode(ECHO_PIN,INPUT);
  pinMode(TRIGGER_PIN,OUTPUT);

  //TH02
  TH02.begin();
  delay(500);
  //LoRa
  if (!LoRa.begin(867000000)) 
  {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  LoRa.setSyncWord(0x34);
  
  //Making sure everything is hot!
  delay(500);
  Serial.println("All systems armed");
}

void loop() 
{
  //Ultrasound trigger pulse
  digitalWrite(TRIGGER_PIN, LOW); 
  delayMicroseconds(2); 
  digitalWrite(TRIGGER_PIN, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(TRIGGER_PIN, LOW);

  //Ultrasound pulse IN
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = (duration*.0343)/2;
  data["water_level"]=distance;
  
  //Temperature and humidity
  temperature = TH02.ReadTemperature();
  humidity = TH02.ReadHumidity();
  data["temperature"]=temperature;
  data["humidity"]=humidity;

  //Json data
  String final_data;
  serializeJsonPretty(data, final_data);
  Serial.println();
  
  // compose and send packet
  LoRa.beginPacket();
  LoRa.print("<");
  LoRa.print(DEVICE_ID);
  LoRa.print(">");
  LoRa.print(final_data); 
  
  // LoRa.print(counter);
  LoRa.endPacket(true);
  delay(5000);
  Serial.println("Data sent: \t");
  Serial.println(final_data);
}
