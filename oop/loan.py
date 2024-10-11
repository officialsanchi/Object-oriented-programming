class Loan:
    def __init__(self, borrower: str, loan_amount: float, loan_period:int, interest_rate:int):

        self.borrower = borrower
        self.loan_amount = loan_amount
        self.loan_period = loan_period
        self.interest_rate = interest_rate

    def get_borrower(self):
        return self.borrower

    def get_loan_amount(self):
        return self.loan_amount

    def get_loan_period(self):
        return self.loan_period

    def get_interest_rate(self):
        return self.interest_rate

    def compute_monthly_payment(self, principal : int, monthly_interest_rate : float,duration_months: int):
        numerator = principal * monthly_interest_rate
        denominator = 1 - (1 / (1 + monthly_interest_rate) ** duration_months)
        monthly_payment = numerator / denominator
        return monthly_payment

    def calculate_total_payment(self, monthly_payment, duration_months):
        total_payment = monthly_payment * duration_months
        return total_payment