import json
from types import BuiltinMethodType
import requests
from time import sleep, thread_time, time

from requests.api import request
from reatorEtoh import reatorEtohGet

from reatorNaoh import reatorNaohGet
from tanqueDeOleo import tanqueGetOleo
import reator

def generateBody(x):
    s = {"x": x }
    r = json.dumps(s)
    return r


def decantadorSet():
    while True:
        sleep(3)
        reator2 = reator.PostarVolume()
        a = generateBody(reator2)
        p = requests.post('http://localhost:5000/Decantador/SetDecantador',verify=False,headers={'content-type':'application/json'},data=a)
        s = p.json()
        
        #if s == 42:
            #print("Tanque cheio")
        #else:
            #print("SetDecantador = "  + str(s))

def decantadorSee():
    g = requests.get('http://localhost:5000/Decantador/SeeDecantador',verify=False)
    s = g.json()
    #print(s)
    return s

def decantadorGet():
    g = requests.get('http://localhost:5000/Decantador/GetDecantador',verify=False)
    d = g.json()
    #print("DecantadorGet = " + str(d))
    return d
    