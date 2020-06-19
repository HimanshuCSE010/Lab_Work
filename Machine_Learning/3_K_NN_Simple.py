#K-NN classifier (Non Weighted)

from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris 

# Loading data 
Data = load_iris() 

# Create feature and target arrays 
X = Data.data 
y = Data.target 

print("\nA sample of training Data (only 10 samples):")
for i in range(10):
	print(*X[i])

# Split into training and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) 

# trainig over train data 
KNN = KNeighborsClassifier(n_neighbors=7) 
KNN.fit(X_train, y_train) 

# Prediction 
print("\nPredictions: ")
result = KNN.predict(X_test)
print(f"{'Test Sample':<17}: {'Class'}") 
for pre in X_test[:10]:
	print(f"{pre}:   {result[i]}") 
