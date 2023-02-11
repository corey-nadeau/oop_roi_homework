class Income():
    def __init__(self,rent,other_income):
        self.rent = rent
        self.other_income = other_income
    def summInc(self):
        return self.rent + self.other_income

class Expenses():
    def __init__(self,tax,insurance,utilities,hoa,vacancy,repairs,capex,prop_mgmt,mortgage):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.prop_mgmt = prop_mgmt
        self.mortgage = mortgage
    def summExp(self):
        return self.tax + self.insurance + self.utilities + self.hoa + self.vacancy + self.repairs + self.capex + self.prop_mgmt + self. mortgage

class Investment():
    def __init__(self,down_payment,closing_costs,rehab_budget,misc):
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc = misc
    def summInv(self):
        return self.down_payment + self.closing_costs + self.rehab_budget + self.misc

sumIncome = Income(2000,0).summInc()
sumExpenses = Expenses(150,100,0,0,100,100,100,200,860).summExp()
sumInvestment = Investment(40000,3000,7000,0).summInv()
cashflow = int(sumIncome) - int(sumExpenses)
roi = cashflow * 12 / sumInvestment *100

print(roi)
