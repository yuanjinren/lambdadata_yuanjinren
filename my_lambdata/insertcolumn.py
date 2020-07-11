import pandas


def insertcol (mylist,mydf,column_name = 'new_col'):
    """
    You need to take a list, a dataframe and the new column name as parameters, then add the list
    as a column of the dataframe with the new column name.
    """

    se = pandas.Series(mylist)
    mydf[column_name] = se.values
    
    print(mydf)


if __name__ == "__main__":
    
    list1 = [1,3,5,7]
    df1 = pandas.DataFrame({'Col1':pandas.Series(['A','B','C','D']),
                           'Col2':pandas.Series([2,4,6,8])})
    df1.column_name = input("Please input new column name: ")
    insertcol(list1, df1,column_name = df1.column_name)