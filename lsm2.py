import numpy as np
#サンプル点
a1 =[0,1,2,3]
b1 =[3,6,5,4]
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
    for j in range(len(b1)):
        b[i]+=pow(a1[j],n-1-i)*b1[j]

a=np.array(a)
ans=np.dot(np.linalg.inv(a),b)
print(ans)



import matplotlib.pyplot as plt
N=1024
l=1e9
r=-1e9
for i in range(len(a1)):
    r=max(r,a1[i])
    l=min(l,a1[i])
pp = np.linspace( l-(r-l)/2, r+(r-l)/2, N)  
def f(x):
    return ans[0]*x*x+ans[1]*x+ans[2] #手動

plt.plot(
    pp,[f(pp[k]) for k in range(N)],color='red'
)

for i in range(len(b1)):
    plt.plot(a1[i],b1[i],marker='o')
plt.show()
