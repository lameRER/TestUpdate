import os

# os.system('git pull')
os.popen('git fetch')
a = os.popen('git status').read()
print(a)
# os.system('py main.py')
