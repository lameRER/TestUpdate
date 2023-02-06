import os

# os.system('git pull')
# os.popen('git fetch')
if 'origin/master' in os.popen('git fetch').read():
    os.popen('git pull')

os.system('py main.py')
