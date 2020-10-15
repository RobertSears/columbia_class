import random
listing = [random.randint(0,10) for i in range(1000)]
value_counts = {key: float(listing.count(key))/float(len(listing)) for key in range(len(set(listing)))}


