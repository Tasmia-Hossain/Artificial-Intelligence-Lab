df = load_dataset('penguins')

df.head()

df.columns



df.info()

df.describe()

df = df.dropna()

df.info()

X = df[['bill_length_mm', 'bill_depth_mm']]
y = df['species']

X.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

knn = KNeighborsClassifier(metric="euclidean", n_neighbors=3)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)



print(predictions)

pred = knn.predict([[23.9, 17.2]])
print(pred)

from sklearn.metrics import accuracy_score

acc = accuracy_score(y_test, predictions)
print(acc)
