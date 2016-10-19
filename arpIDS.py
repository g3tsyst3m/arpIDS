import subprocess
import time
import os
from collections import Counter


def checker(poisoned):
    os.system("cls")
    batcmd="for /F \"tokens=1,2\" %a in ('arp -a') do @echo %a %b"
    ipaddress=subprocess.check_output(batcmd, shell=True)
    ipaddress=ipaddress.split()
    #print ipaddress

    batcmd2="for /F \"tokens=2\" %a in ('arp -a') do @echo %a"
    macaddress=subprocess.check_output(batcmd2, shell=True)
    macaddress=macaddress.split()
    #print macaddress
    if poisoned==0:
        print "checking arp entries...so far so good"
    for k,v in Counter(macaddress).items():
        if v>1 and k != "01-00-5e-7f-ff-fa" and k != "01-00-5e-00-00-02" and k != "ff-ff-ff-ff-ff-ff" and k != "Address" and k != "01-00-5e-00-00-0d" and k != "01-00-5e-00-00-fc" and k != "01-00-5e-00-00-fb" and k != "01-00-5e-00-01-28" and k != "01-00-5e-00-00-16":
            print "SOMEONE IS UP TO NO GOOD! HERE'S THE SUSPECT'S MAC ADDRESS:",k
            indices = [i for i, x in enumerate(ipaddress) if x == k]
            #ourindex=ipaddress.index(k)
            print "HOSTS POISONED COUNT:", len(indices)
            for theirip in indices:
                print "Here are the suspected IP addresses that match the Attacker's MAC Address:"
                print(ipaddress[theirip-1])
            #print "HERE'S THE IP ADDRESSES THAT COULD BE THE SUSPECTED ATTACKER: ",ipaddress[indices[0]-1], ipaddress[indices[1]-1]
            #print ipaddress[ourindex]			
            poisoned=1
            time.sleep(5)
            checker(poisoned)
        
    time.sleep(5)
    checker(0)    

checker(0)




          
		
