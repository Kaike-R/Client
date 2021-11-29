import json
from types import BuiltinMethodType
import requests
from time import sleep, thread_time, time

from requests.api import request
from decantador import decantadorGet, generateBody
from reatorEtoh import reatorEtohGet

from reatorNaoh import reatorNaohGet
from tanqueDeOleo import tanqueGetOleo
import reator


def SetLavagem():
    while True:
        sleep(1)
        decan = decantadorGet()
        a = generateBody(decan)
        p = requests.post('http://localhost:5000/Lavagem/SetLavagem',verify=False,headers={'content-type':'application/json'},data=a)

        s = p.json()
        
        #print("SetLavagem1 = "  + str(s))

def GetLavagem():
    c = requests.get('http://localhost:5000/Lavagem/GetLavagem',verify=False)
    d = c.json()
    #print("getLavagem1 = "  + str(d))
    return d    

# def SetLavagem2():
#     while True:
#         sleep(1)
#         lavan = GetLavagem()
#         a = generateBody(lavan)
#         p = requests.post('http://localhost:5000/Lavagem/SetLavagem2',verify=False,headers={'content-type':'application/json'},data=a)

#         s = p.json()
        
#         print("SetLavagem2 = "  + str(s))

# def GetLavagem2():
#     c = requests.get('http://localhost:5000/Lavagem/GetLavagem2',verify=False)
#     d = c.json()
#     #print("getLavagem2 = "  + str(d))
#     return d 

# def SetLavagem3():
#     while True:
#         sleep(1)
#         lavan = GetLavagem2()
#         a = generateBody(lavan)
#         p = requests.post('http://localhost:5000/Lavagem/SetLavagem3',verify=False,headers={'content-type':'application/json'},data=a)

#         s = p.json()
        
#         print("SetLavagem3 = "  + str(s))

# def GetLavagem3():
#     c = requests.get('http://localhost:5000/Lavagem/GetLavagem3',verify=False)
#     d = c.json()
#     #print("getLavagem3 = "  + str(d))
#     return d 



