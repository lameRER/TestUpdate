import os

# os.system('git pull')
# os.popen('git fetch')
fetch = os.popen('git fetch').read()
if 'master' in fetch:
    os.popen('git pull')
    print("yes")

os.system('py main.py')
