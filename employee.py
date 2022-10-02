"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    
    # enums
    HOURLY_CONTRACT = 0
    SALARY_CONTRACT = 1
    
    NO_COMMISSION = 0
    BONUS_COMMISSION = 1
    CONTRACT_COMMISSION = 2

    def __init__(self, name, contract_type, contract_rate, commission_type, **kwargs):
        self.name = name
        self.contract_type = contract_type
        self.contract_rate = contract_rate
        self.commission_type = commission_type

        if contract_type == Employee.HOURLY_CONTRACT:
            self.hours = kwargs['hours']

        if commission_type == Employee.CONTRACT_COMMISSION:
            self.contracts = kwargs['contracts']
            self.commission_rate = kwargs['commission_rate']

        elif commission_type == Employee.BONUS_COMMISSION:
            self.bonus = kwargs['bonus']

    def get_pay(self):
        total = 0
        
        if self.contract_type == Employee.HOURLY_CONTRACT:
            total += self.hours * self.contract_rate
        else:
            total += self.contract_rate

        if self.commission_type == Employee.BONUS_COMMISSION:
            total += self.bonus
        elif self.commission_type == Employee.CONTRACT_COMMISSION:
            total += self.contracts * self.commission_rate

        return total

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Employee.SALARY_CONTRACT, 4000, Employee.NO_COMMISSION)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Employee.HOURLY_CONTRACT, 25, Employee.NO_COMMISSION, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Employee.SALARY_CONTRACT, 3000, Employee.CONTRACT_COMMISSION, commission_rate=200, contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Employee.HOURLY_CONTRACT, 25, Employee.CONTRACT_COMMISSION, hours=150, commission_rate=220, contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Employee.SALARY_CONTRACT, 2000, Employee.BONUS_COMMISSION, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Employee.HOURLY_CONTRACT, 30, Employee.BONUS_COMMISSION, hours=120, bonus=600)
