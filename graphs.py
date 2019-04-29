import matplotlib.pyplot as plt

"""
#error bars
name_1 = ["data 1", "data 2", "data 1&2"]
gb_1=[0.0297560, 0.0315333, 0.0279794]
rf_1=[0.0334763, 0.0301520, 0.0281442]

x =list(range(3))
total_width, n = 0.6, 2
width = total_width / n

res = plt.bar(x, gb_1, width=width, label='GB', color = 'tomato')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] + width

res = plt.bar(x, rf_1, width=width, label='RF', color='cornflowerblue')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] - width/2

plt.xticks(x,name_1)
plt.legend(frameon=True, fancybox=True)
plt.title("Mean Absolute Error")
plt.ylabel("error values")
plt.show()

#import matplotlib.pyplot as plt

name_1 = ["data 1", "data 2", "data 1&2"]

gb_1=[0.2121428, 0.2167832, 0.1901408]
rf_1=[0.2391164, 0.2153714, 0.1981985]

x =list(range(3))
total_width, n = 0.6, 2
width = total_width / n

res = plt.bar(x, gb_1, width=width, label='GB', color = 'tomato')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] + width

res = plt.bar(x, rf_1, width=width, label='RF', color='cornflowerblue')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] - width/2

plt.xticks(x,name_1)
plt.legend(frameon=True, fancybox=True)
plt.title("Mean Absolute Error / Ground Truth")
plt.ylabel("error percentage")
plt.show()

#import matplotlib.pyplot as plt

name_1 = ["data 1", "data 2", "data 1&2"]

gb_1=[0.0029009, 0.0031346, 0.0027712]
rf_1=[0.0031181, 0.0029004, 0.0026396]

x =list(range(3))
total_width, n = 0.6, 2
width = total_width / n

res = plt.bar(x, gb_1, width=width, label='GB', color = 'tomato')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] + width

res = plt.bar(x, rf_1, width=width, label='RF', color='cornflowerblue')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] - width/2

plt.xticks(x,name_1)
plt.legend(frameon=True, fancybox=True)
plt.title("Mean Square Error")
plt.ylabel("error values")
plt.show()

#import matplotlib.pyplot as plt

name_1 = ["data 1", "data 2", "data 1&2"]

gb_1=[0.8568078, 0.7477663, 0.7699633]
rf_1=[0.8131888, 0.7819863, 0.7619820]

x =list(range(3))
total_width, n = 0.6, 2
width = total_width / n

res = plt.bar(x, gb_1, width=width, label='GB', color = 'tomato')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] + width

res = plt.bar(x, rf_1, width=width, label='RF', color='cornflowerblue')
for r in res:
    r.set_edgecolor('black')

for i in range(len(x)):
    x[i] = x[i] - width/2

plt.xticks(x,name_1)
plt.legend(frameon=True, fancybox=True)
plt.title("R2 Score")
plt.ylabel("values")
plt.show()

"""
"""

#r2score lines
gb_d1=[0.90241935, 0.90503832, 1.0, 0.89639045, 0.8908148, 0.90185546, 0.8637456, 0.84681994, 0.92114758, 0.80308528, 0.78111503, 0.35080594, 0.72401932, 0.93408721, 0.87444958, 0.91848531, 0.93829512, 0.90209333, 0.87929288, 0.90219589]
gb_d2=[0.78887095, 0.80658461, 1.0, 0.82873714, 0.8164332, 0.76862276, 0.7317022, 0.71488868, 0.8633243, 0.67180902, 0.77859756, 0.4822892, 0.56345116, 0.57730685, 0.69880768, 0.69354954, 0.6373809, 0.85792352, 0.87906585, 0.79598223]
gb_d12=[0.7953329, 0.80777538, 1.0, 0.74865049, 0.82276316, 0.82076555, 0.80617572, 0.79135202, 0.87103294, 0.78925081, 0.77035631, 0.48840653, 0.61137739, 0.70829024, 0.79174878, 0.74718564, 0.81431023, 0.67090675, 0.76593186, 0.77765511]
rf_d1=[0.77499563, 0.83267776, 1.0, 0.81926521, 0.83876501, 0.79746327, 0.70781683, 0.65014246, 0.87985038, 0.71324669, 0.82357684, 0.4302329, 0.65623099, 0.64571452, 0.71401089, 0.54903142, 0.68718669, 0.86468625, 0.88182937, 0.72366584]
rf_d2=[0.88950188, 0.87537784, 1.0, 0.85176937, 0.89139028, 0.89033992, 0.89795454, 0.79161216, 0.91758494, 0.73773166, 0.7971787, 0.407937, 0.7310298, 0.88529696, 0.87798916, 0.88171414, 0.88499349, 0.87432373, 0.8345306, 0.81345486]
rf_d12=[0.82213195, 0.78618815, 1.0, 0.7258877, 0.80539907, 0.83517031, 0.72906742, 0.69943009, 0.88511216, 0.76001531, 0.81575567, 0.48658621, 0.69995871, 0.6350692, 0.72553947, 0.70822495, 0.78297197, 0.80383053, 0.79591685, 0.66183038]
x=list(range(20))


plt.plot(x,gb_d1,'r--',label='data 1')
plt.plot(x,gb_d2,'g--',label='data 2')
plt.plot(x,gb_d12,'b--',label='data 1&2')
plt.plot(x,gb_d1,'ro-',x,gb_d2,'g+-',x,gb_d12,'b^-')
plt.title("GB R2 Score in all joints")
plt.xticks(x)
plt.legend(frameon=True, fancybox=True)
plt.xlabel("joints")
plt.ylabel("values")
plt.show()


plt.plot(x,rf_d1,'r--',label='data 1')
plt.plot(x,rf_d2,'g--',label='data 2')
plt.plot(x,rf_d12,'b--',label='data 1&2')
plt.plot(x,rf_d1,'ro-',x,rf_d2,'g+-',x,rf_d12,'b^-')
plt.title("RF R2 Score in all joints ")
plt.xticks(x)
plt.legend(frameon=True, fancybox=True)
plt.xlabel("joints")
plt.ylabel("values")
plt.show()

"""


"""
#train parameters lines

x1=[]
x2=[]
for i in range(10):
    x1.append(50+i*50)
    x2.append(0.2+0.2*i)

r1=[0.5935721, 0.7357103, 0.7862851, 0.8090999, 0.8219706, 0.8302616, 0.8356574, 0.8399648, 0.8429253, 0.8451876]
r2=[0.7372708, 0.8092872, 0.8304691, 0.8402667, 0.8457407, 0.8491228, 0.8513973, 0.8534838, 0.8551004, 0.8566649]
r3=[0.7879929, 0.8301353, 0.8432474, 0.8487349, 0.8525685, 0.8548608, 0.8565881, 0.8580092, 0.8589984, 0.8597620]
r4=[0.8096426, 0.8394843, 0.8484805, 0.8529445, 0.8556527, 0.8577317, 0.8593732, 0.8603726, 0.8614072, 0.8618174]
r5=[0.8218892, 0.8452983, 0.8519828, 0.8555361, 0.8579564, 0.8592213, 0.8603899, 0.8613708, 0.8618787, 0.8621309]
label_r=["learning rate = 0.02", "learning rate = 0.04", "learning rate = 0.06", "learning rate = 0.08", "learning rate = 0.1"]

n1=[0.5935721, 0.7372708, 0.7879929, 0.8096426, 0.8218892, 0.8294977, 0.8348541, 0.8352025, 0.8366131, 0.8383542]
n2=[0.7357104, 0.8092873, 0.8301354, 0.8394843, 0.8452984, 0.8475005, 0.8506790, 0.8477179, 0.8489580, 0.8497986]
n3=[0.7862851, 0.8304691, 0.8432474, 0.8484805, 0.8519828, 0.8538603, 0.8562423, 0.8530332, 0.8528979, 0.8530185]
n4=[0.8090999, 0.8402667, 0.8487349, 0.8529445, 0.8555362, 0.8579045, 0.8588624, 0.8549935, 0.8547545, 0.8547038]
n5=[0.8219706, 0.8457408, 0.8525685, 0.8556528, 0.8579564, 0.8599594, 0.8599771, 0.8560682, 0.8562093, 0.8551862]
label_n=["n_estimators = 50","n_estimators = 100", "n_estimators = 150", "n_estimators = 200", "n_estimators = 250"]

plt.plot(x1,r1,'ro-',label=label_r[0])
plt.plot(x1,r2,'gs-',label=label_r[1])
plt.plot(x1,r3,'b*-',label=label_r[2])
plt.plot(x1,r4,'m^-',label=label_r[3])
plt.plot(x1,r5,'y+-',label=label_r[4])

plt.title("R2 Score when training learning rate")
plt.xticks(x1)
plt.legend(frameon=True, fancybox=True)
plt.xlabel("n_estimators values")
plt.ylabel("Score")
plt.show()


plt.plot(x2,n1,'ro-',label=label_n[0])
plt.plot(x2,n2,'gs-',label=label_n[1])
plt.plot(x2,n3,'b*-',label=label_n[2])
plt.plot(x2,n4,'m^-',label=label_n[3])
plt.plot(x2,n5,'y+-',label=label_n[4])

plt.title("R2 Score when training n_estimators")
plt.xticks(x2)
plt.legend(frameon=True, fancybox=True)
plt.xlabel("learning rate")
plt.ylabel("Score")
plt.show()
"""
"""
#correlation
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes

heap=[[0.04408721, 0.39650017, 0.029273, 0.11804212, 0.03237284, 0.1079763, 0.0082433, 0.00605288, 0.03884217, 0.05947219, 0.00457001, 0.01684748, 0.05334572, 0.03584184, 0.01479801, 0.02584108, 0.00364273, 0.00425092],
      [0.03432089, 0.02494967, 0.07211388, 0.03059834, 0.01746143, 0.04073442, 0.00883406, 0.01719016, 0.03615193, 0.047923, 0.00762222, 0.04816105, 0.1536261, 0.26667079, 0.04891684, 0.13181846, 0.00590409, 0.00700268],
      [0.03778814, 0.10324175, 0.03907204, 0.07939898, 0.03312685, 0.11653415, 0.01938474, 0.15217088, 0.03485265, 0.10130584, 0.01379097, 0.06140711, 0.02671689, 0.05401495, 0.04009598, 0.06119393, 0.01299385, 0.01291031],
      [0.01493894, 0.01815848, 0.0163123, 0.48994174, 0.01848968, 0.0226906, 0.00633742, 0.00870018, 0.04009388, 0.04853095, 0.00244805, 0.05400931, 0.01541968, 0.17009696, 0.05778189, 0.01071007, 0.00265708, 0.00268277],
      [0.12724775, 0.25761824, 0.03215914, 0.11402525, 0.02169996, 0.10241111, 0.01159481, 0.00723015, 0.02515941, 0.0422936, 0.00474011, 0.02193667, 0.05318634, 0.05517127, 0.01315558, 0.10367497, 0.00356527, 0.00313035],
      [0.05015032, 0.15246231, 0.02785778, 0.09253481, 0.04447268, 0.1347004, 0.01097102, 0.04276392, 0.03148737, 0.13614944, 0.00653491, 0.04054105, 0.02418088, 0.07035203, 0.05222414, 0.06875484, 0.00705536, 0.00680675],
      [0.04924268, 0.0745356, 0.02415938, 0.04017576, 0.01429918, 0.04003088, 0.01521998, 0.00945147, 0.0249025, 0.03312867, 0.00898147, 0.03767992, 0.21315771, 0.19045655, 0.07805499, 0.1308801, 0.00827994, 0.00736322],
      [0.06059634, 0.29716533, 0.03615681, 0.14381982, 0.02537603, 0.1130546, 0.01235067, 0.00801477, 0.03788478, 0.04566023, 0.00389435, 0.0173526, 0.02048406, 0.02370319, 0.01265561, 0.13516115, 0.00350047, 0.00316917],
      [0.1638747, 0.02250709, 0.16436379, 0.03018796, 0.19660595, 0.04248747, 0.0320836, 0.01268329, 0.03354495, 0.02550473, 0.0087211, 0.07505418, 0.04476373, 0.05797923, 0.04572268, 0.02900902, 0.00732136, 0.00758517],
      [0.03938112, 0.04109625, 0.09970001, 0.05660743, 0.13030204, 0.05492803, 0.24365385, 0.0307895, 0.03247438, 0.03111586, 0.02032445, 0.05705753, 0.02978873, 0.0406856, 0.02896602, 0.02745996, 0.01895875, 0.01671051],
      [0.04075055, 0.09286246, 0.04959606, 0.07178413, 0.0244661, 0.02368071, 0.01150983, 0.0158265, 0.02614595, 0.06231639, 0.00599434, 0.02821591,0.09927907, 0.14716796, 0.24031508, 0.04477176, 0.00690128, 0.00841593],
      [0.03833606, 0.35263166, 0.03727416, 0.11939574, 0.0412803, 0.12468411, 0.0074644, 0.00762165, 0.02258305, 0.0400902,  0.00467571, 0.01535456, 0.11680878, 0.0196722, 0.01988852, 0.02470965, 0.00346264, 0.00406661],
      [0.01493894, 0.01815848, 0.0163123, 0.48994174, 0.01848968, 0.0226906, 0.00633742, 0.00870018, 0.04009388, 0.04853095, 0.00244805, 0.05400931, 0.01541968, 0.17009696, 0.05778189, 0.01071007, 0.00265708, 0.00268277],
      [0.04924268, 0.0745356, 0.02415938, 0.04017576, 0.01429918, 0.04003088, 0.01521998, 0.00945147, 0.0249025, 0.03312867, 0.00898147, 0.03767992, 0.21315771, 0.19045655, 0.07805499, 0.1308801, 0.00827994, 0.00736322]]
x_name=[]
y_name = ["left shoulder", "left foot", "left hand", "left elbow", "left hip", "left wrist", "left knee", "right shoulder", "right wrist", "right hand", "right foot", "right hip", "right elbow", "right knee"]
for i in range(18):
    x_name.append(str((i+1)))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_yticks(range(14))
ax.set_yticklabels(y_name)
ax.set_xticks(range(18))
ax.set_xticklabels(x_name)

im = ax.imshow(heap, cmap=plt.cm.gist_heat_r)
plt.colorbar(im)
plt.title("Correlation between angles and depth")
plt.xlabel("Angles")
plt.ylabel("Joints")
plt.show()

"""
"""
size = 4
a = list(range(size))

total_width, n = 0.8, 3
width = total_width / n

x=[0.0177305838971930, 0.120203868516904, 0.0582290345424788, 0.67626140464330]
y=[0.00880843025088983, 0.0108779367465477, 0.00600069528568168, 0.0149431032180285]
z=[0.013652187419018538, 0.015426790309226014, 0.014105832696132796, 0.017554400529275774]
x_names=["Rignt Elbow", "Rignt Wrist", "Right Hand", "Left Elbow"]

plt.legend()
plt.title("Real deviation distance")
plt.xticks(x_names)
plt.xlabel("Joints")
plt.ylabel("Deviation (cm)")
plt.show()


"""
import numpy as np
import matplotlib.pyplot as plt

size = 3
x = np.arange(size)
a = np.array([0.0177305838971930, 0.120203868516904, 0.0582290345424788])
b = np.array([0.00880843025088983, 0.0108779367465477, 0.00600069528568168])
c = np.array([0.013652187419018538, 0.015426790309226014, 0.014105832696132796])
x_names=["Rignt Elbow", "Rignt Wrist", "Right Hand"]

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

res = plt.bar(x, a, width=width, label='X values')
for r in res:
    r.set_edgecolor('black')
res = plt.bar(x + width, b, width=width, label='Y values')
for r in res:
    r.set_edgecolor('black')
res = plt.bar(x + 2 * width, c, width=width, label='Z values')
for r in res:
    r.set_edgecolor('black')
plt.xticks(x + width, x_names)
plt.xlabel("Joints")
plt.ylabel("Deviation (m)")
plt.title("Real deviation distance")
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

size = 3
x = np.arange(size)
a = np.array([0.00213309935819642, 0.00272487912492553, 0.00163415278059287])
b = np.array([0.00134774376766736, 0.00270911356373328, 0.001800849299898087])
c = np.array([0.011203450333095567, 0.010543398699497691, 0.008432527638600253])
x_names=["Left Knee", "Left Ankle", "Left Foot"]

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

res = plt.bar(x, a, width=width, label='X values')
for r in res:
    r.set_edgecolor('black')
res = plt.bar(x + width, b, width=width, label='Y values')
for r in res:
    r.set_edgecolor('black')
res = plt.bar(x + 2 * width, c, width=width, label='Z values')
for r in res:
    r.set_edgecolor('black')
plt.xticks(x + width, x_names)
plt.xlabel("Joints")
plt.ylabel("Deviation (m)")
plt.title("Real deviation distance")
plt.legend()
plt.show()