import random
listing = [random.randint(0,10) for i in range(1000)]
value_counts = {key: listing.count(key) for key in range(len(set(listing)))}

