import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # def setUp(self):
    #     self.compound_interest = CompoundInterest()
   

    # Tests
    
    def test_get_principal_amount(self):
        self.compound_interest = CompoundInterest(100.00, 0.10, 20)
        self.assertEqual(100, self.compound_interest.amount)

    def test_get_interest_rate(self):
        self.compound_interest = CompoundInterest(100.00, 0.10, 20)
        self.assertEqual(0.10, self.compound_interest.interest)

    def test_get_number_of_years(self):
        self.compound_interest = CompoundInterest(100.00, 0.10, 20)
        self.assertEqual(20, self.compound_interest.years)

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    # def test_compound_interest_function_ten_percent_twenty_years(self,)

    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

