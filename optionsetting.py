import pandas

def optionsetting():
   
    pandas.options.display.max_columns = 100
    pandas.options.display.max_rows = 1000
    
    print('Max columns of this dataframe is: ',pandas.options.display.max_columns)
    print('Max rows of this dataframe is: ',pandas.options.display.max_rows)
