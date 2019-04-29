import math

#open file
length = 43
data=[]
with open('../real3d/a01_s01_e03_skeleton3D.txt', 'r') as f:
    for line in f.readlines():
        tmp=[]
        for x in (line.strip().split(" ")):
            tmp.append(float(x))
        #print(zz)
        data.append(tmp)
#print(data)

#get x,y,z,c
x=[]
y=[]
z=[]
c=[]
for i in range(length):
    for j in range(20):
        index = i*20+j
        x.append(data[index][0])
        y.append(data[index][1])
        z.append(data[index][2])
        c.append(data[index][3])

#write z,c
with open('data/a1s1x.txt', 'a') as f:
    for i in range(length):
        for j in range(20):
            f.write(str(x[i*20+j]))
            f.write(" ")
        f.write("\n")
with open('data/a1s1y.txt', 'a') as f:
    for i in range(length):
        for j in range(20):
            f.write(str(y[i*20+j]))
            f.write(" ")
        f.write("\n")
with open('data/a1s1z.txt', 'a') as f:
    for i in range(length):
        for j in range(20):
            f.write(str(z[i*20+j]))
            f.write(" ")
        f.write("\n")
with open('data/a1s1c.txt', 'a') as f:
    for i in range(length):
        for j in range(20):
            f.write(str(c[i*20+j]))
            f.write(" ")
        f.write("\n")

#compute the distance between two joints
def distance(m,n):
    xx = (x[m] - x[n]) ** 2
    yy = (y[m] - y[n]) ** 2
    zz = (z[m] - z[n]) ** 2
    return (math.sqrt(xx+yy+zz))

#compute the lines
lines=[]
for i in range(length):
    j=i*20
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
#print(lines)
#write the average of lines
#print(len(lines))
sum=[]
for j in range(19):
    sum.append(0)
for i in range(length):
    for j in range(19):
        index = j+i*19
        sum[j]+=lines[index]

with open('data/a1s1lines.txt', 'a') as f:
    for j in range(19):
        f.write(str(sum[j]/54))
        f.write(" ")

#compute angles
angles=[]
for i in range(length):
    j=i*20
    k=i*19
    #1
    tmp=distance((0 + j), (19 + j))
    ang=(lines[0+k]**2+lines[1+k]**2-tmp**2)/(2*lines[0+k]*lines[1+k])
    angles.append(math.acos(ang))
    #2
    tmp = distance((1 + j), (19 + j))
    ang=(lines[0+k]**2+lines[2+k]**2-tmp**2)/(2*lines[0+k]*lines[2+k])
    angles.append(math.acos(ang))
    #3
    tmp = distance((2 + j), (7 + j))
    ang=(lines[1+k]**2+lines[3+k]**2-tmp**2)/(2*lines[1+k]*lines[3+k])
    angles.append(math.acos(ang))
    #4
    tmp = distance((2 + j), (8 + j))
    ang=(lines[2+k]**2+lines[6+k]**2-tmp**2)/(2*lines[2+k]*lines[6+k])
    angles.append(math.acos(ang))
    #5
    tmp = distance((0 + j), (9 + j))
    ang=(lines[3+k]**2+lines[4+k]**2-tmp**2)/(2*lines[3+k]*lines[4+k])
    angles.append(math.acos(ang))
    #6
    tmp = distance((1 + j), (10 + j))
    ang=(lines[6+k]**2+lines[7+k]**2-tmp**2)/(2*lines[6+k]*lines[7+k])
    angles.append(math.acos(ang))
    #7
    tmp = distance((7 + j), (11 + j))
    ang=(lines[4+k]**2+lines[5+k]**2-tmp**2)/(2*lines[4+k]*lines[5+k])
    angles.append(math.acos(ang))
    #8
    tmp = distance((8 + j), (12 + j))
    ang=(lines[7+k]**2+lines[8+k]**2-tmp**2)/(2*lines[7+k]*lines[8+k])
    angles.append(math.acos(ang))
    #9
    tmp = distance((2 + j), (6 + j))
    ang=(lines[10+k]**2+lines[9+k]**2-tmp**2)/(2*lines[10+k]*lines[9+k])
    angles.append(math.acos(ang))
    #10
    tmp = distance((3 + j), (4 + j))
    ang=(lines[10+k]**2+lines[11+k]**2-tmp**2)/(2*lines[10+k]*lines[11+k])
    angles.append(math.acos(ang))
    #11
    tmp = distance((4 + j), (5 + j))
    ang=(lines[11+k]**2+lines[15+k]**2-tmp**2)/(2*lines[11+k]*lines[15+k])
    angles.append(math.acos(ang))
    #12
    tmp = distance((3 + j), (5 + j))
    ang=(lines[10+k]**2+lines[15+k]**2-tmp**2)/(2*lines[10+k]*lines[15+k])
    angles.append(math.acos(ang))
    #13
    tmp = distance((6 + j), (13 + j))
    ang=(lines[11+k]**2+lines[12+k]**2-tmp**2)/(2*lines[11+k]*lines[12+k])
    angles.append(math.acos(ang))
    #14
    tmp = distance((6 + j), (14 + j))
    ang=(lines[15+k]**2+lines[16+k]**2-tmp**2)/(2*lines[15+k]*lines[16+k])
    angles.append(math.acos(ang))
    #15
    tmp = distance((4 + j), (15 + j))
    ang=(lines[12+k]**2+lines[13+k]**2-tmp**2)/(2*lines[12+k]*lines[13+k])
    angles.append(math.acos(ang))
    #16
    tmp = distance((5 + j), (16 + j))
    ang=(lines[16+k]**2+lines[17+k]**2-tmp**2)/(2*lines[16+k]*lines[17+k])
    angles.append(math.acos(ang))
    #17
    tmp = distance((13 + j), (17 + j))
    ang=(lines[13+k]**2+lines[14+k]**2-tmp**2)/(2*lines[13+k]*lines[14+k])
    angles.append(math.acos(ang))
    #18
    tmp = distance((14 + j), (18 + j))
    ang=(lines[17+k]**2+lines[18+k]**2-tmp**2)/(2*lines[17+k]*lines[18+k])
    angles.append(math.acos(ang))

#write angles
with open('data/a1s1angles.txt', 'a') as f:
    for i in range(length):
        for j in range(18):
            f.write(str(angles[i*18+j]))
            f.write(" ")
        f.write("\n")

#print(angles)

#compute depth
dep=[]
for i in range(length):
    j=i*20
    tmp = (z[2 + j] - z[0 + j]) / distance(2 + j, 0 + j)
    #print(tmp)
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

#write depth
with open('data/a1s1dep.txt', 'a') as f:
    for i in range(length):
        for j in range(20):
            f.write(str(dep[i*20+j]))
            f.write(" ")
        f.write("\n")




