#include <WiFi.h>
// This code is for ESP32-CAM

// This website is useful when you wanna use ESP32
// https://qiita.com/Nabeshin/items/b195cad1afe99ce29f1e


void setup() {
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
}

void loop() {
  int n = WiFi.scanNetworks();
  if (n > 0){
    for (int i=0; i<n; i++){
      Serial.print("WiFi:");
      Serial.print(i);
      Serial.print("\t");
      Serial.print(WiFi.channel(i));
      Serial.print("\t");
      Serial.print(WiFi.RSSI(i));
      Serial.print("\t");
      Serial.print((WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? " " : "*");
      Serial.print("\t");
      Serial.print(WiFi.SSID(i));
      Serial.print("\t");
      delay(10);
    }
  }
}
