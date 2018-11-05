'''

保存和装载MATLAB格式的文件

*.mat

Anaconda Python
'''

import numpy as np
from scipy import io

a = np.array([[2,3,5],[5,4,3]])

io.savemat('a.mat',{'array':a})

b = io.loadmat('a.mat')
print(b['array'] * 20)




