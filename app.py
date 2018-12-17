#!/usr/bin/python
# coding: utf-8
from flask import Flask
import Adafruit_DHT as DHT
import notifer
import sys


## センサーの種類
SENSOR_TYPE = DHT.DHT22

## 接続したGPIOポート
DHT_GPIO = 26

app = Flask(__name__)



@app.route('/')
def get_kion():
    h, t = DHT.read_retry(SENSOR_TYPE, DHT_GPIO)
    notifer.output(f'現在の部屋の気温は{t:.3g} 度です。')
    notifer.output(f'湿度は{h:.3g} %です。')
    return 'SUCCESS!!!'


if __name__ == '__main__':
    app.run()
