#KNN Classifer

clf3 = KNeighborsClassifier()
clf3 = clf3.fit(X,y)

X_train, X_test, y_train, y_test = train_test_split(X, y)

clf3.fit(X_train,y_train)
y_pred2 = clf3.predict(X_test)
accuracy2 = accuracy_score(y_test, y_pred2)
print('Accuracy Score',accuracy2*100)
recall3 = recall_score(y_test, y_pred2, average = 'macro')
print('Recall Score',recall3*100)
conf_mat2 = confusion_matrix(y_true=y_test, y_pred=y_pred2)
print('Confusion matrix:\n', conf_mat2)
