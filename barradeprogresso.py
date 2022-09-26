import time
import tqdm

count = 0

for i in tqdm.tqdm(range(100)):
    count+=1
    time.sleep(0.4)
print(f'{count}')