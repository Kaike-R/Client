#from multiprocessing.spawn import freeze_support
#import tanqueDeOleo
#from typing_extensions import runtime
import requests
#import json
#import asyncio

#import subprocess
from random import randint
from time import sleep, thread_time, time
#from multiprocessing.pool import ThreadPool



def tanqueOleo():
        sleep(10)
        p = requests.get('http://localhost:5000/TanqueDeOleo/SeeOleo',verify=False)
        p.json()
        print(p)

tanqueOleo()