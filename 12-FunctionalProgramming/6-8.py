arr=[37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit
wyn1=list(filter(min_pts(70),arr))
wyn2=list(filter(min_pts(40),arr))
wyn3=list(filter(min_pts(30),arr))

print(wyn1,wyn2,wyn3)

