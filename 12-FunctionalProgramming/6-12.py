arr=[508,500,512,499,492,511,503,476,501,509]
wyn1=list(filter(lambda x:abs(x-500)>x*0.02,arr))
print(len(wyn1)*100//len(arr))