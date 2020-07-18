import pandas


def setting(my_df):
    """[A function to do settings for dataframe, including maximum rows and columns and display float format.]

    Args:
        my_df ([dataframe])

    Returns:
        [dataframe]: [a dataframe with the new settings will be returned]
    """
   
    pandas.options.display.max_columns = 100
    pandas.options.display.max_rows = 1000
    pandas.options.display.float_format = '{:,.2f}'.format
    print('Max columns of this dataframe is: ',pandas.options.display.max_columns)
    print('Max rows of this dataframe is: ',pandas.options.display.max_rows)
    return my_df

if __name__ == "__main__":
    df = pandas.DataFrame({'Col_01':pandas.Series([1.1111,2.2222,3.3333]),
                           'Col_02':pandas.Series(['A','B','C'])})
    setting(df)
    