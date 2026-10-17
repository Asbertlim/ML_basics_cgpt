import pandas as pd

data = {
    "Hours": [3, 5, 1, 7],
    "Sleep": [6.5, 7, 5.5, 8],
    "School": ["A", "B", "A", "C"],
    "Score": [55, 75, 40, 92]
}

df = pd.DataFrame(data)
# df.isnull() -> produces a data frame with Trues and Falses, True means there is a missing value
# df.isnull().sum() -> produces amount of Trues(missing value) for certain feature
# df.dropna() -> removes a row containing missing values
# df["StudyHours"] = df["StudyHours"].fillna(
#     df["StudyHours"].mean()
# ) -> this fills the missing value with the average
# df.drop_duplicates() -> removes duplicate data

print(df)
