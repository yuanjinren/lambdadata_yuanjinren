import pandas


def setting(my_df):
   
    pandas.options.display.max_columns = 100
    pandas.options.display.max_rows = 1000
    pandas.options.display.float_format = '{:,.2f}'.format
    print('Max columns of this dataframe is: ',pandas.options.display.max_columns)
    print('Max rows of this dataframe is: ',pandas.options.display.max_rows)

if __name__ == "__main__":
    df = pandas.DataFrame({'Col_01':pandas.Series([1.1111,2.2222,3.3333]),
                           'Col_02':pandas.Series(['A','B','C'])})
    setting(df)
    print(df)
    