class CompoundInterestCalculator:

    def __init__(self, amount, interest, years):
        self.amount = amount 
        self.years = years
        self.interest = interest
        self.n = 12 #nr of times interest is compounded per year

    def calculate(self):
        P = self.amount
        r = self.interest
        t = self.years
        n = self.n

        calculated_interest = P*(1+(r/n))**(n*t)

        return round(calculated_interest, 2)