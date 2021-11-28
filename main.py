#from typing_extensions import runtime
import multiprocessing
import requests
import json
import asyncio
import urllib3



from random import randint
from time import sleep, thread_time, time
from multiprocessing.pool import ThreadPool
import tanqueDeOleo
import reatorNaoh
import reator
import decantador


runtime = []
threas  = []
names   = []

#desabilitando o warning para o localhost
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def cabulando():
    while True:
        sleep(1)
        print("estou rodando")

#p = requests.post('http://localhost:5000/TanqueDeOleo/SetOleo',verify=False)
if __name__ == '__main__':
    ColocarOleo = multiprocessing.Process(target=tanqueDeOleo.tanqueSetOleo)

    ColocarOleo.start()
    p2 = multiprocessing.Process(target=cabulando)
    #p2.start()
    RetirarOleo = multiprocessing.Process(target=tanqueDeOleo.tanqueGetOleo)
    #RetirarOleo.start()
    ColocarNaoh = multiprocessing.Process(target=reatorNaoh.reatorNaohSet)
    ColocarNaoh.start()
    RetirarNaoh = multiprocessing.Process(target=reatorNaoh.reatorNaohGet)
    #RetirarNaoh.start()
    ColocarReator = multiprocessing.Process(target=reator.reatorSet)
    ColocarReator.start()
    Misturar = multiprocessing.Process(target=reator.reatorMistura)
    Misturar.start()
    SetDecantador = multiprocessing.Process(target=decantador.decantadorSet)
    SetDecantador.start()
#resposta = json.loads(stringer)