#from typing_extensions import runtime
import multiprocessing
import requests
import json
import asyncio
import urllib3

from tkinter import *


from random import randint
from time import sleep, thread_time, time
from multiprocessing.pool import ThreadPool
from lavagem import SetLavagem
from reatorEtoh import reatorEtohSet

import secador
import tanqueDeOleo
import reatorNaoh
import reator
import decantador
import observer
import reatorEtoh
import lavagem
import tanqueDeBiodiesel

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
    Printar = multiprocessing.Process(target=observer.colect)
    Printar.start()
    
    ColocarOleo = multiprocessing.Process(target=tanqueDeOleo.tanqueSetOleo)
    ColocarOleo.start()
    ColocarNaoh = multiprocessing.Process(target=reatorNaoh.reatorNaohSet)
    ColocarNaoh.start()
    ColocarEtoh = multiprocessing.Process(target=reatorEtoh.reatorEtohSet)
    ColocarEtoh.start()

    sleep(20)


    ColocarReator = multiprocessing.Process(target=reator.reatorSet)
    ColocarReator.start()
    Misturar = multiprocessing.Process(target=reator.reatorMistura)
    Misturar.start()
    SetDecantador = multiprocessing.Process(target=decantador.decantadorSet)
    SetDecantador.start()
    SetLavagem = multiprocessing.Process(target=lavagem.SetLavagem)
    SetLavagem.start()
    # SetLavagem2 = multiprocessing.Process(target=lavagem.SetLavagem2)
    # SetLavagem2.start()
    # SetLavagem3 = multiprocessing.Process(target=lavagem.SetLavagem3)
    # SetLavagem3.start()
    SetSecador = multiprocessing.Process(target=secador.SetSecador)
    SetSecador.start()
    ColocarBio = multiprocessing.Process(target=secador.GetSecador)
    ColocarBio.start()

    


  


    

#resposta = json.loads(stringer)