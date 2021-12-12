
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split


"""
## Load data
"""


df = pd.read_csv("./data.csv")
df.head()


# normalize column names

df.columns = df.columns.str.lower()
df.head()

# drop lines with missing values
print(df.shape)
df = df.dropna()
print(df.shape)
df.head()


"""
## Data pre-processing
"""


# save raw data
df_raw = df.copy()


# load raw data
df = df_raw.copy()
df.head()


# map stroke column to have meaningful column names after one-hot encoding
df['stroke'] = df['stroke'].map({1: 'had_stroke', 0: 'no_stroke'})
df['stroke']


# one-hot encoding for categorical variables:
categorical_cols = ['gender', 'work_type', 'smoking_status', 'stroke']

for col in categorical_cols:
    if col not in df.columns:
        continue
    dummies = pd.get_dummies(df[col])
    df = pd.concat((df, dummies), axis=1)
    df.drop(col, axis=1, inplace=True)

df.head()


# binarize binary categorical data
binary_col_mapping = {
    'ever_married': {'No': 0, 'Yes': 1},
    'residence_type': {'Rural': 0, 'Urban': 1}
}

for (col, mapping) in binary_col_mapping.items():
    if col not in df.columns:
        continue
    df[col] = df[col].map(mapping)

df.head()


# normalize non-binary columns
non_binary_cols = ['age', 'avg_glucose_level', 'bmi']

for col in non_binary_cols:
    df[col] = (df[col] - df[col].mean()) / df[col].std()
    print(f'{col}: mean = {df[col].mean():.2f}; stdev = {df[col].std():.2f}')

df.head()


# create training and testing set

x_cols = [col for col in df.columns if col not in ['had_stroke', 'no_stroke', 'id']]
x = df[x_cols]
y = df[['had_stroke', 'no_stroke']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(x_train.shape, y_train.shape)


"""
## Build & train model
"""


# build model

model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(19,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.summary()


model.compile(
    optimizer='adam',  # Optimizer
    # Loss function to minimize
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.Recall()]
)

model.fit(
    x_train,
    y_train,
    epochs=10,
    verbose=2,
    batch_size=64
)


"""
## Evaluate
"""


# evaluate on test set
loss, acc, recall = model.evaluate(x_test, y_test)
print(f'test loss = {loss}\ntest accuracy = {acc}\nrecall = {recall}')


# evaluate on single instance
test_individual = np.array(x_test.iloc[0])
test_individual.shape = (1, 19, 1)
print(model.predict(test_individual))
print(y_test.iloc[0])


model.weights


"""
## Build linear model
"""


# build model

model = Sequential()
model.add(Dense(1, activation='linear', input_shape=(19,)))
model.add(Dense(2, activation='softmax'))

model.summary()

model.compile(
    optimizer='adam',  # Optimizer
    # Loss function to minimize
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.Recall()]
)

model.fit(
    x_train,
    y_train,
    epochs=10,
    verbose=2,
    batch_size=64
)


# evaluate on test set
loss, acc, recall = model.evaluate(x_test, y_test)
print(f'test loss = {loss}\ntest accuracy = {acc}\nrecall = {recall}')