#!/usr/bin/python



ans = 0
for i in range(100,1000):
    for j in range(100,1000):
        k = i*j
        if k>ans:
            str_k = str(k)
            if str_k == str_k[::-1]:
                ans = k

print(ans)
