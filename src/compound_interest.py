class CompoundInterest:

    def __init__(self, amount, interest, years):
        self.amount = amount 
        self.years = years
        self.interest = interest
        self.n = 12 #nr of times interest is compounded per year
