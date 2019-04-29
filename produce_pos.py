from sympy import *
from math import *

lines = []
angles = []
dep_tru = []
dep_res = []
index =[]
x = []
y = []
z = []
x_res = []
y_res = []
z_res = []

x_error=[]
x_dis=[]
y_error=[]
y_dis=[]
z_error=[]
z_dis=[]

def onepoint(d_ab, d_ac, dep_b, dep_a, angle, a_x, a_y, c_x, c_y):

    def distance(x, y):
        xx = (x[0] - y[0]) ** 2
        yy = (x[1] - y[1]) ** 2
        zz = (x[2] - y[2]) ** 2
        return (sqrt(xx + yy + zz))

    # comput the intput values
    #d_ab = distance(a, b)
    #d_ac = distance(a, c)

    #zz = (a[2] - b[2]) / d_ab
    #theta = asin(zz)
    #angle = acos((d_ab ** 2 + d_ac ** 2 - distance(b, c) ** 2) / (2 * d_ab * d_ac))
    # print(angle)
    #print(theta)

    # compute outputs
    b_a = d_ab * sin(dep_b)
    d_bc = sqrt(d_ab ** 2 + d_ac ** 2 - 2 * d_ab * d_ac * cos(angle))
    c_a = d_ac * sin(dep_a)

    ab = d_ab ** 2 - (b_a) ** 2
    bc = d_bc ** 2 - (c_a + b_a) ** 2

    ra = sqrt(ab)
    rc = sqrt(bc)

    x = Symbol('x')
    y = Symbol('y')

    res = solve([(x - a_x) ** 2 + (y - a_y) ** 2 - ab, (x - c_x) ** 2 + (y - c_y) ** 2 - bc], [x, y])
    final_res=[list(res[0]), list(res[1])]
    return final_res

def onepoint2(d_ab, d_ac, dep_b, angle, a_x, a_y, a_z, c_x, c_y, c_z):

    def distance(x, y):
        xx = (x[0] - y[0]) ** 2
        yy = (x[1] - y[1]) ** 2
        zz = (x[2] - y[2]) ** 2
        return (sqrt(xx + yy + zz))

    # comput the intput values
    #d_ab = distance(a, b)
    #d_ac = distance(a, c)

    #zz = (a[2] - b[2]) / d_ab
    #theta = asin(zz)
    #angle = acos((d_ab ** 2 + d_ac ** 2 - distance(b, c) ** 2) / (2 * d_ab * d_ac))
    # print(angle)
    #print(theta)

    # compute outputs
    b_a = d_ab * sin(dep_b)
    d_bc = sqrt(d_ab ** 2 + d_ac ** 2 - 2 * d_ab * d_ac * cos(angle))
    c_b = c_z-a_z+b_a

    ab = abs(d_ab ** 2 - b_a ** 2)
    bc = abs(d_bc ** 2 - c_b ** 2)

    #ra = sqrt(ab)
    #rc = sqrt(bc)

    x = Symbol('x')
    y = Symbol('y')

    res = solve([(x - a_x) ** 2 + (y - a_y) ** 2 - ab, (x - c_x) ** 2 + (y - c_y) ** 2 - bc], [x, y])
    final_res=[list(res[0]), list(res[1])]
    return final_res

def read_test():
    tmp1=[]
    with open("data/allMotion05dep.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp1.append(float(kk))
    tmp2=[]
    with open("data/test_selected05.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp2.append(float(kk))
    tmp_all = []
    tmp_part = []
    for i in range(int(len(tmp1)/20)):
        tmp = []
        for j in range(20):
            tmp.append(tmp1[i*20+j])
        tmp_all.append(tmp)
    for i in range(int(len(tmp2)/20)):
        tmp = []
        for j in range(20):
            tmp.append(tmp2[i*20+j])
        tmp_part.append(tmp)
        dep_tru.append(tmp)

    index=[]
    #print(len(tmp_all))
    #print(len(tmp_part))
    #print(tmp_part)
    for list in tmp_part:
        for i in range(int(len(tmp_all))):
            if tmp_all[i] == list:
            #print(tmp_list)
                index.append(i)
                break
    #for j in tmp_part:
        #print(j)

    #print(len(index))
    return index

#read_test()


def read_xyd():

    index = read_test()

    #read lines, angles and depths
    tmp1=[]
    with open("data/linesallMotion10.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp1.append(float(kk))
    tmp2 = []
    with open("data/allMotion05angles.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp2.append(float(kk))
    tmp3 = []
    with open("data/test_results05.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp3.append(float(kk))
    tmp_x=[]

    for i in range(int(len(tmp1)/19)):
        tmp = []
        for j in range(19):
            tmp.append(tmp1[i*19+j])
        tmp_x.append(tmp)
    tmp_y=[]
    for i in range(int(len(tmp2)/18)):
        tmp = []
        for j in range(18):
            tmp.append(tmp2[i * 18 + j])
        tmp_y.append(tmp)
    for i in range(int(len(tmp3)/20)):
        tmp = []
        for j in range(20):
            tmp.append(tmp3[i * 20 + j])
        dep_res.append(tmp)

    for i in index:
        lines.append(tmp_x[i])
        angles.append(tmp_y[i])


    #read x, y, z
    tmp1 = []
    with open("data/axies_allMotion05x.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp1.append(float(kk))
    tmp2 = []
    with open("data/axies_allMotion05y.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp2.append(float(kk))
    tmp3 = []
    with open("data/axies_allMotion05z.txt", 'r') as f:
        for line in f.readlines():
            for kk in (line.strip().split(" ")):
                tmp3.append(float(kk))
    tmp_x = []
    for i in range(int(len(tmp1)/20)):
        tmp = []
        for j in range(20):
            tmp.append(tmp1[i * 20 + j])
        tmp_x.append(tmp)
    tmp_y = []
    for i in range(int(len(tmp2)/20)):
        tmp = []
        for j in range(20):
            tmp.append(tmp2[i * 20 + j])
        tmp_y.append(tmp)
    tmp_z = []
    for i in range(int(len(tmp2)/20)):
        tmp = []
        for j in range(20):
            tmp.append(tmp3[i * 20 + j])
        tmp_z.append(tmp)

    for i in index:
        x.append(tmp_x[i])
        y.append(tmp_y[i])
        z.append(tmp_z[i])

    #print(x[0])
    #print(len(y))
    #print(len(z))
    #print(len(lines))
    #print(len(angles))
    #print(len(dep_tru))
    #print(len(dep_res))

#read_xyd()

def produce_pos_1():
    read_xyd()
    #onepoint(d_ab, d_ac, dep_b, dep_c, angle, a_x, a_y, c_x, c_y)


    #compute the right elbow
    x_t = []
    y_t = []
    for i in range(525):
        #i=0
        res = onepoint2(lines[i][3], lines[i][1], dep_res[i][7], angles[i][2], x[i][0], y[i][0], z[i][0], x[i][2], y[i][2], z[i][2])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][7]-x1) + abs(y[i][7]-y1)
        dis2 = abs(x[i][7]-x2) + abs(y[i][7]-y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
         sum1 = sum1 + abs(x_t[i]-x[i][7])/abs(x[i][7])
         sum2 = sum2 + abs(y_t[i] - y[i][7]) / abs(y[i][7])
         sum3 = sum3 + abs(x_t[i]-x[i][7])
         sum4 = sum4 + abs(y_t[i] - y[i][7])
    x_error.append(sum1/525)
    y_error.append(sum2/525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(1)
    print(sum1/525)
    print(sum2/525)
    print(sum3 / 525)
    print(sum4 / 525)
    

    #compute the right wrist
    x_t = []
    y_t = []
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][4], lines[i][3], dep_res[i][9], angles[i][4], x[i][7], y[i][7], z[i][7], x[i][0],
                       y[i][0], z[i][0])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][9] - x1) + abs(y[i][9] - y1)
        dis2 = abs(x[i][9] - x2) + abs(y[i][9] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][9]) / abs(x[i][9])
        sum2 = sum2 + abs(y_t[i] - y[i][9]) / abs(y[i][9])
        sum3 = sum3 + abs(x_t[i] - x[i][9])
        sum4 = sum4 + abs(y_t[i] - y[i][9])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(2)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)


    # compute the right hand
    x_t = []
    y_t = []
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][5], lines[i][4], dep_res[i][11], angles[i][6], x[i][9], y[i][9], z[i][9], x[i][7],
                       y[i][7], z[i][7])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][11] - x1) + abs(y[i][11] - y1)
        dis2 = abs(x[i][11] - x2) + abs(y[i][11] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][11]) / abs(x[i][11])
        sum2 = sum2 + abs(y_t[i] - y[i][11]) / abs(y[i][11])
        sum3 = sum3 + abs(x_t[i] - x[i][11])
        sum4 = sum4 + abs(y_t[i] - y[i][11])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(3)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the left elbow
    x_t = []
    y_t = []
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][6], lines[i][2], dep_res[i][8], angles[i][3], x[i][1], y[i][1], z[i][1], x[i][2],
                       y[i][2], z[i][2])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][8] - x1) + abs(y[i][8] - y1)
        dis2 = abs(x[i][8] - x2) + abs(y[i][8] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][8]) / abs(x[i][8])
        sum2 = sum2 + abs(y_t[i] - y[i][8]) / abs(y[i][8])
        sum3 = sum3 + abs(x_t[i] - x[i][8])
        sum4 = sum4 + abs(y_t[i] - y[i][8])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(4)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the left wrist
    x_t = []
    y_t = []
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][7], lines[i][6], dep_res[i][10], angles[i][5], x[i][8], y[i][8], z[i][8], x[i][1],
                       y[i][1], z[i][1])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][10] - x1) + abs(y[i][10] - y1)
        dis2 = abs(x[i][10] - x2) + abs(y[i][10] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][10]) / abs(x[i][10])
        sum2 = sum2 + abs(y_t[i] - y[i][10]) / abs(y[i][10])
        sum3 = sum3 + abs(x_t[i] - x[i][10])
        sum4 = sum4 + abs(y_t[i] - y[i][10])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(5)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)


    # compute the left hand
    x_t = []
    y_t = []
    num = 12
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][8], lines[i][7], dep_res[i][12], angles[i][7], x[i][10], y[i][10], z[i][10], x[i][8],
                       y[i][8], z[i][8])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(6)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)


    # compute the left knee
    x_t = []
    y_t = []
    num = 13
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][12], lines[i][11], dep_res[i][13], angles[i][12], x[i][4], y[i][4], z[i][4], x[i][6],
                        y[i][6], z[i][6])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(7)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the left ankle
    x_t = []
    y_t = []
    num = 15
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][13], lines[i][12], dep_res[i][15], angles[i][14], x[i][13], y[i][13], z[i][13], x[i][4],
                        y[i][4], z[i][4])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(8)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the left foot
    x_t = []
    y_t = []
    num = 17
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][14], lines[i][13], dep_res[i][17], angles[i][16], x[i][15], y[i][15], z[i][15], x[i][13],
                        y[i][13], z[i][13])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(9)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the right knee
    x_t = []
    y_t = []
    num = 14
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][16], lines[i][15], dep_res[i][14], angles[i][13], x[i][5], y[i][5], z[i][5], x[i][6],
                        y[i][6], z[i][6])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(10)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the right ankle
    x_t = []
    y_t = []
    num = 16
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][17], lines[i][16], dep_res[i][16], angles[i][15], x[i][14], y[i][14], z[i][14], x[i][5],
                        y[i][5], z[i][5])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(11)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)

    # compute the right foot
    x_t = []
    y_t = []
    num = 18
    for i in range(525):
        # i=0
        res = onepoint2(lines[i][18], lines[i][17], dep_res[i][18], angles[i][17], x[i][16], y[i][16], z[i][16], x[i][14],
                        y[i][14], z[i][14])
        x1 = res[0][0]
        x2 = res[1][0]
        y1 = res[0][1]
        y2 = res[1][1]
        dis1 = abs(x[i][num] - x1) + abs(y[i][num] - y1)
        dis2 = abs(x[i][num] - x2) + abs(y[i][num] - y2)
        if dis1 < dis2:
            x_t.append(x1)
            y_t.append(y1)
        else:
            x_t.append(x2)
            y_t.append(y2)
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for i in range(525):
        sum1 = sum1 + abs(x_t[i] - x[i][num]) / abs(x[i][num])
        sum2 = sum2 + abs(y_t[i] - y[i][num]) / abs(y[i][num])
        sum3 = sum3 + abs(x_t[i] - x[i][num])
        sum4 = sum4 + abs(y_t[i] - y[i][num])
    x_error.append(sum1 / 525)
    y_error.append(sum2 / 525)
    x_dis.append(sum3 / 525)
    y_dis.append(sum4 / 525)
    print(12)
    print(sum1 / 525)
    print(sum2 / 525)
    print(sum3 / 525)
    print(sum4 / 525)


#produce_pos_1()

def produce_z():
    read_xyd()
    #print(len(z_res))
    sum1=0
    sum2=0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][7])-sin(dep_res[i][7]))*lines[i][3]
        sum2 = sum2 + abs(sin(dep_tru[i][7])-sin(dep_res[i][7]))/abs(sin(dep_tru[i][7])*lines[i][3])
    z_dis.append(sum1/525)
    z_error.append(sum2/525)
    print(sum1/525)
    print(sum2/525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][9]) - sin(dep_res[i][9])) * lines[i][4]
        sum2 = sum2 + abs(sin(dep_tru[i][9]) - sin(dep_res[i][9])) / abs(sin(dep_tru[i][9]) * lines[i][4])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][11]) - sin(dep_res[i][11])) * lines[i][5]
        sum2 = sum2 + abs(sin(dep_tru[i][11]) - sin(dep_res[i][11])) / abs(sin(dep_tru[i][11]) * lines[i][5])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][8]) - sin(dep_res[i][8])) * lines[i][6]
        sum2 = sum2 + abs(sin(dep_tru[i][8]) - sin(dep_res[i][8])) / abs(sin(dep_tru[i][8]) * lines[i][6])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][10]) - sin(dep_res[i][10])) * lines[i][7]
        sum2 = sum2 + abs(sin(dep_tru[i][10]) - sin(dep_res[i][10])) / abs(sin(dep_tru[i][10]) * lines[i][7])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][12]) - sin(dep_res[i][12])) * lines[i][8]
        sum2 = sum2 + abs(sin(dep_tru[i][12]) - sin(dep_res[i][12])) / abs(sin(dep_tru[i][12]) * lines[i][8])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][13]) - sin(dep_res[i][13])) * lines[i][12]
        sum2 = sum2 + abs(sin(dep_tru[i][13]) - sin(dep_res[i][13])) / abs(sin(dep_tru[i][13]) * lines[i][12])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][15]) - sin(dep_res[i][15])) * lines[i][13]
        sum2 = sum2 + abs(sin(dep_tru[i][15]) - sin(dep_res[i][15])) / abs(sin(dep_tru[i][15]) * lines[i][13])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][17]) - sin(dep_res[i][17])) * lines[i][14]
        sum2 = sum2 + abs(sin(dep_tru[i][17]) - sin(dep_res[i][17])) / abs(sin(dep_tru[i][17]) * lines[i][14])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][14]) - sin(dep_res[i][14])) * lines[i][16]
        sum2 = sum2 + abs(sin(dep_tru[i][14]) - sin(dep_res[i][14])) / abs(sin(dep_tru[i][14]) * lines[i][16])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][16]) - sin(dep_res[i][16])) * lines[i][17]
        sum2 = sum2 + abs(sin(dep_tru[i][16]) - sin(dep_res[i][16])) / abs(sin(dep_tru[i][16]) * lines[i][17])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)

    sum1 = 0
    sum2 = 0
    for i in range(525):
        sum1 = sum1 + abs(sin(dep_tru[i][18]) - sin(dep_res[i][18])) * lines[i][18]
        sum2 = sum2 + abs(sin(dep_tru[i][18]) - sin(dep_res[i][18])) / abs(sin(dep_tru[i][18]) * lines[i][18])
    z_dis.append(sum1 / 525)
    z_error.append(sum2 / 525)
    print(sum1 / 525)
    print(sum2 / 525)


produce_z()