import os
import time

# os.system('git pull')
# os.popen('git fetch')
os.system('git fetch')
status = os.popen('git status').read()
if 'git pull' in status:
    os.popen('git pull')
    # print("yes")

time.sleep(1)
os.system('py main.py')
