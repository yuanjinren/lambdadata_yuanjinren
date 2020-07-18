import pandas as pd
import unittest
from my_lambdata.optionsetting import setting

class TestOptionSetting(unittest.TestCase):

    def test_setting(self):
        df = pd.DataFrame({'Col_01':pd.Series([10.1234,2.2222,3.3333]),
                           'Col_02':pd.Series(['A','B','C'])})
        self.assertEqual(pd.options.display.max_columns,0)
        self.assertEqual(pd.options.display.max_rows,60)
        self.assertEqual(pd.options.display.float_format,None)
        

        setting(df)

        self.assertEqual(pd.options.display.max_columns,100)
        self.assertEqual(pd.options.display.max_rows,1000)
        self.assertIsNotNone(pd.options.display.float_format)
        

if  __name__ == "__main__":
    unittest.main()