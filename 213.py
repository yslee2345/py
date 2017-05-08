d={
    'a' : [1,2,3],
    'b' : [4,5]
}

e={
    'a' : {1,2,3},
    'b' : {4,5}
}
print(d)
print(e)

from collections import defaultdict
d= defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
d=defaultdict(set)

d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d={}
d.setdefault('a',[]).append(1)

d={}
for key,value in pairs:
    if key not in d:
        d[key]=[]
    d[key].append(value)

from collections import OrderedDict

d=OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4

for key in d:
    print(key,d[key])

import json
json.dumps(d)


prices = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB'  : 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
max(zip(prices.values(),prices.keys()))
swipe = zip(prices.values(),prices.keys())
min_price
print(swipe)
prices_sorted = sorted(zip(prices.values(),prices.keys()))
prices_sorted

prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names))
print(max(prices_and_names))

min(prices.values())
max(prices.values())
min(prices, key=lambda k:prices[k])
max(prices, key=lambda k:prices[k])



