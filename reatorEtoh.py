import requests
from time import sleep, thread_time, time



global LastEtohGet

def reatorEtohSet():
    while True:
        sleep(0.125)
        p = requests.post('http://localhost:5000/ReatorEtoh/SetEtoh',verify=False)
        s = p.json()
        #print("SetEtoh = "  + str(s))

def reatorEtohSee():
    r = requests.get('http://localhost:5000/ReatorEtoh/SeeEtoh',verify=False)
    stringer = r.json()
    #print(stringer)
    return stringer

def reatorEtohGet():
    c = requests.get('http://localhost:5000/ReatorEtoh/GetEtoh',verify=False)
    d = c.json()
    #print("getEtoh = "  + str(d))
    return d