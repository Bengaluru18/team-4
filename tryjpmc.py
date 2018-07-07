import random 
import numpy as np 


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
data = []
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

    data.append([st, no, tq, beforea, a, b, c, d, mdm, ni, pp, sdmc])














