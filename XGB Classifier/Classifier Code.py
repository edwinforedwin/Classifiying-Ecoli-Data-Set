#XGB Classifier

X_train, X_test, y_train, y_test = train_test_split(X, y)
clf1 = XGBClassifier()
clf1.fit(X_train, y_train)
y_pred = clf1.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
recall1 = recall_score(y_test, y_pred, average='micro')
print("Recall: %.2f%%" % (recall1 * 100.0))
conf_mat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print('Confusion matrix:\n', conf_mat)
