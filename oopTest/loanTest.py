import unittest
from oop import loan


class LoanTest(unittest.TestCase):

    def setUp(self):
        self.loan = loan.Loan("chidinma", 200000000,12,200)

    def test_that_loan_class_exist(self):
        pass


    def test_that_loan_contract_has_borrower(self):
        borrower = self.loan.borrower
        self.assertTrue(borrower)

    def test_that_loan_contract_has_loan_amount(self):
        loan_amount = self.loan.loan_amount
        self.assertTrue(loan_amount)

    def test_that_loan_contract_has_loan_period(self):
        loan_period = self.loan.loan_period
        self.assertTrue(loan_period)

    def test_that_loan_contract_has_interest_rate(self):
        interest_rate = self.loan.interest_rate
        self.assertTrue(interest_rate)

    def test_that_loan_compute_monthly_payment(self):
        loan_amount = self.loan.loan_amount
        self.assertTrue(loan_amount)
        monthly_payment = self.loan.compute_monthly_payment(1000000, 0.005,60)
        self.assertTrue(monthly_payment)
    def test_that_loan_contract_can_calculate_total_payment(self):
        loan_amount = self.loan.loan_amount
        self.assertTrue(loan_amount)
        monthly_payment = self.loan.compute_monthly_payment(1000000, 0.005,60)
        self.assertTrue(monthly_payment)
        total_payment = self.loan.calculate_total_payment(0.005, 60)
        self.assertTrue(total_payment)