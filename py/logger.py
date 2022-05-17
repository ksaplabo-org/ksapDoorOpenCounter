from this import d
import paho.mqtt.client
import json
import ssl
import datetime
import time

#openした時のログを保存するクラス
class Logger():

    global mqtt

    def __init__(self):
        self.mqtt = Mqtt()
        self.mqtt.connect()

#    def __del__(self):
        #del self.mqtt

    #ログの登録
    def write(self):
        #メッセージを作成
        tmstr = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        json_msg = json.dumps({"GetDateTime": tmstr})
        #MQTT送信
        self.mqtt.publish(json_msg)

#MQTT通信により、日時をDynamoDBに登録するクラス
class Mqtt():

    global client
    global is_connected

    #変数宣言
    AWSIOT_ENDPOINT = 'alij9rhkrwgll-ats.iot.ap-northeast-1.amazonaws.com'
    MQTT_PORT = 8883
    MQTT_TOPIC_PUB = "ksap-dooropencounter"
    MQTT_TOPIC_SUB = "ksap-dooropencounterSub"
    MQTT_ROOTCA = "/home/pi/Downloads/AmazonRootCA1.pem"
    MQTT_CERT = "/home/pi/Downloads/d809f41470b4a2d96ef70d807bbaabae3a27b7df436c049c34366bb90985d4fe-certificate.pem.crt"
    MQTT_PRIKEY = "/home/pi/Downloads/d809f41470b4a2d96ef70d807bbaabae3a27b7df436c049c34366bb90985d4fe-private.pem.key"

    def __init__(self):

        self.is_connected = False

        # Mqtt Client Initialize
        self.client = paho.mqtt.client.Client()
        self.client.on_connect = self.__on_connect
        self.client.on_disconnect = self.__on_disconnect
        self.client.tls_set(self.MQTT_ROOTCA, certfile=self.MQTT_CERT, keyfile=self.MQTT_PRIKEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        print("init!!")

    def __del__(self):
        self.client.disconnect()

    #初期接続
    def connect(self):
        # Connect To Mqtt Broker(aws)
        self.client.loop_start()

        try:
            self.client.connect(self.AWSIOT_ENDPOINT, port=self.MQTT_PORT, keepalive=5)
            self.is_connected = True
            print("connect!!")
        except:
            print("Wi-Fi接続が切れています")
            self.is_connected = False

    #MQTT接続イベント
    def __on_connect(self, client, userdata, flags, rc):
        self.is_connected = True

    #MQTT切断イベント
    def __on_disconnect(self, client, userdata, msg):
        print("MQTT切断")
        self.is_connected = False

    #パブリッシュ（データ送信）
    def publish(self, json_msg):
        try:
            #接続
            if self.is_connected == False:
                self.connect()
            #MQTT送信
            if self.is_connected:
           
               print("publish!!")
               self.client.publish(self.MQTT_TOPIC_PUB ,json_msg)
        except:
            print('publish 失敗')
