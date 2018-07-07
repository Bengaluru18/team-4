import pandas

data0_copy = data0.copy()
datag_copy = datag.copy()
datab_copy = datab.copy()
datam_copy = datam.copy()


df0 = pandas.DataFrame(data0_copy)
dfg = pandas.DataFrame(datag_copy)
dfb = pandas.DataFrame(datab_copy)
dfm = pandas.DataFrame(datam_copy)

yg = dfg[:][12]
yg = np.array(yg)
yg.shape
yg = yg.reshape(20000,1)

yb = dfb[:][12]
yb = np.array(yb)
yb.shape
yb = yb.reshape(20000,1)

ym = dfm[:][12]
ym = np.array(ym)
ym.shape
ym = ym.reshape(20000,1)

temp = np.concatenate((yg,yb), axis = 0)
y = np.concatenate((temp, ym), axis = 0)

np.save("y", y)
