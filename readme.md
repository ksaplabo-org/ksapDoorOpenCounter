# DoorOpenCounter  

## 目次  
- [概要説明](#content1)  
- [リードスイッチの使い方](#content2)  
- [配線接続](#content3)
- [ESP32のセッティング](#content4)  
- [Raspberry Piのセッティング](#content5)  

<h2 id="content1">概要説明</h2>  

<図を挿入>  aa

支店のプロジェクトルームのドアが開いた回数を記録する  

支店のプロジェクトルームのドアが開く  
↓  
リードスイッチが反応しESP32が起動  
↓  
ESP32からRaspberry Piへ通知  
↓  
Raspberry PiからDynamoDBへ現在時刻をMQTT送信   

<h2 id="content2">リードスイッチの使い方</h2>  

リードスイッチとは...  
```  

``` 

- リードスイッチを利用して、LEDライトを点灯させる  

