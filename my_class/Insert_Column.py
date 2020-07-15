import pandas
class Insert_Column:
    
    
    def __init__(self, df):
        self.df = df

    def insertcol (self, df, column_name, addlist):
        """[A function allows you to insert column to a dataframe]

        Args:
            df ([dataframe]): [dataframe]
            column_name ([string]): name of the new column
            addlist ([list]): [pass a list you need to add to the dataframe]
        """

        se = pandas.Series(addlist)
        df[column_name] = se.values
        print(df)


if __name__ == "__main__":

    df1 = pandas.DataFrame({'Col1':pandas.Series(['A','B','C','D']),
                           'Col2':pandas.Series([2,4,6,8])})
    list1 = [1,3,5,7]
    column_name1='Col3'
    insert_column1 = Insert_Column(df = df1)
    insert_column1.insertcol(df = df1, addlist = list1, column_name = column_name1)


