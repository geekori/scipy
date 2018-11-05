'''

随机数分析

均值、标准差

偏度、峰度、正态性检测

'''

from scipy import stats
import matplotlib.pyplot as plt

# 产生100个正态分布的随机数
generated = stats.norm.rvs(size=100)
print(generated)

# 计算均值和标准差
print('均值','标准差',stats.norm.fit(generated))

# 偏度：可以得到随机数服从正态分布的概率，取值范围从0到1
print('偏度','概率',stats.skewtest(generated))

# 峰度：概率分布曲线的陡峭程度
print('峰度','陡峭程度',stats.kurtosistest(generated))

#正态性检测
print('正态性检测','符合正态性程度',stats.normaltest(generated))

plt.hist(generated)
plt.show()



