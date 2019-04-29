from sklearn.datasets import make_regression
import random

import numpy as np
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import precision_score
#X, y = make_regression(n_samples=10, n_targets=3, random_state=1)
#MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X, y).predict(X)

x=[]
y=[]
yy=[]
tmp=[]
with open("data/allMotion05angles.txt", 'r') as f:
    for line in f.readlines():
        for kk in (line.strip().split(" ")):
            tmp.append(float(kk))
#with open("data/allMotion01angles.txt", 'r') as f:
    for line in f.readlines():
        for kk in (line.strip().split(" ")):
            tmp.append(float(kk))

for j in range(int(len(tmp)/18)):
    kk=[]
    for i in range(18):
        kk.append(tmp[i+j*18])
    x.append(kk)

tmp=[]
with open("data/allMotion05dep.txt", 'r') as f:
    for line in f.readlines():
        for ww in (line.strip().split(" ")):
            tmp.append(float(ww))
#with open("data/allMotion01dep.txt", 'r') as f:
    for line in f.readlines():
        for kk in (line.strip().split(" ")):
            tmp.append(float(kk))

for j in range(int(len(tmp) / 20)):
    kk = []
    for i in range(20):
        kk.append(tmp[i + j * 20])
    y.append(kk)
#print(len(x))
#print(len(y))
#normalize the data
xx=[]
yy=[]
mm = MinMaxScaler()
xx = mm.fit_transform(x)
yy = mm.fit_transform(y)

x_train = []
x_test = []
y_train = []
y_test = []


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
res=MultiOutputRegressor(GradientBoostingRegressor(n_estimators=150, random_state=0)).fit(x_train, y_train)

"""
for i in range(20):
    lr = 0.01+i*0.01
    for j in range (10):
        est = 50 + j*50
        res = MultiOutputRegressor(GradientBoostingRegressor(n_estimators=est, learning_rate=lr, random_state=0)).fit(x_train, y_train)
#y_pred = res.predict(x_test)
#res = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, oob_score=True, random_state=0)).fit(x_train, y_train)

        print("n: "+str(est)+" rate: "+str(lr)+" score: "+str(res.score(x_test, y_test)))
"""
"""
y_pred = res.predict(x_test)
y_res=[]
for i in range(len(y_pred)):
    tmp=[]
    for zz in y_pred[i]:
        tmp.append(str(zz))
    for j in range(20):
        tmp[j] = float(tmp[j])
    y_res.append(tmp)


print(mean_absolute_error(y_test, y_res))
print(np.mean(y_test))
#print(mean_squared_error(y_test, y_res))
#print(r2_score(y_test, y_res, multioutput='raw_values'))

#y_res1=mm.fit_transform(y_res)
#y_test1=mm.fit_transform(y_test)
"""
'''

with open('data/test_results05.txt', 'w') as f:
    for he in y_res:
        for i in range(20):
            f.write(str(he[i]))
            f.write(" ")
        f.write("\n")
with open('data/test_selected05.txt', 'w') as f:
    for he in y_test:
        for i in range(20):
            f.write(str(he[i]))
            f.write(" ")
        f.write("\n")

'''
