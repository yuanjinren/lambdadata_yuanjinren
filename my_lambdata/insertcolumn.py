import pandas


def insertcol (list):
    """
    You are able to take a list as parameter, then add the list
    as a column of a dataframe.
    """
    se = pandas.Series(list)
    df = pandas.DataFrame({'A': [2, 4, 6, 8]})
    df['new_col'] = se.values
    print(df)


if __name__ == "__main__":
    
    mylist = [1,3,5,7]
    insertcol(mylist)