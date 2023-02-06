import os
import time

# os.system('git pull')
# os.popen('git fetch')
os.system('git fetch')
status = os.popen('git status').read()
if 'git pull' in status:
    os.popen('git pull')
    time.sleep(1)
    # print("yes")

os.system('py main.py')
