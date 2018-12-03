# Divide and conquer solution

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def min(a, b):
    if (a > b):
        a = b
    return a

def closest(x):
    x = sorted(x)
    n = len(x)
    if (n == 2):
        return distance(x[0], x[1])

    x1 = closest(x[:int(n/2)])
    x2 = closest(x[(int(n/2)+1):])
    d = min(x1, x2)
    strip = []
    for i in range(n-1):
        if d > abs(x[i][0] - x[int(n/2)][0]):
            strip.append(x[i])
    
    strip = sorted(strip, key = lambda y: y[1])

    k = len(strip)
    for i in range(k-2):
        if (d > distance(strip[i], strip[i+1])):
            d = distance(strip[i], strip[i+1])
    
    return d

test1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest(test1))