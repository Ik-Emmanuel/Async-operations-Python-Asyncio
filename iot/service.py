import asyncio
import random 
import string
from typing import Protocol

from iot.message import Message, MessageType

def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class Device(Protocol):
    ## protocol class is used to defined what methods it expects when a device is registered
    # It expects that all Devices to be registered should have asynchronous methods  
    async def connect(self) -> None:
        ...
    
    async def disconnect(self) -> None:
        ...

    async def send_message(self, message_type: MessageType, data:str) -> None:
        ...

class IOTService:
    def __init__(self):
        #a list of paired devices 
        self.devices: dict[str, Device] = {}

    async def register_device(self, device: Device) -> str:
        await device.connect()
        device_id = generate_id()
        #adds to list of devices
        self.devices[device_id] = device
        return device_id

    async def unregister_device(self, device_id: str) -> None:
        await  self.devices[device_id].disconnect()
        del self.devices[device_id]

    
    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    async def run_program(self, program: list[Message]) -> None:
        print("==== RUNNING IOT PROGRAMS ===")
        #this is still going to run each received command in sequence hence defeating the purpose of async 
        # for msg in program:
        #     await self.send_msg(msg)

        #a better approach using async
        # async.gather expects arguments so you need to unpack the list elements
        await asyncio.gather(*[self.send_msg(msg) for msg in program ])
        print("==== END of PROGRAM ===")

    
    async def send_msg(self, msg: Message) -> None:
        await self.devices[msg.device_id].send_message(msg.msg_type, msg.data)
