import os

# os.system('git pull')
# os.popen('git fetch')
if 'forced update' in os.popen('git fetch').read():
    os.popen('git pull')

os.system('py main.py')
