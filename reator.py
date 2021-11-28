import json
from types import BuiltinMethodType
import requests
from time import sleep, thread_time, time
from reatorEtoh import reatorEtohGet

from reatorNaoh import reatorNaohGet
from tanqueDeOleo import tanqueGetOleo



def prepareBody(naoh, etoh, tanque):
    s = {"Etoh":naoh,"Naoh":etoh,"Oleo":tanque}
    #s = r'{"Naoh":"' + str(naoh) + r'", "Etoh" :"' + str(etoh) + r'", "Oleo":"' + str(tanque) + r'"}' 
    n = json.dumps(s)
    #o =json.loads(n)
    #print(n)
    return n





def reatorSet():
    while True:
        sleep(1)
        naoh = reatorNaohGet()
        etoh = reatorEtohGet()
        tanque = tanqueGetOleo()
        body = prepareBody(naoh, etoh, tanque)
        p = requests.post('http://localhost:5000/Reator/SetReator',verify=False,headers={'content-type':'application/json'},data=body)
        s = p.json()
        
        print("SetReator = "  + str(s))

def reatorSee():
    
    p = requests.get('http://localhost:5000/Reator/GetMistura',verify=False)

    s = p.json()

    print("SeeReator = " + str(s))

def reatorMistura():
    while True:
        sleep(1)
        p = requests.post('http://localhost:5000/Reator/ProcessarLiquido',verify=False)
        s = p.json()
        if s != 0:
            print("Quantidade Misturada = " + str(s))

def PostarVolume():
        p = requests.post('http://localhost:5000/Reator/ProcessarLiquido',verify=False)
        s = p.json()
        print("Liquido Processado = " + str(s))
        return s



