
import requests
import urllib3
import reatorNaoh
import reatorEtoh
import tanqueDeOleo
import tanqueDeGli
import reator
import tanqueDeBiodiesel
import os
from time import sleep, thread_time, time

biodisel = 0
glicerina = 0
cliclosReator = 0

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




def imprimir(x,y,z,a,d,b):
    #os.system('cls') or None
    print("----------------------------------------------------------------------\n")
    print("| Oleo: " + str(x) +" | " + "Cliclos: " + str(1) + " |\n")
    print("| Etoh: " + str(y) +" | " + "Biodisel: " + str(b) + " |\n")
    print("| Naoh: " + str(z) +" | " + "Glicerina: " + str(a) + " |\n")
    print("| Reator: " + str(d) +" | " + "Glicerina: " + str(a) + " |\n")
    print("---------------------------------------------------------------------\n")



def colect():
    while True:
        sleep(1)
        volumeNaoh = reatorNaoh.reatorNaohSee()
        volumeEtoh = reatorEtoh.reatorEtohSee()
        volumeOleo = tanqueDeOleo.tanqueSeeOleo()
        volumeGli = tanqueDeGli.tanqueSeeOleo()
        volumeReator = reator.reatorSee()
        volumeBiodiesel = tanqueDeBiodiesel.tanqueSeeBiodiesel()
        #ciclos = reator.GetCiclos()
        imprimir(volumeOleo,volumeEtoh,volumeNaoh,volumeGli,volumeReator,volumeBiodiesel)

