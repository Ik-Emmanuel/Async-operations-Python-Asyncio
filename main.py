from re import L
from typing import Any, Awaitable
from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService

import asyncio
 
#helper functions 
async def run_sequence(*functions: Awaitable[Any]) -> None:
    """ This helper functions helps you run some functions in sequential order, since the functions are dependent on each other
    """
    for function in functions:
        await function

async def run_parallel(*functions: Awaitable[Any]) -> None:
    """ This helper functions helps you run some functions in parallel since order is irrelevant and they are independent
    """
    await asyncio.gather(*functions)


async def main() -> None:
    #create an IOT service
    service  = IOTService()

    #create and register devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()
    #old synchronous method 
    # hue_light_id = await service.register_device(hue_light)
    # speaker_id = await service.register_device(speaker)
    # toilet_id=  await  service.register_device(toilet)

    # Asynchronous method using asyncio.gather
    hue_light_id, speaker_id, toilet_id = await asyncio.gather(
    service.register_device(hue_light),
    service.register_device(speaker),
    service.register_device(toilet),
    )


    #some programs to be ran 
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Ed sheeran -  Thinking out loud"),
    ]

   
    # sleep_program = [
    #     Message(hue_light_id, MessageType.SWITCH_OFF),
    #     Message(speaker_id, MessageType.SWITCH_OFF),
    #     Message(toilet_id, MessageType.FLUSH),
    #     Message(toilet_id, MessageType.CLEAN),]

    #run the programs asynchronousely by passing a list of functions 
    # 1f the functions are purely independent on one another
    # and running -->  await asyncio.gather(*[self.send_msg(msg) for msg in program ])
    await service.run_program(wake_up_program)

    # taking function dependency into consideration and using helper functions to split them in parallel and sequential bits 
    await run_parallel(
        # 3 programs to be ran in parallel 2 are independent and last 2 are dependent
        service.send_msg(Message(hue_light_id, MessageType.SWITCH_OFF)),
        service.send_msg(Message(speaker_id, MessageType.SWITCH_OFF)),
        # this then runs the program within, in sequence
        run_sequence(
            service.send_msg(Message(toilet_id, MessageType.FLUSH)),
            service.send_msg(Message(toilet_id, MessageType.CLEAN)),
        ),
        run_sequence(
            service.send_msg(Message(speaker_id, MessageType.SWITCH_ON)),
            service.send_msg(Message(speaker_id, MessageType.PLAY_SONG, "Bruno Mars - Uptown Func❤")),
        )
    )


if __name__ == "__main__":
    asyncio.run(main())