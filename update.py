import os

# os.system('git pull')
# os.popen('git fetch')
os.system('git fetch')
status = os.popen('git status').read()
if 'git pull' in status:
    os.popen('git pull')
    print("yes")

# os.system('py main.py')
