#from typing_extensions import runtime
#from math import tan
import requests
#import json
#import asyncio
#import concurrent.futures


#from random import randint
from time import sleep, thread_time, time
#from multiprocessing.pool import ThreadPool
import multiprocessing


def tanqueSeeOleo():
    r = requests.get('http://localhost:5000/TanqueDeGli/SeeGli',verify=False)
    stringer = r.json()
    #print(stringer)
    return stringer