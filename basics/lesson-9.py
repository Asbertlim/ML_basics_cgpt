# accuracy is how often the model is correct

# Confusion matrix:
# TP (True Positive) -> spam correctly detected
# FP (False Positive) -> Legitimate email wrongly flagged as spam
# TN -> Legitimate email correctly identified
# FN -> spam missed by the model

# True -> the prediction was correct
# False -> the prediction was wrong
# Positive -> the model predicted positve class
# Negative -> the model predicted negative class

# Precision vs Recall
# Precision : of all emails predicted as spam, how many really were spam
# P = TP/ (TP + FP)
# Recall : of all emails that were really spam, how many did the model catch
# R = TP/ (TP + FN)

from sklearn.metrics import accuracy_score

actual = ["Spam", "Not Spam", "Spam", "Spam"]
predicted = ["Spam", "Not Spam", "Not Spam", "Spam"]

accuracy = accuracy_score(actual, predicted)
print(accuracy)
