# scikit-learn is a Python library that provides tools for building and evaluating machine learning code.
# sklearn is the name used in python
# sklearn.metrics is a module containing evaluation metrics, including MAE and accuracy
# MAE = average absolute difference between actual values and predicted values.
# lower MAE -> more accurate

# example
from sklearn.metrics import mean_absolute_error

actual = [70, 80, 90]
predicted = [75, 76, 95]

mae = mean_absolute_error(actual, predicted)
print(mae)
