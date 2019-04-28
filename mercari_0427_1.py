import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

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


def split_cat(text):
    try:
        return text.split('/')
    except Exception as e:
        return ('No Label', 'No Label', 'No Label')


train['general_cat'], train['subcat_1'],  train['subcat_2'] = \
    zip(*train['category_name'].apply(lambda x: split_cat(x)))

print(train.head())

print("There are %d unique first sub-categories." %
      train['subcat_1'].nunique())
print("There are %d unique second sub-categories." %
      train['subcat_2'].nunique())

x = train['general_cat'].value_counts().index.values.astype('str')
y = train['general_cat'].value_counts().values
pct = [("%.2f" % (v*100))+"%"for v in (y/len(train))]

# trace1 = go.Bar(x=x, y=y, text=pct)
# layout = dict(title='Number of Items by Main Category',
#               yaxis=dict(title='Count'),
#               xaxis=dict(title='Category'))
# fig = dict(data=[trace1], layout=layout)
# py.iplot(fig)

x = train['subcat_1'].value_counts().index.values.astype('str')[:15]
y = train['subcat_1'].value_counts().values[:15]
pct = [("%.2f" % (v*100))+"%"for v in (y/len(train))][:15]

print("There are %d unique brand names in the training dataset." %
      train['brand_name'].nunique())
