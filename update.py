import os

# os.system('git pull')
# os.popen('git fetch')
fetch = os.popen('git fetch').read()
status = os.popen('git status').read()
if 'git pull' in status:
    os.popen('git pull')
    print("yes")

# os.system('py main.py')
