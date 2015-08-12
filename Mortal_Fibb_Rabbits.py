n, k = (int (x) for x in raw_input().split())

f = [0] * (n + 1)
f[0] = 1
for i in range (2, n + 1):
    f[i] = f[i-2] + f[i-1] - f[i - k - 1]

print f[n] + f[n-1]


#!/usr/bin/env python
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)