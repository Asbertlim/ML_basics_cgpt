# Classification is predicting the category whereas Regression is predicting the numerical data

from sklearn.linear_model import LogisticRegression

# Input: study hours
X = [[1], [2], [3], [5], [6], [7]]

# Target: pass or fail
y = ["No", "No", "No", "Yes", "Yes", "Yes"]

# Create and train the model
model = LogisticRegression()
model.fit(X, y)

# Predict for a new student
prediction = model.predict([[4]])

print("Prediction:", prediction[0])
