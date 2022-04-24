# Async-operations-Python-Asyncio (Implementing asynchronous programming with Python). 
Working with python asyncio module that allows you to run program in "seemingly" parallel fashion. 

## Code description

This is a simulation of IOT device connections with an asynchronous python program. Where several IOT devices are created, registered, and commands sent to them to carry out actions. 

With asyncio we see that for independent functions or program blocks, we don't need to have code idle time when the program could be doing other things, preventing what is known as "Code blocking". Where needed we can also introduce some level of sequence for functions that dependent on each other. 

Using asyncio and python methods such as 
- asyncio.gather()
- asyncio.run()
- python list comprehension and functional programming

 We define awaitable functions and truly take advantage of parallel programming.

