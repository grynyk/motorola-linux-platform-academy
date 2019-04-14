res1 = sum(filter(lambda x: x%3==0 or x%5==0, range(0,1000)))
res2 = sum(map(int, str(2**1000)))
res3 = sum(filter(lambda x: x%2==0, map(int, str(2**1000))))

res11 = sum([
    i for i in range(0,1000)
    if i%3==0 or i%5==0
])

print(res1)
print(res11)
print(res2)
print(res3)