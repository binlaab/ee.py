import time
import random
random.seed()

def eep(zzz=0, message='goodnight'):
    print(message)
    time.sleep(random.random() * 10 if not zzz else zzz)
