import random 
import numpy as np 
from sklearn import preprocessing
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
min_max_scaler = preprocessing.MaxAbsScaler()
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
    data0[0]=min_max_scaler.fit_transform(data0[0])
print data0[0][0]

datab = []
for _ in range(5000):
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

    datab.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc, 0])

datag = []
for _ in range(5000):
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
    
    datag.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc,2])


datam = []
for _ in range(5000):
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

    datam.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc,1])












