import requests
from time import sleep, thread_time, time





def reatorNaohSet():
    while True:
        sleep(0.25)

        p = requests.post('http://localhost:5000/ReatorNaoh/SetNaoh',verify=False)
        s = p.json()
        
        #print("SetNaoh = "  + str(s))

    

def reatorNaohSee():
    r = requests.get('http://localhost:5000/ReatorNaoh/SeeNaoh',verify=False)
    stringer = r.json()
    #print(stringer)
    return stringer

def reatorNaohGet():
        
    c = requests.get('http://localhost:5000/ReatorNaoh/GetNaoh',verify=False)
    d = c.json()
    #print("getNaoh = "  + str(d))
    return d    