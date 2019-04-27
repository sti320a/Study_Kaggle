import pandas as pd
train = pd.read_csv(f'./dataset/train.tsv', sep='\t')
test = pd.read_csv(f'./dataset/test.tsv', sep='\t')

print('=== train.shape ===')
print(train.shape)

print('=== test.shape ===')
print(test.shape)

print('=== dtypes ===')
print(train.dtypes)

print('=== train.head ===')
print(train.head())

print('=== train.price.describe() ===')
print(train.price.describe())

print('=== train.shipping.describe() ===')
print(train.shipping.describe())

print('=== train.shipping.mean() ===')
print(train.shipping.mean())
print(train['shipping'].value_counts())

print('=== category_name value_counts ===')
print(train['category_name'].value_counts()[:5])
