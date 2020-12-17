import time,os
import subprocess
from subprocess import Popen

while 1:
	p = Popen(r'C:\\Users\\Admin\\Desktop\\лфн\\python.py', shell=True)
	time.sleep(60)
	p.kill()
	p = Popen(r'C:\\Users\\Admin\\Desktop\\лфн\\test.py', shell=True)
	time.sleep(10)