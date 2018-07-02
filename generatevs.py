import random
names={}
for line in open('names.txt','r'):
	name = line.strip()
	names[name.lower()]=name


for i in range(10):
	selections = [random.choice(names.keys()) for _ in range(2)]
	print ' vs. '.join([names[x] for x in selections])