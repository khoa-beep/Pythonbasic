
n = int(input())
def nt(t):
     if t < 2: return False
     for i in range(2, int(t**(1/2))+1):
          if t % i == 0: return False
     return True
a = []
for i in range(10):
     if nt(i):
          a.append(i)
for j in a:
     for k in range(10):
          if nt(j*10 + k) and (j*10 + k) < n:
               a.append(j*10 + k)
print(*a)