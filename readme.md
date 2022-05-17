# DoorOpenCounter  

## 目次  
- [概要説明](#content1)  
- [リードスイッチの使い方](#content2)  
- [配線接続](#content3)
- [ESP32のセッティング](#content4)  
- [Raspberry Piのセッティング](#content5)  

<h2 id="content1">概要説明</h2>  

![全景](./img/概要図.png)  

支店のプロジェクトルームのドアが開いた回数を記録する  

支店のプロジェクトルームのドアが開く  
↓  
リードスイッチが反応しESP32が起動  
↓  
ESP32からRaspberry PiへBluetooth接続  
↓  
Raspberry PiからDynamoDBへ現在時刻をMQTT送信   

<h2 id="content2">リードスイッチの使い方</h2>  

リードスイッチとは...  
```  
密閉されたガラス管内に2つの強磁性ブレードを含む電気機械式スイッチングデバイス  
```  

リードスイッチについて→参考サイト：https://standexelectronics.com/ja/reed-switch-technology-ja/what-is-a-reed-switch-and-how-does-it-work/  

- リードスイッチを利用して、LEDライトを点灯させる  
回路作成  

![A](./img/リードスイッチサンプル.png)  
<img alt="リードサンプル" src="./img/リードサンプル.jpg" width="700" height="400">   





