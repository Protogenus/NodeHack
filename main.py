import random
import time
import sys

def typing(message):
    # This is for realistic slow typing.
    print("")
    for word in message:
        time.sleep(random.choice([0.1, 0.2, 0.3, 0.08,   0.08, 0.09, 0.1, 0.1, 0.2, 0.3]))
        sys.stdout.write(word)
        sys.stdout.flush()
    time.sleep(.1)
    return ""

class Hacker:
    def __init__(self, atk, btc, root):
        # Hackers base attack stat, Bitcoin and root access flag,
        self.atk = 0
        self.btc = 0
        self.root = 0
    
    def probe(self):
        # TODO: IP scan.
        pass
        
    def exploit(self):
        # Try to exploit the Node to gain access.
        payload = ["malware ", "phishing ", "trojan "]
        print("----Attempting to send " + random.choice(payload) + "payload.----")
        n = random.randint(1, 20) + self.atk
        # If ranom int + the hackers atk stat is greater than the Nodes defense the node is infected.
        if n > Node.sec:
            root = 1
            Node.infection()
        else:
            Node.defense()
        
      
    def keylogger(self):
        # Returns keypresses from the Node.
        logs = ["Hey this is Mike. I need you to fax me that thing or Mr. Kawasaki is gonna ask me to commit Hari Kari.",
                "Ill pick the kids up at 4:30.",
                "Mike Haskell    1732 8893 2011 5932"]
        print("----KEYL0GGER INJECTED----")
        time.sleep(2)
        print("----Waiting for input...----")
        time.sleep(4)
        n = random.choice(logs)
        print(typing(n))
            
      
    def miner(self):
        # Uploads cryptominer to generate money
        print("----Crypt0Miner INJECTED----")
        time.sleep(1)
        print("----MINING.----")
        time.sleep(1)
        print("----MINING..----")
        time.sleep(1)
        print("----MINING...----")
        print("----Block Complete----")
        payout = random.randint(1, 5)
        self.btc += payout
        print("You have gained " + str(payout)  + "BTC")
        print("You currently have: " + str(self.btc) +"BTC")      
    

class Node:
    infected = 0
    def __init__(self, sec):
        # Nodes base security stat.
        self.sec = 15
    
    def defense(self):
        print("----CONNECTION ENDED----")
        print("Node has detected the attack and closed the connection")
    
    def infection(self):
        print("----NODE INFECTED----")
        infected = 1



# Create the Hacker and a Node.
Hacker = Hacker(25, 0, 0)
Node = Node(150)

# Test hacker functions.
Hacker.miner()