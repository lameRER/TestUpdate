import os
from subprocess import run, STDOUT, PIPE

# os.system('git pull')
# os.popen('git fetch')
# os.system('git fetch')
# status = os.popen('git status').read()
output = run('git fetch', stderr=STDOUT, stdout=PIPE, text=True)
if 'origin/master' in output.stdout:
    out = run('git pull', stderr=STDOUT, stdout=PIPE, text=True)
    print(out.stdout)
    # time.sleep(1)
    # print("yes")

os.system('py main.py')
