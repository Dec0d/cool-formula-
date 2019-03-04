import time

p = [2, 3, 5, 7,]
for i in range(1,5000):
	if i%2:
		if i%3:
			if i%5:
				if i%7:
					p.append(i)
p.remove(1)
a = 5
b = 83
y = a
x = b
for i in range(0, 20):
    if a < b:
        c = a
        a = b
        b = c

    
    y =p[abs((a - b) -1)]
    x =abs(p[a - 1] - p[b - 1])
    a = abs(y)
    b = abs(x)    
    print(a ,b)

