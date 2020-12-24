import numpy as np
import numpy.linalg as LA

#固有値、固有ベクトル出力
a=np.array([[2,-0.2,0.5],[-0.2,1,0.1],[0.5,0.1,0]])
print("固有値")
print(LA.eig(a)[0])
print("固有ベクトル　縦から読む")
print(LA.eig(a)[1])
