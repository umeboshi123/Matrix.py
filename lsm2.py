import numpy as np
#サンプル点
a1 =[-1,0,0,1]
b1 =[0,-2,-1,0]
n=3#次元変更
a =[[0 for j in range(n)] for i in range(n)]
b = [0 for j in range(n)]

pm=(n-1)*2
for i in range(n):
    for i2 in range(n):
        p = pm-i-i2
        for j in range(len(a1)):
            a[i][i2]+=pow(a1[j],p)

for i in range(n):
    for j in range(len()):
        b[i]+=pow(a1[j],n-1-i)*b1[j]

a=np.array(a)
ans=np.dot(np.linalg.inv(a),b)
print(ans)
