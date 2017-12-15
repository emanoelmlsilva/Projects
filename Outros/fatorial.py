num = int(input())
"""res = 1
for i in range(num,1,-1):
	res *= i
print(res)"""

n = num 
for i in range(1,num):
	n *= (num-i)
print(n)
