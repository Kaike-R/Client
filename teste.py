from multiprocessing.spawn import freeze_support

import urllib3
from reator import prepareBody
from reatorEtoh import reatorEtohGet
from reatorNaoh import reatorNaohGet
import tanqueDeOleo
#from typing_extensions import runtime
import requests
import json
import asyncio

import subprocess
from random import randint
from time import sleep, thread_time, time
from multiprocessing.pool import ThreadPool
import observer



async def cabulando():
    while True:
        await asyncio.sleep(5)
        print("estou rodando")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def reatorSet():
    while True:
        sleep(1)
        naoh = reatorNaohGet()
        etoh = reatorEtohGet()
        tanque = tanqueDeOleo.tanqueGetOleo()
        body = prepareBody(naoh, etoh, tanque)
        p = requests.post('http://localhost:5000/Reator/SetReator',verify=False, data=body)
        s = p.json()
        
        print("SetReator = "  + str(s))
if __name__ =="__main__":
    #body = prepareBody(0.5,0.5,0.5)
    #a = {"Etoh" : 0.5,"Naoh" : 0.5,"Oleo" : 0.25}
    #p = requests.post('http://localhost:5000/Reator/SetReator',verify=False,headers={'content-type':'application/json'},data=body)
    #print(p.json())
    #print(body)
    
    observer.colect()
        

