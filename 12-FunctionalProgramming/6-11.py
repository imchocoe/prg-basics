test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

wyn=(filter((lambda x: x['result']>=50 and x['result']<=70),test_results))
res=list(map(lambda x: x['name'],wyn))
print(res)