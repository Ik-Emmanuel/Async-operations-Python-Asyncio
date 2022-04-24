from iot.message import MessageType
import asyncio

class HueLightDevice:
    async def connect(self) -> None:
        #run connect logic
        print("Connecting Hue Light..")
        await asyncio.sleep(2)
        print("Hue Light connected")

        
    async def disconnect(self) -> None:
        #run disconnect logic
        print("Disconnecting Hue Light..")
        await asyncio.sleep(2)
        print("Hue Light disconnected")

        
    async def send_message(self, message_type: MessageType, data: str= "") -> None:
        print(
            f"Hue Light handling message of type {message_type.name} with data  [{data}]."
        )
        await asyncio.sleep(2)
        print("Hue light received message.")


class SmartSpeakerDevice:
    async def connect(self) -> None:
        #run connect logic
        print("Connecting Smart Speaker..")
        await asyncio.sleep(2)
        print("Smart Speaker connected")

        
    async def disconnect(self) -> None:
        #run disconnect logic
        print("Disconnecting Smart Speaker..")
        await asyncio.sleep(2)
        print("Smart Speaker disconnected")

        
    async def send_message(self, message_type: MessageType, data: str= "") -> None:
        print(
            f"Smart Speaker handling message of type {message_type.name} with data  [{data}]."
        )
        await asyncio.sleep(2)
        print("Smart Speaker received message.")


class SmartToiletDevice:
    async def connect(self) -> None:
        #run connect logic
        print("Connecting Smart Toilet..")
        await asyncio.sleep(2)
        print("Smart Toilet connected")

        
    async def disconnect(self) -> None:
        #run disconnect logic
        print("Disconnecting Smart Toilet..")
        await asyncio.sleep(2)
        print("Smart Toilet disconnected")

        
    async def send_message(self, message_type: MessageType, data: str= "") -> None:
        print(
            f"Smart Toilet handling message of type {message_type.name} with data  [{data}]."
        )
        await asyncio.sleep(2)
        print("Smart Toilet received message.")