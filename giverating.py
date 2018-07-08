from sklearn.preprocessing import normalize

X_0 = X[:,[0,1,2,21]]
X_1 = X[:,3:21]
X_2 = X[:,22:]


X_0 = normalize(X_0,  axis = 1)
temp_X = np.concatenate((X_1, X_2), axis = 1)
final_X = np.concatenate((temp_X, X_0), axis = 1)
sum_X = np.sum(final_X, axis = 1)
sum_X = sum_X.reshape(75000,1)
tsum = np.sum(sum_X,axis = 0)/75000
target = sum_X - tsum
for _ in range(len(target)):
    if target[_]<0:
        target[_] = 0
    elif target[_]>0.09:
        target[_] = 1
    elif
        target[_] = 2
