import classdemo

peter=classdemo.BasicStaff('Peter', 0)
john=classdemo.MStaff('John', 0, 1000, 0)

print(peter)
print (john)

print('Peter\'s Pay = ', peter.calculatePay())

print('John\'s Pay = ' ,  john.calculatePay())

print('John\'s Perf Bonus = ', john.calculatePerfBonus())

      
