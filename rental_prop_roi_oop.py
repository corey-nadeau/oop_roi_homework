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

sumIncome = Income(input("Income from rent: "),input("Other income: ")).summInc()
sumExpenses = Expenses(input("Enter monthly taxes: "),input("Enter monthly insurance: "),input("Enter monthly utilities: "),input("Enter monthly HOA fee: "),
    input("Enter monthly vacancy savings: "),input("Enter monthly repair budget: "),input("Enter monthly capex: "),input("Enter monthly prop mgmt fees: "),input("Enter mortgage: ")).summExp()
sumInvestment = Investment(input("Enter your total down payment: "),input("Enter your closing cost: "),input("Enter your rehab budget: "),input("Enter any other upfront costs: ")).summInv()
cashflow = int(sumIncome) - int(sumExpenses)
roi = int(cashflow) * 12 / int(sumInvestment) *100

print(f"Your total return on investement is: ", int(roi))
