arr=[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
mean=sum(list(filter(lambda a:a>2,arr)))/len(list(filter(lambda a :a>2,arr)))
print(mean)