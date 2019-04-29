import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

x=[]
y=[]
yy=[]
tmp=[]
#read the data
with open("data/allMotion05angles.txt", 'r') as f:
    for line in f.readlines():
        for kk in (line.strip().split(" ")):
            tmp.append(float(kk))
#with open("data/allMotion01angles.txt", 'r') as f:
#    for line in f.readlines():
#        for kk in (line.strip().split(" ")):
#            tmp.append(float(kk))

for j in range(int(len(tmp)/18)):
    kk=[]
    for i in range(18):
        kk.append(tmp[i+j*18])
    x.append(kk)
tmp=[]
with open("data/allMotion05dep.txt", 'r') as f:
    for line in f.readlines():
        for kk in (line.strip().split(" ")):
            tmp.append(float(kk))
#with open("data/allMotion01dep.txt", 'r') as f:
#    for line in f.readlines():
#        for kk in (line.strip().split(" ")):
#            tmp.append(float(kk))

for j in range(int(len(tmp)/20)):
    kk=[]
    for i in range(20):
        kk.append(tmp[i+j*20])
    y.append(kk)

#normalize the data
xx=[]
yy=[]
mm = MinMaxScaler()
xx = mm.fit_transform(x)
yy = mm.fit_transform(y)


x_train, x_test, y_train, y_test = train_test_split(xx, yy, test_size = 0.2, random_state = 0)
print(len(x_train))
print(len(x_test))

#print(x_train[0])
#print(y_train[0])

forest = RandomForestRegressor(n_estimators=100, oob_score=True)
forest.fit(x_train, y_train)
#print(forest.feature_importances_)
#print(forest.oob_score_)
print(forest.score(x_test, y_test))

'''
y_pred = forest.predict(x_test)
y_res=[]
for i in range(len(y_pred)):
    tmp=[]
    for zz in y_pred[i]:
        tmp.append(str(zz))
    for j in range(20):
        tmp[j] = float(tmp[j])
    y_res.append(tmp)

print(mean_absolute_error(y_test, y_res))
print(mean_squared_error(y_test, y_res))
print(r2_score(y_test, y_res, multioutput='raw_values'))
#y_pred = forest.predict(x_test)
#origin_data = mm.inverse_transform(mm_data)


'''








"""

#t1=[-0.5655915757819999, -0.39738151170250874, 0.0, -0.7939513974372373, 0.582256441447695, 0.8326302359339847, 0.06453715277386532, 0.024864378106398487, 0.007873105286198043, 0.09795492670809625, 0.08542675446545796, -0.06010093466819578, -0.03038112127969972, -0.047371831900688534, -0.15112314917560102, -0.4617106603463273, -0.2925954026832368, 0.2977986028931367, 1.2625269197385713, 0.10510045791732782]
#test = []
#for ww in y_pred[0]:
    #test.append(float(ww))
#print(test)
#print ("AUC Score (Train): "+ str(roc_auc_score(y_test[0],test)))
#print(roc_auc_score(t1, test))
"""