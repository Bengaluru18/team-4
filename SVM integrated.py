import random 
import numpy as np 
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
#data generation for 5000 schools

#quantify all schools as a vecotr as following  = [1.student/teacher, 
#                                                  2.strength,
#                                                  3.teacher quality,
#                                                  4.e-learning,
#                                                  5.lab_quality, 
#                                                  6.library_qaulity, 
#                                                  7.toilets_quality,
#                                                  8. medical_provisons, 
#                                                  9.mid-day_meal,
#                                                  10.new_infrastructure
#                                                  11.pass_percentage,
#                                                  12.SDMC]
#student teacher ratio
data0 = []
for _ in range(5000):
    #this is 1
    st = round(random.uniform(15, 90), 3)
    #2
    no = random.randint(15, 1500)
    #3
    tq = round(random.uniform(0,10), 3)
    #4
    beforea = [0]*2
    el = random.randint(0,1)
    beforea[el] = 1
    #5
    a=[0]*3
    i = random.randint(0,2)
    a[i] = 1
    #6
    b = [0]*3
    j = random.randint(0,2)
    b[j] = 1
    #7
    c = [0]*3
    k = random.randint(0,2)
    c[k] = 1
    #8
    d = [0]*3
    mp = random.randint(0,2)
    d[mp] = 1
    #9
    mdm = [0]*2
    l = random.randint(0,1)
    mdm[l] = 1
    #10
    ni = [0]*2
    m = random.randint(0,1)
    ni[m] = 1
    #11
    pp = round(random.uniform(10, 95), 3)
    #12
    sdmc=[0]*3
    i = random.randint(0,2)
    sdmc[i] = 1

    data0.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc])
max1=0
for i in range(0,5000) :
    if(max1<data0[i][0]) :
        max1=data0[i][0]
sum1=0;
for j in range(0,5000) :
    sum1=sum1+data0[j][0]
avg=sum1/5000;
z=[data0[0][0],max1,avg]
y=[1,2,3]
w=0.35
#print max1
#p1 = plt.bar(y, z, w)
#plt.ylabel('Score values')
#plt.title('')
#plt.xticks(y, ('school current', 'max value', 'average value'))
#plt.savefig("D:/plot.png")
#plt.show()

datab = []
Y=np.zeros(60000)
def make_flat(datam_copy):
    final_datam = []
    for lol in datam_copy:
        hulala = []
        for item in lol:
            if isinstance(item, list):
                for sub in item:
                    hulala.append(sub)
            else:
                hulala.append(item)
        final_datam.append(hulala[:-1])
    return np.array(final_datam)

p=0
for _ in range(20000):
    #this is 1
    st = round(random.uniform(60, 90), 3)
    #2
    no = random.randint(15, 200)
    #3
    tq = round(random.uniform(0,3), 3)
    #4
    beforea = [1,0]    
    #5
    a=[1,0,0]
    #6
    b =[1,0,0]
    #7
    c = [1,0,0]
    #8
    d = [1,0,0]
    #9
    mdm = [1,0]
    #10
    ni = [1,0]
    #11
    pp = round(random.uniform(20, 40), 3)
    #12
    sdmc=[1,0,0]
    Y[p]=0
    p=p+1
    datab.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc, 0])

a=make_flat(datab)
print len(a)

datag = []
for _ in range(20000):
    #this is 1
    st = round(random.uniform(20, 40), 3)
    #2
    no = random.randint(600, 1500)
    #3
    tq = round(random.uniform(7,10), 3)
    #4
    beforea = [0,1]
    #5
    a=[0,0,1]
    #6
    b = [0,0,1]
    #7
    c = [0,0,1]
    #8
    d = [0,0,1]
    #9
    mdm = [0,1]
    #10
    ni = [0,1]
    #11
    pp = round(random.uniform(65, 95), 3)
    #12
    sdmc=[0,0,1]
    Y[p]=2
    p=p+1
    
    datag.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc,2])
b=make_flat(datag)    


datam = []
for _ in range(20000):
    #this is 1
    st = round(random.uniform(40, 60), 3)
    #2
    no = random.randint(200, 600)
    #3
    tq = round(random.uniform(4,6), 3)
    #4
    beforea = [0]*2
    el = random.randint(0,1)
    beforea[el] = 1
    #5
    a=[0]*3
    i = random.randint(0,2)
    a[i] = 1
    #6
    b = [0]*3
    j = random.randint(0,2)
    b[j] = 1
    #7
    c = [0]*3
    k = random.randint(0,2)
    c[k] = 1
    #8
    d = [0]*3
    mp = random.randint(0,2)
    d[mp] = 1
    #9
    mdm = [0]*2
    l = random.randint(0,1)
    mdm[l] = 1
    #10
    ni = [0]*2
    m = random.randint(0,1)
    ni[m] = 1
    #11
    pp = round(random.uniform(30, 65), 3)
    #12
    sdmc=[0]*3
    i = random.randint(0,2)
    sdmc[i] = 1
    Y[p]=1
    p=p+1
    datam.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc,1])
c=make_flat(datam)
print len(a)
print len(b)
print len(c)
temp_data = np.concatenate((a,b), axis = 0)
X = np.concatenate((temp_data, c), axis = 0)
X_train, X_test,y_train,y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
clf = svm.SVC(kernel = "linear", C = 1)
clf.fit(X_train,y_train)
clf.score(X_test, y_test)












