#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

// BLE characteristic
#define SERVICE_UUID           "28b0883b-7ec3-4b46-8f64-8559ae036e4e"
#define CHARACTERISTIC_UUID_TX "2049779d-88a9-403a-9c59-c7df79e1dd7c"

// BLE Device name
#define DEVICENAME "ESP32"

// serial speed
#define SPI_SPEED 115200

// characteristic valueable
BLECharacteristic *pCharacteristicTX;
bool deviceConnected = false;

// send data
int send_cnt = 0;

// GPIO No
int LED = 4;

// Server Callbacks of Connection
class funcServerCallbacks: public BLEServerCallbacks{
    void onConnect(BLEServer* pServer){
        deviceConnected = true;
    }
    void onDisconnect(BLEServer* pServer){
        deviceConnected = false;
    }
};

// Characteristic
void doPrepare(BLEService *pService){
    // Create Characteristic of Notify
    pCharacteristicTX = pService->createCharacteristic(
                      CHARACTERISTIC_UUID_TX,
                      BLECharacteristic::PROPERTY_NOTIFY
                    );
    pCharacteristicTX->addDescriptor(new BLE2902());
}

void doInitialize() {
  Serial.begin(SPI_SPEED);
}

void setup() {
  // Initialize the pinMode
  doInitialize();

  //LED点灯
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);

  // Initialize the BLE environment
  BLEDevice::init(DEVICENAME);
  
  // Create the server
  BLEServer *pServer = BLEDevice::createServer();

  // Callback the server
  pServer->setCallbacks(new funcServerCallbacks);
  
  // Create the service
  BLEService *pService = pServer->createService(SERVICE_UUID);

  // Create the characteristic
  doPrepare(pService);
  
  // Start the service
  pService->start();
  
  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->start();

  // Wait Connect
  Serial.println("Waiting to connect...");
  while(!deviceConnected){delay(100);}

  // Connection  
  Serial.println("Connection!");

  delay(3000);

  Serial.println("deep_sleep start");
  //deep_sleep_start
  esp_deep_sleep_start();
}

void loop() {
  //pCharacteristicTX->setValue("open");
  //pCharacteristicTX->notify();
  
  //delay(1000);
}
