import json
from time import sleep, thread_time, time
from types import BuiltinMethodType

import requests
from requests.api import request
from lavagem import GetLavagem

import reator
from decantador import decantadorGet, generateBody
from reatorEtoh import reatorEtohGet
from reatorNaoh import reatorNaohGet
from tanqueDeOleo import tanqueGetOleo
import tanqueDeBiodiesel


def SetSecador():
    while True:
        sleep(1)
        lavan = GetLavagem()
        a = generateBody(lavan)
        p = requests.post('http://localhost:5000/Secador/SetSecador',verify=False,headers={'content-type':'application/json'},data=a)

        s = p.json()
        
        #print("SetSecador    = "  + str(s))

def GetSecador():
     while True:
        sleep(5)
        g = requests.get('http://localhost:5000/Secador/GetSecador',verify=False)
        d = g.json()
        #print("GetSecador = " + str(d))