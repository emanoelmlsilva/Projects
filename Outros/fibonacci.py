t1 = 0
t2 = 1
t3 = 0
num = int(input())
for i in range(num):
	if i == 0:
		t2 = 0
	elif i == 1:
		t2 = 1
	t3 = t1 + t2
	t1 = t2 
	t2 = t3
print(t3)
