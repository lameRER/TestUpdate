import os
import time

from tqdm import tqdm

os.system('git pull')

for i in tqdm(range(1000)):
    for j in tqdm(range(1000)):
        time.sleep(1)
