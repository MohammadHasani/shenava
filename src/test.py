arr1={'a':'aa','b':'bb'}
arr2={'aa':'aa','c':'bd'}
x = 0
for i,j in arr1.items():
    print(j)
    if j in arr2:
        x +=1

print(x)