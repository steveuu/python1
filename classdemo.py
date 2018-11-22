class Staff:
    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print ('Creating Staff object')

    def __str__(self):
        return 'Position = %s, Name = %s, Pay = %d' % (self._position, self.name, self.pay)
        #return self.position

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' % (self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: ' % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

    
    @property
    def position(self):
        print('Getter method')
        return self._position
    @position.setter
    def position(self, value):
        if value=='Manager' or value=='Basic':
            print('Setter method')
            self._position = value
        else:
            print('Position is invalid. No changes made.')


class MStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus

    def calculatePay(self):
        basicPay = super().calculatePay()
        perfPay = self.calculatePerfBonus()
        self.pay = basicPay + self.allowance + self.bonus
        return self.pay

    def calculatePerfBonus(self):
        prompt = 'Enter performance grade for %s: ' % (self.name)
        grade = input(prompt)
        if (grade=='A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus

    def __str__(self):
        par=super().__str__()
        return par + ' (includes Allowance = %d, Bonus = %d)' % (self.allowance, self.bonus)
        #return 'Bonus = %d' % (self.bonus)
        #return self.position

class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)

        




            
