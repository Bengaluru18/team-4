from sklearn import svm
from sklearn.model_selection import train_test_split


X_train, X_test,y_train,y_test = train_test_split(X, y_new, test_size = 0.3, random_state = 1)

clf = svm.SVC(kernel = "linear", C = 1)
clf.fit(X_train,y_train)
clf.score(X_test, y_test)
