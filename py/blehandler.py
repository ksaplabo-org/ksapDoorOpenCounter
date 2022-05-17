#!/usr/bin/env python3

import sys
import asyncio
import requests
import warnings
import logger
import time
from datetime import datetime
from bleak import BleakClient

ESP32_CHARACTERISTIC_UUID = "2049779d-88a9-403a-9c59-c7df79e1dd7c"

class BleHandler():
    """ble handler.
    """
    SLEEP_TIME = 0.1
    TIME_OUT = 20
    global logger

    def __init__(self, address:str) -> None:
        self.address:str = address
        self.logger = logger.Logger()

    async def __call__(self) -> None:
        """when call, connect to target address device.
        """
        print(f'connect to device({self.address}) start.')
        await self.connect_to_device()

    def _esp32_notification_handler(self, sender, data:bytearray):
        """Esp32 notification handler."""
        print(f'Esp32 notification handler: {data.decode()}')

    def _disconnect_callback(self, client: BleakClient):
        """disconnect callback. only logging message."""
        print(f'Client with address {client.address} got disconnected. try to reconnect.')

    async def connect_to_device(self):
        while True:
            print("Waiting connect to device.")
            try:
                print(1)
                time.sleep(5)
                async with BleakClient(self.address, timeout=self.TIME_OUT, disconnected_callback=self._disconnect_callback) as client:
                    print(2)
                    if await client.is_connected():
                        print("Connect to device successfuly.")
                        self.logger.write()

                        while True:
                            if not await client.is_connected():
                                print("Device disconnected1.")
                                break
                            await asyncio.sleep(self.SLEEP_TIME)
                            #print("wait for message arraived from device.")
                    else:
                        print("Device disconnected2.")
            except Exception as e:
                print(f"Exception when connect: {e}")
            await asyncio.sleep(self.SLEEP_TIME)
