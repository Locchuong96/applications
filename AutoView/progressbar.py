from tqdm import tqdm,trange
import time

#_______________________________

# for i in trange(10):
# #for i in tqdm(range(1,5)):
# 	time.sleep(0.3)

#_______________________________

# with tqdm(total = 100) as pbar:

# 	for i in range(10):
# 		time.sleep(0.3)
# 		pbar.update(10)

#_______________________________

total    = 100
internal = 33
pbar     = tqdm(total = 100)

for i in range(internal):

	time.sleep(0.3)
	pbar.update(total / internal)

pbar.close()