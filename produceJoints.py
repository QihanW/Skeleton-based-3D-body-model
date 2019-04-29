import math
import os

def read_xyz (mot, sub, ind, x, y, z, c):
    title="../real3d/a"+mot+"_s"+sub+"_e"+ind+"_skeleton3D.txt"
    data=[]
    if(os.path.isfile(title)==False):
        return 0
    with open(title, 'r') as f:
        for line in f.readlines():
            tmp = []
            for kk in (line.strip().split(" ")):
                tmp.append(float(kk))
            data.append(tmp)
    #print(x)
    for w in data:
        x.append(w[0])
        y.append(w[1])
        z.append(w[2])
        c.append(w[3])
    return [x,y,z,c]

def write_xyz (x, y, z, c, label):
    title = "data/axies_"+label
    with open(title+"x.txt", 'a') as f:
        for i in x:
            f.write(str(i))
            f.write(" ")

    with open(title+"y.txt", 'a') as f:
        for i in y:
            f.write(str(i))
            f.write(" ")

    with open(title+"z.txt", 'a') as f:
        for i in z:
            f.write(str(i))
            f.write(" ")

    with open(title+"c.txt", 'a') as f:
        for i in c:
            f.write(str(i))
            f.write(" ")

def trans_xyz(x, y, z):
    xx = []
    yy = []
    zz = []
    length = len(x)/20
    for i in range(length):
        tmp = []
        for j in range(20):
            tmp.append(x[j+i*20])
        xx.append(tmp)
        tmp = []
        for j in range(20):
            tmp.append(y[j + i * 20])
        yy.append(tmp)
        tmp = []
        for j in range(20):
            tmp.append(z[j + i * 20])
        zz.append(tmp)
    return [xx, yy, zz]

def compute_lines(x,y,z):
    lines=[]
    def distance(m, n):
        xx = (x[m] - x[n]) ** 2
        yy = (y[m] - y[n]) ** 2
        zz = (z[m] - z[n]) ** 2
        return (math.sqrt(xx + yy + zz))
    length = int(len(x)/20)
    #print(length)
    for i in range(length):
        j = i * 20
        lines.append(distance((19 + j), (2 + j)))
        lines.append(distance((0 + j), (2 + j)))
        lines.append(distance((1 + j), (2 + j)))
        lines.append(distance((0 + j), (7 + j)))
        lines.append(distance((9 + j), (7 + j)))
        lines.append(distance((9 + j), (11 + j)))
        lines.append(distance((1 + j), (8 + j)))
        lines.append(distance((10 + j), (8 + j)))
        lines.append(distance((10 + j), (12 + j)))
        lines.append(distance((3 + j), (2 + j)))
        lines.append(distance((3 + j), (6 + j)))
        lines.append(distance((6 + j), (4 + j)))
        lines.append(distance((13 + j), (4 + j)))
        lines.append(distance((13 + j), (15 + j)))
        lines.append(distance((17 + j), (15 + j)))
        lines.append(distance((5 + j), (6 + j)))
        lines.append(distance((5 + j), (14 + j)))
        lines.append(distance((14 + j), (16 + j)))
        lines.append(distance((16 + j), (18 + j)))
    return lines

def write_lines(lines, lable):
    title = "data/lines"+lable+".txt"
    with open(title, 'a') as f:
        for i in lines:
            f.write(str(i))
            f.write(" ")

def compute_angles(x, y, z, lines):
    angles = []
    length = int(len(x) / 20)
    def distance(m, n):
        xx = (x[m] - x[n]) ** 2
        yy = (y[m] - y[n]) ** 2
        zz = (z[m] - z[n]) ** 2
        return (math.sqrt(xx + yy + zz))
    for i in range(length):
        j = i * 20
        k = i * 19
        # 1
        tmp = distance((0 + j), (19 + j))
        ang = (lines[0 + k] ** 2 + lines[1 + k] ** 2 - tmp ** 2) / (2 * lines[0 + k] * lines[1 + k])
        angles.append(math.acos(ang))
        # 2
        tmp = distance((1 + j), (19 + j))
        ang = (lines[0 + k] ** 2 + lines[2 + k] ** 2 - tmp ** 2) / (2 * lines[0 + k] * lines[2 + k])
        angles.append(math.acos(ang))
        # 3
        tmp = distance((2 + j), (7 + j))
        ang = (lines[1 + k] ** 2 + lines[3 + k] ** 2 - tmp ** 2) / (2 * lines[1 + k] * lines[3 + k])
        angles.append(math.acos(ang))
        # 4
        tmp = distance((2 + j), (8 + j))
        ang = (lines[2 + k] ** 2 + lines[6 + k] ** 2 - tmp ** 2) / (2 * lines[2 + k] * lines[6 + k])
        angles.append(math.acos(ang))
        # 5
        tmp = distance((0 + j), (9 + j))
        ang = (lines[3 + k] ** 2 + lines[4 + k] ** 2 - tmp ** 2) / (2 * lines[3 + k] * lines[4 + k])
        angles.append(math.acos(ang))
        # 6
        tmp = distance((1 + j), (10 + j))
        ang = (lines[6 + k] ** 2 + lines[7 + k] ** 2 - tmp ** 2) / (2 * lines[6 + k] * lines[7 + k])
        angles.append(math.acos(ang))
        # 7
        tmp = distance((7 + j), (11 + j))
        ang = (lines[4 + k] ** 2 + lines[5 + k] ** 2 - tmp ** 2) / (2 * lines[4 + k] * lines[5 + k])
        angles.append(math.acos(ang))
        # 8
        tmp = distance((8 + j), (12 + j))
        ang = (lines[7 + k] ** 2 + lines[8 + k] ** 2 - tmp ** 2) / (2 * lines[7 + k] * lines[8 + k])
        angles.append(math.acos(ang))
        # 9
        tmp = distance((2 + j), (6 + j))
        ang = (lines[10 + k] ** 2 + lines[9 + k] ** 2 - tmp ** 2) / (2 * lines[10 + k] * lines[9 + k])
        angles.append(math.acos(ang))
        # 10
        tmp = distance((3 + j), (4 + j))
        ang = (lines[10 + k] ** 2 + lines[11 + k] ** 2 - tmp ** 2) / (2 * lines[10 + k] * lines[11 + k])
        angles.append(math.acos(ang))
        # 11
        tmp = distance((4 + j), (5 + j))
        ang = (lines[11 + k] ** 2 + lines[15 + k] ** 2 - tmp ** 2) / (2 * lines[11 + k] * lines[15 + k])
        angles.append(math.acos(ang))
        # 12
        tmp = distance((3 + j), (5 + j))
        ang = (lines[10 + k] ** 2 + lines[15 + k] ** 2 - tmp ** 2) / (2 * lines[10 + k] * lines[15 + k])
        angles.append(math.acos(ang))
        # 13
        tmp = distance((6 + j), (13 + j))
        ang = (lines[11 + k] ** 2 + lines[12 + k] ** 2 - tmp ** 2) / (2 * lines[11 + k] * lines[12 + k])
        angles.append(math.acos(ang))
        # 14
        tmp = distance((6 + j), (14 + j))
        ang = (lines[15 + k] ** 2 + lines[16 + k] ** 2 - tmp ** 2) / (2 * lines[15 + k] * lines[16 + k])
        angles.append(math.acos(ang))
        # 15
        tmp = distance((4 + j), (15 + j))
        ang = (lines[12 + k] ** 2 + lines[13 + k] ** 2 - tmp ** 2) / (2 * lines[12 + k] * lines[13 + k])
        angles.append(math.acos(ang))
        # 16
        tmp = distance((5 + j), (16 + j))
        ang = (lines[16 + k] ** 2 + lines[17 + k] ** 2 - tmp ** 2) / (2 * lines[16 + k] * lines[17 + k])
        angles.append(math.acos(ang))
        # 17
        tmp = distance((13 + j), (17 + j))
        ang = (lines[13 + k] ** 2 + lines[14 + k] ** 2 - tmp ** 2) / (2 * lines[13 + k] * lines[14 + k])
        angles.append(math.acos(ang))
        # 18
        tmp = distance((14 + j), (18 + j))
        ang = (lines[17 + k] ** 2 + lines[18 + k] ** 2 - tmp ** 2) / (2 * lines[17 + k] * lines[18 + k])
        angles.append(math.acos(ang))

    return angles

def write_angles(angles, lable):
    title = "data/" + lable + "angles.txt"
    with open(title, 'a') as f:
        for i in angles:
            f.write(str(i))
            f.write(" ")

def dep_sin(x, y, z):
    dep = []
    length = int(len(x) / 20)

    def distance(m, n):
        xx = (x[m] - x[n]) ** 2
        yy = (y[m] - y[n]) ** 2
        zz = (z[m] - z[n]) ** 2
        return (math.sqrt(xx + yy + zz))

    for i in range(length):
        j = i * 20
        tmp = (z[2 + j] - z[0 + j]) / distance(2 + j, 0 + j)
        # print(tmp)
        dep.append(math.asin(tmp))
        tmp = (z[2 + j] - z[1 + j]) / distance(2 + j, 1 + j)
        dep.append(math.asin(tmp))
        dep.append(0)
        tmp = (z[2 + j] - z[3 + j]) / distance(2 + j, 3 + j)
        dep.append(math.asin(tmp))
        tmp = (z[6 + j] - z[4 + j]) / distance(6 + j, 4 + j)
        dep.append(math.asin(tmp))
        tmp = (z[6 + j] - z[5 + j]) / distance(6 + j, 5 + j)
        dep.append(math.asin(tmp))
        tmp = (z[3 + j] - z[6 + j]) / distance(3 + j, 6 + j)
        dep.append(math.asin(tmp))
        tmp = (z[0 + j] - z[7 + j]) / distance(0 + j, 7 + j)
        dep.append(math.asin(tmp))
        tmp = (z[1 + j] - z[8 + j]) / distance(1 + j, 8 + j)
        dep.append(math.asin(tmp))
        tmp = (z[7 + j] - z[9 + j]) / distance(7 + j, 9 + j)
        dep.append(math.asin(tmp))
        tmp = (z[8 + j] - z[10 + j]) / distance(8 + j, 10 + j)
        dep.append(math.asin(tmp))
        tmp = (z[9 + j] - z[11 + j]) / distance(9 + j, 11 + j)
        dep.append(math.asin(tmp))
        tmp = (z[10 + j] - z[12 + j]) / distance(10 + j, 12 + j)
        dep.append(math.asin(tmp))
        tmp = (z[4 + j] - z[13 + j]) / distance(4 + j, 13 + j)
        dep.append(math.asin(tmp))
        tmp = (z[5 + j] - z[14 + j]) / distance(5 + j, 14 + j)
        dep.append(math.asin(tmp))
        tmp = (z[13 + j] - z[15 + j]) / distance(13 + j, 15 + j)
        dep.append(math.asin(tmp))
        tmp = (z[14 + j] - z[16 + j]) / distance(14 + j, 16 + j)
        dep.append(math.asin(tmp))
        tmp = (z[15 + j] - z[17 + j]) / distance(15 + j, 17 + j)
        dep.append(math.asin(tmp))
        tmp = (z[16 + j] - z[18 + j]) / distance(16 + j, 18 + j)
        dep.append(math.asin(tmp))
        tmp = (z[2 + j] - z[19 + j]) / distance(2 + j, 19 + j)
        dep.append(math.asin(tmp))
    return dep

def write_dep(dep, lable):
    title = "data/"+lable+"dep.txt"
    with open(title, 'a') as f:
        for i in dep:
            f.write(str(i))
            f.write(" ")


def produce_one(sub, lable):
    x = []
    y = []
    z = []
    c = []
    #sub = "01"
    for i in range(1, 10):
        mot = "0" + str(i)
        for j in range(3):
            ind = "0" + str(j+1)
            #print(x)
            judge = read_xyz(mot, sub, ind, x, y, z, c)
            if (judge == 0):
                pass
            else:
                [x, y, z, c] = judge

    for i in range(10, 21):
        mot = str(i)
        for j in range(3):
            ind = "0" + str(j+1)
            judge = read_xyz(mot, sub, ind, x, y, z, c)
            if (judge == 0):
                pass
            else:
                [x, y, z, c] = judge
    #lable = "forOne"

    lines = compute_lines(x, y, z)
    angles = compute_angles(x, y, z, lines)
    dep = dep_sin(x, y, z)

    write_xyz(x, y, z, c, lable)
    write_lines(lines, lable)
    write_angles(angles, lable)
    write_dep(dep, lable)
    return True

#def produce_all():
def produce_all_people():
    sub = "0" + str(2)
    lable = "allMotion"+sub
    judge = produce_one(sub, lable)
        #if (judge == False):
        #    print(sub)
    produce_one("10", "allMotion10")

def produce_all():
    lable = "all"
    x = []
    y = []
    z = []
    c = []

produce_one("10", "allMotion10")