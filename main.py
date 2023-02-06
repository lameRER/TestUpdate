import time
# from colorama import Fore

from tqdm import tqdm


for i in tqdm(range(1000), desc='STEP 1'):
    for j in tqdm(range(1000), leave=False, desc='STEP 2'):
        for j in tqdm(range(1000), leave=False, desc='STEP 3'):
            for j in tqdm(range(1000), leave=False, desc='STEP 4'):
                for j in tqdm(range(1001), leave=False, desc='STEP 5'):
                    time.sleep(0.00001)
