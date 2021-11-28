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






def tanqueSetOleo():
    while True:
        sleep(10)
        p = requests.post('http://localhost:5000/TanqueDeOleo/SetOleo',verify=False)
        s = p.json()
        print("SetTanque = "  + str(s))

def tanqueSeeOleo():
    r = requests.get('http://localhost:5000/TanqueDeOleo/SeeOleo',verify=False)
    stringer = r.json()
    print(stringer)

def tanqueGetOleo():
    c = requests.get('http://localhost:5000/TanqueDeOleo/GetOleo',verify=False)
    d = c.json()
        
    print("getTanque = "  + str(d))
    return d



#start = time.perf_counter()
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     while True:
#         f1 = executor.submit(tanqueOleo)
#         f2 = executor.submit(cabulando)


#p1 = multiprocessing.Process(target = cabulando)
#p2 = multiprocessing.Process(target = tanqueOleo)

#p1.start()
#p2.start()
