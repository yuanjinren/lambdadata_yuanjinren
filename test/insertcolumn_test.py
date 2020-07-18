import pandas as pd
import unittest
from my_lambdata.insertcolumn import insertcol

class TestInsertCol(unittest.TestCase):

    def test_insertcol(self):
        df1 = pd.DataFrame({'Col1':pd.Series(['A','B','C','D']),
                           'Col2':pd.Series([2,4,6,8])})
        self.assertEqual(len(df1.columns),2)
        self.assertEqual(list(df1.columns),['Col1','Col2'])

        insertcol(mydf=df1,mylist=[1,3,5,7], column_name = 'Col3')

        self.assertEqual(len(df1.columns),3)
        self.assertEqual(list(df1.columns),['Col1','Col2','Col3'])
        

if  __name__ == "__main__":
    unittest.main()