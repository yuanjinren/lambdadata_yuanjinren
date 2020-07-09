import pandas
from series import series
from optionsetting import optionsetting
df = pandas.DataFrame({'Col_01':pandas.Series([1,2,3])})
l = ['A','B','C']

df['Col_02'] = series(l)
# df
print(df)
optionsetting()
