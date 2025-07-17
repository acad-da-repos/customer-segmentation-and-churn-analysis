
import unittest
import pandas as pd
from datetime import datetime
from assignment import perform_rfm_analysis, calculate_churn_rate

class TestCustomerAnalysis(unittest.TestCase):
    def test_perform_rfm_analysis(self):
        data = {
            'CustomerID': [1, 1, 2, 2, 3],
            'OrderDate': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-10', '2023-03-01'],
            'Sales': [100, 150, 200, 50, 300]
        }
        df = pd.DataFrame(data)
        rfm_df = perform_rfm_analysis(df)

        self.assertIsInstance(rfm_df, pd.DataFrame)
        self.assertIn('Recency', rfm_df.columns)
        self.assertIn('Frequency', rfm_df.columns)
        self.assertIn('Monetary', rfm_df.columns)
        self.assertEqual(len(rfm_df), 3)

    def test_calculate_churn_rate(self):
        data = {'CustomerID': [1, 2, 3, 4, 5],
                'Churn': [0, 1, 0, 1, 0]}
        df = pd.DataFrame(data)
        churn_rate = calculate_churn_rate(df)

        self.assertIsInstance(churn_rate, float)
        self.assertEqual(churn_rate, 0.4)

if __name__ == '__main__':
    unittest.main()
