#!/usr/bin/env python
sum = 0
for dig in range(0,1000):
    if dig % 3 == 0 or dig % 5 == 0:
        sum +=dig
print(sum)

sum1 = sum([i for i in range(1001) 
if i % 5 == 0 or i % 3 == 0])
print(sum1)