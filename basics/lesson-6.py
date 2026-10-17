# Linear Regression model tries to learn a straight-relationship between inputs and numerical output
# Training set is used to teach the model patterns from examples
# Testing set is used to check how well the trained model predicts unseen exmaples
# Overfitting -> excellent performance on training data but poor on unseen data

# given code:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Features: study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# Target: exam scores
y = [42, 48, 55, 63, 68,
     75, 81, 87, 92, 98]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# test_size=0.2 -> reserves 20% of records for testing
# random_state=42 -> makes random split reproducible
# X_train, y_train -> inputs and answers for training
# X_test, y_test -> inputs and actual reserved answers for testing
# train_test_split() -> returns corresponding training and testing portions of the inputs and targets

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
# the model learns the best fitting linear relationship from the data

# Predict scores for the test examples
predictions = model.predict(X_test)
# mode estimates scores

print("Actual scores:", y_test)
print("Predicted scores:", predictions)

# Predict for a new student who studies 5.5 hours
new_prediction = model.predict([[5.5]])
print("Predicted score:", new_prediction[0])
