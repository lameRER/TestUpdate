import time

from tqdm import tqdm


for i in tqdm(range(1000)):
    for j in tqdm(range(1000)):
        time.sleep(1)
