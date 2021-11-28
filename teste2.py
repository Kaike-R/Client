from multiprocessing.spawn import freeze_support
import tanqueDeOleo
#from typing_extensions import runtime
import requests
import json
import asyncio

import subprocess
from random import randint
from time import sleep, thread_time, time
from multiprocessing.pool import ThreadPool



async def cabulando():
        await asyncio.sleep(5)
        print("estou rodando")
def cabulando2():
    print("estou esperando")

while True:
    asyncio.run(cabulando)
    cabulando2()