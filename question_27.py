import random
listing = [random.randint(0,10) for i in range(1000)]
result=[]
for i in listing:
	if i not in result:
		result.append(i)




