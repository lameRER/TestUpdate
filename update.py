import os

# os.system('git pull')
# os.popen('git fetch')
if 'master' in os.popen('git fetch').read():
    os.popen('git pull')

os.system('py main.py')
